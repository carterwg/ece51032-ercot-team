"""Fixed capacity fractions across selected buses, with a matched resource ratio."""
from dataclasses import dataclass
import math
from numbers import Real

from ..contracts import Plan, PlanningContext, SiteProposal


@dataclass(frozen=True)
class CorridorPortfolio:
    bus_ids: tuple[str, ...] = ()
    weights: tuple[float, ...] = ()
    generator_fraction: float = 0.0

    def __post_init__(self):
        object.__setattr__(self, "bus_ids", tuple(self.bus_ids))
        object.__setattr__(self, "weights", tuple(self.weights))
        if len(set(self.bus_ids)) != len(self.bus_ids) or any(not isinstance(b, str) or not b for b in self.bus_ids):
            raise ValueError("bus IDs must be distinct nonempty strings")
        if (isinstance(self.generator_fraction, bool) or not isinstance(self.generator_fraction, Real)
                or not math.isfinite(self.generator_fraction) or not 0 <= self.generator_fraction <= 1):
            raise ValueError("generator_fraction must be in [0,1]")
        if self.weights and (not self.bus_ids or len(self.weights) != len(self.bus_ids)
                             or any(isinstance(w, bool) or not isinstance(w, Real) or not math.isfinite(w) or w <= 0 for w in self.weights)
                             or abs(math.fsum(self.weights) - 1) > 1e-9):
            raise ValueError("weights must be positive, sum to one, and match the buses")

    def propose(self, context: PlanningContext) -> Plan:
        buses = self.bus_ids or (min(context.bus_ids),)
        if not set(buses) <= context.bus_ids:
            raise ValueError("portfolio contains an unknown bus")
        if self.generator_fraction > context.max_generator_to_connection_ratio:
            raise ValueError("generator fraction exceeds active rules")
        weights = self.weights or tuple(1 / len(buses) for _ in buses)
        total = math.fsum(weights)
        capacities = [context.connection_budget_mw * w / total for w in weights]
        capacities[-1] = context.connection_budget_mw - math.fsum(capacities[:-1])
        return Plan(tuple(SiteProposal(b, mw, mw * self.generator_fraction)
                          for b, mw in zip(buses, capacities, strict=True)))
