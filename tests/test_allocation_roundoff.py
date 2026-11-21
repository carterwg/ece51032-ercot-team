"""The numerical retry may remove only bounded sub-watt residues, never add capacity."""
import pytest

from team_strategy.evaluation.allocation_roundoff import (zero_allocation_roundoff, omit_zero_generator_columns,
                                                         correct_zero_anchor_cuts, required_full_output,
                                                         presolve_exact_self_supply)


def sample(monkeypatch):
    from tools.activsg2000 import allocation
    sites = tuple(allocation.AllocationSite(name, "site", "1", 500., (500.,))
                  for name in ["full", "residue", "meaningful"])
    fractions = {s.key: a for s,a in zip(sites, [1., 1e-11, .01])}
    result = allocation.AllocationResult(fractions, 505.000000005, 505.000000005, 1500., 4, 2, 1e-8)
    original = lambda *args, **kwargs: result
    monkeypatch.setattr(allocation, "allocate_sites", original)
    return allocation, sites, original


def test_roundoff_is_only_downward_and_keeps_meaningful_allocations(monkeypatch):
    allocation, sites, original = sample(monkeypatch)
    with zero_allocation_roundoff() as audit:
        result = allocation.allocate_sites("network", sites)
        assert result.alpha_by_site[sites[0].key] == 1.
        assert result.alpha_by_site[sites[1].key] == 0.
        assert result.alpha_by_site[sites[2].key] == .01
        assert result.total_capacity_mw == 505.
        assert audit[0]["removed_capacity_mw"] == pytest.approx(5e-9)
    assert allocation.allocate_sites is original


def test_total_guard_and_exception_restore_the_official_allocator(monkeypatch):
    allocation, sites, original = sample(monkeypatch)
    with pytest.raises(ValueError, match="total allocation roundoff"):
        with zero_allocation_roundoff(total_mw=1e-10):
            allocation.allocate_sites("network", sites)
    assert allocation.allocate_sites is original


@pytest.mark.parametrize("kwargs", [{"per_site_mw": 1e-3}, {"total_mw": 1.}, {"per_site_mw": 0.}])
def test_limits_cannot_be_relaxed(kwargs):
    with pytest.raises(ValueError, match="conservative retry bounds"):
        with zero_allocation_roundoff(**kwargs): pass


def test_zero_column_cleanup_keeps_sites_and_all_positive_generators(monkeypatch):
    from dataclasses import dataclass
    from ercot_game import batch_evaluation

    @dataclass
    class Generator:
        generator_id: str
        capacity_mw: float

    @dataclass
    class Plan:
        team_id: str
        generators: tuple
        connections: tuple = ("unchanged-zero-load-site",)

    plan = Plan("team", (Generator("zero", 0.), Generator("tiny-positive", 1e-12), Generator("full", 500.)))
    original = lambda *args, **kwargs: plan
    monkeypatch.setattr(batch_evaluation, "_scaled_plan", original)
    with omit_zero_generator_columns() as audit:
        reduced = batch_evaluation._scaled_plan(None, {})
        assert reduced.connections == plan.connections
        assert [g.generator_id for g in reduced.generators] == ["tiny-positive", "full"]
        assert audit == [{"team_id": "team", "removed_zero_capacity_generator_ids": ["zero"]}]
    assert batch_evaluation._scaled_plan is original


@pytest.mark.parametrize("validated,rhs,expected", [(True,-5e-7,0.), (False,-5e-7,-5e-7), (True,-1e-3,-1e-3)])
def test_cut_roundoff_requires_a_validated_zero_anchor_and_tiny_error(tmp_path, monkeypatch, validated, rhs, expected):
    import json
    from tools.activsg2000 import allocation
    (tmp_path/"manifest.json").write_text(json.dumps({"submission_2_base_load": {},
        "validation_status": "passed" if validated else "pending", "validation": {"passed_period_count": 120}}))
    observed = []
    def master(capacities, cuts, **kwargs): observed.extend(cuts); return [1.,0.]
    def allocate(directory, sites, **kwargs):
        return allocation._solve_master([500.,500.], [([0.,1250.],rhs)], minimum_total=None)
    monkeypatch.setattr(allocation, "allocate_sites", allocate); monkeypatch.setattr(allocation, "_solve_master", master)
    with correct_zero_anchor_cuts() as audit:
        allocation.allocate_sites(tmp_path, ())
    assert observed[0][1] == expected
    assert bool(audit) == (validated and rhs == -5e-7)
    assert allocation._solve_master is master and allocation.allocate_sites is allocate


def test_exact_balance_presolve_changes_only_bounds_already_implied_by_balance():
    from tools.activsg2000.dcopf import Bus, Generator
    generators = (Generator("a","1",10.,60.,20.), Generator("b","1",0.,40.,80.))
    fixed, active = required_full_output((Bus("1",100.,True),), generators, {})
    assert active and [g.p_min_mw for g in fixed] == [60.,40.]
    assert [g.p_max_mw for g in fixed] == [60.,40.]
    assert [g.marginal_cost_per_mwh for g in fixed] == [20.,80.]
    unchanged, active = required_full_output((Bus("1",99.9999999,True),), generators, {})
    assert not active and unchanged is generators


def test_presolve_requires_self_supply_and_checks_independent_balances(monkeypatch):
    from tools.activsg2000 import dcopf, plan_adapter
    buses = (dcopf.Bus("1",100.,True),)
    generators = (dcopf.Generator("native","1",0.,50.,20.), dcopf.Generator("private","1",0.,50.,80.))
    observed = []
    def solve(**kwargs):
        observed.append(kwargs["generators"])
        return dcopf.DCOPFResult("optimal",5000.,{"native":50.,"private":50.},{"1":0.},{},{"1":80.})
    def period(*args, **kwargs):
        return dcopf.solve_dcopf(buses=buses,generators=generators,branches=(),fixed_injection_mw_by_bus={})
    monkeypatch.setattr(dcopf,"solve_dcopf",solve);monkeypatch.setattr(plan_adapter,"solve_prepared_period",period)
    with presolve_exact_self_supply() as audit:
        plan_adapter.solve_prepared_period("network",period_index=109,
            additional_demand_mw_by_bus={"1":50.},additional_generators=(generators[1],))
    assert [g.p_min_mw for g in observed[0]] == [50.,50.]
    assert audit[0]["max_balance_error_mw"] == 0.
    assert dcopf.solve_dcopf is solve and plan_adapter.solve_prepared_period is period


def test_retry_rejects_threaded_dispatch_before_creating_an_attempt(tmp_path):
    import json
    from team_strategy.experiments.retry_scheduled_roundoff import retry
    run = tmp_path/"run";run.mkdir()
    (run/"experiment.json").write_text("{}")
    (run/"manifest.json").write_text(json.dumps({"identity": {"workers_per_evaluation": 2}}))
    with pytest.raises(ValueError, match="workers=1"):
        retry(tmp_path, run, "layout/scenario", tmp_path/"attempt", exact_presolve=True)
    assert not (tmp_path/"attempt").exists()
