"""Validate saved campaign evidence for interpretation without running dispatch.

This module uses the standard library. Plotting and pandas stay in the optional
notebook environment. Monetary values in returned records are USD.
"""

from collections import defaultdict
import csv
from dataclasses import dataclass
import json
import math
from pathlib import Path

from ..contracts import GRADED_ROUNDS
from .scoring import ScoreBounds

ROUND_KEYS = tuple(item.key for item in GRADED_ROUNDS)
COST_FIELDS = (
    "energy_cost", "generator_operating_cost", "generator_capital_cost",
    "storage_capital_cost", "site_cost",
)


@dataclass(frozen=True)
class ResultSource:
    strategy: str
    label: str
    summary_json: Path
    details_csv: Path | None = None
    scenario_id: str = "solo"


def _number(value, label: str) -> float:
    if isinstance(value, bool):
        raise ValueError(f"{label} must be a finite number")
    try:
        result = float(value)
    except (ValueError, TypeError):
        raise ValueError(f"{label} must be a finite number") from None
    if not math.isfinite(result):
        raise ValueError(f"{label} must be a finite number")
    return result


def _flag(value, label: str) -> bool:
    if value is True or value == "True":
        return True
    if value is False or value == "False":
        return False
    raise ValueError(f"{label} must be True or False")


def _detail_key(row, default_scenario):
    return (row["experiment"], _number(row["capacity_per_submission_mw"], "capacity"),
            row.get("scenario_id", default_scenario), row["round"])


def load_result_records(sources: list[ResultSource]) -> list[dict]:
    """Read summary JSONs, optionally enriching them with per-round CSV details.

    Incomplete campaigns are retained for per-round plots, but are not normalized.
    A recorded invalid submission may legitimately score zero. Missing/nonfinite
    scores and infrastructure failures are rejected rather than converted to zero.
    """
    records = []
    seen = set()
    for source in sources:
        payload = json.loads(source.summary_json.read_text(encoding="utf-8"))
        details = {}
        if source.details_csv is not None:
            with source.details_csv.open(newline="", encoding="utf-8") as handle:
                for row in csv.DictReader(handle):
                    key = _detail_key(row, source.scenario_id)
                    if key in details:
                        raise ValueError(f"duplicate per-round CSV detail: {key}")
                    details[key] = row
        used_details = set()
        for campaign in payload["campaigns"]:
            capacity = _number(campaign["capacity_per_submission_mw"], "capacity")
            ScoreBounds(capacity)  # Positive capacity and the shared normalization contract.
            scenario = campaign.get("scenario_id", source.scenario_id)
            for row in campaign["rounds"]:
                if row["round"] not in ROUND_KEYS:
                    raise ValueError(f"unexpected graded round: {row['round']}")
                if row.get("status") == "evaluator_failure":
                    raise ValueError("an evaluator failure cannot be plotted as a scored outcome")
                key = (campaign["experiment"], capacity, scenario, row["round"])
                unique = (source.strategy, *key)
                if unique in seen:
                    raise ValueError(f"duplicate strategy/campaign/round: {unique}")
                seen.add(unique)
                valid = _flag(row["valid"], "valid")
                feasible = _flag(row["feasible"], "feasible")
                fraction = row.get("service_fraction")
                if fraction in (None, "") and (not valid or not feasible):
                    fraction = None
                else:
                    fraction = _number(fraction, "service fraction")
                record = {
                    "strategy": source.strategy, "label": source.label,
                    "experiment": campaign["experiment"], "scenario_id": scenario,
                    "capacity_per_submission_mw": capacity, "round": row["round"],
                    "hypothetical": _flag(campaign["hypothetical_capacity_override"], "hypothetical"),
                    "initial_network_sha256": campaign.get("source_scenario_sha256"),
                    "effective_rules_sha256": campaign.get("effective_rules_sha256"),
                    "effective_release_sha256": campaign.get("effective_release_sha256"),
                    "valid": valid,
                    "feasible": feasible,
                    "score_usd": _number(row["score"], "score"),
                    "it_value_usd": _number(row["it_value"], "IT value"),
                    "service_fraction": fraction,
                    "raw_run_directory": payload.get("raw_run_directory"),
                    "summary_path": str(source.summary_json),
                }
                if fraction is not None and not 0 <= fraction <= 1:
                    raise ValueError("service fraction must lie between 0 and 1")
                for field in COST_FIELDS:
                    record[field + "_usd"] = _number(row[field], field)
                reconstructed = record["it_value_usd"] - math.fsum(record[field + "_usd"] for field in COST_FIELDS)
                if not math.isclose(record["score_usd"], reconstructed, rel_tol=1e-10, abs_tol=1.0):
                    raise ValueError(f"score breakdown does not reconcile: {unique}")
                detail = details.get(key)
                if detail is not None:
                    used_details.add(key)
                    if not math.isclose(_number(detail["score_billions"], "CSV score") * 1e9,
                                        record["score_usd"], rel_tol=1e-10, abs_tol=1.0):
                        raise ValueError(f"CSV and summary score disagree: {unique}")
                    record["bus_id"] = detail.get("bus_id")
                    shares = ("grid_supply_share", "private_generation_share")
                    if all(detail.get(field) not in (None, "") for field in shares):
                        values = [_number(detail[field], field) for field in shares]
                        if any(value < -1e-8 or value > 1 + 1e-8 for value in values):
                            raise ValueError(f"energy shares out of range: {unique}")
                        if not math.isclose(math.fsum(values), 1, abs_tol=1e-6):
                            raise ValueError(f"energy shares must sum to one: {unique}")
                        record.update(zip(shares, values))
                records.append(record)
        if used_details != set(details):
            raise ValueError(f"CSV details have no matching summary round: {source.details_csv}")
    if not records:
        raise ValueError("no saved campaign records were loaded")
    return records


