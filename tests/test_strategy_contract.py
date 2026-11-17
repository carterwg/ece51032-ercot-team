from dataclasses import replace
import math

import pytest

from team_strategy.contracts import BusFeatures, Plan, Strategy
from team_strategy.strategies import STRATEGIES, build_strategy
from team_strategy.strategies.full_generation import FullGeneration
from team_strategy.validation import validate_plan


# Every registered strategy is subjected to the common contract checks.
@pytest.mark.parametrize("name", STRATEGIES)
def test_registered_strategy_contract(name, context):
    strategy: Strategy = build_strategy(name, {})
    plan = strategy.propose(context)
    assert isinstance(plan, Plan)
    assert plan == strategy.propose(context)
    assert validate_plan(plan, context).valid


@pytest.mark.parametrize("site_count", [1, 3, 14])
def test_baseline_uses_full_budget_with_c_equal_g(site_count, context):
    plan = FullGeneration(site_count=site_count).propose(context)
    assert len(plan.sites) == site_count
    assert math.fsum(site.connection_mw for site in plan.sites) == pytest.approx(context.connection_budget_mw)
    assert all(site.generator_mw == site.connection_mw for site in plan.sites)
    assert all(site.storage_power_mw == site.storage_energy_mwh == 0 for site in plan.sites)
    assert validate_plan(plan, context).valid


def test_baseline_accepts_json_parameters_and_explicit_buses(context):
    plan = build_strategy("full_generation", {"site_count": 2, "bus_ids": ["13", "14"]}).propose(context)
    assert [site.bus_id for site in plan.sites] == ["13", "14"]


@pytest.mark.parametrize("params", [
    {"site_count": 0}, {"site_count": True}, {"site_count": 1.5},
    {"site_count": 2, "bus_ids": ["1"]},
    {"site_count": 2, "bus_ids": ["1", "1"]},
])
def test_baseline_rejects_invalid_configuration(params):
    with pytest.raises(ValueError):
        FullGeneration(**params)


def test_baseline_rejects_unknown_bus_and_insufficient_buses(context):
    with pytest.raises(ValueError, match="unknown bus"):
        FullGeneration(bus_ids=("missing",)).propose(context)
    with pytest.raises(ValueError, match="not enough"):
        FullGeneration(site_count=15).propose(context)


def test_baseline_obeys_reduced_budget(context):
    context = replace(context, connection_budget_mw=12.5)
    assert FullGeneration().propose(context).sites[0].generator_mw == 12.5


def test_baseline_fails_if_active_rules_disallow_c_equal_g(context):
    with pytest.raises(ValueError, match="do not permit"):
        FullGeneration().propose(replace(context, max_generator_to_connection_ratio=0.5))


def test_stale_screening_is_rejected(context):
    with pytest.raises(ValueError, match="fingerprint"):
        replace(context, candidate_buses=(BusFeatures("1", 20),), screening_scenario_fingerprint="old")
    fresh = replace(context, candidate_buses=(BusFeatures("1", 20),),
                    screening_scenario_fingerprint=context.scenario_fingerprint)
    assert fresh.candidate_buses[0].bus_id == "1"


def test_evaluator_failure_cannot_be_mistaken_for_a_zero_score(tmp_path):
    from team_strategy.contracts import EvaluationResult, EvaluationStatus

    with pytest.raises(ValueError, match="not a scored"):
        EvaluationResult(EvaluationStatus.EVALUATOR_FAILURE, 0, None, tmp_path)
    failure = EvaluationResult(EvaluationStatus.EVALUATOR_FAILURE, None, None, tmp_path)
    zero = EvaluationResult(EvaluationStatus.VALID, 0, 0, tmp_path)
    assert failure.score_usd is None
    assert zero.score_usd == 0


def test_score_breakdown_uses_separate_cost_terms():
    from team_strategy.contracts import ScoreBreakdown

    breakdown = ScoreBreakdown(100, 10, 20, 5, 2, 30)
    assert breakdown.total_usd == 33
