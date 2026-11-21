"""Part 2: matched full-game campaigns for concentrated and distributed siting.

From the repository root:
PYTHONPATH=src:ercot-connection-game:ercot-connection-game/src .venv/bin/python \
 -m team_strategy.experiments.concentration --output-dir runs/part2-full --summary-dir analysis/strategy/part2 --jobs 2

Use --resume only with identical source/input fingerprints. Every completed
cell is checked against its artifact hashes. Failed attempts are preserved;
an explicit resume retries them in a new attempt directory. Nothing is uploaded.
"""
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import asdict
import csv
import html
import json
import math
from pathlib import Path
import shutil
import sys

from ..context import file_fingerprint, scenario_fingerprint
from ..contracts import GRADED_ROUNDS
from ..evaluation.campaign import run_campaign, save_json
from ..experiments.comparison import compare, frontier_names
from ..experiments.scoring import ScoreBounds, combined_score_usd
from ..strategies.corridor_portfolio import CorridorPortfolio


def load_experiment(path, root):
    config = json.loads(path.read_text())
    if config.get("schema_version") != 1 or config.get("capacity_per_submission_mw") != 500:
        raise ValueError("experiment must use schema 1 and the finalized 500 MW cap")
    if config.get("decision_rule") != "maximin_primary":
        raise ValueError("unsupported decision rule")
    for key in ("portfolios", "scenarios"):
        names = [x["name"] for x in config[key]]
        if not names or len(names) != len(set(names)) or any(not n or any(c not in 'abcdefghijklmnopqrstuvwxyz0123456789_-' for c in n) for n in names):
            raise ValueError(f"{key} names must be distinct safe identifiers")
    primary = [p for p in config["portfolios"] if p["role"] == "primary"]
    if len(primary) < 2 or len({p["generator_fraction"] for p in primary}) != 1:
        raise ValueError("at least two primary portfolios must share the same resource ratio")
    if sum(bool(s["include_in_risk"]) for s in config["scenarios"]) < 2:
        raise ValueError("at least two matched stress scenarios are required")
    directory = root / config["part1_directory"]
    part1 = json.loads((directory / "manifest.json").read_text())
    if part1["status"] != "complete" or part1.get("verification_status") != "passed":
        raise ValueError("Part 1 must be complete and verified")
    verification_file = directory / "verification.json"
    if file_fingerprint(verification_file) != part1["verification_sha256"]:
        raise ValueError("Part 1 verification fingerprint changed")
    verification = json.loads(verification_file.read_text())
    for name, digest in verification["artifact_sha256"].items():
        if file_fingerprint(directory / name) != digest:
            raise ValueError(f"Part 1 artifact changed: {name}")
    scenario = root / config["scenario_directory"]
    if scenario_fingerprint(scenario) != part1["scenario_sha256"]:
        raise ValueError("Part 1 and Part 2 network inputs differ")
    candidates = {b["bus_id"] for b in part1["candidate_pool"]["candidates"]}
    for portfolio in config["portfolios"]:
        make_strategy(portfolio)
        if portfolio["role"] not in {"primary", "benchmark"} or not set(portfolio["bus_ids"]) <= candidates:
            raise ValueError("portfolio role/buses do not match Part 1")
    for s in config["scenarios"]:
        if (type(s["include_in_risk"]) is not bool
                or not math.isfinite(s["rival_generator_fraction"]) or not 0 <= s["rival_generator_fraction"] <= 1
                or not set(s["rival_bus_ids"]) <= candidates):
            raise ValueError("invalid opponent locations or resource ratio")
        if s["name"] == "solo" and s["include_in_risk"]:
            raise ValueError("solo reference must be excluded from competitive risk")
    return config, {"manifest": file_fingerprint(directory / "manifest.json"),
                    "groups": file_fingerprint(directory / "groups.json"),
                    "interactions": file_fingerprint(directory / "interactions.json")}


def make_strategy(spec):
    return CorridorPortfolio(tuple(spec["bus_ids"]), tuple(spec["weights"]), spec["generator_fraction"])


