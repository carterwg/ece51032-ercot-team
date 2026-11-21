"""Matched siting comparison: grid-only S1, C=G at new S2 sites.

python -m team_strategy.experiments.submission_schedule --output-dir RUN
 --summary-dir analysis/strategy/part2-s1-grid-s2-cg --jobs 4
"""
import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import csv
import html
import json
import math
from pathlib import Path
import shutil
import sys
import zipfile

from ..context import file_fingerprint, scenario_fingerprint
from ..evaluation.campaign import run_campaign, save_json
from ..strategies.corridor_portfolio import CorridorPortfolio
from ..strategies.submission_generation import SubmissionGenerationPortfolio
from .concentration import (load_experiment, make_comparison, verify_cell,
                            verify_experiment_inputs)
from .pool_comparisons import verify_matrix


def load_schedule(path, root):
    config, part1 = load_experiment(path, root)
    if (config.get("generation_schedule") != {"1": 0., "2": 1.}
            or any(p["role"] != "primary" or p["generator_fraction"] != 1. for p in config["portfolios"])):
        raise ValueError("all layouts must use zero generation in S1 and C=G in S2")
    reference = root / config["opponent_reference_directory"]
    manifest = json.loads((reference / "manifest.json").read_text())
    digest = file_fingerprint(reference / "cells.json")
    if manifest["status"] != "complete" or digest != manifest["artifact_sha256"]["cells.json"]:
        raise ValueError("original opponent reference evidence changed")
    original = json.loads((reference / "experiment.json").read_text())
    if config["scenarios"] != original["scenarios"]:
        raise ValueError("opponent scenarios must match the original Part 2 experiment")
    return config, part1, digest


def scheduled_job(job):
    p, s = job["portfolio"], job["scenario"]
    opponents = tuple((f"rival-{i+1:02d}", CorridorPortfolio((bus,), generator_fraction=s["rival_generator_fraction"]))
                      for i, bus in enumerate(s["rival_bus_ids"]))
    result = run_campaign(strategy=SubmissionGenerationPortfolio(p["bus_ids"], p["weights"]),
        opponent_strategies=opponents, scenario_name=s["name"], seed=job["seed"], output_dir=Path(job["output"]),
        release_file=Path(job["release"]), scenario_dir=Path(job["network"]), rules_file=Path(job["rules"]),
        workers=job["workers"], solver_backend="highs")
    result.update(portfolio=p["name"], role="primary", generator_fraction=1.,
                  generation_schedule={"1": 0., "2": 1.}, include_in_risk=s["include_in_risk"])
    save_json(Path(job["output"]) / "campaign.json", result)
    return {"status": "complete", "output": job["output"], "result": result,
            "artifact_sha256": {str(f.relative_to(job["output"])): file_fingerprint(f)
                                for f in sorted(Path(job["output"]).rglob("*")) if f.is_file()}}


def check_requested_resources(rows, portfolio, submission):
    expected = dict(zip(portfolio["bus_ids"], (500*w for w in portfolio["weights"]), strict=True))
    if len(rows) != len(expected) or {r["bus_id"] for r in rows} != set(expected):
        raise ValueError("requested site geometry differs from the declared layout")
    for row in rows:
        c = expected[row["bus_id"]]
        g = c if submission == 2 else 0.
        if (row["team_id"] != "our-team"
                or not math.isclose(float(row["connection_capacity_mw"]), c, abs_tol=1e-8, rel_tol=0)
                or not math.isclose(float(row["generator_capacity_mw"]), g, abs_tol=1e-8, rel_tol=0)
                or float(row["storage_power_mw"]) != 0 or float(row["storage_energy_mwh"]) != 0):
            raise ValueError("requested load/generation does not match the submission schedule")


