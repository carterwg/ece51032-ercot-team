"""Generate a validated candidate or compare supplied complete campaign scores."""

import argparse
import csv
from dataclasses import asdict
import json
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory

from .context import file_fingerprint, load_context, scenario_fingerprint
from .contracts import GRADED_ROUNDS, RoundKey
from .experiments.comparison import compare, frontier_names
from .experiments.scoring import ScoreBounds, combined_score_usd
from .strategies import build_strategy
from .settings import DEFAULT_RELEASE
from .submissions import export_plan


def _unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique_keys)


def _write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def _snapshot_source(output: Path) -> dict:
    package = Path(__file__).resolve().parent
    snapshot = output / "source" / "team_strategy"
    shutil.copytree(package, snapshot, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    repository = package.parents[1]
    project_file = repository / "pyproject.toml"
    if project_file.is_file():
        shutil.copyfile(project_file, output / "source" / "pyproject.toml")
    try:
        revision = subprocess.run(
            ["git", "-C", str(repository), "rev-parse", "HEAD"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        revision = None
    return {"git_revision": revision, "source_snapshot_sha256": scenario_fingerprint(output / "source")}


def _propose(args, output: Path) -> None:
    config = read_json(args.config)
    prior_ids = frozenset()
    if args.submission == 2 and args.prior_submission is None:
        raise ValueError("Submission 2 requires --prior-submission with our submitted S1 CSV")
    if args.prior_submission is not None:
        with args.prior_submission.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        if not rows or any(row.get("team_id") != args.team_id or not row.get("site_id") for row in rows):
            raise ValueError("prior submission must contain this team's site IDs")
        prior_ids = frozenset(row["site_id"] for row in rows)
    context = load_context(
        release_file=args.release, round=RoundKey(args.week, args.submission),
        team_id=args.team_id, scenario_dir=args.scenario_dir, rules_file=args.rules,
        connection_budget_mw=args.budget_mw, seed=args.seed, prior_site_ids=prior_ids,
    )
    strategy = build_strategy(config["strategy"], config.get("params", {}))
    plan = strategy.propose(context)
    candidate = output / "candidate.csv"
    export_plan(plan, context, candidate)
    _write_json(output / "config.json", config)
    bounds = ScoreBounds(context.connection_budget_mw)
    _write_json(output / "manifest.json", {
        **_snapshot_source(output),
        "kind": "validated_candidate_not_evaluated", "round": context.round.key,
        "team_id": context.team_id, "strategy": config["strategy"], "seed": context.seed,
        "connection_budget_mw": context.connection_budget_mw,
        "energy_cost_enabled": context.energy_cost_enabled,
        "scenario_dir": str(context.scenario_dir), "rules_file": str(context.rules_file),
        "scenario_sha256": context.scenario_fingerprint, "rules_sha256": context.rules_fingerprint,
        "release_file": str(args.release.resolve()), "release_sha256": file_fingerprint(args.release),
        "prior_submission_sha256": file_fingerprint(args.prior_submission) if args.prior_submission else None,
        "candidate_sha256": file_fingerprint(candidate),
        "comparison_bounds_billions": {"lower": bounds.lower_billions, "upper": bounds.upper_billions},
        "normalization_assumption": "full new budget in each of four graded submissions",
    })
    _write_json(output / "validation.json", {"valid": True, "issues": [], "official_csv_checker": True})


def _report(args, output: Path) -> None:
    payload = read_json(args.input)
    bounds = ScoreBounds(payload["capacity_per_submission_mw"])
    graded_keys = {round.key: round for round in GRADED_ROUNDS}
    totals = {}
    for strategy, scenarios in payload["strategies"].items():
        totals[strategy] = {}
        for scenario, scores in scenarios.items():
            if set(scores) != set(graded_keys):
                raise ValueError(f"{strategy}/{scenario}: exactly four graded round scores required")
            totals[strategy][scenario] = combined_score_usd({graded_keys[key]: value for key, value in scores.items()})
    summaries = compare(totals, bounds)
    frontier = frontier_names(summaries)
    rows = [{**asdict(item), "on_frontier": item.name in frontier} for item in summaries]
    _write_json(output / "input.json", payload)
    _write_json(output / "comparison.json", {
        "capacity_per_submission_mw": bounds.capacity_per_submission_mw,
        "bounds_billions": {"lower": bounds.lower_billions, "upper": bounds.upper_billions},
        "normalization": "unclipped; four graded submissions; USD inputs converted to billions",
        "downside_risk": "sqrt(mean(min(Q - mean(Q), 0)^2)); equally weighted scenarios",
        "campaign_scores_usd": totals, "strategies": rows,
    })
    with (output / "comparison.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    if args.plot:
        from .experiments.plotting import plot_frontier
        plot_frontier(summaries, bounds, output / "frontier.png")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    propose = subparsers.add_parser("propose", help="generate and validate one strategy candidate")
    propose.add_argument("--config", required=True, type=Path)
    propose.add_argument("--team-id", required=True)
    propose.add_argument("--week", required=True, type=int, choices=(1, 2, 3))
    propose.add_argument("--submission", required=True, type=int, choices=(1, 2))
    propose.add_argument("--release", type=Path, default=DEFAULT_RELEASE)
    propose.add_argument("--scenario-dir", type=Path)
    propose.add_argument("--rules", type=Path)
    propose.add_argument("--prior-submission", type=Path)
    propose.add_argument("--budget-mw", type=float)
    propose.add_argument("--seed", type=int, default=0)
    propose.add_argument("--output-dir", required=True, type=Path)
    report = subparsers.add_parser("report", help="compare supplied complete campaign scores")
    report.add_argument("--input", required=True, type=Path)
    report.add_argument("--output-dir", required=True, type=Path)
    report.add_argument("--plot", action="store_true")
    args = parser.parse_args(argv)
    try:
        target = args.output_dir.resolve()
        if target.exists():
            raise ValueError(f"output directory already exists: {target}; choose a new run ID")
        target.parent.mkdir(parents=True, exist_ok=True)
        with TemporaryDirectory(prefix=".team-run-", dir=target.parent) as directory:
            staging = Path(directory) / "result"
            staging.mkdir()
            if args.command == "propose":
                _propose(args, staging)
            else:
                _report(args, staging)
            staging.rename(target)
        print(f"Wrote {args.command} outputs to {target}")
        return 0
    except (OSError, ValueError, KeyError, TypeError, ImportError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
