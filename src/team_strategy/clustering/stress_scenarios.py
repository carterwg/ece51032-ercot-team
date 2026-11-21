"""Stage 3: residual hosting limits and actual 500 MW operating observations.

Background teams are assumed to withdraw their requested grid power without
curtailment. This is an electrical experiment, not the game's allocation or
economic score. Every team is capped at 500 MW; several teams may share a bus.
"""
from collections import Counter
from dataclasses import asdict, dataclass, replace
import math
import sys

import numpy as np

from tools.activsg2000.dcopf import GurobiReusableDCOPFModel, ReusableDCOPFModel
from .bottlenecks import HostingLP, Tolerances


@dataclass(frozen=True)
class BackgroundTeam:
    team_id: str
    sites: tuple[tuple[str, float], ...]

    def __post_init__(self):
        if not self.team_id or not self.sites:
            raise ValueError("background teams require an ID and sites")
        if any(not math.isfinite(q) or q <= 0 for _, q in self.sites):
            raise ValueError("background loads must be finite and positive")
        if math.fsum(q for _, q in self.sites) > 500 + 1e-9:
            raise ValueError("each background team is limited to 500 MW")


@dataclass(frozen=True)
class StressScenario:
    name: str
    teams: tuple[BackgroundTeam, ...] = ()

    def loads(self):
        if len({t.team_id for t in self.teams}) != len(self.teams):
            raise ValueError("background team IDs must be distinct")
        total = Counter()
        for team in self.teams:
            for bus, q in team.sites:
                total[bus] += q
        return dict(total)


def default_scenarios():
    """Small, explicit hypothesis set; names do not imply opponent probabilities."""
    def one(name, sites):
        return StressScenario(name, (BackgroundTeam("rival-1", tuple(sites)),))
    return (
        StressScenario("baseline"),
        one("hub_500", [("6141", 500.)]),
        one("generation_500", [("1079", 500.)]),
        one("shared_line_500", [("5413", 500.)]),
        one("alternative_split_500", [("6062", 250.), ("6298", 250.)]),
        StressScenario("hub_2000", tuple(BackgroundTeam(f"rival-{i}", (("6141", 500.),)) for i in range(4))),
        StressScenario("distributed_2000", tuple(BackgroundTeam(f"rival-{i}", ((bus, 500.),))
                                               for i, bus in enumerate(("6141", "1079", "6062", "6298")))),
    )


def add_loads(period, loads):
    known = {b.bus_id for b in period.buses}
    if set(loads) - known or any(not math.isfinite(q) or q < 0 for q in loads.values()):
        raise ValueError("additional loads must be nonnegative and refer to known buses")
    return replace(period, buses=tuple(replace(b, demand_mw=b.demand_mw + loads.get(b.bus_id, 0.))
                                       for b in period.buses))


def compact_diagnosis(diagnosis):
    return {"period_index": diagnosis.period_index,
            "hosting_capacity_mw": diagnosis.hosting_capacity_mw,
            "generation_headroom_mw": diagnosis.generation_headroom_mw,
            "limiting_resource": diagnosis.limiting_resource,
            "tight_lines": [asdict(line) for line in diagnosis.tight_lines],
            "generator_pmax_count": len(diagnosis.generator_pmax_ids),
            "generator_pmin_count": len(diagnosis.generator_pmin_ids),
            "max_balance_error_mw": diagnosis.max_balance_error_mw,
            "max_limit_violation_mw": diagnosis.max_limit_violation_mw,
            "duality_gap_mw": diagnosis.duality_gap_mw}


def critical_operating_periods(periods, baseline):
    """Each day's demand peak, unique capacity-limiting hours, and peak neighbors."""
    totals = [math.fsum(b.demand_mw for b in p.buses) for p in periods]
    chosen = {max(range(start, min(start + 24, len(periods))), key=lambda i: totals[i])
              for start in range(0, len(periods), 24)}
    for result in baseline:
        if len(result.limiting_periods) == 1:
            chosen.add(result.limiting_periods[0])
    peak = max(range(len(periods)), key=lambda i: totals[i])
    chosen.update(i for i in (peak - 1, peak, peak + 1) if 0 <= i < len(periods))
    return tuple(sorted(chosen))


def _infeasible(model):
    if model.backend == "gurobi":
        return model.solver.Status == model.model._gp.GRB.INFEASIBLE
    return model.solver.getModelStatus() == model.highspy.HighsModelStatus.kInfeasible


