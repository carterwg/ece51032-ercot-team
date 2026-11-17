"""C = G baseline: request the full available budget with no batteries."""

from dataclasses import dataclass

from ..contracts import Plan, PlanningContext, SiteProposal


@dataclass(frozen=True)
class FullGeneration:
    site_count: int = 1
    bus_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if type(self.site_count) is not int or self.site_count < 1:
            raise ValueError("site_count must be a positive integer")
        # JSON configurations contain lists; freeze them at the boundary.
        object.__setattr__(self, "bus_ids", tuple(self.bus_ids))
        if self.bus_ids and len(self.bus_ids) != self.site_count:
            raise ValueError("explicit bus_ids must contain site_count entries")
        if len(set(self.bus_ids)) != len(self.bus_ids):
            raise ValueError("explicit bus_ids must be distinct")

    def propose(self, context: PlanningContext) -> Plan:
        if context.max_generator_to_connection_ratio < 1.0:
            raise ValueError("the active rules do not permit the C = G baseline")
        buses = self.bus_ids or tuple(sorted(context.bus_ids))[:self.site_count]
        if len(buses) != self.site_count:
            raise ValueError("not enough distinct buses for site_count")
        if not set(buses) <= context.bus_ids:
            raise ValueError("baseline configuration contains an unknown bus")
        capacity = context.connection_budget_mw / self.site_count
        capacities = [capacity] * self.site_count
        capacities[-1] = context.connection_budget_mw - sum(capacities[:-1])
        return Plan(tuple(SiteProposal(bus, mw, mw) for bus, mw in zip(buses, capacities)))
