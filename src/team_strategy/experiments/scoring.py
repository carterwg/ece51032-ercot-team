"""Team comparison scale, separate from the instructor's grade formula.

The 500 MW anchors retain the team's agreed normalization scale. They
assume a full new capacity budget in EACH of four graded submissions. The
upper anchor assumes full allocation, zero grid prices, and no private assets.
Neither anchor is a promised network outcome or a simulated baseline score.
"""

from dataclasses import dataclass
import math
from typing import Mapping

from ..contracts import GRADED_ROUNDS, RoundKey
from ..settings import FINALIZED_CAPACITY_MW


@dataclass(frozen=True)
class ScoreBounds:
    capacity_per_submission_mw: float = FINALIZED_CAPACITY_MW

    def __post_init__(self) -> None:
        if not math.isfinite(self.capacity_per_submission_mw) or self.capacity_per_submission_mw <= 0:
            raise ValueError("capacity per submission must be finite and positive")
        if self.capacity_per_submission_mw > FINALIZED_CAPACITY_MW:
            raise ValueError("comparison capacity exceeds the finalized 500 MW cap")

    @property
    def lower_billions(self) -> float:
        return 49.67 * (self.capacity_per_submission_mw / FINALIZED_CAPACITY_MW)

    @property
    def upper_billions(self) -> float:
        return 73.0525 * (self.capacity_per_submission_mw / FINALIZED_CAPACITY_MW)

    def normalize_billions(self, score_billions: float) -> float:
        if not math.isfinite(score_billions):
            raise ValueError("score must be finite")
        # Deliberately unclipped, including negative scores and values > 100.
        return 100.0 * (score_billions - self.lower_billions) / (
            self.upper_billions - self.lower_billions
        )

    def normalize_usd(self, score_usd: float) -> float:
        return self.normalize_billions(score_usd / 1_000_000_000.0)


def combined_score_usd(scores: Mapping[RoundKey, float]) -> float:
    if set(scores) != set(GRADED_ROUNDS):
        raise ValueError("campaign must contain exactly W2S1, W2S2, W3S1, and W3S2")
    if not all(math.isfinite(value) for value in scores.values()):
        raise ValueError("all round scores must be finite USD amounts")
    return math.fsum(scores[key] for key in GRADED_ROUNDS)