def run_stress_scenarios(periods, pool, baseline, *, solver_backend="auto", scenarios=None,
                         requested_mw=500., near_limit_fraction=.95):
    if not periods or not 0 < requested_mw <= 500 or not 0 < near_limit_fraction <= 1:
        raise ValueError("invalid periods, request, or near-limit threshold")
    scenarios = default_scenarios() if scenarios is None else tuple(scenarios)
    if len({s.name for s in scenarios}) != len(scenarios):
        raise ValueError("scenario names must be distinct")
    candidates = tuple(b.bus_id for b in pool.candidates)
    if {r.bus_id for r in baseline} != set(candidates):
        raise ValueError("baseline and candidate pool differ")
    model = HostingLP(periods[0], solver_backend=solver_backend)
    backend = model.backend
    dispatch_class = GurobiReusableDCOPFModel if backend == "gurobi" else ReusableDCOPFModel
    dispatch = dispatch_class(buses=tuple(periods[0].buses), generators=tuple(periods[0].generators),
                              branches=tuple(periods[0].branches), solver_threads=1)
    operating_periods = critical_operating_periods(periods, baseline)
    output = []
    for scenario in scenarios:
        loads = scenario.loads()
        stressed = tuple(add_loads(p, loads) for p in periods)
        print(f"Stress scenario {scenario.name}: {sum(loads.values()):g} MW background", file=sys.stderr)
        item = {"scenario": asdict(scenario), "background_loads_mw": loads, "status": "valid",
                "operating_periods": operating_periods, "candidates": {}}
        capacities = np.empty((len(candidates), len(periods)))
        if not loads:
            by_bus = {r.bus_id: r for r in baseline}
            capacities[:] = np.array([by_bus[bus].capacity_by_period_mw for bus in candidates])
        else:
            for t, period in enumerate(stressed):
                try:
                    model.set_period(period)
                except RuntimeError:
                    if not _infeasible(model):
                        raise
                    item.update(status="infeasible_background", infeasible_period=t)
                    break
                for row, bus in enumerate(candidates):
                    capacities[row, t] = model.maximize(bus)
                if (t + 1) % 24 == 0:
                    print(f"  capacity scan {t + 1}/{len(periods)}", file=sys.stderr)
        if item["status"] != "valid":
            output.append(item)
            continue
        for row, bus in enumerate(candidates):
            low = float(capacities[row].min())
            ties = [int(i) for i in np.flatnonzero(capacities[row] <= low + model.tolerances.period_tie_mw)]
            item["candidates"][bus] = {
                "minimum_hosting_capacity_mw": low, "limiting_periods": ties,
                "capacity_by_period_mw": capacities[row].tolist(), "diagnoses": [],
                "full_request_feasible": low >= requested_mw - model.tolerances.tight_mw,
                "observed_request_mw": min(requested_mw, low), "near_lines": {},
            }
        # Retain every tied limiting period, but give scenarios equal weight later.
        for t in sorted({t for c in item["candidates"].values() for t in c["limiting_periods"]}):
            model.set_period(stressed[t])
            for bus, c in item["candidates"].items():
                if t in c["limiting_periods"]:
                    d = model.diagnose(bus)
                    if abs(d.hosting_capacity_mw - capacities[candidates.index(bus), t]) > 1e-4:
                        raise RuntimeError("stress capacity changed between scan and diagnosis")
                    c["diagnoses"].append(compact_diagnosis(d))
        # At actual request sizes use economic dispatch, not the maximum-HC dispatch.
        for t in operating_periods:
            before = dispatch.solve(tuple(stressed[t].buses), stressed[t].fixed_injection_mw_by_bus)
            for bus, c in item["candidates"].items():
                if not c["full_request_feasible"]:
                    continue
                operating = add_loads(stressed[t], {bus: c["observed_request_mw"]})
                after = dispatch.solve(tuple(operating.buses), operating.fixed_injection_mw_by_bus)
                for branch in operating.branches:
                    if branch.thermal_limit_mw <= 0:
                        continue
                    flow = after.flow_mw_by_branch[branch.branch_id]
                    utilization = abs(flow) / branch.thermal_limit_mw
                    sign = 1 if flow >= 0 else -1
                    impact = sign * (flow - before.flow_mw_by_branch[branch.branch_id])
                    if utilization < near_limit_fraction or impact <= max(.001, .001 * branch.thermal_limit_mw):
                        continue
                    key = f"{branch.branch_id}:{'upper' if sign > 0 else 'lower'}"
                    record = c["near_lines"].setdefault(key, {"periods": [], "max_utilization": 0., "max_aligned_impact_mw": 0.})
                    record["periods"].append(t)
                    record["max_utilization"] = max(record["max_utilization"], utilization)
                    record["max_aligned_impact_mw"] = max(record["max_aligned_impact_mw"], impact)
        output.append(item)
    return {"solver": backend, "requested_mw": requested_mw,
            "near_limit_fraction": near_limit_fraction, "operating_periods": operating_periods,
            "scenarios": output}
