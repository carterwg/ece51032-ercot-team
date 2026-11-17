"""Load round settings from the release and fingerprint the planning inputs."""

import hashlib
import json
from pathlib import Path

from ercot_game.csv_submission import load_bus_ids
from ercot_game.scenario_package import require_validated_block

from .contracts import PlanningContext, RoundKey
from .settings import FINALIZED_CAPACITY_MW


def file_fingerprint(path: Path) -> str:
    """Reads a file and computes a SHA-256 hash—a content identifier.
        We use this to record exactly which scoring-rules file an experiment used. 
        Changing the file's contents changes its fingerprint."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def scenario_fingerprint(directory: Path) -> str:
    """ A scenario contains multiple files, so this function:
        1. Finds every file inside the directory.
        2. Sorts them into a consistent order.
        3. Hashes each file's relative name and contents.
        4. Combines those into one fingerprint."""
    digest = hashlib.sha256()
    files = sorted(p for p in directory.rglob("*") if p.is_file())
    if not files:
        raise ValueError(f"scenario package is empty: {directory}")
    for path in files:
        digest.update(path.relative_to(directory).as_posix().encode() + b"\0")
        digest.update(bytes.fromhex(file_fingerprint(path)))
    return digest.hexdigest()


def load_context(
    *,
    release_file: Path,
    round: RoundKey,
    team_id: str,
    scenario_dir: Path | None = None,
    rules_file: Path | None = None,
    connection_budget_mw: float | None = None,
    seed: int = 0,
    prior_site_ids: frozenset[str] = frozenset(),
) -> PlanningContext:
    release_file = release_file.resolve()
    release = json.loads(release_file.read_text())
    # Release paths are relative to the package root (two levels above its folder).
    course_root = release_file.parents[2]
    scenario = (scenario_dir or course_root / release["scenario_package"]).resolve()
    rules_path = (rules_file or course_root / release["scoring_rules"]).resolve()
    rules = json.loads(rules_path.read_text())
    manifest = require_validated_block(scenario)
    if round.submission == 2 and "submission_2_base_load" not in manifest:
        raise ValueError("Submission 2 requires an explicitly supplied carried-base-load package")
    if round.submission == 1 and "submission_2_base_load" in manifest:
        raise ValueError("Submission 1 must start from the weekly reset base package")
    cap = min(
        FINALIZED_CAPACITY_MW,
        float(release["max_team_connection_capacity_mw"]),
        float(rules["max_team_connection_capacity_mw"]),
    )
    budget = cap if connection_budget_mw is None else connection_budget_mw
    if budget > cap:
        raise ValueError(f"requested budget {budget} MW exceeds finalized cap {cap} MW")
    week = next(w for w in release["weeks"] if w["week_id"] == f"week-{round.week}")
    return PlanningContext(
        round=round, team_id=team_id, connection_budget_mw=budget,
        max_generator_to_connection_ratio=min(
            float(release["max_generator_to_connection_ratio"]),
            float(rules["max_generator_to_connection_ratio"]),
        ),
        energy_cost_enabled=bool(week["energy_cost_enabled"]),
        scenario_dir=scenario, rules_file=rules_path,
        scenario_fingerprint=scenario_fingerprint(scenario),
        rules_fingerprint=file_fingerprint(rules_path),
        bus_ids=load_bus_ids(scenario), horizon=int(manifest["horizon"]),
        seed=seed, prior_site_ids=prior_site_ids,
    )


def assert_inputs_current(context: PlanningContext) -> None:
    if scenario_fingerprint(context.scenario_dir) != context.scenario_fingerprint:
        raise ValueError("scenario package changed since context creation")
    if file_fingerprint(context.rules_file) != context.rules_fingerprint:
        raise ValueError("scoring rules changed since context creation")
