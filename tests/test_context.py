import pytest

from team_strategy.context import load_context
from team_strategy.contracts import RoundKey

from conftest import DEMO, DEMO_RULES, RELEASE


@pytest.mark.parametrize("week", [1, 2, 3])
@pytest.mark.parametrize("submission", [1, 2])
def test_round_settings_and_baseline_validity(week, submission, carried_scenario):
    from team_strategy.strategies.full_generation import FullGeneration
    from team_strategy.validation import validate_plan

    context = load_context(
        release_file=RELEASE, round=RoundKey(week, submission), team_id="team-test",
        scenario_dir=carried_scenario if submission == 2 else DEMO, rules_file=DEMO_RULES,
    )
    assert context.energy_cost_enabled == (week == 3)
    assert context.round.graded == (week != 1)
    assert context.connection_budget_mw == 500
    assert validate_plan(FullGeneration().propose(context), context).valid


def test_submission2_requires_carried_base_and_submission1_resets(carried_scenario):
    with pytest.raises(ValueError, match="Submission 2"):
        load_context(release_file=RELEASE, round=RoundKey(2, 2), team_id="team-test",
                     scenario_dir=DEMO, rules_file=DEMO_RULES)
    with pytest.raises(ValueError, match="weekly reset"):
        load_context(release_file=RELEASE, round=RoundKey(3, 1), team_id="team-test",
                     scenario_dir=carried_scenario, rules_file=DEMO_RULES)


@pytest.mark.parametrize("budget", [0, -1, float("nan"), float("inf"), 501])
def test_active_release_budget_cannot_be_overridden(budget):
    with pytest.raises(ValueError):
        load_context(release_file=RELEASE, round=RoundKey(2, 1), team_id="team-test",
                     scenario_dir=DEMO, rules_file=DEMO_RULES, connection_budget_mw=budget)


@pytest.mark.parametrize("week,submission", [(0, 1), (4, 1), (2, 3), (True, 1), (2, True)])
def test_invalid_rounds(week, submission):
    with pytest.raises(ValueError):
        RoundKey(week, submission)


def test_older_imported_release_cannot_raise_finalized_cap():
    from conftest import COURSE

    imported_release = COURSE / "data/teaching/game_release_representative_v1.json"
    context = load_context(release_file=imported_release, round=RoundKey(2, 1), team_id="team-test")
    assert context.connection_budget_mw == 500
    with pytest.raises(ValueError, match="finalized cap"):
        load_context(release_file=imported_release, round=RoundKey(2, 1), team_id="team-test",
                     connection_budget_mw=501)


def test_direct_context_construction_obeys_finalized_cap(context):
    from dataclasses import replace

    with pytest.raises(ValueError, match="500 MW"):
        replace(context, connection_budget_mw=501)
