"""Combine disjoint completed opponent matrices without rerunning or relabeling them.

Example: python -m team_strategy.experiments.pool_comparisons --runs RUN1 RUN2
 --output-dir analysis/strategy/part2
"""
import argparse
import csv
import hashlib
import html
import json
import math
from pathlib import Path
import shutil
import zipfile

from ..context import file_fingerprint
from ..contracts import GRADED_ROUNDS
from ..evaluation.campaign import save_json
from .concentration import (load_experiment, make_comparison, verify_cell,
                            verify_experiment_inputs, write_report)


def combine_specifications(configs, identities):
    """Only scenarios and explanatory assumptions may differ between runs."""
    if not configs or len(configs) != len(identities):
        raise ValueError("matching configurations and identities are required")
    base = configs[0]
    stable = lambda c: {k: v for k, v in c.items() if k not in {"scenarios", "assumptions"}}
    identity = lambda i: {k: v for k, v in i.items() if k != "config_sha256"}
    if any(stable(c) != stable(base) for c in configs[1:]):
        raise ValueError("portfolio, seed, resource, or rule specifications differ")
    if any(identity(i) != identity(identities[0]) for i in identities[1:]):
        raise ValueError("source, network, rules, or solver identities differ")
    scenarios = [s for c in configs for s in c["scenarios"]]
    names = [s["name"] for s in scenarios]
    if len(names) != len(set(names)):
        raise ValueError("scenario names overlap between component matrices")
    return {**base, "scenarios": scenarios,
            "assumptions": base["assumptions"] + " Pooled disjoint matched matrices with identical source, inputs, portfolios, and seed; all competitive hypotheses receive equal weight."}


def verify_site_permutation(original, executed):
    """A numerical retry may change row order, never physical bus capacities."""
    other = lambda p: {k: v for k, v in p.items() if k not in {"bus_ids", "weights"}}
    geometry = lambda p: dict(zip(p["bus_ids"], p["weights"], strict=True))
    if (other(original) != other(executed)
            or len(set(executed["bus_ids"])) != len(executed["bus_ids"])
            or geometry(original) != geometry(executed)):
        raise ValueError("retry changes the physical portfolio rather than its row order")


def recover_run(root, directory, retry_directory):
    """Finalize a failed matrix using a fully evaluated equivalent row permutation.

    Call only after the original process has stopped. Its interrupted attempt,
    failure manifest, and original checkpoint remain in the evidence directory.
    """
    manifest = json.loads((directory / "manifest.json").read_text())
    if manifest["status"] != "failed":
        raise ValueError("recovery requires a stopped, failed original run")
    config = freeze_inputs(root, directory, manifest["identity"])
    audit = json.loads((retry_directory / "execution.json").read_text())
    if audit["kind"] != "site_order_permutation" or audit["identity"] != manifest["identity"]:
        raise ValueError("retry source and network identity differ")
    original = next(p for p in config["portfolios"] if p["name"] == audit["original_portfolio"]["name"])
    if original != audit["original_portfolio"] or audit["scenario"] not in config["scenarios"]:
        raise ValueError("retry specification differs from the original experiment")
    verify_site_permutation(original, audit["executed_portfolio"])
    cell = json.loads((retry_directory / "cell.json").read_text())
    if not verify_cell(cell):
        raise ValueError("retry is not complete")
    expected_mw = {b: 500 * w for b, w in zip(original["bus_ids"], original["weights"], strict=True)}
    for key in GRADED_ROUNDS:
        path = Path(cell["output"]) / key.key / "inputs/team-000.csv"
        with path.open(newline="") as stream:
            rows = list(csv.DictReader(stream))
        if len(rows) != len(expected_mw) or {r["bus_id"] for r in rows} != set(expected_mw):
            raise ValueError("retry CSV geometry differs from the original portfolio")
        for row in rows:
            mw = expected_mw[row["bus_id"]]
            if (row["team_id"] != "our-team" or not math.isclose(float(row["connection_capacity_mw"]), mw, abs_tol=1e-8, rel_tol=0)
                    or not math.isclose(float(row["generator_capacity_mw"]), mw * original["generator_fraction"], abs_tol=1e-8, rel_tol=0)
                    or float(row["storage_power_mw"]) != 0 or float(row["storage_energy_mwh"]) != 0):
                raise ValueError("retry changes requested bus capacity or resources")
    key = original["name"] + "/" + audit["scenario"]["name"]
    cells = json.loads((directory / "cells.json").read_text())
    if {k for k, v in cells.items() if v["status"] != "complete"} != {key}:
        raise ValueError("recovery requires exactly the declared failed campaign")
    failed = cells[key]
    cells[key] = cell
    verify_matrix(config, cells, manifest["identity"])
    comparison = make_comparison(config, cells)
    shutil.copyfile(directory / "manifest.json", directory / "failed_manifest_before_recovery.json")
    shutil.copyfile(directory / "cells.json", directory / "failed_cells_before_recovery.json")
    recovery = {"campaign": key, "method": "Reverse site rows; identical capacity and resource allocation by bus.",
                "reason": "Original quadratic allocation tie-break exceeded the diagnostic waiting period and was interrupted; no score was inferred from that attempt.",
                "original_failed_cell": failed, "retry_directory": str(retry_directory.resolve()),
                "execution_sha256": file_fingerprint(retry_directory / "execution.json"),
                "retry_cell_sha256": file_fingerprint(retry_directory / "cell.json"),
                "source_sha256": file_fingerprint(Path(__file__)),
                "prior_manifest_sha256": file_fingerprint(directory / "failed_manifest_before_recovery.json"),
                "prior_cells_sha256": file_fingerprint(directory / "failed_cells_before_recovery.json")}
    save_json(directory / "cells.json", cells)
    save_json(directory / "comparison.json", comparison)
    write_report(directory, config, comparison, cells)
    manifest.update(status="complete", campaign_count=len(cells), evaluation_count=4 * len(cells),
                    selected_primary=comparison["maximin_primary"], numerical_recovery=recovery)
    manifest.pop("failed_cells", None)
    save_json(directory / "manifest.json", manifest)
    return recovery