def _cell_job(job):
    portfolio, scenario = job["portfolio"], job["scenario"]
    opponents = tuple((f"rival-{i + 1:02d}", CorridorPortfolio((bus,), generator_fraction=scenario["rival_generator_fraction"]))
                      for i, bus in enumerate(scenario["rival_bus_ids"]))
    result = run_campaign(strategy=make_strategy(portfolio), opponent_strategies=opponents,
                          scenario_name=scenario["name"], seed=job["seed"], output_dir=Path(job["output"]),
                          release_file=Path(job["release"]), scenario_dir=Path(job["network"]),
                          rules_file=Path(job["rules"]), workers=job["workers"], solver_backend="highs")
    keys = {r.key: r for r in GRADED_ROUNDS}
    scores = {r["round"]: r["score_usd"] for r in result["rounds"]}
    if set(scores) != set(keys):
        raise RuntimeError("campaign is incomplete")
    result["campaign_score_usd"] = combined_score_usd({keys[key]: value for key, value in scores.items()})
    result.update(portfolio=portfolio["name"], role=portfolio["role"],
                  generator_fraction=portfolio["generator_fraction"], include_in_risk=scenario["include_in_risk"])
    save_json(Path(job["output"]) / "campaign.json", result)
    artifacts = {str(p.relative_to(job["output"])): file_fingerprint(p)
                 for p in sorted(Path(job["output"]).rglob("*")) if p.is_file()}
    return {"status": "complete", "output": job["output"], "result": result, "artifact_sha256": artifacts}


def verify_cell(cell):
    if cell["status"] != "complete" or cell["result"]["status"] != "complete":
        return False
    if not cell["artifact_sha256"] or "campaign.json" not in cell["artifact_sha256"]:
        raise ValueError("cached campaign has no evidence")
    output = Path(cell["output"])
    if not all((output / name).is_file() and file_fingerprint(output / name) == digest
               for name, digest in cell["artifact_sha256"].items()):
        raise ValueError("cached campaign evidence changed")
    if json.loads((output / "campaign.json").read_text()) != cell["result"]:
        raise ValueError("cached scores differ from their campaign artifact")
    if {r["round"] for r in cell["result"]["rounds"]} != {r.key for r in GRADED_ROUNDS}:
        raise ValueError("cached campaign is incomplete")
    return True


def verify_experiment_inputs(root, config_file, config, identity):
    expected = {
        "config_sha256": file_fingerprint(config_file),
        "scenario_sha256": scenario_fingerprint(root / config["scenario_directory"]),
        "rules_sha256": file_fingerprint(root / config["rules_file"]),
        "release_sha256": file_fingerprint(root / config["release_file"]),
    }
    if any(identity[key] != value for key, value in expected.items()):
        raise ValueError("experiment configuration, network, or economic inputs changed")
    if any(file_fingerprint(root / name) != digest for name, digest in identity["source_sha256"].items()):
        raise ValueError("experiment source changed")
    directory = root / config["part1_directory"]
    if any(file_fingerprint(directory / f"{name}.json") != digest for name, digest in identity["part1_sha256"].items()):
        raise ValueError("Part 1 evidence changed")


