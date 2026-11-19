"""Generate, validate, preview, and record ERCOT strategy candidates."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time
import uuid
from datetime import datetime, timezone
from typing import Iterable, Mapping, Sequence

from ercot_game.csv_submission import CANONICAL_CSV_COLUMNS
from ercot_game.csv_validator import validate_csv_submission


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SCENARIO_DIR = REPOSITORY_ROOT / "ercot-connection-game" / "data" / "processed" / "activsg2000_representative_v1"
DEFAULT_RELEASE = REPOSITORY_ROOT / "configs" / "rounds" / "finalized_release_500mw.json"
DEFAULT_RULES = REPOSITORY_ROOT / "configs" / "scoring" / "dispatch_scoring_rules_500mw.json"
DEFAULT_DATABASE = REPOSITORY_ROOT / "analysis" / "run_database.csv"
DEFAULT_EXPERIMENT_LOG = REPOSITORY_ROOT / "analysis" / "experiment_log.csv"
DEFAULT_RUNS_DIR = REPOSITORY_ROOT / "runs" / "experiments"

RUN_DATABASE_COLUMNS = (
    "record_id",
    "experiment_id",
    "run_id",
    "timestamp_utc",
    "plan_name",
    "plan_source",
    "team_id",
    "week",
    "submission",
    "scenario_id",
    "scenario_sha256",
    "rules_sha256",
    "release_sha256",
    "base_load_sha256",
    "seed",
    "mode",
    "status",
    "valid",
    "allocation_triggered",
    "evaluation_status",
    "candidate_csv_path",
    "validation_output_path",
    "preview_output_path",
    "official_output_path",
    "git_revision",
    "buses_used_json",
    "connection_capacity_mw_by_bus_json",
    "generator_capacity_mw_by_bus_json",
    "storage_power_mw_by_bus_json",
    "storage_energy_mwh_by_bus_json",
    "total_connection_capacity_mw",
    "total_generator_capacity_mw",
    "total_storage_power_mw",
    "total_storage_energy_mwh",
    "requested_capacity_mw",
    "allocated_capacity_mw",
    "score_usd",
    "served_load_mwh",
    "served_fraction",
    "it_value_usd",
    "energy_cost_usd",
    "generator_operating_cost_usd",
    "generator_capital_cost_usd",
    "storage_capital_cost_usd",
    "site_cost_usd",
    "alpha_min",
    "alpha_mean",
    "alpha_max",
    "curtailment_mw",
    "cpu_runtime_seconds",
    "peak_memory_gib",
    "binding_period_indices_json",
    "binding_branches_json",
    "congestion_indicators_json",
    "maximum_branch_loading_pct",
    "maximum_generator_utilization_pct",
    "warning_text",
    "issues_json",
    "raw_output_sha256",
)

EXPERIMENT_LOG_COLUMNS = (
    "event_id",
    "timestamp_utc",
    "experiment_id",
    "run_id",
    "plan_name",
    "phase",
    "event_type",
    "status",
    "elapsed_seconds",
    "candidate_csv_path",
    "validation_output_path",
    "preview_output_path",
    "official_output_path",
    "details_path",
    "message",
    "git_revision",
    "scenario_sha256",
    "rules_sha256",
    "base_load_sha256",
)


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_directory(directory: Path) -> str:
    if not directory.is_dir():
        raise ValueError(f"scenario package does not exist: {directory}")
    digest = hashlib.sha256()
    for path in sorted(p for p in directory.rglob("*") if p.is_file()):
        digest.update(path.relative_to(directory).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(sha256_file(path).encode("ascii"))
        digest.update(b"\0")
    return digest.hexdigest()


def git_revision() -> str:
    try:
        completed = subprocess.run(
            ["git", "-C", str(REPOSITORY_ROOT), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return completed.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


def _finite_number(value: object, label: str, default: float = 0.0) -> float:
    if value is None:
        return default
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{label} must be finite") from exc
    if not math.isfinite(number) or number < 0:
        raise ValueError(f"{label} must be finite and non-negative")
    return number


def normalize_candidate_plan(
    candidate: Mapping[str, object],
    *,
    default_team_id: str,
    week: int,
    submission: int,
) -> dict[str, object]:
    plan_name = candidate.get("plan_name") or candidate.get("name")
    if not isinstance(plan_name, str) or not plan_name.strip():
        raise ValueError("candidate plan requires plan_name or name")

    team_id = candidate.get("team_id", default_team_id)
    if not isinstance(team_id, str) or not team_id.strip():
        raise ValueError(f"{plan_name}: team_id must be a non-empty string")

    candidate_week = int(candidate.get("week", week))
    candidate_submission = int(candidate.get("submission", submission))
    if candidate_week not in (1, 2, 3):
        raise ValueError(f"{plan_name}: week must be 1, 2, or 3")
    if candidate_submission not in (1, 2):
        raise ValueError(f"{plan_name}: submission must be 1 or 2")

    raw_sites = candidate.get("sites")
    if raw_sites is None:
        raw_sites = candidate.get("site_list")
    if not isinstance(raw_sites, Sequence) or isinstance(raw_sites, (str, bytes)):
        raise ValueError(f"{plan_name}: sites must be a list")
    if not raw_sites:
        raise ValueError(f"{plan_name}: at least one site is required")

    sites: list[dict[str, object]] = []
    for index, raw_site in enumerate(raw_sites, start=1):
        if not isinstance(raw_site, Mapping):
            raise ValueError(f"{plan_name}: site {index} must be an object")

        bus_id = raw_site.get("bus_id")
        if bus_id is None:
            bus_id = raw_site.get("bus")
        if bus_id is None:
            raise ValueError(f"{plan_name}: site {index} requires bus_id")

        connection = _finite_number(
            raw_site.get("connection_capacity_mw", raw_site.get("connection_mw")),
            f"{plan_name}: site {index} connection_capacity_mw",
        )
        generator = _finite_number(
            raw_site.get("generator_capacity_mw", raw_site.get("generator_mw")),
            f"{plan_name}: site {index} generator_capacity_mw",
        )
        storage_power = _finite_number(
            raw_site.get("storage_power_mw", raw_site.get("storage_mw")),
            f"{plan_name}: site {index} storage_power_mw",
        )
        storage_energy = _finite_number(
            raw_site.get("storage_energy_mwh"),
            f"{plan_name}: site {index} storage_energy_mwh",
            default=-1.0,
        )
        if storage_energy < 0:
            storage_energy = 4.0 * storage_power

        supplied_site_id = raw_site.get("site_id")
        site_id = supplied_site_id if isinstance(supplied_site_id, str) and supplied_site_id else (
            f"w{candidate_week}-s{candidate_submission}-{index:04d}"
        )

        sites.append({
            "site_id": site_id,
            "bus_id": str(bus_id),
            "connection_capacity_mw": connection,
            "generator_capacity_mw": generator,
            "storage_power_mw": storage_power,
            "storage_energy_mwh": storage_energy,
        })

    return {
        "plan_name": plan_name.strip(),
        "plan_source": candidate.get("plan_source", "candidate-list"),
        "team_id": team_id,
        "week": candidate_week,
        "submission": candidate_submission,
        "scenario_id": candidate.get("scenario_id", ""),
        "seed": int(candidate.get("seed", 0)),
        "sites": sites,
    }


def generate_submission_csv(
    plan: Mapping[str, object],
    path: Path,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    sites = plan["sites"]
    if not isinstance(sites, Sequence):
        raise ValueError("normalized plan has invalid sites")
    with path.open("x", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(CANONICAL_CSV_COLUMNS)
        for site in sites:
            writer.writerow((
                plan["team_id"],
                site["site_id"],
                site["bus_id"],
                site["connection_capacity_mw"],
                site["generator_capacity_mw"],
                site["storage_power_mw"],
                site["storage_energy_mwh"],
            ))


def append_csv_row(path: Path, columns: Sequence[str], row: Mapping[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        with path.open("x", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore")
            writer.writeheader()
    else:
        with path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.reader(handle)
            existing = next(reader, None)
        if existing is not None and tuple(existing) != tuple(columns):
            raise ValueError(f"{path} has a schema that differs from the experiment runner")

    with path.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore")
        writer.writerow(dict(row))


def append_experiment_event(
    log_path: Path,
    *,
    experiment_id: str,
    run_id: str,
    plan_name: str,
    phase: str,
    event_type: str,
    status: str,
    message: str,
    git_revision_value: str,
    scenario_sha256: str,
    rules_sha256: str,
    base_load_sha256: str,
    candidate_csv_path: str = "",
    validation_output_path: str = "",
    preview_output_path: str = "",
    official_output_path: str = "",
    details_path: str = "",
    elapsed_seconds: float = 0.0,
) -> None:
    append_csv_row(log_path, EXPERIMENT_LOG_COLUMNS, {
        "event_id": str(uuid.uuid4()),
        "timestamp_utc": utc_timestamp(),
        "experiment_id": experiment_id,
        "run_id": run_id,
        "plan_name": plan_name,
        "phase": phase,
        "event_type": event_type,
        "status": status,
        "elapsed_seconds": elapsed_seconds,
        "candidate_csv_path": candidate_csv_path,
        "validation_output_path": validation_output_path,
        "preview_output_path": preview_output_path,
        "official_output_path": official_output_path,
        "details_path": details_path,
        "message": message,
        "git_revision": git_revision_value,
        "scenario_sha256": scenario_sha256,
        "rules_sha256": rules_sha256,
        "base_load_sha256": base_load_sha256,
    })


def _json_text(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def _aggregate_by_bus(plan: Mapping[str, object], field: str) -> dict[str, float]:
    result: dict[str, float] = {}
    for site in plan["sites"]:
        bus = str(site["bus_id"])
        result[bus] = result.get(bus, 0.0) + float(site[field])
    return result


def _preview_team_output(payload: Mapping[str, object], team_id: str) -> Mapping[str, object]:
    team_scores = payload.get("team_scores")
    if not isinstance(team_scores, Sequence):
        return {}
    for score in team_scores:
        if isinstance(score, Mapping) and score.get("team_id") == team_id:
            return score
    return {}


def _preview_issues(payload: Mapping[str, object], validation_issues: Sequence[str]) -> list[str]:
    issues = [str(issue) for issue in validation_issues]
    rejected = payload.get("rejected_submissions")
    if isinstance(rejected, Sequence):
        issues.extend(
            f"rejected submission: {item.get('team_id')}: {item.get('reason')}"
            for item in rejected
            if isinstance(item, Mapping)
        )
    return issues


def load_candidate_plans(input_spec: object) -> list[dict[str, object]]:
    if isinstance(input_spec, (str, Path)):
        path = Path(input_spec)
        if path.is_file():
            payload = json.loads(path.read_text(encoding="utf-8"))
        else:
            payload = json.loads(str(input_spec))
    else:
        payload = input_spec

    if isinstance(payload, Mapping):
        candidates = payload.get("plans") or payload.get("candidates")
    elif isinstance(payload, Sequence) and not isinstance(payload, (str, bytes)):
        candidates = payload
    else:
        raise ValueError("candidate input must be a JSON list or an object containing plans/candidates")
    if not isinstance(candidates, Sequence) or isinstance(candidates, (str, bytes)):
        raise ValueError("plans/candidates must be a list")
    return [dict(candidate) for candidate in candidates if isinstance(candidate, Mapping)]


def run_experiment(
    candidate_plans: Iterable[Mapping[str, object]],
    *,
    experiment_id: str = "strategy-experiment",
    team_id: str = "team-experiment",
    week: int = 2,
    submission: int = 1,
    scenario_dir: str | Path = DEFAULT_SCENARIO_DIR,
    rules: str | Path = DEFAULT_RULES,
    release: str | Path = DEFAULT_RELEASE,
    base_load_from: str | Path | None = None,
    runs_dir: str | Path = DEFAULT_RUNS_DIR,
    database: str | Path = DEFAULT_DATABASE,
    experiment_log: str | Path = DEFAULT_EXPERIMENT_LOG,
    preview_stride: int = 1,
) -> list[dict[str, object]]:
    scenario_path = Path(scenario_dir).resolve()
    rules_path = Path(rules).resolve()
    release_path = Path(release).resolve()
    runs_path = Path(runs_dir).resolve()
    database_path = Path(database).resolve()
    log_path = Path(experiment_log).resolve()

    if not scenario_path.is_dir():
        raise ValueError(f"scenario package does not exist: {scenario_path}")
    if not rules_path.is_file():
        raise ValueError(f"rules file does not exist: {rules_path}")
    if not release_path.is_file():
        raise ValueError(f"release file does not exist: {release_path}")
    if preview_stride < 1:
        raise ValueError("preview_stride must be at least 1")

    rules_payload = json.loads(rules_path.read_text(encoding="utf-8"))
    release_payload = json.loads(release_path.read_text(encoding="utf-8"))
    team_cap = min(
        float(rules_payload["max_team_connection_capacity_mw"]),
        float(release_payload["max_team_connection_capacity_mw"]),
    )
    max_generator_ratio = min(
        float(rules_payload["max_generator_to_connection_ratio"]),
        float(release_payload["max_generator_to_connection_ratio"]),
    )
    scenario_sha = sha256_directory(scenario_path)
    rules_sha = sha256_file(rules_path)
    release_sha = sha256_file(release_path)
    base_load_sha = ""
    if base_load_from is not None:
        base_load_path = Path(base_load_from).resolve()
        if not base_load_path.is_dir():
            raise ValueError(f"base-load output directory does not exist: {base_load_path}")
        base_load_sha = sha256_directory(base_load_path)

    git_revision_value = git_revision()
    horizon = int(release_payload.get("horizon", 120))
    results: list[dict[str, object]] = []

    for candidate_index, candidate in enumerate(candidate_plans, start=1):
        normalized = normalize_candidate_plan(
            candidate,
            default_team_id=team_id,
            week=week,
            submission=submission,
        )
        plan_name = str(normalized["plan_name"])
        run_id = str(uuid.uuid4())
        record_id = str(uuid.uuid4())
        timestamp = utc_timestamp()
        run_dir = runs_path / experiment_id / run_id
        run_dir.mkdir(parents=True, exist_ok=False)

        candidate_csv = run_dir / "candidate.csv"
        validation_json = run_dir / "validation.json"
        preview_dir = run_dir / "preview"
        preview_submissions = preview_dir / "submissions"
        preview_output = preview_dir / "preview.json"
        plan_json = run_dir / "plan.json"

        append_experiment_event(
            log_path,
            experiment_id=experiment_id,
            run_id=run_id,
            plan_name=plan_name,
            phase="generate",
            event_type="candidate_csv_started",
            status="started",
            message="Generating canonical candidate CSV",
            git_revision_value=git_revision_value,
            scenario_sha256=scenario_sha,
            rules_sha256=rules_sha,
            base_load_sha256=base_load_sha,
        )

        try:
            generate_submission_csv(normalized, candidate_csv)
        except (OSError, ValueError) as exc:
            append_experiment_event(
                log_path,
                experiment_id=experiment_id,
                run_id=run_id,
                plan_name=plan_name,
                phase="generate",
                event_type="candidate_csv_failed",
                status="failure",
                message=str(exc),
                git_revision_value=git_revision_value,
                scenario_sha256=scenario_sha,
                rules_sha256=rules_sha,
                base_load_sha256=base_load_sha,
            )
            raise

        plan_json.write_text(json.dumps(normalized, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        validation_report = validate_csv_submission(
            candidate_csv,
            artifact_dir=scenario_path,
            horizon=horizon,
            max_generator_to_connection_ratio=max_generator_ratio,
            max_team_connection_capacity_mw=team_cap,
        )
        validation_payload = validation_report.as_json()
        validation_json.write_text(json.dumps(validation_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        issues = [issue.display() for issue in validation_report.issues]

        append_experiment_event(
            log_path,
            experiment_id=experiment_id,
            run_id=run_id,
            plan_name=plan_name,
            phase="validate",
            event_type="csv_validation_completed",
            status="success" if validation_report.valid else "failure",
            message="CSV is valid" if validation_report.valid else "; ".join(issues),
            git_revision_value=git_revision_value,
            scenario_sha256=scenario_sha,
            rules_sha256=rules_sha,
            base_load_sha256=base_load_sha,
            candidate_csv_path=str(candidate_csv),
            validation_output_path=str(validation_json),
        )

        preview_payload: dict[str, object] = {}
        preview_started = time.monotonic()
        preview_status = "not_run"
        preview_exception = ""

        if validation_report.valid:
            preview_submissions.mkdir(parents=True)
            preview_candidate = preview_submissions / "candidate.csv"
            preview_candidate.write_bytes(candidate_csv.read_bytes())

            command = [
                sys.executable,
                "-m",
                "ercot_game.student_preview",
                "--submissions-dir",
                str(preview_submissions),
                "--artifact-dir",
                str(scenario_path),
                "--rules",
                str(rules_path),
                "--horizon",
                str(horizon),
                "--week",
                str(normalized["week"]),
                "--submission-number",
                str(normalized["submission"]),
                "--preview-stride",
                str(preview_stride),
                "--workers",
                "2",
                "--output",
                str(preview_output),
            ]
            if base_load_from is not None:
                command.extend(["--base-load-from", str(Path(base_load_from).resolve())])

            append_experiment_event(
                log_path,
                experiment_id=experiment_id,
                run_id=run_id,
                plan_name=plan_name,
                phase="preview",
                event_type="preview_started",
                status="started",
                message="Running student preview",
                git_revision_value=git_revision_value,
                scenario_sha256=scenario_sha,
                rules_sha256=rules_sha,
                base_load_sha256=base_load_sha,
                candidate_csv_path=str(candidate_csv),
                preview_output_path=str(preview_output),
            )

            try:
                completed = subprocess.run(
                    command,
                    cwd=REPOSITORY_ROOT,
                    capture_output=True,
                    text=True,
                    timeout=3600,
                )
                preview_elapsed = time.monotonic() - preview_started
                if completed.stdout:
                    (preview_dir / "preview.stdout.txt").write_text(completed.stdout, encoding="utf-8")
                if completed.stderr:
                    (preview_dir / "preview.stderr.txt").write_text(completed.stderr, encoding="utf-8")
                if completed.returncode == 0 and preview_output.is_file():
                    preview_payload = json.loads(preview_output.read_text(encoding="utf-8"))
                    preview_status = "success"
                else:
                    preview_status = "evaluator_failure"
                    preview_exception = completed.stderr.strip() or f"preview exited with status {completed.returncode}"
                    preview_payload = {
                        "mode": "student_preview",
                        "exact": False,
                        "warning": preview_exception,
                    }
                    preview_output.write_text(json.dumps(preview_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            except (OSError, subprocess.TimeoutExpired, json.JSONDecodeError) as exc:
                preview_elapsed = time.monotonic() - preview_started
                preview_status = "evaluator_failure"
                preview_exception = str(exc)
                preview_payload = {
                    "mode": "student_preview",
                    "exact": False,
                    "warning": preview_exception,
                }
                preview_output.write_text(json.dumps(preview_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

            append_experiment_event(
                log_path,
                experiment_id=experiment_id,
                run_id=run_id,
                plan_name=plan_name,
                phase="preview",
                event_type="preview_completed",
                status="success" if preview_status == "success" else "failure",
                elapsed_seconds=preview_elapsed,
                message="Preview completed" if preview_status == "success" else preview_exception,
                git_revision_value=git_revision_value,
                scenario_sha256=scenario_sha,
                rules_sha256=rules_sha,
                base_load_sha256=base_load_sha,
                candidate_csv_path=str(candidate_csv),
                preview_output_path=str(preview_output),
            )
        else:
            preview_elapsed = time.monotonic() - preview_started

        buses = _aggregate_by_bus(normalized, "connection_capacity_mw")
        generators = _aggregate_by_bus(normalized, "generator_capacity_mw")
        storage_power = _aggregate_by_bus(normalized, "storage_power_mw")
        storage_energy = _aggregate_by_bus(normalized, "storage_energy_mwh")
        total_connection = sum(float(site["connection_capacity_mw"]) for site in normalized["sites"])
        total_generator = sum(float(site["generator_capacity_mw"]) for site in normalized["sites"])
        total_storage_power = sum(float(site["storage_power_mw"]) for site in normalized["sites"])
        total_storage_energy = sum(float(site["storage_energy_mwh"]) for site in normalized["sites"])

        team_output = _preview_team_output(preview_payload, str(normalized["team_id"])) if preview_status == "success" else {}
        served_fraction = team_output.get("service_fraction")
        if not isinstance(served_fraction, (int, float)):
            served_fraction = preview_payload.get("service_fraction_by_team", {}).get(str(normalized["team_id"])) if isinstance(preview_payload, Mapping) else None
        if not isinstance(served_fraction, (int, float)):
            served_fraction = None
        else:
            served_fraction = float(served_fraction)

        requested_capacity = total_connection
        allocated_capacity = requested_capacity
        curtailment = 0.0
        if served_fraction is not None:
            allocated_capacity = requested_capacity * served_fraction
            curtailment = max(0.0, requested_capacity - allocated_capacity)

        projection = preview_payload.get("projection")
        allocation_triggered = isinstance(projection, Mapping) and bool(projection.get("applied"))
        if preview_status == "evaluator_failure":
            status = "evaluator_failure"
            evaluation_status = "evaluator_failure"
        elif not validation_report.valid:
            status = "invalid_plan"
            evaluation_status = "invalid_plan"
        else:
            status = "success"
            evaluation_status = "valid_preview"

        if preview_status != "success":
            score = None
            served_load = None
            it_value = None
            energy_cost = None
            generator_cost = None
            generator_capital = None
            storage_capital = None
            site_cost = None
        else:
            score = team_output.get("score")
            served_load = team_output.get("served_load_mwh")
            it_value = team_output.get("it_value")
            energy_cost = team_output.get("energy_cost")
            generator_cost = team_output.get("generator_operating_cost")
            generator_capital = team_output.get("generator_capital_cost")
            storage_capital = team_output.get("storage_capital_cost")
            site_cost = team_output.get("site_cost")

        raw_output_files = [candidate_csv]
        if preview_output.is_file():
            raw_output_files.append(preview_output)
        raw_output_sha = sha256_file(raw_output_files[-1]) if raw_output_files else ""

        congestion_indicators: dict[str, object] = {
            "preview_storage_dispatched": False,
            "projection_applied": allocation_triggered,
        }
        if isinstance(projection, Mapping):
            congestion_indicators.update({
                "dispatch_error": projection.get("dispatch_error"),
                "common_level_mw": projection.get("common_level_mw"),
                "dropped_team_ids": projection.get("dropped_team_ids"),
            })

        row = {
            "record_id": record_id,
            "experiment_id": experiment_id,
            "run_id": run_id,
            "timestamp_utc": timestamp,
            "plan_name": plan_name,
            "plan_source": normalized["plan_source"],
            "team_id": normalized["team_id"],
            "week": normalized["week"],
            "submission": normalized["submission"],
            "scenario_id": normalized["scenario_id"],
            "scenario_sha256": scenario_sha,
            "rules_sha256": rules_sha,
            "release_sha256": release_sha,
            "base_load_sha256": base_load_sha,
            "seed": normalized["seed"],
            "mode": "preview",
            "status": status,
            "valid": str(validation_report.valid).lower(),
            "allocation_triggered": str(allocation_triggered).lower(),
            "evaluation_status": evaluation_status,
            "candidate_csv_path": str(candidate_csv),
            "validation_output_path": str(validation_json),
            "preview_output_path": str(preview_output) if preview_output.is_file() else "",
            "official_output_path": "",
            "git_revision": git_revision_value,
            "buses_used_json": _json_text(sorted(buses)),
            "connection_capacity_mw_by_bus_json": _json_text(buses),
            "generator_capacity_mw_by_bus_json": _json_text(generators),
            "storage_power_mw_by_bus_json": _json_text(storage_power),
            "storage_energy_mwh_by_bus_json": _json_text(storage_energy),
            "total_connection_capacity_mw": total_connection,
            "total_generator_capacity_mw": total_generator,
            "total_storage_power_mw": total_storage_power,
            "total_storage_energy_mwh": total_storage_energy,
            "requested_capacity_mw": requested_capacity,
            "allocated_capacity_mw": allocated_capacity,
            "score_usd": "" if score is None else score,
            "served_load_mwh": "" if served_load is None else served_load,
            "served_fraction": "" if served_fraction is None else served_fraction,
            "it_value_usd": "" if it_value is None else it_value,
            "energy_cost_usd": "" if energy_cost is None else energy_cost,
            "generator_operating_cost_usd": "" if generator_cost is None else generator_cost,
            "generator_capital_cost_usd": "" if generator_capital is None else generator_capital,
            "storage_capital_cost_usd": "" if storage_capital is None else storage_capital,
            "site_cost_usd": "" if site_cost is None else site_cost,
            "alpha_min": "",
            "alpha_mean": "" if served_fraction is None else served_fraction,
            "alpha_max": "",
            "curtailment_mw": curtailment,
            "cpu_runtime_seconds": preview_elapsed,
            "peak_memory_gib": "",
            "binding_period_indices_json": "[]",
            "binding_branches_json": "[]",
            "congestion_indicators_json": _json_text(congestion_indicators),
            "maximum_branch_loading_pct": "",
            "maximum_generator_utilization_pct": "",
            "warning_text": preview_payload.get("warning", ""),
            "issues_json": _json_text(_preview_issues(preview_payload, issues)),
            "raw_output_sha256": raw_output_sha,
        }
        append_csv_row(database_path, RUN_DATABASE_COLUMNS, row)

        append_experiment_event(
            log_path,
            experiment_id=experiment_id,
            run_id=run_id,
            plan_name=plan_name,
            phase="database",
            event_type="run_database_appended",
            status="success",
            elapsed_seconds=preview_elapsed,
            message=f"Appended {database_path}",
            git_revision_value=git_revision_value,
            scenario_sha256=scenario_sha,
            rules_sha256=rules_sha,
            base_load_sha256=base_load_sha,
            candidate_csv_path=str(candidate_csv),
            validation_output_path=str(validation_json),
            preview_output_path=str(preview_output) if preview_output.is_file() else "",
        )
        results.append(row)

    return results


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run candidate ERCOT strategy previews and append results")
    parser.add_argument("--plans", required=True, help="JSON plan list, JSON object, or path to JSON")
    parser.add_argument("--experiment-id", default="strategy-experiment")
    parser.add_argument("--team-id", default="team-experiment")
    parser.add_argument("--week", type=int, choices=(1, 2, 3), default=2)
    parser.add_argument("--submission", type=int, choices=(1, 2), default=1)
    parser.add_argument("--scenario-dir", type=Path, default=DEFAULT_SCENARIO_DIR)
    parser.add_argument("--rules", type=Path, default=DEFAULT_RULES)
    parser.add_argument("--release", type=Path, default=DEFAULT_RELEASE)
    parser.add_argument("--base-load-from", type=Path)
    parser.add_argument("--runs-dir", type=Path, default=DEFAULT_RUNS_DIR)
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    parser.add_argument("--experiment-log", type=Path, default=DEFAULT_EXPERIMENT_LOG)
    parser.add_argument("--preview-stride", type=int, default=1)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        candidate_plans = load_candidate_plans(args.plans)
        manifest_payload: dict[str, object] = {}
        if isinstance(args.plans, str) and Path(args.plans).is_file():
            loaded = json.loads(Path(args.plans).read_text(encoding="utf-8"))
            if isinstance(loaded, Mapping):
                manifest_payload = dict(loaded)
        results = run_experiment(
            candidate_plans,
            experiment_id=str(manifest_payload.get("experiment_id", args.experiment_id)),
            team_id=str(manifest_payload.get("team_id", args.team_id)),
            week=int(manifest_payload.get("week", args.week)),
            submission=int(manifest_payload.get("submission", args.submission)),
            scenario_dir=manifest_payload.get("scenario_dir", args.scenario_dir),
            rules=manifest_payload.get("rules", args.rules),
            release=manifest_payload.get("release", args.release),
            base_load_from=manifest_payload.get("base_load_from", args.base_load_from),
            runs_dir=args.runs_dir,
            database=args.database,
            experiment_log=args.experiment_log,
            preview_stride=int(manifest_payload.get("preview_stride", args.preview_stride)),
        )
        print(f"Appended {len(results)} preview runs to {Path(args.database).resolve()}")
        return 0
    except (OSError, ValueError, KeyError, json.JSONDecodeError, subprocess.TimeoutExpired) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
