"""Use the instructor's canonical columns and deterministic round-specific IDs."""

import csv
import io
from pathlib import Path

from ercot_game.csv_submission import CANONICAL_CSV_COLUMNS

from ..contracts import Plan, PlanningContext


def site_ids(plan: Plan, context: PlanningContext) -> tuple[str, ...]:
    return tuple(
        f"w{context.round.week}-s{context.round.submission}-{index:04d}"
        for index in range(1, len(plan.sites) + 1)
    )


def plan_csv(plan: Plan, context: PlanningContext) -> str:
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(CANONICAL_CSV_COLUMNS)
    for site_id, site in zip(site_ids(plan, context), plan.sites):
        writer.writerow((
            context.team_id, site_id, site.bus_id, site.connection_mw,
            site.generator_mw, site.storage_power_mw, site.storage_energy_mwh,
        ))
    return output.getvalue()


def export_plan(plan: Plan, context: PlanningContext, path: Path) -> None:
    from ..validation import validate_plan

    report = validate_plan(plan, context)
    if not report.valid:
        raise ValueError("invalid plan: " + "; ".join(report.issues))
    # Never silently replace a previously frozen candidate or submission.
    with path.open("x", encoding="utf-8", newline="") as handle:
        handle.write(plan_csv(plan, context))