def make_comparison(config, cells):
    bounds = ScoreBounds(500.)
    by_portfolio = {p["name"]: {} for p in config["portfolios"]}
    all_scores = {p["name"]: {} for p in config["portfolios"]}
    for cell in cells.values():
        if not verify_cell(cell):
            raise ValueError("comparison requires the complete matched matrix")
        r = cell["result"]
        all_scores[r["portfolio"]][r["scenario"]] = r["campaign_score_usd"]
        if r["include_in_risk"]:
            by_portfolio[r["portfolio"]][r["scenario"]] = r["campaign_score_usd"]
    required = {s["name"] for s in config["scenarios"]}
    if any(set(scores) != required for scores in all_scores.values()):
        raise ValueError("a candidate is missing matched scenarios")
    summaries = compare(by_portfolio, bounds)
    primary_names = {p["name"] for p in config["portfolios"] if p["role"] == "primary"}
    primary = tuple(x for x in summaries if x.name in primary_names)
    frontier = frontier_names(primary)
    worst = max(x.worst_normalized_score for x in primary)
    # Treat solver-scale score differences as ties, then prefer mean and fewer sites.
    sizes = {p["name"]: len(p["bus_ids"]) for p in config["portfolios"]}
    choices = [x for x in primary if x.worst_normalized_score >= worst - 1e-4]
    selected = max(choices, key=lambda x: (round(x.average_normalized_score, 4), -sizes[x.name], x.name))
    best_mean = max(primary, key=lambda x: (x.average_normalized_score, -sizes[x.name], x.name))
    scenarios = sorted(next(iter(by_portfolio.values())))
    best_by_scenario = {s: max(bounds.normalize_usd(by_portfolio[name][s]) for name in primary_names) for s in scenarios}
    regrets = {name: max(best_by_scenario[s] - bounds.normalize_usd(by_portfolio[name][s]) for s in scenarios)
               for name in primary_names}
    minimax_regret = min(primary_names, key=lambda name: (regrets[name], sizes[name], name))
    rows = [{**asdict(s), "role": "primary" if s.name in primary_names else "benchmark",
             "on_primary_frontier": s.name in frontier,
             "worst_regret_normalized_points": regrets.get(s.name)} for s in summaries]
    # Compare each primary to concentration at 6141 under exactly the same opponents.
    reference = "concentrate_6141" if "concentrate_6141" in all_scores else sorted(primary_names)[0]
    paired = {name: {s: (all_scores[name][s] - all_scores[reference][s]) / 1e9 for s in sorted(required)}
              for name in all_scores}
    return {"scope": "Finite candidate menu and declared opponent hypotheses; no calibrated opponent probabilities.",
            "risk_scenarios": scenarios, "solo_excluded_from_risk": True,
            "summary": rows, "campaign_scores_usd": all_scores,
            "paired_gain_billions_vs": reference, "paired_gains_billions": paired,
            "maximin_primary": selected.name, "best_mean_primary": best_mean.name,
            "minimax_regret_primary": minimax_regret, "primary_pareto_frontier": sorted(frontier),
            "decision_rule": "Maximize worst stress-campaign Q; ties within 0.0001 points prefer mean then fewer sites. Benchmarks excluded."}