def campaign_records(records: list[dict]) -> list[dict]:
    groups = defaultdict(list)
    for row in records:
        groups[(row["strategy"], row["experiment"], row["capacity_per_submission_mw"], row["scenario_id"])].append(row)
    result = []
    for key, rows in sorted(groups.items()):
        first = rows[0]
        rounds = [row["round"] for row in rows]
        if len(rounds) != len(set(rounds)):
            raise ValueError(f"duplicate round in campaign: {key}")
        complete = set(rounds) == set(ROUND_KEYS)
        total = math.fsum(row["score_usd"] for row in rows)
        result.append({
            "strategy": first["strategy"], "label": first["label"],
            "experiment": first["experiment"], "scenario_id": first["scenario_id"],
            "capacity_per_submission_mw": first["capacity_per_submission_mw"],
            "completed_rounds": len(rows), "complete": complete,
            "score_usd": total, "score_billions": total / 1e9,
            "normalized_score": ScoreBounds(first["capacity_per_submission_mw"]).normalize_usd(total) if complete else None,
            "minimum_service_fraction": min((row["service_fraction"] for row in rows
                                             if row["service_fraction"] is not None), default=None),
            "all_valid": all(row["valid"] for row in rows),
            "all_feasible": all(row["feasible"] for row in rows),
        })
    return result


def assert_comparable(records: list[dict]) -> None:
    """Require one budget/experiment and matching initial network and rules.

    S2 base-load packages may differ: each strategy follows its own S1 outcome.
    Matching fingerprints do not prove matching opponents; scenario IDs must be
    assigned consistently by the experiment author.
    """
    if not records:
        raise ValueError("no rows match the selected experiment")
    signature_fields = ("experiment", "capacity_per_submission_mw", "hypothetical",
                        "initial_network_sha256", "effective_rules_sha256", "effective_release_sha256")
    if any(not row.get(field) for row in records for field in signature_fields[3:]):
        raise ValueError("comparison requires network, rules, and release fingerprints")
    signatures = {tuple(row[field] for field in signature_fields) for row in records}
    if len(signatures) != 1:
        raise ValueError("select one experiment/budget with matching initial network and rules")
