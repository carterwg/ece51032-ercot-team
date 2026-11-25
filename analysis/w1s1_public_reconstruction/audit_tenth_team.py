"""Rank ten W1S1 teams after duplicating an inferred rival submission."""

import argparse
import json
from pathlib import Path

from team_strategy.context import load_context
from team_strategy.contracts import NamedPlan, RoundKey, Scenario
from team_strategy.evaluation.campaign import BatchEvaluator

from week1_public_reconstruction import make_plans, plan


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--ours", choices=("submitted", "g1"), required=True)
    parser.add_argument("--duplicate", default="rival-20mw-x25")
    args = parser.parse_args()
    repo = args.repo.resolve()
    _, rivals = make_plans(repo / "analysis/w1s1_public_reconstruction/new_installations_by_bus_w1s1.csv")
    original = next(r for r in rivals if r.team_id == args.duplicate)
    copy_id = f"{original.team_id}-copy"
    opponents = rivals + (NamedPlan(copy_id, original.plan),)
    context = load_context(
        release_file=repo / "configs/rounds/finalized_release_500mw.json",
        rules_file=repo / "configs/scoring/dispatch_scoring_rules_500mw.json",
        scenario_dir=repo / "ercot-connection-game/data/processed/activsg2000_representative_v1",
        round=RoundKey(1, 1), team_id="team07", seed=20261123,
    )
    ours = (plan((("6141", 500, 97, 99, 396),)) if args.ours == "submitted"
            else plan((("6141", 500, 1, 0, 0),)))
    outcome = BatchEvaluator(args.output / "evaluation", workers=2,
                             solver_backend="highs", storage_solver="monolithic").evaluate_round(
        context=context, our_plan=ours,
        scenario=Scenario("public-reconstruction-plus-duplicate", opponents, 20261123),
    )
    allocations = {p.team_id: sum(s.connection_capacity_mw for s in p.sites)
                   for p in outcome.evaluation.evaluated_plans}
    scores = sorted(outcome.summary["team_scores"], key=lambda row: row["rank"])
    result = {
        "ours": args.ours,
        "duplicate_of": original.team_id,
        "duplicate_team_id": copy_id,
        "all_teams_valid_feasible": all(s["valid"] and s["feasible"] for s in scores),
        "class_allocated_mw": sum(allocations.values()),
        "rankings": [
            {"rank": s["rank"], "team_id": s["team_id"],
             "allocated_mw": allocations[s["team_id"]], "score_usd": s["score"]}
            for s in scores
        ],
    }
    assert len(scores) == 10 and len(allocations) == 10
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "audit_summary.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2), flush=True)


if __name__ == "__main__":
    main()