def verify_matrix(config, cells, identity, *, match_rival_hashes=True):
    """Check complete evidence, score arithmetic, matched rivals, and carryover."""
    required = {p["name"] + "/" + s["name"] for p in config["portfolios"] for s in config["scenarios"]}
    if set(cells) != required:
        raise ValueError("component does not contain its exact complete matrix")
    opponent_hashes = {}
    for p in config["portfolios"]:
        for s in config["scenarios"]:
            cell = cells[p["name"] + "/" + s["name"]]
            if not verify_cell(cell):
                raise ValueError("component contains an incomplete campaign")
            result = cell["result"]
            expected = {"portfolio": p["name"], "scenario": s["name"], "role": p["role"],
                        "generator_fraction": p["generator_fraction"], "seed": config["seed"],
                        "include_in_risk": s["include_in_risk"]}
            if any(result.get(k) != v for k, v in expected.items()):
                raise ValueError("campaign metadata differs from experiment specifications")
            if len(result["rounds"]) != 4 or not math.isclose(result["campaign_score_usd"], sum(r["score_usd"] for r in result["rounds"]), abs_tol=.01, rel_tol=0):
                raise ValueError("campaign score does not equal four round scores")
            rounds = {r["round"]: r for r in result["rounds"]}
            rival_count = s.get("rival_count", len(s["rival_bus_ids"]))
            teams = {"our-team"} | {f"rival-{i+1:02d}" for i in range(rival_count)}
            for key in GRADED_ROUNDS:
                r = rounds[key.key]
                if (r["status"] != "valid" or r["horizon"] != 120 or r["competition_scope"] not in {"joint", "joint_projection"}
                        or r["rules_sha256"] != identity["rules_sha256"] or set(r["input_sha256_by_team"]) != teams):
                    raise ValueError("round scope, rules, horizon, or team roster differs")
                rivals = {k: v for k, v in r["input_sha256_by_team"].items() if k != "our-team"}
                matched_key = (s["name"], key.key)
                if opponent_hashes.setdefault(matched_key, rivals) != rivals and match_rival_hashes:
                    raise ValueError("opponent requests are not matched across portfolios")
                if r["energy_cost_enabled"] != (key.week == 3):
                    raise ValueError("energy pricing does not match the graded week")
                b = r["score_breakdown"]
                score = b["it_value_usd"] - sum(v for k, v in b.items() if k != "it_value_usd")
                if not math.isclose(score, r["score_usd"], abs_tol=.01, rel_tol=0):
                    raise ValueError("round economic components do not sum to the score")
            if len(result["carryovers"]) != 2:
                raise ValueError("both weekly carryovers are required")
            for week in (2, 3):
                a, b = (rounds[f"week-{week}-submission-{i}"] for i in (1, 2))
                carried = next(c for c in result["carryovers"] if c["week"] == week)
                if (a["scenario_sha256"] != identity["scenario_sha256"]
                        or carried["source_scenario_sha256"] != identity["scenario_sha256"]
                        or b["scenario_sha256"] != carried["carried_scenario_sha256"]
                        or set(carried["team_ids"]) != teams
                        or carried["validation"]["passed_period_count"] != 120
                        or not {x["site_id"] for x in a["site_allocations"]}.isdisjoint(x["site_id"] for x in b["site_allocations"])):
                    raise ValueError("weekly reset or all-team carryover is inconsistent")
    return {"campaign_count": len(cells), "evaluation_count": 4 * len(cells),
            "matched_opponent_round_count": len(opponent_hashes), "all_artifact_hashes_verified": True,
            "weekly_resets_and_all_team_carryover_verified": True, "economic_arithmetic_verified": True}