def write_report(output, config, comparison, cells):
    def table(headers, rows):
        esc = lambda x: html.escape(str(x))
        return '<table><thead><tr>' + ''.join(f'<th>{esc(x)}</th>' for x in headers) + '</tr></thead><tbody>' + ''.join(
            '<tr>' + ''.join(f'<td>{esc(x)}</td>' for x in row) + '</tr>' for row in rows) + '</tbody></table>'
    selected = next(p for p in config["portfolios"] if p["name"] == comparison["maximin_primary"])
    save_json(output / "recommended_strategy.json", {"strategy": "corridor_portfolio", "params": {
        "bus_ids": selected["bus_ids"], "weights": selected["weights"], "generator_fraction": selected["generator_fraction"]}})
    with (output / "comparison.csv").open("w", newline="") as stream:
        w = csv.DictWriter(stream, fieldnames=list(comparison["summary"][0])); w.writeheader(); w.writerows(comparison["summary"])
    with (output / "rounds.csv").open("w", newline="") as stream:
        headers = ["portfolio", "scenario", "round", "score_billions", "service_fraction", "energy_cost_billions", "generator_cost_billions"]
        w = csv.writer(stream); w.writerow(headers)
        for cell in cells.values():
            result = cell["result"]
            for r in result["rounds"]:
                w.writerow([result["portfolio"], result["scenario"], r["round"], r["score_usd"] / 1e9,
                            r["service_fraction"], r["score_breakdown"]["grid_energy_cost_usd"] / 1e9,
                            r["score_breakdown"]["generator_operating_cost_usd"] / 1e9])
    spec_rows = [(p["name"], ', '.join(f'{b}: {500*w:g} MW' for b,w in zip(p["bus_ids"],p["weights"],strict=True)),
                  p["generator_fraction"],p["role"],p["description"]) for p in config["portfolios"]]
    summary_rows = [(r["name"],r["role"],f'{r["average_normalized_score"]:.3f}', f'{r["worst_normalized_score"]:.3f}',
                     f'{r["downside_risk"]:.3f}',r["on_primary_frontier"]) for r in comparison["summary"]]
    scenario_names = [s["name"] for s in config["scenarios"]]
    scores = comparison["campaign_scores_usd"]
    score_rows = [(name,*(f'{scores[name][s]/1e9:.3f}' for s in scenario_names)) for name in scores]
    text = f'''<!doctype html><html><head><meta charset="utf-8"><title>Part 2 — Concentration versus distribution</title>
<style>body{{font:16px/1.55 system-ui;max-width:1300px;margin:36px auto;padding:0 24px;color:#172233}}table{{border-collapse:collapse;width:100%;font-size:14px;margin:20px 0}}th,td{{border:1px solid #d7dee7;padding:9px;text-align:left}}th{{background:#edf2f8}}.note{{background:#edf5ff;padding:16px;border-left:4px solid #3262a8}}td{{overflow-wrap:anywhere}}</style></head><body>
<h1>Part 2: concentration versus distribution</h1><p>Complete four-submission campaigns over all 120 periods, with matched opponents,
500 MW of new capacity each submission, all-team S1 withdrawal carried into S2, and a weekly reset.</p>
<div class="note">Conservative choice among the primary grid-only menu: <b>{html.escape(selected['name'])}</b>.
Best mean: {html.escape(comparison['best_mean_primary'])}. Minimax regret: {html.escape(comparison['minimax_regret_primary'])}.
These are conditional choices under the declared hypotheses, not an optimum over all buses, capacity fractions, or resource sizes.</div>
<h2>Candidate plans</h2>{table(('Portfolio','New capacity per submission','G/C','Role','Reason'),spec_rows)}
<p>The 6062/6298 pair shares b02136 under stress despite distinct individual limits. Four sites do not imply four independent resources.
The C=G benchmark has a different resource mix and is excluded from the grid-only siting decision.</p>
<h2>Opponent assumptions</h2>{table(('Scenario','Rival buses, each requesting 500 MW','Rival G/C','Included in risk'),[(s['name'],', '.join(s['rival_bus_ids']) or 'none',s['rival_generator_fraction'],s['include_in_risk']) for s in config['scenarios']])}
<p>Rivals repeat these plans in S2. Their S1 allocations and hourly private generation determine the actual carried base load.
Scenarios have equal comparison weight; they are not estimated competitor probabilities. Solo is a reference and is excluded from risk.</p>
<h2>Campaign score (billions of USD)</h2>{table(('Portfolio',*scenario_names),score_rows)}
<h2>Stress-scenario return and downside</h2>{table(('Portfolio','Role','Mean Q','Worst Q','Downside semideviation','Primary frontier'),summary_rows)}
<p>Q=100×(S−49.67)/(73.0525−49.67), where S is the sum of W2S1, W2S2, W3S1, W3S2 in billions.
Negative Q is retained. Downside is measured around each strategy's own mean. No weighted composite is used.</p>
<h2>How to inspect the result</h2><p><a href="rounds.csv">Per-round scores and allocation</a> distinguish a site-selection benefit from
S2 supply exhaustion, private-generation cost, or Week 3 grid energy charges. A genuine zero allocation remains zero; evaluator failures never become zero scores.
<a href="comparison.json">Paired gains and complete statistics</a> compare every candidate with the same concentrated reference under identical opponents.</p>
<p>Recommended geometry: <a href="recommended_strategy.json">strategy configuration</a>. This uses simulation team IDs and is not a classroom submission.
Use the existing propose/validate workflow with the actual team ID and released round data before submitting anything.</p>
<p>Source/input fingerprints and per-campaign artifact hashes: <a href="manifest.json">manifest</a> and <a href="cells.json">campaign evidence</a>.</p>
</body></html>'''
    (output / "report.html").write_text(text)


