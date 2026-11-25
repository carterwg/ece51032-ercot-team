"""Vary one full-generation rival's five S2 buses in the reconstructed W1 field."""

from __future__ import annotations

import argparse
import csv
import json
import random
from pathlib import Path

from ercot_game.base_load import read_site_net_withdrawal, site_ids_by_team
from team_strategy.context import load_context
from team_strategy.contracts import NamedPlan, Plan, RoundKey, Scenario, SiteProposal
from team_strategy.evaluation.campaign import BatchEvaluator
from week1_public_reconstruction import make_plans


FOCAL_TEAM = "rival-100mw-mixed"
ORIGINAL_BUSES = ("2101", "6066", "7099", "8126", "6197")


def candidates(repo: Path, *, canonical_order: bool = False) -> list[tuple[str, tuple[str, ...]]]:
    with (repo / "analysis/hosting_capacity_all_buses.csv").open(newline="") as handle:
        hosting = {row["bus_id"]: float(row["min_hosting_capacity_mw"])
                   for row in csv.DictReader(handle)}
    with (repo / "analysis/bus_screening_metrics.csv").open(newline="") as handle:
        screen = [row["bus_id"] for row in csv.DictReader(handle)]
    eligible = sorted((bus for bus, mw in hosting.items() if mw >= 2500),
                      key=lambda bus: (-hosting[bus], bus))
    eligible_set = set(eligible)
    assert len(eligible) >= 50
    assert all(hosting[bus] >= 2500 for bus in ORIGINAL_BUSES)

    result: list[tuple[str, tuple[str, ...]]] = []
    seen: set[tuple[str, ...]] = set()

    def add(name: str, buses: tuple[str, ...]) -> None:
        if canonical_order:
            buses = tuple(sorted(buses))
        assert len(buses) == len(set(buses)) == 5
        assert all(bus in eligible_set for bus in buses)
        if buses not in seen:
            result.append((name, buses))
            seen.add(buses)

    add("original", ORIGINAL_BUSES)
    add("original_reversed", tuple(reversed(ORIGINAL_BUSES)))
    add("original_rotated", ORIGINAL_BUSES[1:] + ORIGINAL_BUSES[:1])
    add("top5_hosting", tuple(eligible[:5]))
    add("top5_screening", tuple(bus for bus in screen if bus in eligible_set)[:5])
    add("bottom5_among_2500plus", tuple(reversed(eligible[-5:])))
    for prefix in ("5", "6", "7"):
        add(f"cluster_prefix_{prefix}", tuple(bus for bus in eligible if bus.startswith(prefix))[:5])
    for label, prefixes in (("spread_25678", "25678"), ("spread_23568", "23568")):
        add(label, tuple(next(bus for bus in eligible if bus.startswith(prefix)) for prefix in prefixes))
    for i in range(5):
        replacement = next(bus for bus in eligible if bus not in ORIGINAL_BUSES)
        buses = list(ORIGINAL_BUSES)
        buses[i] = replacement
        add(f"replace_original_site_{i+1}", tuple(buses))

    rng = random.Random(20261124)
    for i in range(20):
        add(f"random_high_hosting_{i+1:02d}", tuple(rng.sample(eligible, 5)))
    for i in range(20):
        prefixes = rng.sample(("2", "3", "5", "6", "7", "8"), 5)
        buses = tuple(rng.choice([bus for bus in eligible if bus.startswith(prefix)])
                      for prefix in prefixes)
        add(f"random_spread_{i+1:02d}", buses)
    for name, buses in (
        ("best_set", ("7098", "5047", "7042", "6141", "6197")),
        ("worst_set", ("5388", "5295", "5380", "5304", "5395")),
    ):
        add(f"{name}_reversed", tuple(reversed(buses)))
        add(f"{name}_rotated", buses[1:] + buses[:1])
        add(f"{name}_sorted", tuple(sorted(buses)))
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--public-csv", type=Path, required=True)
    parser.add_argument("--s1-output", type=Path, required=True)
    parser.add_argument("--s2-base", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--canonical-order", action="store_true")
    args = parser.parse_args()

    repo = args.repo.resolve()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    portfolios = candidates(repo, canonical_order=args.canonical_order)
    manifest = {
        "scenario": "nine-team reconstructed W1S2; only focal team's five buses vary",
        "focal_team": FOCAL_TEAM,
        "focal_site_plan": "five separate C100/G100/P0/B0 sites",
        "team07_plan": "one C500/G500/P0/B0 site at bus 6141",
        "other_rivals": "same inferred S1 bus layouts and connection capacities, each new S2 site G=C and no storage",
        "s2_base": str(args.s2_base.resolve()),
        "selection": "all tested buses had at least 2500 MW standalone S1 hosting capacity; 40 seeded random cases plus defined controls and substitutions",
        "canonical_order": args.canonical_order,
        "portfolios": [{"name": name, "buses": buses} for name, buses in portfolios],
    }
    (output / "candidate_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    _, original_rivals = make_plans(args.public_csv)
    base_rivals = {
        rival.team_id: Plan(tuple(SiteProposal(site.bus_id, site.connection_mw,
                                               site.connection_mw, 0, 0)
                                  for site in rival.plan.sites))
        for rival in original_rivals
    }
    assert len(base_rivals) == 8 and FOCAL_TEAM in base_rivals
    s1_rows = read_site_net_withdrawal(
        args.s1_output / "evaluation/week-1-submission-1/canonical/site_net_withdrawal.csv"
    )
    reserved = site_ids_by_team(s1_rows)
    assert set(reserved) == {"team07", *base_rivals}
    context = load_context(
        release_file=repo / "configs/rounds/finalized_release_500mw.json",
        rules_file=repo / "configs/scoring/dispatch_scoring_rules_500mw.json",
        scenario_dir=args.s2_base.resolve(), round=RoundKey(1, 2),
        team_id="team07", seed=20261124, prior_site_ids=reserved["team07"],
    )
    our_plan = Plan((SiteProposal("6141", 500, 500, 0, 0),))

    for index, (name, buses) in enumerate(portfolios, start=1):
        case_dir = output / name
        result_file = case_dir / "case.json"
        if result_file.exists():
            print(f"{index}/{len(portfolios)} already complete: {name}", flush=True)
            continue
        rivals = tuple(
            NamedPlan(
                team_id,
                Plan(tuple(SiteProposal(bus, 100, 100, 0, 0) for bus in buses))
                if team_id == FOCAL_TEAM else plan,
            )
            for team_id, plan in base_rivals.items()
        )
        outcome = BatchEvaluator(case_dir / "evaluation", workers=2,
                                 solver_backend="highs").evaluate_round(
            context=context, our_plan=our_plan,
            scenario=Scenario(name, rivals, 20261124),
            reserved_by_team=reserved,
        )
        scores = {score["team_id"]: score for score in outcome.summary["team_scores"]}
        if not all(score["valid"] and score["feasible"] for score in scores.values()):
            raise RuntimeError(f"invalid or infeasible score for {name}")
        allocations = {
            owner.team_id: sum(site.connection_capacity_mw for site in owner.sites)
            for owner in outcome.evaluation.evaluated_plans
        }
        result = {
            "name": name,
            "buses": buses,
            "canonical_order": args.canonical_order,
            "focal_team": FOCAL_TEAM,
            "focal_allocated_mw": allocations[FOCAL_TEAM],
            "focal_score_usd": scores[FOCAL_TEAM]["score"],
            "focal_rank": scores[FOCAL_TEAM]["rank"],
            "focal_generator_operating_cost_usd": scores[FOCAL_TEAM]["generator_operating_cost"],
            "team07_allocated_mw": allocations["team07"],
            "team07_score_usd": scores["team07"]["score"],
            "team07_rank": scores["team07"]["rank"],
            "all_team_allocations_mw": allocations,
            "all_valid_feasible": True,
            "competition_scope": outcome.summary["competition_scope"],
            "horizon": outcome.summary["horizon"],
        }
        case_dir.mkdir(parents=True, exist_ok=True)
        result_file.write_text(json.dumps(result, indent=2) + "\n")
        print(f"{index}/{len(portfolios)} {name}: "
              f"focal ${result['focal_score_usd']/1e9:.6f}B rank {result['focal_rank']}, "
              f"allocated {result['focal_allocated_mw']:.6f} MW", flush=True)


if __name__ == "__main__":
    main()