def verify_schedule(config, cells, reference_cells, weights):
    """Check actual CSV resources and rivals, then measure actual energy sources."""
    rows = []
    for p in config["portfolios"]:
        for s in config["scenarios"]:
            cell = cells[p["name"] + "/" + s["name"]]
            original = {r["round"]: r for r in reference_cells["concentrate_6141/" + s["name"]]["result"]["rounds"]}
            for r in cell["result"]["rounds"]:
                submission = int(r["round"][-1]); folder = Path(cell["output"]) / r["round"]
                with (folder / "inputs/team-000.csv").open(newline="") as stream:
                    check_requested_resources(list(csv.DictReader(stream)), p, submission)
                rivals = lambda x: {k: v for k, v in x["input_sha256_by_team"].items() if k != "our-team"}
                if rivals(r) != rivals(original[r["round"]]):
                    raise ValueError("opponent requests differ from the original Part 2 experiment")
                with (folder / "canonical/site_net_withdrawal.csv").open(newline="") as stream:
                    actual = [x for x in csv.DictReader(stream) if x["team_id"] == "our-team"]
                load = math.fsum(float(x["load_mw"])*weights[int(x["period_index"])] for x in actual)
                gen = math.fsum(float(x["generation_mw"])*weights[int(x["period_index"])] for x in actual)
                by_period = {}
                for x in actual:
                    i = int(x["period_index"])
                    by_period[i] = by_period.get(i, 0.) + float(x["generation_mw"])
                b = r["score_breakdown"]
                rows.append({"portfolio": p["name"], "scenario": s["name"], "round": r["round"],
                    "requested_load_mw": 500., "requested_generation_mw": 500. if submission == 2 else 0.,
                    "allocated_load_mw": 500*r["service_fraction"], "service_fraction": r["service_fraction"],
                    "score_billions": r["score_usd"]/1e9, "it_value_billions": b["it_value_usd"]/1e9,
                    "site_cost_billions": b["site_cost_usd"]/1e9,
                    "generator_capital_billions": b["generator_capital_cost_usd"]/1e9,
                    "generator_operation_billions": b["generator_operating_cost_usd"]/1e9,
                    "grid_energy_cost_billions": b["grid_energy_cost_usd"]/1e9,
                    "private_generation_energy_fraction": gen/load if load else 0.,
                    "peak_private_generation_mw": max(by_period.values(), default=0.)})
    return rows


