"""Stage 1: select a reproducible pool of buses for constraint-based clustering.

Keep the union of high hosting-capacity buses, high composite-screening buses,
and explicitly requested buses. These are screening candidates, not clusters or
predictions of competitors' choices. Later stages must recompute their limits.
Input hashes identify the rankings used; they do not certify that historical
rankings remain valid for a changed network or Submission 2 base load.
"""

from dataclasses import asdict, dataclass
import csv
import hashlib
import io
import json
import math
from pathlib import Path


@dataclass(frozen=True)
class CandidateBus:
    bus_id: str
    hosting_capacity_mw: float
    binding_period_index: int
    hosting_rank: int
    screening_rank: int
    inclusion_reasons: tuple[str, ...]


@dataclass(frozen=True)
class CandidatePool:
    candidates: tuple[CandidateBus, ...]
    catalog_bus_count: int
    top_hosting_count: int
    top_screening_count: int
    required_bus_ids: tuple[str, ...]
    input_sha256: tuple[tuple[str, str], ...]


def _read_csv(path: Path, required: set[str]) -> tuple[list[dict[str, str]], str]:
    """Parse and hash the same bytes, so the fingerprint matches what we read."""
    content = path.read_bytes()
    reader = csv.DictReader(io.StringIO(content.decode("utf-8-sig")))
    fields = reader.fieldnames or []
    if len(fields) != len(set(fields)) or not required.issubset(fields):
        raise ValueError(f"{path.name}: duplicate headers or missing columns {sorted(required)}")
    rows = list(reader)
    if not rows:
        raise ValueError(f"{path.name}: CSV has no bus rows")
    if any(None in row or any(value is None for value in row.values()) for row in rows):
        raise ValueError(f"{path.name}: row length does not match the header")
    ids = [row["bus_id"] for row in rows]
    if any(not bus or bus != bus.strip() for bus in ids) or len(ids) != len(set(ids)):
        raise ValueError(f"{path.name}: empty, padded, or duplicate bus IDs")
    return rows, hashlib.sha256(content).hexdigest()


def _integer(value: str, *, field: str, minimum: int) -> int:
    try:
        result = int(value)
    except (ValueError, TypeError) as error:
        raise ValueError(f"{field} must be an integer") from error
    if result < minimum:
        raise ValueError(f"{field} must be at least {minimum}")
    return result


def _bus_order(bus_id: str) -> tuple[int, int, str]:
    return (0, int(bus_id), bus_id) if bus_id.isdecimal() else (1, 0, bus_id)


def load_candidate_pool(
    *,
    hosting_capacity_file: Path,
    screening_file: Path,
    bus_catalog_file: Path,
    top_hosting_count: int = 100,
    top_screening_count: int = 20,
    required_bus_ids: tuple[str, ...] = (),
) -> CandidatePool:
    """Select the union, retaining each bus's ranks and reasons for inclusion.

    Hosting capacities are rounded to six decimals ONLY for sorting; nearly
    identical solver outputs then tie consistently by bus ID. Original MW
    values are preserved. Composite screening uses its published overall_rank;
    it is not treated as the game score. Both input tables must cover the full
    supplied bus catalog, preventing accidental use of a partial ranking.
    """
    for name, count in (("top_hosting_count", top_hosting_count),
                        ("top_screening_count", top_screening_count)):
        if type(count) is not int or count < 0:
            raise ValueError(f"{name} must be a nonnegative integer")
    hosting, hosting_hash = _read_csv(
        hosting_capacity_file, {"bus_id", "min_hosting_capacity_mw", "binding_period_index"}
    )
    screening, screening_hash = _read_csv(screening_file, {"bus_id", "overall_rank"})
    catalog, catalog_hash = _read_csv(bus_catalog_file, {"bus_id"})
    catalog_ids = {row["bus_id"] for row in catalog}
    for name, rows in (("hosting capacity", hosting), ("screening", screening)):
        if {row["bus_id"] for row in rows} != catalog_ids:
            raise ValueError(f"{name} bus IDs must match the supplied bus catalog exactly")
    if any(bus not in catalog_ids for bus in required_bus_ids):
        raise ValueError("required_bus_ids contains a bus outside the supplied catalog")

    capacity, period = {}, {}
    for row in hosting:
        bus = row["bus_id"]
        try:
            mw = float(row["min_hosting_capacity_mw"])
        except ValueError as error:
            raise ValueError(f"bus {bus}: hosting capacity must be numeric") from error
        if not math.isfinite(mw) or mw < 0:
            raise ValueError(f"bus {bus}: hosting capacity must be finite and nonnegative")
        capacity[bus] = mw
        period[bus] = _integer(row["binding_period_index"], field="binding_period_index", minimum=0)
    screening_rank = {
        row["bus_id"]: _integer(row["overall_rank"], field="overall_rank", minimum=1)
        for row in screening
    }
    if set(screening_rank.values()) != set(range(1, len(catalog_ids) + 1)):
        raise ValueError("screening overall_rank must be a permutation of 1 through the bus count")

    ordered = sorted(catalog_ids, key=lambda bus: (-round(capacity[bus], 6), _bus_order(bus)))
    hosting_rank = {bus: rank for rank, bus in enumerate(ordered, start=1)}
    high_hosting = set(ordered[:top_hosting_count])
    high_screening = {bus for bus, rank in screening_rank.items() if rank <= top_screening_count}
    required = set(required_bus_ids)
    selected = high_hosting | high_screening | required
    if not selected:
        raise ValueError("candidate selection is empty; request a ranking cutoff or required bus")

    candidates = []
    for bus in ordered:
        if bus not in selected:
            continue
        reasons = tuple(label for label, group in (
            ("high_hosting_capacity", high_hosting),
            ("high_composite_screening", high_screening),
            ("required", required),
        ) if bus in group)
        candidates.append(CandidateBus(
            bus, capacity[bus], period[bus], hosting_rank[bus], screening_rank[bus], reasons
        ))
    return CandidatePool(
        tuple(candidates), len(catalog_ids), top_hosting_count, top_screening_count,
        tuple(sorted(required, key=_bus_order)),
        (("hosting_capacity", hosting_hash), ("screening", screening_hash), ("bus_catalog", catalog_hash)),
    )


def main() -> None:
    """Print a reviewable JSON pool; no optimization is performed at this stage."""
    import argparse

    root = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hosting-capacity", type=Path, default=root / "analysis/hosting_capacity_all_buses.csv")
    parser.add_argument("--screening", type=Path, default=root / "analysis/bus_screening_metrics.csv")
    parser.add_argument("--bus-catalog", type=Path, default=root / "ercot-connection-game/data/processed/activsg2000_representative_v1/bus.csv")
    parser.add_argument("--top-hosting", type=int, default=100)
    parser.add_argument("--top-screening", type=int, default=20)
    parser.add_argument("--include", action="append", default=[], help="Bus to retain regardless of rank; repeatable")
    args = parser.parse_args()
    pool = load_candidate_pool(
        hosting_capacity_file=args.hosting_capacity, screening_file=args.screening,
        bus_catalog_file=args.bus_catalog, top_hosting_count=args.top_hosting,
        top_screening_count=args.top_screening, required_bus_ids=tuple(args.include),
    )
    print(json.dumps(asdict(pool), indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
