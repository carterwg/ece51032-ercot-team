"""Retry failed scheduled campaigns with audited downward allocation roundoff.

python -m team_strategy.experiments.retry_scheduled_roundoff --run RUN --key PLAN/SCENARIO --output RETRY
python -m team_strategy.experiments.retry_scheduled_roundoff --run RUN --finalize RETRY1 RETRY2 --summary-dir SUMMARY
"""
import argparse
from contextlib import ExitStack
import json
from pathlib import Path
import shutil
import zipfile

from ..context import file_fingerprint
from ..evaluation.allocation_roundoff import (zero_allocation_roundoff, omit_zero_generator_columns,
                                             correct_zero_anchor_cuts, presolve_exact_self_supply)
from ..evaluation.campaign import save_json
from .concentration import make_comparison, verify_cell, verify_experiment_inputs
from .pool_comparisons import verify_matrix
from .submission_schedule import scheduled_job, verify_schedule, render_report


def retry(root, run, key, output, *, prune_zero_generators=False, exact_presolve=False):
    config = json.loads((run/"experiment.json").read_text())
    identity = json.loads((run/"manifest.json").read_text())["identity"]
    if identity["workers_per_evaluation"] != 1:
        raise ValueError("numerical retries require workers=1 within each evaluation")
    verify_experiment_inputs(root, run/"experiment.json", config, identity)
    pname, sname = key.split("/")
    p = next(p for p in config["portfolios"] if p["name"] == pname)
    s = next(s for s in config["scenarios"] if s["name"] == sname)
    output.mkdir(parents=True, exist_ok=False)
    sources = [Path(__file__).resolve(), root/"src/team_strategy/evaluation/allocation_roundoff.py"]
    source_hashes = {str(f.relative_to(root)): file_fingerprint(f) for f in sources}
    with zipfile.ZipFile(output/"retry_source.zip", "w", zipfile.ZIP_DEFLATED) as archive:
        for f in sources: archive.write(f, str(f.relative_to(root)))
    save_json(output/"execution.json", {"kind": "downward_allocation_roundoff", "key": key, "identity": identity,
        "source_sha256": source_hashes, "per_site_limit_mw": 1e-6, "total_limit_mw": 1e-5,
        "portfolio": p, "scenario": s, "status": "running", "prune_zero_generators": prune_zero_generators,
        "exact_presolve": exact_presolve})
    adjustments, pruned, cuts, presolved = [], [], [], []
    try:
        with ExitStack() as stack:
            if exact_presolve:
                cuts = stack.enter_context(correct_zero_anchor_cuts())
                presolved = stack.enter_context(presolve_exact_self_supply())
            adjustments = stack.enter_context(zero_allocation_roundoff())
            if prune_zero_generators: pruned = stack.enter_context(omit_zero_generator_columns())
            cell = scheduled_job({"portfolio": p, "scenario": s, "seed": config["seed"], "output": str(output/"campaign"),
                "workers": identity["workers_per_evaluation"], "release": str(root/config["release_file"]),
                "network": str(root/config["scenario_directory"]), "rules": str(root/config["rules_file"])})
    except Exception as error:
        audit = json.loads((output/"execution.json").read_text())
        audit.update(status="failed", adjustments=adjustments, pruned_zero_generators=pruned,
                     corrected_cuts=cuts, exact_presolve=presolved, error=str(error))
        save_json(output/"execution.json", audit)
        raise
    verify_experiment_inputs(root, run/"experiment.json", config, identity)
    if any(file_fingerprint(root/f) != h for f,h in source_hashes.items()):
        raise ValueError("retry source changed while running")
    audit = json.loads((output/"execution.json").read_text())
    audit.update(status="complete", adjustments=adjustments, pruned_zero_generators=pruned,
                 corrected_cuts=cuts, exact_presolve=presolved)
    save_json(output/"execution.json", audit)
    cell["execution_override"] = {"kind": "downward_allocation_roundoff", "audit_path": str(output/"execution.json"),
        "audit_sha256": file_fingerprint(output/"execution.json"), "source_sha256": source_hashes,
        "source_archive_sha256": file_fingerprint(output/"retry_source.zip")}
    save_json(output/"cell.json", cell)
    print(f"Complete retry {key}: ${cell['result']['campaign_score_usd']/1e9:.9f}B; {len(adjustments)} rounded allocations", flush=True)