def render_report(output, config, comparison, cells, rounds, reference):
    def table(headers, rows):
        esc = lambda x: html.escape(str(x))
        return '<table><tr>'+''.join(f'<th>{esc(x)}</th>' for x in headers)+'</tr>'+''.join(
            '<tr>'+''.join(f'<td>{esc(x)}</td>' for x in row)+'</tr>' for row in rows)+'</table>'
    selected = next(p for p in config["portfolios"] if p["name"] == comparison["maximin_primary"])
    save_json(output / "recommended_strategy.json", {"strategy": "submission_generation", "params": {
        "bus_ids": selected["bus_ids"], "weights": selected["weights"]}})
    for name, records in [("comparison.csv", comparison["summary"]), ("rounds.csv", rounds)]:
        with (output / name).open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=list(records[0])); writer.writeheader(); writer.writerows(records)
    risk = comparison["risk_scenarios"]
    scores = comparison["campaign_scores_usd"]
    mean = lambda name: math.fsum(scores[name][s] for s in risk)/len(risk)/1e9
    concentrate = max((p for p in config["portfolios"] if len(p["bus_ids"]) == 1), key=lambda p: mean(p["name"]))
    split = max((p for p in config["portfolios"] if len(p["bus_ids"]) > 1), key=lambda p: mean(p["name"]))
    matched = {s: (scores[split["name"]][s]-scores[concentrate["name"]][s])/1e6 for s in risk}
    baseline = []
    for label, name in [("Grid-only S1 and S2", "concentrate_6141"), ("C=G in S1 and S2", "carter_cg_benchmark")]:
        values = [reference[name+"/"+s]["result"]["campaign_score_usd"]/1e9 for s in risk]
        baseline.append((label, f'{sum(values)/len(values):.6f}', f'{min(values):.6f}'))
    baseline.append(("Grid-only S1; C=G S2 (new)", f'{mean("concentrate_6141"):.6f}',
                     f'{min(scores["concentrate_6141"][s] for s in risk)/1e9:.6f}'))
    interpretation = {"best_mean_concentrated": concentrate["name"], "best_mean_split": split["name"],
        "best_split_minus_best_concentrated_mean_million_usd": (mean(split["name"])-mean(concentrate["name"]))*1000,
        "paired_split_minus_concentrated_million_usd": matched,
        "minimum_allocation_fraction": min(r["service_fraction"] for r in rounds),
        "maximum_allocation_fraction": max(r["service_fraction"] for r in rounds),
        "mean_scores_billions": {p["name"]: mean(p["name"]) for p in config["portfolios"]},
        "solo_scores_billions": {p["name"]: scores[p["name"]]["solo"]/1e9 for p in config["portfolios"]}}
    save_json(output / "interpretation.json", interpretation)
    specs = [(p["name"], ', '.join(f'{b}: {500*w:g} MW' for b,w in zip(p["bus_ids"],p["weights"],strict=True))) for p in config["portfolios"]]
    metrics = [(p["name"],f'{mean(p["name"]):.6f}',f'{min(scores[p["name"]][s] for s in risk)/1e9:.6f}',
                f'{(mean(p["name"])-mean("concentrate_6141"))*1000:+.3f}') for p in config["portfolios"]]
    scenarios = [s["name"] for s in config["scenarios"]]
    html_text = f'''<!doctype html><html><head><meta charset="utf-8"><title>S1 grid-only, S2 C=G: siting comparison</title>
<style>body{{font:16px/1.55 system-ui;max-width:1400px;margin:32px auto;padding:0 24px;color:#172233}}table{{border-collapse:collapse;margin:20px 0;width:100%;font-size:14px}}td,th{{border:1px solid #d7dee7;padding:9px;text-align:left}}th{{background:#edf2f8}}.note{{padding:16px;background:#edf5ff}}.wide{{overflow-x:auto}}</style></head><body>
<h1>Concentrate or split: grid-only S1, C=G in S2</h1>
<p>Every layout requests 500 MW of new load and zero generation in S1, then 500 MW of new load and 500 MW of new generation in S2, in both weeks. Generation is installed at each new S2 site's own bus in proportion to its load. Existing S1 sites remain grid-only; their actual withdrawals carry into S2 and are not scored again. Weeks reset.</p>
<div class="note">Complete matched comparison: {len(cells)} campaigns × 4 submissions × 120 periods. Conditional maximin choice: <b>{html.escape(selected['name'])}</b>. Best mean concentrated: {html.escape(concentrate['name'])}; best mean split: {html.escape(split['name'])}. Their mean difference (split minus concentrated) is {(mean(split['name'])-mean(concentrate['name']))*1000:+.3f} million USD.</div>
<h2>Allocation and economics</h2><p>Across all scored rounds, admitted fractions range from {interpretation['minimum_allocation_fraction']:.9f} to {interpretation['maximum_allocation_fraction']:.9f}. Full admission makes IT value and site costs equal across layouts; when full admission holds, remaining score differences come from grid electricity prices and private-generator operating costs. The S1/S2 schedule requests $2B of generator capital per four-round campaign at full admission, versus $4B for C=G in both submissions. These are game scores with present-value energy economics.</p>
<h2>Layouts (same requested MW each submission)</h2>{table(('Layout','Bus allocation'),specs)}
<p>6062 and 6298 share b02136 under stress; site count does not establish independent corridors. S1 and S2 use the same layout in this experiment.</p>
<h2>Competitive scenarios: scores and paired differences</h2>{table(('Layout','Mean score, $B','Worst score, $B','Mean gain vs 6141, $M'),metrics)}
<p>Six competitive hypotheses receive equal weight, not forecast probabilities. Solo is excluded. Mean differences use unrounded scores. Maximin, mean, and regret are retained separately in <a href="comparison.json">comparison data</a>.</p>
<h2>Same-bus policy comparison at 6141</h2>{table(('Resource policy','Competitive mean, $B','Worst, $B'),baseline)}
<p>The two earlier policies come from the verified original Part 2 report under identical rival request CSVs. The new policy is freshly evaluated. This table holds our bus fixed; rival dispatch and carried withdrawals may respond to our resource policy.</p>
<h2>Campaign scores by scenario ($B)</h2><div class="wide">{table(('Layout',*scenarios),[(p['name'],*(f'{scores[p['name']][s]/1e9:.6f}' for s in scenarios)) for p in config['portfolios']])}</div>
<h2>Opponent hypotheses</h2>{table(('Scenario','Rival buses (500 MW each)','Rival G/C in both S1 and S2','Risk'),[(s['name'],', '.join(s['rival_bus_ids']) or 'none',s['rival_generator_fraction'],s['include_in_risk']) for s in config['scenarios']])}
<p>Only our generation schedule changes. Five-rival scenarios remain grid-only; the seven-rival scenario retains G/C=0.5 in both submissions. Opponent CSV fingerprints match the original experiment round by round.</p>
<h2>Evidence and scope</h2><p><a href="rounds.csv">Round scores, allocation, generation energy shares, and cost breakdowns</a>; <a href="interpretation.json">interpretation data</a>; <a href="recommended_strategy.json">exportable scheduled strategy</a>; <a href="experiment.json">configuration</a>; <a href="verification.json">verification</a>; <a href="manifest.json">source and input hashes</a>; <a href="cells.json">raw campaign references</a>.</p>
<p>Finite fixed-layout comparison under the declared opponents. Opponent adaptation, changes of S2 location relative to S1, generator-size optimization, and calibrated probability forecasts are outside this experiment. No submissions are uploaded.</p></body></html>'''
    (output / "report.html").write_text(html_text)


