import csv
import json

import pytest

from team_strategy.cli import main, read_json
from team_strategy.context import file_fingerprint
from team_strategy.contracts import GRADED_ROUNDS

from conftest import DEMO, DEMO_RULES, RELEASE, ROOT


def propose_args(output):
    return [
        "propose", "--config", str(ROOT / "configs/strategies/full_generation.json"),
        "--team-id", "team-test", "--week", "2", "--submission", "1",
        "--release", str(RELEASE), "--scenario-dir", str(DEMO), "--rules", str(DEMO_RULES),
        "--budget-mw", "10", "--output-dir", str(output),
    ]


def test_propose_bundle_and_no_overwrite(tmp_path):
    output = tmp_path / "candidate"
    assert main(propose_args(output)) == 0
    manifest = read_json(output / "manifest.json")
    assert manifest["candidate_sha256"] == file_fingerprint(output / "candidate.csv")
    assert manifest["kind"] == "validated_candidate_not_evaluated"
    assert manifest["connection_budget_mw"] == 10
    assert read_json(output / "validation.json")["valid"]
    assert main(propose_args(output)) == 2


def test_cli_defaults_use_finalized_500mw_profile(tmp_path, monkeypatch):
    monkeypatch.chdir(ROOT)
    output = tmp_path / "finalized-candidate"
    assert main([
        "propose", "--config", "configs/strategies/full_generation.json",
        "--team-id", "team-test", "--week", "2", "--submission", "1",
        "--output-dir", str(output),
    ]) == 0
    manifest = read_json(output / "manifest.json")
    assert manifest["connection_budget_mw"] == 500
    assert manifest["rules_file"] == str(ROOT / "configs/scoring/dispatch_scoring_rules_500mw.json")
    assert manifest["comparison_bounds_billions"] == {"lower": 49.67, "upper": 73.0525}
    with (output / "candidate.csv").open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert sum(float(row["connection_capacity_mw"]) for row in rows) == 500


def test_failed_proposal_does_not_leave_partial_bundle(tmp_path):
    output = tmp_path / "bad"
    args = propose_args(output)
    args[args.index("--budget-mw") + 1] = "501"
    assert main(args) == 2
    assert not output.exists()


def test_baseline_csv_can_be_evaluated_on_all_120_demo_periods(tmp_path):
    from ercot_game.batch_cli import main as official_main

    candidate = tmp_path / "candidate"
    assert main(propose_args(candidate)) == 0
    inputs = tmp_path / "submissions"
    inputs.mkdir()
    (inputs / "team-test.csv").write_bytes((candidate / "candidate.csv").read_bytes())
    results = tmp_path / "official-results"
    assert official_main([
        "run", "--submissions-dir", str(inputs), "--artifact-dir", str(DEMO),
        "--rules", str(DEMO_RULES), "--week", "2", "--submission-number", "1",
        "--solver-backend", "highs", "--workers", "1", "--output-mode", "compact",
        "--output-dir", str(results),
    ]) == 0
    with (results / "leaderboard.csv").open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 1
    assert rows[0]["team_id"] == "team-test"
    assert rows[0]["feasible"] == "True"
    assert float(rows[0]["service_fraction"]) == pytest.approx(1)


def test_report_with_plot_from_synthetic_complete_campaigns(tmp_path, monkeypatch):
    monkeypatch.setenv("MPLCONFIGDIR", str(tmp_path / "mpl-cache"))
    def campaign(total):
        return {round.key: total / 4 for round in GRADED_ROUNDS}
    payload = {
        "capacity_per_submission_mw": 500,
        "strategies": {
            "synthetic-steady": {"scenario-a": campaign(52.5e9), "scenario-b": campaign(53.75e9)},
            "synthetic-variable": {"scenario-a": campaign(45e9), "scenario-b": campaign(67.5e9)},
        },
    }
    path = tmp_path / "input.json"
    path.write_text(json.dumps(payload))
    output = tmp_path / "report"
    assert main(["report", "--input", str(path), "--output-dir", str(output), "--plot"]) == 0
    report = read_json(output / "comparison.json")
    assert report["bounds_billions"] == {"lower": 49.67, "upper": 73.0525}
    assert report["strategies"][1]["worst_normalized_score"] < 0
    assert (output / "frontier.png").read_bytes().startswith(b"\x89PNG")


def test_duplicate_json_keys_are_rejected(tmp_path):
    path = tmp_path / "bad.json"
    path.write_text('{"week-2-submission-1": 1, "week-2-submission-1": 2}')
    with pytest.raises(ValueError, match="duplicate"):
        read_json(path)
