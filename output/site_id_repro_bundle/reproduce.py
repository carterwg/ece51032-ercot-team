"""Separate CSV row order from site-ID assignment in an S2 dispatch tie."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
from pathlib import Path

from ercot_game.base_load import read_site_net_withdrawal, site_ids_by_team
from ercot_game.batch_evaluation import evaluate_csv_batch, load_scoring_rules


FOCAL_TEAM = "rival-100mw-mixed"


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or ()), list(reader)


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-inputs", type=Path, required=True)
    parser.add_argument("--s1-output", type=Path, required=True)
    parser.add_argument("--s2-base", type=Path, required=True)
    parser.add_argument("--rules", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    source_files = sorted(args.source_inputs.glob("*.csv"))
    assert len(source_files) == 9
    focal_source = next(path for path in source_files
                        if read_csv(path)[1][0]["team_id"] == FOCAL_TEAM)
    fields, original = read_csv(focal_source)
    assert len(original) == 5
    original_ids = [row["site_id"] for row in original]
    reserved = site_ids_by_team(read_site_net_withdrawal(
        args.s1_output / "evaluation/week-1-submission-1/canonical/site_net_withdrawal.csv"
    ))
    rules = load_scoring_rules(args.rules.resolve(), artifact_dir=args.s2_base.resolve(), horizon=120)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)

    for variant in ("original", "reverse_rows_only", "reverse_ids_only", "reverse_both"):
        case_dir = output / variant
        result_file = case_dir / "result.json"
        if result_file.exists():
            print(f"already complete: {variant}", flush=True)
            continue
        input_dir = case_dir / "inputs"
        input_dir.mkdir(parents=True, exist_ok=False)
        for source in source_files:
            shutil.copy2(source, input_dir / source.name)
        focal_file = input_dir / focal_source.name
        rows = [dict(row) for row in original]
        if variant in ("reverse_rows_only", "reverse_both"):
            rows.reverse()
        if variant in ("reverse_ids_only", "reverse_both"):
            for row, site_id in zip(rows, reversed(original_ids)):
                row["site_id"] = site_id
        write_csv(focal_file, fields, rows)
        evaluation = evaluate_csv_batch(
            input_dir, artifact_dir=args.s2_base.resolve(), horizon=120, rules=rules,
            dispatch_workers=2, storage_parallel_workers=2,
            storage_solver_backend="highs", storage_solver="benders",
            submission_number=2, energy_cost_enabled=False,
            reserved_site_ids_by_team=reserved,
        )
        scores = {score.team_id: score for score in evaluation.team_scores}
        assert len(scores) == 9 and all(score.valid and score.feasible for score in scores.values())
        assert evaluation.dispatch is not None and len(evaluation.dispatch.periods) == 120
        allocations = {plan.team_id: sum(site.connection_capacity_mw for site in plan.sites)
                       for plan in evaluation.evaluated_plans}
        assert all(abs(value - 500) < 1e-5 for value in allocations.values())
        result = {
            "variant": variant,
            "focal_rows": [{"site_id": row["site_id"], "bus_id": row["bus_id"]} for row in rows],
            "focal_score_usd": scores[FOCAL_TEAM].score,
            "focal_generator_operating_cost_usd": scores[FOCAL_TEAM].generator_operating_cost,
            "team07_score_usd": scores["team07"].score,
            "sum_nine_team_scores_usd": sum(score.score for score in scores.values()),
            "sum_120_hour_dispatch_objective_usd": sum(
                period.dcopf.objective_cost for period in evaluation.dispatch.periods
            ),
            "all_allocated_mw": allocations,
            "competition_scope": evaluation.competition_scope,
        }
        result_file.write_text(json.dumps(result, indent=2) + "\n")
        print(variant, "focal score", result["focal_score_usd"],
              "sum scores", result["sum_nine_team_scores_usd"], flush=True)


if __name__ == "__main__":
    main()
