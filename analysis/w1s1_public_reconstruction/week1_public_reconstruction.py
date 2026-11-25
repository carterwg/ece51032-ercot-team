"""Test a plausible reconstruction of Week 1 Submission 1 public bus totals."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from dataclasses import replace
from pathlib import Path

from team_strategy.context import load_context
from team_strategy.contracts import NamedPlan, Plan, RoundKey, Scenario, SiteProposal
from team_strategy.evaluation.campaign import BatchEvaluator


def plan(items):
    return Plan(tuple(SiteProposal(*item) for item in items))


def make_plans(public_csv: Path):
    rows = list(csv.DictReader(public_csv.open(newline="")))
    def buses(load, generator=0, storage=0):
        return [r["bus_id"] for r in rows if
                r["load_mw"] == load and r["generator_mw"] == generator and
                r["storage_power_mw"] == storage]

    five_mw_buses = buses("4.548", "0.000", "0.000") + ["1079"]
    twenty_mw_buses = [r["bus_id"] for r in rows if r["generator_mw"] == "1.000"]
    grid_hundred_buses = buses("90.967", "0.000", "0.000") + ["1079"]
    g20_buses = buses("100.000", "20.000", "0.000") + ["6197"]
    assert tuple(map(len, (five_mw_buses, twenty_mw_buses, grid_hundred_buses, g20_buses))) == (100, 25, 5, 5)

    opponents = (
        NamedPlan("rival-5mw-x100", plan((bus, 5, 0, 0, 0) for bus in five_mw_buses)),
        NamedPlan("rival-20mw-x25", plan((bus, 20, 1, 0, 0) for bus in twenty_mw_buses)),
        NamedPlan("rival-100mw-grid", plan((bus, 100, 0, 0, 0) for bus in grid_hundred_buses)),
        NamedPlan("rival-250mw-grid", plan((bus, 250, 0, 0, 0) for bus in ("3048", "6147"))),
        NamedPlan("rival-100mw-g20", plan((bus, 100, 20, 0, 0) for bus in g20_buses)),
        NamedPlan("rival-250mw-hybrid", plan((bus, 250, 175, 62.5, 250) for bus in ("5131", "6197"))),
        NamedPlan("rival-500mw-g350", plan((("6197", 500, 350, 0, 0),))),
        NamedPlan("rival-100mw-mixed", plan((bus, 100, g, 0, 0) for bus, g in
                                             (("2101", 25), ("6066", 10), ("7099", 50), ("8126", 100), ("6197", 0)))),
    )
    assert len(opponents) == 8
    return rows, opponents


def aggregate(evaluated_plans):
    by_bus = defaultdict(lambda: [0., 0., 0., 0.])
    for owner in evaluated_plans:
        for site in owner.sites:
            sums = by_bus[site.bus_id]
            sums[0] += site.connection_capacity_mw
            sums[1] += site.generator_capacity_mw
            sums[2] += site.storage_power_mw
            sums[3] += site.storage_energy_mwh
    return by_bus


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--repo", type=Path, required=True)
    p.add_argument("--public-csv", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--grid-only", action="store_true")
    p.add_argument("--energy-price", action="store_true", help="Charge hourly LMP as a Week 3-style counterfactual")
    args = p.parse_args()
    repo = args.repo.resolve()
    rows, opponents = make_plans(args.public_csv)
    context = load_context(
        release_file=repo / "configs/rounds/finalized_release_500mw.json",
        rules_file=repo / "configs/scoring/dispatch_scoring_rules_500mw.json",
        scenario_dir=repo / "ercot-connection-game/data/processed/activsg2000_representative_v1",
        round=RoundKey(1, 1), team_id="team07", seed=20261123,
    )
    if args.energy_price:
        context = replace(context, energy_cost_enabled=True)
    our_plan = plan((("6141", 500, 0, 0, 0),)) if args.grid_only else plan((("6141", 500, 97, 99, 396),))
    outcome = BatchEvaluator(args.output / "evaluation", workers=2,
                             solver_backend="highs", storage_solver="monolithic").evaluate_round(
        context=context, our_plan=our_plan,
        scenario=Scenario("public-reconstruction", opponents, 20261123))
    actual = aggregate(outcome.evaluation.evaluated_plans)
    deltas = []
    for row in rows:
        bus = row["bus_id"]
        expected = [float(row[k]) for k in ("load_mw", "generator_mw", "storage_power_mw", "storage_energy_mwh")]
        observed = actual.get(bus, [0.] * 4)
        deltas.append((max(abs(a - b) for a, b in zip(expected, observed)), bus, expected, observed))
    for bus, observed in actual.items():
        if bus not in {r["bus_id"] for r in rows}:
            deltas.append((max(observed), bus, [0.] * 4, observed))
    deltas.sort(reverse=True)
    result = {
        "grid_only": args.grid_only,
        "energy_price_enabled": args.energy_price,
        "our_allocated_mw": sum(a["allocated_connection_mw"] for a in outcome.summary["site_allocations"]),
        "our_score_usd": outcome.summary["score_usd"],
        "our_breakdown": outcome.summary["score_breakdown"],
        "class_allocated_mw": sum(s.connection_capacity_mw for p in outcome.evaluation.evaluated_plans for s in p.sites),
        "scores": [{k: s[k] for k in ("team_id", "rank", "score", "it_value", "energy_cost", "site_cost", "generator_capital_cost", "storage_capital_cost")}
                   for s in outcome.summary["team_scores"]],
        "max_public_bus_difference_mw": deltas[0][0],
        "largest_public_bus_differences": deltas[:10],
    }
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "reconstruction_summary.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("grid_only", "our_allocated_mw", "our_score_usd", "class_allocated_mw", "max_public_bus_difference_mw")}, indent=2), flush=True)
    print("top bus differences:", deltas[:5], flush=True)


if __name__ == "__main__":
    main()
