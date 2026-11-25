"""Sweep our S2 generator with rivals fully generating at their inferred S1 buses."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from ercot_game.base_load import read_site_net_withdrawal, site_ids_by_team
from team_strategy.context import load_context
from team_strategy.contracts import NamedPlan, Plan, RoundKey, Scenario, SiteProposal
from team_strategy.evaluation.campaign import BatchEvaluator
from week1_public_reconstruction import make_plans


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--public-csv", type=Path, required=True)
    parser.add_argument("--s1-output", type=Path, required=True)
    parser.add_argument("--s2-base", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--mode", choices=("fixed500", "matched", "both"), default="both")
    parser.add_argument("--generator", type=int, choices=(100, 200, 300, 400, 500))
    parser.add_argument("--reverse-rivals", action="store_true")
    args = parser.parse_args()

    repo = args.repo.resolve()
    output = args.output.resolve()
    _, original_rivals = make_plans(args.public_csv)
    rivals = tuple(
        NamedPlan(
            rival.team_id,
            Plan(tuple(
                SiteProposal(site.bus_id, site.connection_mw, site.connection_mw, 0, 0)
                for site in rival.plan.sites
            )),
        )
        for rival in original_rivals
    )
    if args.reverse_rivals:
        rivals = tuple(reversed(rivals))
    s1_rows = read_site_net_withdrawal(
        args.s1_output / "evaluation/week-1-submission-1/canonical/site_net_withdrawal.csv"
    )
    reserved = site_ids_by_team(s1_rows)
    assert set(reserved) == {"team07", *(rival.team_id for rival in rivals)}
    context = load_context(
        release_file=repo / "configs/rounds/finalized_release_500mw.json",
        rules_file=repo / "configs/scoring/dispatch_scoring_rules_500mw.json",
        scenario_dir=args.s2_base.resolve(),
        round=RoundKey(1, 2), team_id="team07", seed=20261124,
        prior_site_ids=reserved["team07"],
    )

    modes = ("fixed500", "matched") if args.mode == "both" else (args.mode,)
    generator_values = (args.generator,) if args.generator is not None else (100, 200, 300, 400, 500)
    for mode in modes:
        for generator_mw in generator_values:
            connection_mw = 500 if mode == "fixed500" else generator_mw
            case_dir = output / f"{mode}_g{generator_mw}"
            result_path = case_dir / "case.json"
            if result_path.exists():
                print(f"already complete: {result_path}", flush=True)
                continue
            plan = Plan((SiteProposal("6141", connection_mw, generator_mw, 0, 0),))
            canonical = case_dir / "evaluation/week-1-submission-2/canonical/evaluation.json"
            outcome = None
            if not canonical.exists():
                try:
                    outcome = BatchEvaluator(case_dir / "evaluation", workers=2,
                                             solver_backend="highs").evaluate_round(
                        context=context, our_plan=plan,
                        scenario=Scenario("rivals-repeat-s1-buses-with-full-generation", rivals, 20261124),
                        reserved_by_team=reserved,
                    )
                except RuntimeError:
                    if not canonical.exists():
                        raise
            if outcome is None:
                evaluator_result = json.loads(canonical.read_text())
                scores = evaluator_result["team_scores"]
                our_score = next(score for score in scores if score["team_id"] == "team07")
                if not our_score["valid"] or our_score["feasible"]:
                    raise RuntimeError("unexpected incomplete evaluation; inspect canonical output")
                allocated_mw = 0.0 if our_score["served_load_mwh"] == 0.0 else None
                class_allocated_mw = None
                rival_allocations = None
                scope = our_score["competition_scope"]
                breakdown = None
                failure_reason = our_score["failure_reason"]
            else:
                scores = outcome.summary["team_scores"]
                our_score = next(score for score in scores if score["team_id"] == "team07")
                allocated = {
                    owner.team_id: sum(site.connection_capacity_mw for site in owner.sites)
                    for owner in outcome.evaluation.evaluated_plans
                }
                allocated_mw = allocated["team07"]
                class_allocated_mw = sum(allocated.values())
                rival_allocations = {k: v for k, v in allocated.items() if k != "team07"}
                scope = outcome.summary["competition_scope"]
                breakdown = outcome.summary["score_breakdown"]
                failure_reason = None
            result = {
                "mode": mode,
                "our_request": {"bus_id": "6141", "connection_mw": connection_mw,
                                "generator_mw": generator_mw, "storage_power_mw": 0},
                "rival_assumption": "Eight inferred W1S1 teams request the same S1 site capacities and buses as new S2 sites, with G=C and no storage at every site",
                "rival_input_order": "reversed" if args.reverse_rivals else "original",
                "base_assumption": "Reconstructed nine-team W1S1 hourly net withdrawals carried into S2",
                "our_allocated_mw": allocated_mw,
                "our_score_usd": our_score["score"],
                "our_rank": our_score["rank"],
                "class_allocated_mw": class_allocated_mw,
                "rival_allocations_mw": rival_allocations,
                "all_valid_feasible": all(score["valid"] and score["feasible"] for score in scores),
                "competition_scope": scope,
                "horizon": context.horizon,
                "score_breakdown": breakdown,
                "our_feasible": our_score["feasible"],
                "failure_reason": failure_reason,
            }
            case_dir.mkdir(parents=True, exist_ok=True)
            result_path.write_text(json.dumps(result, indent=2) + "\n")
            print(json.dumps({k: result[k] for k in ("mode", "our_request", "our_allocated_mw",
                                                     "our_score_usd", "our_rank", "class_allocated_mw")}), flush=True)


if __name__ == "__main__":
    main()
