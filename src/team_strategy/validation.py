"""Delegate game legality to the instructor checker; add team workflow checks."""

from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory

from ercot_game.csv_validator import validate_csv_submission

from .context import assert_inputs_current
from .contracts import Plan, PlanningContext
from .submissions.csv_export import plan_csv, site_ids


@dataclass(frozen=True)
class PlanValidation:
    issues: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.issues


def validate_plan(plan: Plan, context: PlanningContext) -> PlanValidation:
    try:
        assert_inputs_current(context)
    except ValueError as exc:
        return PlanValidation((str(exc),))
    issues = []
    repeated = set(site_ids(plan, context)) & context.prior_site_ids
    if repeated:
        issues.append("site IDs repeat prior submitted sites: " + ", ".join(sorted(repeated)))
    with TemporaryDirectory(prefix="team-plan-check-") as directory:
        csv_file = Path(directory) / "candidate.csv"
        csv_file.write_text(plan_csv(plan, context), encoding="utf-8")
        official = validate_csv_submission(
            csv_file, artifact_dir=context.scenario_dir,
            max_generator_to_connection_ratio=context.max_generator_to_connection_ratio,
            max_team_connection_capacity_mw=context.connection_budget_mw,
            horizon=context.horizon,
        )
        issues.extend(issue.display() for issue in official.issues)
    return PlanValidation(tuple(issues))
