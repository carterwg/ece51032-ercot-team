"""Stage 4: overlapping signed-constraint groups and PTDF refinement.

A system-wide generation ceiling is shared by ALL buses, so it is metadata,
not a transmission cluster. PTDFs use a common reference injection convention;
candidate differences do not depend on which common slack bus is selected.
"""
from collections import defaultdict
import math

import numpy as np


def signature_features(stress):
    valid = [s for s in stress["scenarios"] if s["status"] == "valid"]
    if not valid:
        raise ValueError("no valid stress scenarios")
    buses = sorted(valid[0]["candidates"])
    features = {b: defaultdict(float) for b in buses}
    evidence = defaultdict(lambda: defaultdict(set))
    for scenario in valid:
        if sorted(scenario["candidates"]) != buses:
            raise ValueError("candidate sets differ across stress scenarios")
        name = scenario["scenario"]["name"]
        for bus, result in scenario["candidates"].items():
            diagnoses = result["diagnoses"]
            if not diagnoses:
                raise ValueError("missing limiting-period diagnoses")
            # Each scenario has total weight one, regardless of how many hours tie.
            for diagnosis in diagnoses:
                for line in diagnosis["tight_lines"]:
                    if not line["materially_limiting"]:
                        continue
                    key = f"{line['branch_id']}:{line['direction']}"
                    features[bus][key] += 1 / len(diagnoses) / len(valid)
                    evidence[key][bus].add(f"hosting_limit:{name}")
            for key, record in result["near_lines"].items():
                features[bus][key] += len(record["periods"]) / len(stress["operating_periods"]) / len(valid)
                evidence[key][bus].add(f"actual_request:{name}")
    return ({bus: dict(values) for bus, values in features.items()},
            {key: {bus: sorted(names) for bus, names in members.items()}
             for key, members in evidence.items()})


def jaccard(left, right):
    """Empty signatures supply no evidence of similarity."""
    a, b = set(left), set(right)
    return len(a & b) / len(a | b) if a | b else 0.


def ptdf_features(period, bus_ids, critical_signatures, *, reference_bus=None):
    """Solve the DC susceptance system once for all candidate columns.

    Rows are signed flow changes per MW of ADDED LOAD, balanced at the common
    reference. Rating-normalized values describe line-capacity use per MW.
    Absolute load impacts depend on balancing; column differences do not.
    """
    ids = [b.bus_id for b in period.buses]
    if len(set(bus_ids)) != len(bus_ids) or set(bus_ids) - set(ids):
        raise ValueError("PTDF candidates must be distinct known buses")
    reference = reference_bus or next((b.bus_id for b in period.buses if b.reference), ids[0])
    if reference not in ids:
        raise ValueError("unknown PTDF reference bus")
    index = {b: i for i, b in enumerate(ids)}
    matrix = np.zeros((len(ids), len(ids)))
    branches = {b.branch_id: b for b in period.branches}
    for line in period.branches:
        a, b, value = index[line.from_bus_id], index[line.to_bus_id], line.susceptance_pu
        matrix[a, a] += value; matrix[b, b] += value
        matrix[a, b] -= value; matrix[b, a] -= value
    keep = [i for i, b in enumerate(ids) if b != reference]
    rhs = np.zeros((len(ids), len(bus_ids)))
    for column, bus in enumerate(bus_ids):
        rhs[index[bus], column] += 1.
        rhs[index[reference], column] -= 1.
    try:
        reduced = np.linalg.solve(matrix[np.ix_(keep, keep)], rhs[keep])
    except np.linalg.LinAlgError as error:
        raise ValueError("PTDF refinement requires a connected, nonsingular DC network") from error
    angles = np.zeros_like(rhs); angles[keep] = reduced
    residual = float(np.max(np.abs(matrix @ angles - rhs)))
    if residual > 1e-6:
        raise RuntimeError(f"PTDF nodal residual is too large: {residual}")
    values, names = [], []
    for signature in sorted(critical_signatures):
        branch_id, direction = signature.rsplit(":", 1)
        if branch_id not in branches or direction not in {"upper", "lower"}:
            raise ValueError(f"unknown signed branch {signature}")
        branch = branches[branch_id]
        if branch.thermal_limit_mw <= 0:
            continue
        injection_flow = branch.susceptance_pu * (angles[index[branch.from_bus_id]] - angles[index[branch.to_bus_id]])
        load_flow = -injection_flow
        values.append(load_flow * (1 if direction == "upper" else -1) / branch.thermal_limit_mw)
        names.append(signature)
    if not names:
        raise ValueError("PTDF refinement requires positive-rated critical lines")
    return {"bus_ids": list(bus_ids), "signatures": names, "reference_bus": reference,
            "rating_normalized_load_ptdf": np.array(values).T.tolist(), "max_nodal_residual": residual}


