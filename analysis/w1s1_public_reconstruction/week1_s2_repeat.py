"""Repeat reconstructed Week 1 S1 plans as new S2 sites using official carryover."""

from __future__ import annotations

import argparse
import json
from dataclasses import replace
from pathlib import Path

from ercot_game.base_load import (materialize_base_load_artifact, net_withdrawal_by_bus,
                                  read_site_net_withdrawal, site_ids_by_team)
from team_strategy.context import load_context
from team_strategy.contracts import RoundKey, Scenario, SiteProposal, Plan
from team_strategy.evaluation.campaign import BatchEvaluator
from week1_public_reconstruction import make_plans


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--repo", type=Path, required=True)
    p.add_argument("--public-csv", type=Path, required=True)
    p.add_argument("--s1-output", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--energy-price", action="store_true", help="Charge hourly LMP as a Week 3-style counterfactual")
    args = p.parse_args()
    repo = args.repo.resolve()
    out = args.output.resolve()
    source = repo / "ercot-connection-game/data/processed/activsg2000_representative_v1"
    rows = read_site_net_withdrawal(args.s1_output / "evaluation/week-1-submission-1/canonical/site_net_withdrawal.csv")
    reserved = site_ids_by_team(rows)
    assert len(reserved) == 9
    base_dir = out / "s2-base"
    manifest = materialize_base_load_artifact(
        source, net_withdrawal_by_bus(rows, 120), base_dir, validate=True, workers=2,
        provenance={"source": "reconstructed nine-team Week 1 Submission 1 full joint evaluation"},
    )
    print("S2 base validation:", manifest["validation_status"], flush=True)
    _, opponents = make_plans(args.public_csv)
    our_plan = Plan((SiteProposal("6141", 500, 97, 99, 396),))
    context = load_context(
        release_file=repo / "configs/rounds/finalized_release_500mw.json",
        rules_file=repo / "configs/scoring/dispatch_scoring_rules_500mw.json",
        scenario_dir=base_dir,
        round=RoundKey(1, 2), team_id="team07", seed=20261123,
        prior_site_ids=reserved["team07"],
    )
    if args.energy_price:
        context = replace(context, energy_cost_enabled=True)
    outcome = BatchEvaluator(out / "evaluation", workers=2,
                             solver_backend="highs", storage_solver="monolithic").evaluate_round(
        context=context, our_plan=our_plan,
        scenario=Scenario("repeat-s1-methodology-in-s2", opponents, 20261123),
        reserved_by_team=reserved,
    )
    scores = sorted(outcome.summary["team_scores"], key=lambda s: s["rank"])
    allocation = {p.team_id: sum(s.connection_capacity_mw for s in p.sites)
                  for p in outcome.evaluation.evaluated_plans}
    result = {
        "scenario": "All nine reconstructed teams request the same S1 buses, load and equipment as new S2 sites",
        "s1_base_source": str(args.s1_output),
        "s1_site_count": len({(r["team_id"], r["site_id"]) for r in rows}),
        "s2_base_validation_status": manifest["validation_status"],
        "scope": outcome.summary["competition_scope"],
        "energy_price_enabled": args.energy_price,
        "horizon": outcome.summary["horizon"],
        "all_valid_feasible": all(s["valid"] and s["feasible"] for s in scores),
        "class_new_allocation_mw": sum(allocation.values()),
        "scores": [{"rank": s["rank"], "team_id": s["team_id"], "new_allocated_mw": allocation[s["team_id"]],
                    "score_usd": s["score"], "it_value_usd": s["it_value"],
                    "grid_energy_cost_usd": s["energy_cost"],
                    "site_cost_usd": s["site_cost"],
                    "generator_capital_cost_usd": s["generator_capital_cost"],
                    "storage_capital_cost_usd": s["storage_capital_cost"],
                    "generator_operating_cost_usd": s["generator_operating_cost"]}
                   for s in scores],
    }
    out.mkdir(parents=True, exist_ok=True)
    (out / "repeat_s2_summary.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"class_new_allocation_mw": result["class_new_allocation_mw"],
                      "scores": [(s["rank"], s["team_id"], round(s["new_allocated_mw"], 6),
                                  round(s["score_usd"] / 1e9, 6)) for s in result["scores"]]}, indent=2), flush=True)


if __name__ == "__main__":
    main()
