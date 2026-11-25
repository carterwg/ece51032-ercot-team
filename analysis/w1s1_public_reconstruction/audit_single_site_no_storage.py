"""Compare single-bus, generator-only S1 plans in the reconstructed public field."""

import argparse
import json
from pathlib import Path

from team_strategy.context import load_context
from team_strategy.contracts import RoundKey, Scenario
from team_strategy.evaluation.campaign import BatchEvaluator

from week1_public_reconstruction import make_plans, plan


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--generator", type=int, required=True)
    args = parser.parse_args()
    repo = args.repo.resolve()
    _, rivals = make_plans(repo / "analysis/w1s1_public_reconstruction/new_installations_by_bus_w1s1.csv")
    context = load_context(
        release_file=repo / "configs/rounds/finalized_release_500mw.json",
        rules_file=repo / "configs/scoring/dispatch_scoring_rules_500mw.json",
        scenario_dir=repo / "ercot-connection-game/data/processed/activsg2000_representative_v1",
        round=RoundKey(1, 1), team_id="team07", seed=20261123,
    )
    outcome = BatchEvaluator(args.output / "evaluation", workers=2,
                             solver_backend="highs", storage_solver="monolithic").evaluate_round(
        context=context,
        our_plan=plan((("6141", 500, args.generator, 0, 0),)),
        scenario=Scenario("public-reconstruction", rivals, 20261123),
    )
    result = {
        "plan": {"bus": "6141", "connection_mw": 500, "generator_mw": args.generator,
                 "storage_power_mw": 0},
        "allocated_mw": sum(s["allocated_connection_mw"] for s in outcome.summary["site_allocations"]),
        "score_usd": outcome.summary["score_usd"],
        "rank": next(s["rank"] for s in outcome.summary["team_scores"] if s["team_id"] == "team07"),
        "team_scores": outcome.summary["team_scores"],
    }
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "audit_summary.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("plan", "allocated_mw", "score_usd", "rank")}), flush=True)


if __name__ == "__main__":
    main()