def freeze_inputs(root, directory, identity):
    """Preserve the exact configuration and source after checking their hashes."""
    config_path = directory / "experiment.json"
    if not config_path.exists():
        matches = [p for p in (root / "configs/experiments").glob("*.json")
                   if file_fingerprint(p) == identity["config_sha256"]]
        if not matches:
            raise ValueError("exact experiment configuration is unavailable")
        config_path = matches[0]
    config, _ = load_experiment(config_path, root)
    verify_experiment_inputs(root, config_path, config, identity)
    if config_path != directory / "experiment.json":
        shutil.copyfile(config_path, directory / "experiment.json")
    snapshot = directory / "source_snapshot.zip"
    if not snapshot.exists():
        with zipfile.ZipFile(snapshot, "w", zipfile.ZIP_DEFLATED) as archive:
            for name in identity["source_sha256"]:
                archive.writestr(zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0)),
                                 (root / name).read_bytes(), compress_type=zipfile.ZIP_DEFLATED)
    with zipfile.ZipFile(snapshot) as archive:
        if any(hashlib.sha256(archive.read(name)).hexdigest() != digest
               for name, digest in identity["source_sha256"].items()):
            raise ValueError("archived evaluation source differs from the manifest")
    return config


def write_interpretation(output, config, comparison, cells):
    """Make the measured allocation mechanism visible beside aggregate scores."""
    primary = [p["name"] for p in config["portfolios"] if p["role"] == "primary"]
    risk = comparison["risk_scenarios"]
    selected = comparison["maximin_primary"]
    scores = comparison["campaign_scores_usd"]
    selected_values = [scores[selected][s] / 1e9 for s in risk]
    s2 = [r["service_fraction"] for c in cells.values()
          if c["result"]["portfolio"] in primary and c["result"]["scenario"] in risk
          for r in c["result"]["rounds"] if r["round"].endswith("submission-2")]
    selected_rounds = {key.key: [next(r for r in cells[selected + "/" + s]["result"]["rounds"]
                                    if r["round"] == key.key)["service_fraction"] for s in risk]
                       for key in GRADED_ROUNDS}
    insights = {"selected_primary": selected, "selected_mean_score_billions": sum(selected_values) / len(selected_values),
                "selected_worst_score_billions": min(selected_values),
                "primary_s2_fraction_range": [min(s2), max(s2)],
                "selected_mean_service_fraction_by_round": {k: sum(v) / len(v) for k, v in selected_rounds.items()}}
    # Preserve the successful numerical row order when exporting this geometry.
    for cell in cells.values():
        override = cell.get("execution_override")
        if cell["result"]["portfolio"] == selected and override:
            original = next(p for p in config["portfolios"] if p["name"] == selected)
            executed = {**original, "bus_ids": override["executed_bus_ids"], "weights": override["weights"]}
            verify_site_permutation(original, executed)
            save_json(output / "recommended_strategy.json", {"strategy": "corridor_portfolio", "params": {
                "bus_ids": executed["bus_ids"], "weights": executed["weights"],
                "generator_fraction": executed["generator_fraction"]}})
            insights["recommended_export_bus_order"] = executed["bus_ids"]
    benchmark = next((p for p in config["portfolios"] if p["name"] == "carter_cg_benchmark"), None)
    benchmark_text = ""
    if benchmark:
        name = benchmark["name"]
        values = [scores[name][s] / 1e9 for s in risk]
        gaps = [(scores[name][s] - max(scores[p][s] for p in primary)) / 1e9 for s in risk]
        insights["cg_benchmark"] = {"mean_score_billions": sum(values) / len(values),
                                   "worst_score_billions": min(values),
                                   "minimum_advantage_over_best_primary_billions": min(gaps),
                                   "beats_every_primary_in_every_stress_scenario": min(gaps) > 0}
        save_json(output / "benchmark_strategy.json", {"strategy": "corridor_portfolio", "params": {
            "bus_ids": benchmark["bus_ids"], "weights": benchmark["weights"],
            "generator_fraction": benchmark["generator_fraction"]}})
        benchmark_text = (f"<p>The C = G benchmark averages ${sum(values)/len(values):.3f}B and has a worst campaign of ${min(values):.3f}B. "
                          + (f"It exceeds every grid-only primary in every competitive scenario; its smallest advantage over that scenario's best primary is ${min(gaps):.3f}B. " if min(gaps) > 0 else "Its resource cost and allocation tradeoff is reported separately. ")
                          + 'The grid-only geometry recommendation therefore does not establish the best overall resource plan. '
                            'Only bus 6141 was tested with C = G; the experiment does not rank C = G locations or optimize generator size. '
                            '<a href="benchmark_strategy.json">Benchmark configuration</a>.</p>')
    section = (f'<h2>Reading the measured result</h2><p>The conditional grid-only choice, <b>{html.escape(selected)}</b>, '
               f'averages ${insights["selected_mean_score_billions"]:.3f}B across {len(risk)} competitive hypotheses '
               f'and has a worst campaign of ${min(selected_values):.3f}B. '
               f'Across the primary plans, S2 service fractions range from {100*min(s2):.3f}% to {100*max(s2):.3f}% in these scenarios. '
               'Moving capacity between corridors does not remove the common supply ceiling. These fractions are genuine scored allocations, '
               'with existing S1 withdrawals already carried into the network.</p>' + benchmark_text
               + '<p>These are fixed opponent stress tests, not predictions of classmates or evidence of an equilibrium. '
                 '<a href="interpretation.json">Computed interpretation data</a>.</p>')
    if comparison.get("numerical_recoveries"):
        section += ('<p><b>Numerical retry:</b> The 6062/6298 split against five rivals at 6141 required '
                    'reversing the two site rows after the original quadratic tie-break ran for an extended period. '
                    'Both sites still request 250 MW, with the same opponents, source, solver, and tolerances. '
                    'The original attempt and complete official retry are retained; no zero or estimated score was substituted. '
                    'The selected geometry is exported using the successful row order. '
                    'See component recovery records in the manifest.</p>')
    save_json(output / "interpretation.json", insights)
    report = output / "report.html"
    report.write_text(report.read_text().replace('<h2>Candidate plans</h2>', section + '<h2>Candidate plans</h2>'))