def main():
    import argparse
    root = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=root / "configs/experiments/corridor_part2.json")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--summary-dir", type=Path, help="Export compact report/evidence separately from raw campaigns")
    parser.add_argument("--jobs", type=int, default=1)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    if args.jobs < 1 or args.workers < 1:
        parser.error("jobs/workers must be positive")
    if args.summary_dir and args.summary_dir.exists():
        parser.error("summary directory exists; choose a fresh destination")
    config, part1_hashes = load_experiment(args.config, root)
    sources = sorted((root / "src/team_strategy").rglob("*.py")) + sorted((root / "ercot-connection-game/src").rglob("*.py")) + sorted((root / "ercot-connection-game/tools").rglob("*.py"))
    source_hashes = {str(p.relative_to(root)): file_fingerprint(p) for p in sources}
    identity = {"config_sha256": file_fingerprint(args.config), "source_sha256": source_hashes,
                "part1_sha256": part1_hashes, "scenario_sha256": scenario_fingerprint(root / config["scenario_directory"]),
                "rules_sha256": file_fingerprint(root / config["rules_file"]),
                "release_sha256": file_fingerprint(root / config["release_file"]),
                "solver": "highs", "workers_per_evaluation": args.workers}
    output = args.output_dir.resolve()
    if output.exists() and not args.resume:
        parser.error("output directory exists; use a fresh directory or explicit --resume")
    output.mkdir(parents=True, exist_ok=True)
    cells = {}
    if args.resume:
        prior = json.loads((output / "manifest.json").read_text())
        if prior["identity"] != identity:
            raise ValueError("cannot resume after source, rules, inputs, or experiment settings changed")
        cells = json.loads((output / "cells.json").read_text()) if (output / "cells.json").exists() else {}
    manifest = {"schema_version": 1, "status": "running", "identity": identity,
                "capacity_per_submission_mw": 500, "horizon": 120, "campaign_rounds": [r.key for r in GRADED_ROUNDS],
                "assumptions": config["assumptions"], "job_count": args.jobs}
    import highspy
    manifest.update(python_version=sys.version, solver_version=highspy.Highs().version(),
                    raw_evidence_directory=str(output))
    save_json(output / "manifest.json", manifest)
    jobs = []
    for portfolio in config["portfolios"]:
        for scenario in config["scenarios"]:
            key = portfolio["name"] + "/" + scenario["name"]
            if key in cells and verify_cell(cells[key]):
                continue
            folder = output / "campaigns" / portfolio["name"] / scenario["name"]
            attempt = 1
            while (folder / f"attempt-{attempt:03d}").exists(): attempt += 1
            jobs.append((key, {"portfolio": portfolio, "scenario": scenario, "seed": config["seed"],
                                "output": str(folder / f"attempt-{attempt:03d}"), "workers": args.workers,
                                "release": str(root / config["release_file"]), "network": str(root / config["scenario_directory"]),
                                "rules": str(root / config["rules_file"])}))
    failures = []
    with ProcessPoolExecutor(max_workers=args.jobs) as executor:
        pending = {executor.submit(_cell_job, job): key for key, job in jobs}
        for future in as_completed(pending):
            key = pending[future]
            try:
                cells[key] = future.result()
                r = cells[key]["result"]
                print(f"Complete {key}: ${r['campaign_score_usd']/1e9:.3f}B", flush=True)
            except Exception as error:
                cells[key] = {"status": "failed", "error": f"{type(error).__name__}: {error}"}
                failures.append(key)
                print(f"FAILED {key}: {error}", file=sys.stderr, flush=True)
            save_json(output / "cells.json", cells)
    if failures:
        manifest.update(status="failed", failed_cells=failures)
        save_json(output / "manifest.json", manifest)
        from .findings import export_findings
        export_findings(output, root=root, config_file=args.config)
        raise RuntimeError("one or more campaigns failed; no recommendation issued")
    try:
        verify_experiment_inputs(root, args.config, config, identity)
    except ValueError as error:
        manifest.update(status="failed", error=str(error))
        save_json(output / "manifest.json", manifest)
        raise
    comparison = make_comparison(config, cells)
    save_json(output / "comparison.json", comparison)
    write_report(output, config, comparison, cells)
    manifest.update(status="complete", campaign_count=len(cells), evaluation_count=sum(len(c["result"]["rounds"]) for c in cells.values()),
                    selected_primary=comparison["maximin_primary"])
    save_json(output / "manifest.json", manifest)
    if args.summary_dir:
        args.summary_dir.mkdir(parents=True, exist_ok=False)
        for name in ("report.html", "comparison.json", "comparison.csv", "rounds.csv", "recommended_strategy.json", "manifest.json", "cells.json"):
            shutil.copyfile(output / name, args.summary_dir / name)
    from .findings import export_findings
    export_findings(args.summary_dir or output, root=root, config_file=args.config)
    print(f"Part 2 complete: {output / 'report.html'}")


if __name__ == "__main__":
    main()
