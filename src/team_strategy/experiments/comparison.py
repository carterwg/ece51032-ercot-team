"""Unweighted risk/return summaries and Pareto membership on matched scenarios."""

from dataclasses import dataclass
import math
from typing import Mapping

from .scoring import ScoreBounds


@dataclass(frozen=True)
class StrategySummary:
    name: str
    scenario_count: int
    average_normalized_score: float
    downside_risk: float
    worst_normalized_score: float
    fraction_below_baseline: float


def summarize(
    name: str, campaign_scores_usd: Mapping[str, float], bounds: ScoreBounds
) -> StrategySummary:
    if len(campaign_scores_usd) < 2:
        raise ValueError("risk comparison requires at least two campaign scenarios")
    values = tuple(bounds.normalize_usd(score) for score in campaign_scores_usd.values())
    mean = math.fsum(values) / len(values)
    # Lower semideviation about the mean; denominator includes ALL scenarios.
    downside = math.sqrt(math.fsum(min(value - mean, 0.0) ** 2 for value in values) / len(values))
    return StrategySummary(
        name, len(values), mean, downside, min(values),
        sum(value < 0 for value in values) / len(values),
    )


def compare(
    strategies: Mapping[str, Mapping[str, float]], bounds: ScoreBounds
) -> tuple[StrategySummary, ...]:
    if not strategies:
        raise ValueError("at least one strategy is required")
    scenario_sets = [set(scores) for scores in strategies.values()]
    if any(scenarios != scenario_sets[0] for scenarios in scenario_sets[1:]):
        raise ValueError("strategies must be evaluated on the same campaign scenario IDs")
    return tuple(summarize(name, scores, bounds) for name, scores in sorted(strategies.items()))


def frontier_names(summaries: tuple[StrategySummary, ...]) -> frozenset[str]:
    """Maximize mean return and minimize downside; equal points are both retained."""
    return frozenset(
        item.name for item in summaries
        if not any(
            other.average_normalized_score >= item.average_normalized_score
            and other.downside_risk <= item.downside_risk
            and (
                other.average_normalized_score > item.average_normalized_score
                or other.downside_risk < item.downside_risk
            )
            for other in summaries
        )
    )