def complete_link_groups(bus_ids, allowed):
    """Deterministic agglomeration: EVERY cross-pair must satisfy the cutoff.

    This prevents A~B and B~C from implicitly claiming A~C. Nonoverlapping
    cohorts supplement, rather than replace, the overlapping line groups.
    """
    clusters = [(bus,) for bus in sorted(bus_ids)]
    while True:
        possibilities = []
        for i, a in enumerate(clusters):
            for j in range(i + 1, len(clusters)):
                b = clusters[j]
                if all(allowed(x, y) for x in a for y in b):
                    possibilities.append((tuple(sorted(a + b)), i, j))
        if not possibilities:
            return clusters
        merged, i, j = min(possibilities)
        clusters = [c for k, c in enumerate(clusters) if k not in (i, j)] + [merged]
        clusters.sort()


def build_groups(stress, period, *, minimum_frequency=.20, jaccard_cutoff=.5, ptdf_cutoff_fraction=.20):
    if not 0 < minimum_frequency <= 1 or not 0 <= jaccard_cutoff <= 1 or ptdf_cutoff_fraction <= 0:
        raise ValueError("invalid grouping cutoff")
    features, evidence = signature_features(stress)
    signatures = {bus: {key for key, weight in values.items()
                        if weight >= minimum_frequency or "hosting_limit:baseline" in evidence[key][bus]}
                  for bus, values in features.items()}
    buses = sorted(features)
    ptdf = ptdf_features(period, buses, evidence)
    values = np.array(ptdf["rating_normalized_load_ptdf"])
    # Recurring stressed lines receive more weight; every critical line retains a floor.
    weights = np.array([max(.05, sum(features[b].get(key, 0.) for b in buses) / len(buses))
                        for key in ptdf["signatures"]])
    weights /= weights.sum()
    delta = values[:, None, :] - values[None, :, :]
    distances = np.sqrt(np.sum(delta * delta * weights, axis=2))
    positive = distances[np.triu_indices(len(buses), 1)]
    positive = positive[positive > 1e-12]
    scale = float(np.median(positive)) if len(positive) else 1.
    normalized = distances / scale
    lookup = {b: i for i, b in enumerate(buses)}
    def distance(a, b): return float(normalized[lookup[a], lookup[b]])
    def initial(a, b):
        return bool(signatures[a] and signatures[b]) and jaccard(signatures[a], signatures[b]) >= jaccard_cutoff
    def refined(a, b, cutoff=ptdf_cutoff_fraction):
        d = distance(a, b)
        return d <= cutoff and (initial(a, b) or d <= cutoff / 2)
    cohorts = complete_link_groups(buses, refined)
    overlaps = []
    for key in sorted(evidence):
        members = [bus for bus in buses if key in signatures[bus]]
        if members:
            overlaps.append({"group_id": key, "members": members,
                             "evidence": {bus: evidence[key][bus] for bus in members}})
    sensitivities = []
    for cutoff in (.10, .20, .35):
        clusters = complete_link_groups(buses, lambda a, b: refined(a, b, cutoff))
        sensitivities.append({"ptdf_cutoff_fraction": cutoff, "cohort_count": len(clusters),
                              "singleton_count": sum(len(c) == 1 for c in clusters),
                              "cohorts": [list(c) for c in clusters]})
    return {"features": features, "signatures": {b: sorted(s) for b, s in signatures.items()},
            "overlapping_groups": overlaps,
            "initial_cohorts": [list(c) for c in complete_link_groups(buses, initial)],
            "refined_cohorts": [{"cohort_id": f"C{i + 1:02d}", "members": list(c)} for i, c in enumerate(cohorts)],
            "system_generation_shared_by": buses,
            "ptdf": ptdf, "normalized_ptdf_distances": normalized.tolist(),
            "ptdf_distance_scale": scale, "ptdf_line_weights": weights.tolist(),
            "settings": {"minimum_frequency": minimum_frequency, "jaccard_cutoff": jaccard_cutoff,
                         "ptdf_cutoff_fraction": ptdf_cutoff_fraction},
            "threshold_sensitivity": sensitivities}
