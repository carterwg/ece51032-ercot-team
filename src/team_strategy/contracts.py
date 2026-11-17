"""Immutable records shared by strategies, experiments, and evaluator adapters."""

from dataclasses import dataclass
from enum import Enum
import math
from pathlib import Path
from typing import Protocol

from .settings import FINALIZED_CAPACITY_MW


@dataclass(frozen=True, order=True)
class RoundKey:
    week: int
    submission: int

    def __post_init__(self) -> None:
        if type(self.week) is not int or self.week not in (1, 2, 3):
            raise ValueError("week must be 1, 2, or 3")
        if type(self.submission) is not int or self.submission not in (1, 2):
            raise ValueError("submission must be 1 or 2")

    @property
    def graded(self) -> bool:
        return self.week in (2, 3)

    @property
    def key(self) -> str:
        return f"week-{self.week}-submission-{self.submission}"


GRADED_ROUNDS = tuple(RoundKey(w, s) for w in (2, 3) for s in (1, 2))


@dataclass(frozen=True)
class SiteProposal:
    bus_id: str
    connection_mw: float
    generator_mw: float = 0.0
    storage_power_mw: float = 0.0
    storage_energy_mwh: float = 0.0


@dataclass(frozen=True)
class Plan:
    sites: tuple[SiteProposal, ...]


@dataclass(frozen=True)
class BusFeatures:
    bus_id: str
    hosting_capacity_mw: float


@dataclass(frozen=True)
class PlanningContext:
    round: RoundKey
    team_id: str
    connection_budget_mw: float
    max_generator_to_connection_ratio: float
    energy_cost_enabled: bool
    scenario_dir: Path
    rules_file: Path
    scenario_fingerprint: str
    rules_fingerprint: str
    bus_ids: frozenset[str]
    horizon: int
    seed: int = 0
    prior_site_ids: frozenset[str] = frozenset()
    candidate_buses: tuple[BusFeatures, ...] = ()
    screening_scenario_fingerprint: str | None = None

    def __post_init__(self) -> None:
        if not math.isfinite(self.connection_budget_mw) or self.connection_budget_mw <= 0:
            raise ValueError("connection budget must be finite and positive")
        if self.connection_budget_mw > FINALIZED_CAPACITY_MW:
            raise ValueError(f"connection budget exceeds finalized {FINALIZED_CAPACITY_MW:g} MW cap")
        if self.candidate_buses:
            if self.screening_scenario_fingerprint != self.scenario_fingerprint:
                raise ValueError("screening results do not match the scenario fingerprint")
            if any(bus.bus_id not in self.bus_ids for bus in self.candidate_buses):
                raise ValueError("screening results contain an unknown bus")


class Strategy(Protocol):
    def propose(self, context: PlanningContext) -> Plan: ...


@dataclass(frozen=True)
class NamedPlan:
    team_id: str
    plan: Plan


@dataclass(frozen=True)
class Scenario:
    name: str
    opponents: tuple[NamedPlan, ...]
    seed: int


class EvaluationStatus(str, Enum):
    VALID = "valid"
    INVALID_PLAN = "invalid_plan"
    EVALUATOR_FAILURE = "evaluator_failure"


@dataclass(frozen=True)
class ScoreBreakdown:
    it_value_usd: float
    grid_energy_cost_usd: float
    generator_operating_cost_usd: float
    generator_capital_cost_usd: float
    storage_capital_cost_usd: float
    site_cost_usd: float

    @property
    def total_usd(self) -> float:
        return math.fsum((
            self.it_value_usd, -self.grid_energy_cost_usd,
            -self.generator_operating_cost_usd, -self.generator_capital_cost_usd,
            -self.storage_capital_cost_usd, -self.site_cost_usd,
        ))


@dataclass(frozen=True)
class SiteAllocation:
    site_id: str
    fraction: float
    requested_connection_mw: float
    allocated_connection_mw: float


@dataclass(frozen=True)
class EvaluationResult:
    status: EvaluationStatus
    score_usd: float | None
    service_fraction: float | None
    output_dir: Path
    issues: tuple[str, ...] = ()
    score_breakdown: ScoreBreakdown | None = None
    site_allocations: tuple[SiteAllocation, ...] = ()

    def __post_init__(self) -> None:
        if self.status == EvaluationStatus.EVALUATOR_FAILURE and self.score_usd is not None:
            raise ValueError("an evaluator failure is not a scored outcome")
        if self.status == EvaluationStatus.VALID:
            if self.score_usd is None or not math.isfinite(self.score_usd):
                raise ValueError("a valid evaluation requires a finite score, including zero")


class Evaluator(Protocol):
    def evaluate(
        self, *, context: PlanningContext, our_plan: Plan, scenario: Scenario
    ) -> EvaluationResult: ...
