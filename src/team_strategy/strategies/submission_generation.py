"""Use grid-only new sites in S1 and equal load/generation at new S2 sites."""
from dataclasses import dataclass

from .corridor_portfolio import CorridorPortfolio


@dataclass(frozen=True)
class SubmissionGenerationPortfolio:
    bus_ids: tuple[str, ...] = ()
    weights: tuple[float, ...] = ()

    def __post_init__(self):
        portfolio = CorridorPortfolio(self.bus_ids, self.weights)
        object.__setattr__(self, "bus_ids", portfolio.bus_ids)
        object.__setattr__(self, "weights", portfolio.weights)

    def propose(self, context):
        fraction = 0. if context.round.submission == 1 else 1.
        return CorridorPortfolio(self.bus_ids, self.weights, fraction).propose(context)
