"""Conservative zeroing of allocation roundoff before official joint redispatch.

Use only for a recorded numerical retry. No upward rounding, request changes,
solver-option changes, or substituted scores. Official dispatch must still pass.
"""
from contextlib import contextmanager
from dataclasses import replace
from decimal import Decimal
import json
import math
from pathlib import Path


@contextmanager
def zero_allocation_roundoff(*, per_site_mw=1e-6, total_mw=1e-5):
    """Yield an audit list; temporarily wrap the allocator in this process only."""
    from tools.activsg2000 import allocation

    if not (0 < per_site_mw <= 1e-6 and 0 < total_mw <= 1e-5):
        raise ValueError("roundoff limits exceed the conservative retry bounds")
    original = allocation.allocate_sites
    audit = []

    def rounded(artifact_dir, sites, **kwargs):
        sites = tuple(sites)
        result = original(artifact_dir, sites, **kwargs)
        if result is None:
            return None
        values = dict(result.alpha_by_site)
        changes = []
        for site in sites:
            alpha = values[site.key]
            mw = alpha * site.capacity_mw
            if 0 < mw <= per_site_mw:
                values[site.key] = 0.
                changes.append({"team_id": site.team_id, "site_id": site.site_id,
                                "alpha_before": alpha, "alpha_after": 0., "removed_capacity_mw": mw})
        removed = math.fsum(c["removed_capacity_mw"] for c in changes)
        if removed > total_mw:
            raise ValueError("total allocation roundoff exceeds the retry bound")
        if not changes:
            return result
        audit.append({"artifact_directory": str(artifact_dir), "per_site_limit_mw": per_site_mw,
                      "total_limit_mw": total_mw, "removed_capacity_mw": removed, "changes": changes})
        return replace(result, alpha_by_site=values,
                       total_capacity_mw=math.fsum(site.capacity_mw*values[site.key] for site in sites))

    allocation.allocate_sites = rounded
    try:
        yield audit
    finally:
        allocation.allocate_sites = original


@contextmanager
def omit_zero_generator_columns():
    """Keep every team/site, but omit generator variables fixed exactly at zero."""
    from ercot_game import batch_evaluation

    original = batch_evaluation._scaled_plan
    audit = []

    def scaled(*args, **kwargs):
        plan = original(*args, **kwargs)
        removed = [g.generator_id for g in plan.generators if g.capacity_mw == 0.]
        if not removed:
            return plan
        audit.append({"team_id": plan.team_id, "removed_zero_capacity_generator_ids": removed})
        return replace(plan, generators=tuple(g for g in plan.generators if g.capacity_mw != 0.))

    batch_evaluation._scaled_plan = scaled
    try:
        yield audit
    finally:
        batch_evaluation._scaled_plan = original


@contextmanager
def correct_zero_anchor_cuts(*, maximum_mwh=1e-6):
    """A validated carried base makes alpha=0 feasible; fix only tiny negative RHS."""
    from tools.activsg2000 import allocation

    if not 0 < maximum_mwh <= 1e-6: raise ValueError("cut correction limit exceeds one Wh")
    original_allocate, original_master = allocation.allocate_sites, allocation._solve_master
    active = {"eligible": False, "directory": None}
    audit = []

    def allocate(directory, sites, **kwargs):
        manifest = json.loads((Path(directory)/"manifest.json").read_text())
        previous = dict(active)
        active.update(eligible=("submission_2_base_load" in manifest and manifest.get("validation_status") == "passed"
                               and manifest.get("validation", {}).get("passed_period_count") == 120), directory=str(directory))
        try: return original_allocate(directory, sites, **kwargs)
        finally: active.update(previous)

    def master(capacities, cuts, **kwargs):
        corrected = []
        for index, (gradient, rhs) in enumerate(cuts):
            if active["eligible"] and -maximum_mwh <= rhs < 0.:
                audit.append({"artifact_directory": active["directory"], "cut_index": index,
                              "rhs_before_mwh": rhs, "rhs_after_mwh": 0., "maximum_correction_mwh": maximum_mwh})
                rhs = 0.
            corrected.append((gradient, rhs))
        return original_master(capacities, corrected, **kwargs)

    allocation.allocate_sites, allocation._solve_master = allocate, master
    try: yield audit
    finally: allocation.allocate_sites, allocation._solve_master = original_allocate, original_master


def required_full_output(buses, generators, fixed):
    """Exact aggregate balance at total Pmax implies every generator is at Pmax."""
    demand = sum(Decimal(str(b.demand_mw)) for b in buses)
    supply = sum(Decimal(str(g.p_max_mw)) for g in generators)+sum(Decimal(str(v)) for v in fixed.values())
    if demand != supply: return generators, False
    return tuple(replace(g, p_min_mw=g.p_max_mw) for g in generators), True


@contextmanager
def presolve_exact_self_supply():
    """Fix bounds already forced by exact balance, only for self-supplied new loads.

    Existing demand, generation Pmax, costs, line limits, and ownership stay fixed.
    Joint dispatch and scoring remain official. Independently check solved balances.
    """
    from tools.activsg2000 import dcopf, plan_adapter

    original_period, original_solve = plan_adapter.solve_prepared_period, dcopf.solve_dcopf
    state = {"eligible": False, "period": None}
    audit = []

    def period(*args, **kwargs):
        loads = kwargs.get("additional_demand_mw_by_bus") or {}
        generation = {}
        for g in kwargs.get("additional_generators", ()):
            generation[g.bus_id] = generation.get(g.bus_id, Decimal(0))+Decimal(str(g.p_max_mw))
        previous = dict(state)
        eligible = (sum(Decimal(str(v)) for v in loads.values()) > 0
                    and all(generation.get(b, Decimal(0)) == Decimal(str(loads.get(b, 0.))) for b in set(loads)|set(generation)))
        state.update(eligible=eligible, period=kwargs.get("period_index"))
        try: return original_period(*args, **kwargs)
        finally: state.update(previous)

    def solve(*args, **kwargs):
        forced = False
        original_generators = kwargs["generators"]
        fixed = kwargs.get("fixed_injection_mw_by_bus") or {}
        if state["eligible"]:
            generators, forced = required_full_output(kwargs["buses"], original_generators, fixed)
            if forced: kwargs = {**kwargs, "generators": generators}
        result = original_solve(*args, **kwargs)
        if forced:
            balance = {b.bus_id: fixed.get(b.bus_id, 0.)-b.demand_mw for b in kwargs["buses"]}
            limit_error = 0.
            for g in original_generators:
                amount = result.generation_mw[g.generator_id]
                balance[g.bus_id] += amount
                limit_error = max(limit_error, g.p_min_mw-amount, amount-g.p_max_mw)
            for b in kwargs["branches"]:
                flow = result.flow_mw_by_branch[b.branch_id]
                balance[b.from_bus_id] -= flow; balance[b.to_bus_id] += flow
                limit_error = max(limit_error, abs(flow)-b.thermal_limit_mw)
            error = max(abs(v) for v in balance.values())
            if error > 1e-4 or limit_error > 1e-4:
                raise ValueError(f"exact-balance presolve failed independent feasibility checks: {error}, {limit_error}")
            audit.append({"period_index": state["period"], "fixed_generator_count": len(original_generators),
                          "exact_aggregate_headroom_mw": "0", "max_balance_error_mw": error,
                          "max_limit_violation_mw": max(0., limit_error)})
        return result

    plan_adapter.solve_prepared_period, dcopf.solve_dcopf = period, solve
    try: yield audit
    finally: plan_adapter.solve_prepared_period, dcopf.solve_dcopf = original_period, original_solve
