import math

import pytest

from team_strategy.contracts import GRADED_ROUNDS, RoundKey
from team_strategy.experiments.comparison import StrategySummary, compare, frontier_names, summarize
from team_strategy.experiments.scoring import ScoreBounds, combined_score_usd


def test_finalized_500mw_anchors_and_midpoint():
    bounds = ScoreBounds(500)
    assert bounds.normalize_billions(49.67) == 0
    assert bounds.normalize_billions(73.0525) == pytest.approx(100)
    assert bounds.normalize_billions((49.67 + 73.0525) / 2) == pytest.approx(50)
    assert bounds.normalize_usd(49.67e9) == pytest.approx(0)


def test_documented_profile_matches_the_runtime_scale():
    import json
    from conftest import ROOT

    profile = json.loads((ROOT / "configs/scoring/finalized_500mw_reference.json").read_text())
    bounds = ScoreBounds(profile["capacity_per_submission_mw"])
    assert profile["lower_anchor_billions"] == bounds.lower_billions
    assert profile["upper_anchor_billions"] == bounds.upper_billions
    assert profile["clip"] is False


def test_negative_and_above_100_scores_are_not_clipped():
    bounds = ScoreBounds()
    assert bounds.normalize_billions(45) < 0
    assert bounds.normalize_billions(75) > 100
    assert bounds.normalize_billions(-10) < bounds.normalize_billions(0) < 0


def test_reduced_test_budget_scales_anchors():
    bounds = ScoreBounds(250)
    assert bounds.lower_billions == pytest.approx(24.835)
    assert bounds.upper_billions == pytest.approx(36.52625)
    assert bounds.normalize_billions(24.835) == pytest.approx(0)
    assert bounds.normalize_billions(36.52625) == pytest.approx(100)


def test_report_rejects_capacity_above_finalized_cap():
    with pytest.raises(ValueError, match="500 MW"):
        ScoreBounds(501)


@pytest.mark.parametrize("value", [float("nan"), float("inf"), -float("inf")])
def test_nonfinite_scores_are_rejected(value):
    with pytest.raises(ValueError):
        ScoreBounds().normalize_billions(value)


def test_combined_score_uses_exactly_four_rounds_in_usd():
    assert combined_score_usd(dict(zip(GRADED_ROUNDS, [1e9, -2e9, 3e9, 4e9]))) == 6e9
    with pytest.raises(ValueError, match="exactly"):
        combined_score_usd({GRADED_ROUNDS[0]: 1e9})
    with pytest.raises(ValueError, match="exactly"):
        combined_score_usd({**dict.fromkeys(GRADED_ROUNDS, 1e9), RoundKey(1, 1): 1e9})
    with pytest.raises(ValueError, match="finite"):
        combined_score_usd(dict.fromkeys(GRADED_ROUNDS, float("nan")))


def test_downside_is_lower_semideviation_with_all_scenarios_in_denominator():
    # Synthetic campaign scores chosen to yield Q = -10, 10, 30.
    bounds = ScoreBounds()
    scores = {str(q): (bounds.lower_billions + q / 100 * (bounds.upper_billions - bounds.lower_billions)) * 1e9
              for q in (-10, 10, 30)}
    result = summarize("synthetic", scores, bounds)
    assert result.average_normalized_score == pytest.approx(10)
    assert result.downside_risk == pytest.approx(math.sqrt(400 / 3))
    assert result.worst_normalized_score == pytest.approx(-10)
    assert result.fraction_below_baseline == pytest.approx(1 / 3)


def test_comparison_requires_matched_scenarios_and_multiple_observations():
    with pytest.raises(ValueError, match="same"):
        compare({"a": {"s1": 1e9, "s2": 2e9}, "b": {"s1": 1e9, "s3": 2e9}}, ScoreBounds())
    with pytest.raises(ValueError, match="at least two"):
        compare({"a": {"s1": 1e9}}, ScoreBounds())


def test_pareto_frontier_retains_tradeoffs_and_ties():
    def summary(name, mean, risk):
        return StrategySummary(name, 3, mean, risk, -10, 0.3)
    points = (
        summary("stable", 20, 1), summary("upside", 40, 5),
        summary("dominated", 10, 2), summary("stable-tie", 20, 1),
    )
    assert frontier_names(points) == {"stable", "stable-tie", "upside"}
