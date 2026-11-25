"""Score one new S2 plan against a fixed carried S1 base and reconstructed rivals."""

from __future__ import annotations

import argparse
import json
from dataclasses import replace
from pathlib import Path

from ercot_game.base_load import read_site_net_withdrawal, site_ids_by_team
from ercot_game.batch_evaluation import load_scoring_rules
from team_strategy.context import load_context
from team_strategy.contracts import RoundKey, Scenario, SiteProposal, Plan
from team_strategy.evaluation.campaign import BatchEvaluator
from week1_public_reconstruction import make_plans


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--repo", type=Path, required=True)
    p.add_argument("--public-csv", type=Path, required=True)
    p.add_argument("--s1-output", type=Path, required=True)
    p.add_argument("--s2-base", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--site", nargs=4, action="append", metavar=("BUS", "C", "G", "P"), required=True)
    p.add_argument("--energy-price", action="store_true", help="Charge hourly dispatch LMP as a Week 3-style counterfactual")
    args = p.parse_args()
    repo = args.repo.resolve()
    rows = read_site_net_withdrawal(args.s1_output / "evaluation/week-1-submission-1/canonical/site_net_withdrawal.csv")
    reserved = site_ids_by_team(rows)
    _, opponents = make_plans(args.public_csv)
    sites = [SiteProposal(bus, float(c), float(g), float(power), 4 * float(power))
             for bus, c, g, power in args.site]
    assert sum(site.connection_mw for site in sites) == 500
    context = load_context(
        release_file=repo / "configs/rounds/finalized_release_500mw.json",
        rules_file=repo / "configs/scoring/dispatch_scoring_rules_500mw.json",
        scenario_dir=args.s2_base.resolve(), round=RoundKey(1, 2),
        team_id="team07", seed=20261123, prior_site_ids=reserved["team07"],
    )
    if args.energy_price:
        context = replace(context, energy_cost_enabled=True)
    outcome = BatchEvaluator(args.output / "evaluation", workers=2,
                             solver_backend="highs", storage_solver="monolithic").evaluate_round(
        context=context, our_plan=Plan(tuple(sites)),
        scenario=Scenario("repeat-rivals", opponents, 20261123),
        reserved_by_team=reserved,
    )
    ours = next(s for s in outcome.summary["team_scores"] if s["team_id"] == "team07")
    rules = load_scoring_rules(context.rules_file, artifact_dir=context.scenario_dir, horizon=context.horizon)
    price_samples = {}
    weighted_grid_mwh = 0.0
    for bus in {site.bus_id for site in sites}:
        lmps = [max(0.0, float(period.dcopf.balance_dual_by_bus[bus]))
                for period in outcome.evaluation.dispatch.periods]
        price_samples[bus] = {"simple_mean_lmp_usd_per_mwh": sum(lmps) / len(lmps),
                              "max_lmp_usd_per_mwh": max(lmps)}
    for period in outcome.evaluation.dispatch.periods:
        weighted_grid_mwh += float(period.grid_purchase_mw_by_team.get("team07", 0.0)) * rules.weight_for(period.period_index)
    result = {
        "request": [{"bus": s.bus_id, "connection_mw": s.connection_mw,
                     "generator_mw": s.generator_mw, "storage_power_mw": s.storage_power_mw,
                     "storage_energy_mwh": s.storage_energy_mwh} for s in sites],
        "score_usd": ours["score"], "rank": ours["rank"],
        "allocated_mw": sum(a["allocated_connection_mw"] for a in outcome.summary["site_allocations"]),
        "site_allocations": outcome.summary["site_allocations"],
        "breakdown": outcome.summary["score_breakdown"],
        "class_allocated_mw": sum(sum(s.connection_capacity_mw for s in p.sites)
                                  for p in outcome.evaluation.evaluated_plans),
        "all_valid_feasible": all(s["valid"] and s["feasible"] for s in outcome.summary["team_scores"]),
        "competition_scope": outcome.summary["competition_scope"],
        "horizon": outcome.summary["horizon"],
        "energy_price_enabled": args.energy_price,
        "grid_energy_cost_usd": ours["energy_cost"],
        "energy_off_score_usd": ours["score"] + ours["energy_cost"],
        "weighted_grid_purchase_mwh": weighted_grid_mwh,
        "purchase_weighted_lmp_usd_per_mwh": ours["energy_cost"] / weighted_grid_mwh if weighted_grid_mwh else None,
        "lmp_by_bus": price_samples,
    }
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "candidate_summary.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("request", "allocated_mw", "score_usd", "rank", "class_allocated_mw")}), flush=True)


if __name__ == "__main__":
    main()
