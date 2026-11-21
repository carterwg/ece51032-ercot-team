"""Stage 5: directional fixed-load experiments, with shared supply loss separated.

I(i->j,q) = (HC_j - HC_j_after_q_at_i) / HC_j. The generation ceiling alone
can force a loss, even for electrically distant buses. The excess over that
lower bound is reported separately; neither quantity is a game allocation.
"""
from collections import defaultdict
import math
import random
import statistics
import sys

from .bottlenecks import HostingLP
from .stress_scenarios import add_loads


def interaction_metrics(before, after, q, generation_headroom):
    if any(not math.isfinite(x) for x in (before, after, q, generation_headroom)) or min(before, after) < 0 or q <= 0:
        raise ValueError("invalid capacities, load, or headroom")
    loss = before - after  # Negative is a measured benefit/counterflow, not an error.
    forced = max(0., before - max(0., generation_headroom - q))
    excess = max(0., loss - forced)
    return {"capacity_loss_mw": loss, "interaction_fraction": loss / before if before else None,
            "generation_forced_loss_floor_mw": forced,
            "transmission_excess_loss_mw": excess, "transmission_excess_per_added_mw": excess / q}


def select_pairs(groups, *, pair_count=96, seed=17):
    buses = groups["ptdf"]["bus_ids"]
    if len(buses) < 2 or type(pair_count) is not int or pair_count < math.ceil(len(buses) / 2):
        raise ValueError("pair budget must permit coverage of every candidate")
    index = {b: i for i, b in enumerate(buses)}
    distances = groups["normalized_ptdf_distances"]
    signatures = groups["signatures"]
    def shared(a, b): return bool(set(signatures[a]) & set(signatures[b]))
    def distance(a, b): return distances[index[a]][index[b]]
    def pair(a, b): return tuple(sorted((a, b)))
    chosen = {pair(a, b) for a, b in (("6062", "6298"), ("1079", "2054"),
                                     ("6141", "7414"), ("5413", "5317"), ("6141", "7346"))
              if a in index and b in index}
    uncovered = set(buses) - {b for p in chosen for b in p}
    while uncovered:
        a = min(uncovered)
        options = sorted(uncovered - {a}) or [b for b in buses if b != a]
        b = min(options, key=lambda b: (not shared(a, b), distance(a, b), b))
        chosen.add(pair(a, b)); uncovered -= {a, b}
    if len(chosen) > pair_count:
        raise ValueError("pair budget too small after required benchmarks and coverage")
    remaining = [(a, b) for i, a in enumerate(buses) for b in buses[i + 1:] if (a, b) not in chosen]
    random.Random(seed).shuffle(remaining)
    pools = {True: [p for p in remaining if shared(*p)], False: [p for p in remaining if not shared(*p)]}
    while len(chosen) < min(pair_count, len(buses) * (len(buses) - 1) // 2):
        counts = {kind: sum(shared(*p) == kind for p in chosen) for kind in pools}
        available = [kind for kind in pools if pools[kind]]
        if not available:
            break
        kind = min(available, key=lambda k: (counts[k], k))
        chosen.add(pools[kind].pop())
    return tuple(sorted(chosen))


def run_interactions(periods, baseline, groups, stress, *, pair_count=96, loads_mw=(250., 500.), seed=17,
                     validation_pairs=None, cached_records=()):
    if not loads_mw or len(set(loads_mw)) != len(loads_mw) or any(not math.isfinite(q) or not 0 < q <= 500 for q in loads_mw):
        raise ValueError("interaction loads must be distinct, finite, and in (0,500]")
    pairs = (select_pairs(groups, pair_count=pair_count, seed=seed) if validation_pairs is None
             else tuple(sorted(tuple(sorted(p)) for p in validation_pairs)))
    base = {r.bus_id: r.minimum_hosting_capacity_mw for r in baseline}
    if set(base) != set(groups["ptdf"]["bus_ids"]):
        raise ValueError("baseline and grouping candidates differ")
    if (len(set(pairs)) != len(pairs) or any(len(p) != 2 or p[0] == p[1] for p in pairs)
            or {b for p in pairs for b in p} != set(base)):
        raise ValueError("validation pairs must be distinct and cover all candidates")
    headroom = min(math.fsum(g.p_max_mw for g in p.generators)
                   + math.fsum(p.fixed_injection_mw_by_bus.values())
                   - math.fsum(b.demand_mw for b in p.buses) for p in periods)
    cache = {}
    measured = {}
    for record in cached_records:
        source, target, q = record["source_bus"], record["target_bus"], record["added_load_mw"]
        if source not in base or target not in base or abs(record["baseline_hosting_capacity_mw"] - base[target]) > 1e-4:
            raise ValueError("cached interaction baseline/candidates differ")
        value = record["residual_hosting_capacity_mw"]
        if not math.isfinite(value) or not 0 <= value <= max(0., headroom - q) + 1e-4:
            raise ValueError("cached residual violates the physical capacity bound")
        measured[source, target, q] = value
    for scenario in stress["scenarios"]:
        loads = scenario["background_loads_mw"]
        if scenario["status"] == "valid" and len(loads) == 1:
            source, q = next(iter(loads.items()))
            cache[source, q] = {b: c["minimum_hosting_capacity_mw"] for b, c in scenario["candidates"].items()}
    requests = defaultdict(set)
    for a, b in pairs:
        for q in loads_mw:
            requests[a, q].add(b); requests[b, q].add(a)
    model = HostingLP(periods[0], solver_backend=stress["solver"])
    cohort = {b: c["cohort_id"] for c in groups["refined_cohorts"] for b in c["members"]}
    initial = {b: i for i, members in enumerate(groups["initial_cohorts"]) for b in members}
    index = {b: i for i, b in enumerate(groups["ptdf"]["bus_ids"])}
    records = []
    for number, ((source, q), targets) in enumerate(sorted(requests.items()), 1):
        if q > base[source] + 1e-4:
            raise ValueError(f"source {source} cannot support the fixed {q:g} MW background")
        if (source, q) in cache:
            after = cache[source, q]
            reused = True
        else:
            after = {b: measured.get((source, b, q), math.inf) for b in targets}
            missing = {b for b in targets if (source, b, q) not in measured}
            if missing:
                for period in periods:
                    model.set_period(add_loads(period, {source: q}))
                    for target in sorted(missing):
                        after[target] = min(after[target], model.maximize(target))
            reused = False
        for target in sorted(targets):
            metrics = interaction_metrics(base[target], after[target], q, headroom)
            records.append({"source_bus": source, "target_bus": target, "added_load_mw": q,
                            "baseline_hosting_capacity_mw": base[target], "residual_hosting_capacity_mw": after[target],
                            "shared_signed_bottleneck": bool(set(groups["signatures"][source]) & set(groups["signatures"][target])),
                            "same_initial_cohort": initial[source] == initial[target],
                            "same_refined_cohort": cohort[source] == cohort[target],
                            "normalized_ptdf_distance": groups["normalized_ptdf_distances"][index[source]][index[target]],
                            "baseline_capacity_difference_mw": abs(base[source] - base[target]),
                            "reused_stress_scan": reused,
                            "reused_measurement": not reused and (source, target, q) in measured, **metrics})
        if number % 10 == 0 or number == len(requests):
            print(f"Interaction sources/sizes: {number}/{len(requests)}", file=sys.stderr)
    return {"seed": seed, "pairs": [list(p) for p in pairs], "loads_mw": list(loads_mw),
            "horizon": len(periods), "minimum_generation_headroom_mw": headroom, "records": records,
            "candidate_coverage": sorted({b for p in pairs for b in p})}


def summarize_validation(interactions, groups):
    """Descriptive sample comparisons; thresholds are explicit, not significance tests."""
    records = interactions["records"]
    def compare(rows, label):
        same = [r for r in rows if r[label]]
        other = [r for r in rows if not r[label]]
        def summary(values):
            excess = [r["transmission_excess_per_added_mw"] for r in values]
            return {"directed_test_count": len(values),
                    "unordered_pair_count": len({tuple(sorted((r["source_bus"], r["target_bus"]))) for r in values}),
                    "mean_raw_interaction": statistics.mean(r["interaction_fraction"] for r in values) if values else None,
                    "mean_excess_per_added_mw": statistics.mean(excess) if excess else None,
                    "median_excess_per_added_mw": statistics.median(excess) if excess else None,
                    "fraction_above_5pct_excess": sum(x > .05 for x in excess) / len(excess) if excess else None}
        a, b = summary(same), summary(other)
        enough = a["unordered_pair_count"] >= 3 and b["unordered_pair_count"] >= 3
        separation = (a["mean_excess_per_added_mw"] - b["mean_excess_per_added_mw"]
                      if same and other else None)
        status = ("supported_in_sample" if enough and separation > .02
                  else "not_separated_in_sample" if enough else "limited_evidence")
        return {"within": a, "across": b, "mean_excess_separation": separation, "status": status}
    comparisons = {}
    for q in interactions["loads_mw"]:
        selected = [r for r in records if r["added_load_mw"] == q]
        comparisons[str(q)] = {label: compare(selected, label) for label in
                               ("shared_signed_bottleneck", "same_initial_cohort", "same_refined_cohort")}
        comparisons[str(q)]["capacity_matched_shared_bottleneck"] = compare(
            [r for r in selected if r["baseline_capacity_difference_mw"] <= 150], "shared_signed_bottleneck")
    group_results = []
    for group in groups["overlapping_groups"]:
        members = set(group["members"])
        touching = [dict(r, in_this_group=r["source_bus"] in members and r["target_bus"] in members)
                    for r in records if r["source_bus"] in members or r["target_bus"] in members]
        group_results.append({"group_id": group["group_id"], "member_count": len(members),
                              **compare(touching, "in_this_group")})
    candidate_tests = {b: sum(r["source_bus"] == b or r["target_bus"] == b for r in records)
                       for b in interactions["candidate_coverage"]}
    return {"comparisons_by_added_load_mw": comparisons, "overlapping_group_validation": group_results,
            "candidate_test_counts": candidate_tests,
            "support_rule": "At least 3 unordered pairs on each side and within-minus-across excess/q > 0.02; descriptive only.",
            "sampling_note": "Deterministic coverage sample, group-balanced when originally selected; retained unchanged when backgrounds expand. Not population-random; directions and sizes are dependent."}