def pool_runs(root, run_dirs, output):
    if output.exists():
        raise ValueError("pooled output must be a fresh directory")
    configs, manifests, merged, components = [], [], {}, []
    for directory in run_dirs:
        manifest = json.loads((directory / "manifest.json").read_text())
        if manifest["status"] != "complete":
            raise ValueError("only completed matrices can be pooled")
        config = freeze_inputs(root, directory, manifest["identity"])
        cells = json.loads((directory / "cells.json").read_text())
        checks = verify_matrix(config, cells, manifest["identity"])
        configs.append(config); manifests.append(manifest)
        if merged.keys() & cells.keys():
            raise ValueError("component campaign keys overlap")
        merged.update(cells)
        components.append({"directory": str(directory.resolve()), "checks": checks,
                           "artifact_sha256": {name: file_fingerprint(directory / name) for name in
                                               ("manifest.json", "cells.json", "experiment.json", "source_snapshot.zip")}})
    config = combine_specifications(configs, [m["identity"] for m in manifests])
    checks = verify_matrix(config, merged, manifests[0]["identity"])
    comparison = make_comparison(config, merged)
    comparison["numerical_recoveries"] = [m["numerical_recovery"] for m in manifests if "numerical_recovery" in m]
    output.mkdir(parents=True)
    save_json(output / "experiment.json", config)
    save_json(output / "cells.json", merged)
    save_json(output / "comparison.json", comparison)
    write_report(output, config, comparison, merged)
    write_interpretation(output, config, comparison, merged)
    for i, directory in enumerate(run_dirs, 1):
        shutil.copyfile(directory / "source_snapshot.zip", output / f"component-{i}-source.zip")
    shutil.copyfile(Path(__file__), output / "pool_comparisons.py")
    save_json(output / "verification.json", {"status": "passed", **checks, "components": components})
    save_json(output / "manifest.json", {"schema_version": 1, "kind": "pooled_complete_campaigns", "status": "complete",
        "identity": {**manifests[0]["identity"], "config_sha256": file_fingerprint(output / "experiment.json")},
        "components": components, **checks, "horizon": 120,
        "numerical_recoveries": comparison["numerical_recoveries"],
        "scenario_count": len(config["scenarios"]), "risk_scenario_count": len(comparison["risk_scenarios"]),
        "portfolio_count": len(config["portfolios"]), "selected_primary": comparison["maximin_primary"],
        "pooling_source_sha256": file_fingerprint(Path(__file__)),
        "verification_sha256": file_fingerprint(output / "verification.json"),
        "artifact_sha256": {p.name: file_fingerprint(p) for p in sorted(output.iterdir()) if p.is_file()}})
    from .findings import export_findings
    export_findings(output, root=root)
    return comparison


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runs", nargs="+", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    result = pool_runs(Path(__file__).resolve().parents[3], args.runs, args.output_dir)
    print(f"Verified pooled comparison: {args.output_dir / 'report.html'}; primary choice: {result['maximin_primary']}")


if __name__ == "__main__":
    main()