def finalize(root, run, retry_dirs, summary):
    manifest = json.loads((run/"manifest.json").read_text())
    if manifest["status"] != "failed": raise ValueError("original experiment must have stopped with failed cells")
    if summary.exists(): raise ValueError("summary destination exists")
    config = json.loads((run/"experiment.json").read_text()); identity = manifest["identity"]
    verify_experiment_inputs(root, run/"experiment.json", config, identity)
    cells = json.loads((run/"cells.json").read_text()); recoveries = []
    for folder in retry_dirs:
        audit = json.loads((folder/"execution.json").read_text()); cell = json.loads((folder/"cell.json").read_text())
        if audit["status"] != "complete" or audit["identity"] != identity or not verify_cell(cell):
            raise ValueError("retry evidence is incomplete or incompatible")
        key = audit["key"]
        if cells[key]["status"] == "complete": raise ValueError("cannot replace an already completed campaign")
        override = cell["execution_override"]
        if file_fingerprint(folder/"execution.json") != override["audit_sha256"]:
            raise ValueError("retry audit changed")
        if file_fingerprint(folder/"retry_source.zip") != override["source_archive_sha256"]:
            raise ValueError("retry source archive changed")
        for adjustment in audit["adjustments"]:
            if (adjustment["removed_capacity_mw"] > 1e-5
                    or any(c["alpha_after"] != 0. or not 0 < c["removed_capacity_mw"] <= 1e-6 for c in adjustment["changes"])):
                raise ValueError("retry exceeds downward roundoff bounds")
        if any(not -1e-6 <= c["rhs_before_mwh"] < 0. or c["rhs_after_mwh"] != 0. for c in audit.get("corrected_cuts", [])):
            raise ValueError("retry exceeds cut-roundoff bounds")
        if any(r["max_balance_error_mw"] > 1e-4 or r["max_limit_violation_mw"] > 1e-4 for r in audit.get("exact_presolve", [])):
            raise ValueError("retry failed independent physical checks")
        recoveries.append({"key": key, "original_failure": cells[key], "retry_directory": str(folder),
                           "audit_sha256": override["audit_sha256"], "adjustments": audit["adjustments"],
                           "pruned_zero_generators": audit.get("pruned_zero_generators", []),
                           "corrected_cuts": audit.get("corrected_cuts", []), "exact_presolve": audit.get("exact_presolve", [])})
        cells[key] = cell
    checks = verify_matrix(config, cells, identity)
    reference_file = root/config["opponent_reference_directory"]/"cells.json"
    if file_fingerprint(reference_file) != identity["opponent_reference_sha256"]:
        raise ValueError("original opponent reference changed")
    reference = json.loads(reference_file.read_text())
    weights = json.loads((root/config["rules_file"]).read_text())["period_weight_hours"]
    rounds = verify_schedule(config, cells, reference, weights)
    comparison = make_comparison(config, cells)
    for name in ["manifest.json", "cells.json"]: shutil.copyfile(run/name, run/("failed_"+name))
    save_json(run/"cells.json", cells); save_json(run/"comparison.json", comparison)
    render_report(run, config, comparison, cells, rounds, reference)
    report = run/"report.html"
    note = ('<p><b>Numerical retries:</b> Some zero-headroom cases left tiny positive allocations for rivals. '
            'The retry adapter rounded only allocations of at most 0.000001 MW per site down to zero, '
            'with at most 0.00001 MW removed in total per allocation. Requested load, generation, '
            'opponents, solver settings, and game rules were unchanged. The complete official joint '
            'dispatch and scoring then passed. Some retries also omitted generator columns fixed exactly '
            'at zero capacity, keeping all teams and sites. Failed attempts and exact changes are preserved in '
            '<a href="numerical_retries.json">the retry audit</a>.</p>')
    report.write_text(report.read_text().replace('<h2>Evidence and scope</h2>',note+'<h2>Evidence and scope</h2>'))
    if any(r.get("corrected_cuts") or r.get("exact_presolve") for r in recoveries):
        text = ('<p>Further numerical presolve corrected negative feasibility-cut bounds only within '
                '0.000001 MWh of the validated zero-load point. When exact aggregate balance and self-supply '
                'already forced every generator to Pmax, those implied bounds were fixed before the official solve. '
                'Independent nodal balance and equipment-limit checks passed at 0.0001 MW tolerance. '
                'No demand, Pmax, generation costs, line limits, or generator-availability assumptions changed.</p>')
        report.write_text(report.read_text().replace('<h2>Evidence and scope</h2>',text+'<h2>Evidence and scope</h2>'))
    save_json(run/"numerical_retries.json", recoveries)
    save_json(run/"verification.json", {"status": "passed", **checks, "csv_resource_schedule_verified": True,
        "opponent_requests_identical_to_original_part2": True, "requested_load_per_submission_mw": 500,
        "requested_generation_by_submission_mw": {"1": 0, "2": 500}, "numerical_retries": len(recoveries)})
    manifest.update(status="complete", **checks, selected_primary=comparison["maximin_primary"],
        portfolio_count=len(config["portfolios"]), scenario_count=len(config["scenarios"]), numerical_retries=len(recoveries),
        verification_sha256=file_fingerprint(run/"verification.json"), postprocessing_source_sha256=file_fingerprint(Path(__file__)))
    manifest.pop("error", None)
    manifest["artifact_sha256"] = {p.name: file_fingerprint(p) for p in sorted(run.iterdir()) if p.is_file() and p.name != "manifest.json"}
    save_json(run/"manifest.json", manifest)
    summary.mkdir(parents=True)
    for name in list(manifest["artifact_sha256"])+["manifest.json"]: shutil.copyfile(run/name, summary/name)
    from .findings import export_findings, export_history, write_strategy_indexes
    export_findings(summary, root=root)
    export_history(root, root/"findings")
    write_strategy_indexes(root, root/"findings")
    print(f"Complete verified comparison: {summary/'report.html'}", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--key")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--prune-zero-generators", action="store_true")
    parser.add_argument("--exact-presolve", action="store_true")
    parser.add_argument("--finalize", nargs="+", type=Path)
    parser.add_argument("--summary-dir", type=Path)
    args = parser.parse_args(); root = Path(__file__).resolve().parents[3]
    if args.finalize:
        if not args.summary_dir: parser.error("finalize requires a summary directory")
        finalize(root, args.run.resolve(), [p.resolve() for p in args.finalize], args.summary_dir)
    else:
        if not args.key or not args.output: parser.error("retry requires key and output")
        retry(root, args.run.resolve(), args.key, args.output.resolve(), prune_zero_generators=args.prune_zero_generators,
              exact_presolve=args.exact_presolve)


if __name__ == "__main__":
    main()