def main():
    root = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=root/"configs/experiments/corridor_part2_s2_generation.json")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--summary-dir", type=Path)
    parser.add_argument("--jobs", type=int, default=4)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    if args.jobs < 1 or args.workers < 1 or (args.summary_dir and args.summary_dir.exists()):
        parser.error("jobs/workers must be positive and summary destination must be fresh")
    config, part1, reference_digest = load_schedule(args.config, root)
    sources = sorted((root/"src/team_strategy").rglob("*.py"))+sorted((root/"ercot-connection-game/src").rglob("*.py"))+sorted((root/"ercot-connection-game/tools").rglob("*.py"))
    identity = {"config_sha256": file_fingerprint(args.config), "source_sha256": {str(p.relative_to(root)): file_fingerprint(p) for p in sources},
        "part1_sha256": part1, "scenario_sha256": scenario_fingerprint(root/config["scenario_directory"]),
        "rules_sha256": file_fingerprint(root/config["rules_file"]), "release_sha256": file_fingerprint(root/config["release_file"]),
        "solver": "highs", "workers_per_evaluation": args.workers, "opponent_reference_sha256": reference_digest}
    output = args.output_dir.resolve()
    if output.exists() and not args.resume:
        parser.error("output directory exists; choose a fresh directory or explicit --resume")
    output.mkdir(parents=True, exist_ok=True)
    cells = {}
    if args.resume:
        if json.loads((output/"manifest.json").read_text())["identity"] != identity:
            raise ValueError("resume identity changed")
        cells = json.loads((output/"cells.json").read_text()) if (output/"cells.json").exists() else {}
    import highspy
    manifest = {"schema_version": 1, "status": "running", "kind": "submission_generation_schedule", "identity": identity,
        "generation_schedule": config["generation_schedule"], "capacity_per_submission_mw": 500, "horizon": 120,
        "solver_version": highspy.Highs().version(), "python_version": sys.version, "jobs": args.jobs}
    save_json(output/"manifest.json", manifest)
    shutil.copyfile(args.config, output/"experiment.json")
    if not (output/"source_snapshot.zip").exists():
        with zipfile.ZipFile(output/"source_snapshot.zip", "w", zipfile.ZIP_DEFLATED) as archive:
            for path in sources+[root/"pyproject.toml", args.config.resolve(), root/config["rules_file"], root/config["release_file"]]:
                archive.write(path, str(path.relative_to(root)))
    jobs = {}
    with ProcessPoolExecutor(max_workers=args.jobs) as executor:
        for p in config["portfolios"]:
            for s in config["scenarios"]:
                key = p["name"]+"/"+s["name"]
                if key in cells and verify_cell(cells[key]): continue
                base = output/"campaigns"/p["name"]/s["name"]; attempt=1
                while (base/f"attempt-{attempt:03d}").exists(): attempt += 1
                job = {"portfolio": p, "scenario": s, "seed": config["seed"], "output": str(base/f"attempt-{attempt:03d}"),
                       "workers": args.workers, "release": str(root/config["release_file"]),
                       "network": str(root/config["scenario_directory"]), "rules": str(root/config["rules_file"])}
                jobs[executor.submit(scheduled_job, job)] = key
        for future in as_completed(jobs):
            key = jobs[future]
            try:
                cells[key] = future.result(); print(f"Complete {key}: ${cells[key]['result']['campaign_score_usd']/1e9:.6f}B", flush=True)
            except Exception as error:
                cells[key] = {"status": "failed", "error": f"{type(error).__name__}: {error}"}; print(f"FAILED {key}: {error}", flush=True)
            save_json(output/"cells.json", cells)
    try:
        verify_experiment_inputs(root, args.config, config, identity)
        reference_path = root/config["opponent_reference_directory"]/"cells.json"
        if file_fingerprint(reference_path) != reference_digest: raise ValueError("opponent reference changed")
        checks = verify_matrix(config, cells, identity)
        reference = json.loads(reference_path.read_text())
        weights = json.loads((root/config["rules_file"]).read_text())["period_weight_hours"]
        rounds = verify_schedule(config, cells, reference, weights)
        comparison = make_comparison(config, cells)
    except Exception as error:
        manifest.update(status="failed", error=f"{type(error).__name__}: {error}")
        save_json(output/"manifest.json", manifest)
        from .findings import export_findings
        export_findings(output, root=root)
        raise
    save_json(output/"comparison.json", comparison)
    render_report(output, config, comparison, cells, rounds, reference)
    save_json(output/"verification.json", {"status": "passed", **checks, "csv_resource_schedule_verified": True,
        "opponent_requests_identical_to_original_part2": True, "requested_load_per_submission_mw": 500,
        "requested_generation_by_submission_mw": {"1": 0, "2": 500}})
    manifest.update(status="complete", **checks, portfolio_count=len(config["portfolios"]), scenario_count=len(config["scenarios"]),
        selected_primary=comparison["maximin_primary"], verification_sha256=file_fingerprint(output/"verification.json"))
    manifest["artifact_sha256"] = {p.name: file_fingerprint(p) for p in sorted(output.iterdir()) if p.is_file() and p.name != "manifest.json"}
    save_json(output/"manifest.json", manifest)
    if args.summary_dir:
        args.summary_dir.mkdir(parents=True)
        for name in list(manifest["artifact_sha256"])+["manifest.json"]: shutil.copyfile(output/name, args.summary_dir/name)
    from .findings import export_findings
    export_findings(args.summary_dir or output, root=root)
    print(f"Complete: {output/'report.html'}", flush=True)


if __name__ == "__main__":
    main()
