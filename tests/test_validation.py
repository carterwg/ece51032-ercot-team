import csv
from dataclasses import replace
import shutil

import pytest
from ercot_game.csv_submission import CANONICAL_CSV_COLUMNS, read_student_csv
from ercot_game.csv_validator import validate_csv_submission

from team_strategy.context import file_fingerprint
from team_strategy.contracts import Plan, SiteProposal
from team_strategy.strategies.full_generation import FullGeneration
from team_strategy.submissions import export_plan, site_ids
from team_strategy.validation import validate_plan


@pytest.mark.parametrize("site", [
    SiteProposal("missing", 10),
    SiteProposal("1", -1),
    SiteProposal("1", 0),
    SiteProposal("1", 0, 0, 1, 4),
    SiteProposal("1", 10, -1),
    SiteProposal("1", 10, 11),
    SiteProposal("1", 501),
    SiteProposal("1", 10, 0, 2, 6),
    SiteProposal("1", 10, 0, 0, 4),
    SiteProposal("1", 10, 0, 1, 0),
    SiteProposal("1", 10, 0, -1, -4),
    SiteProposal("1", float("nan")),
    SiteProposal("1", float("inf")),
    SiteProposal("1", 10, float("nan")),
    SiteProposal("1", 10, 0, float("inf"), 4),
])
def test_common_validation_rejects_illegal_sites(site, context):
    assert not validate_plan(Plan((site,)), context).valid


def test_team_cap_is_applied_to_sum_of_sites(context):
    assert not validate_plan(Plan((SiteProposal("1", 300), SiteProposal("2", 300))), context).valid


def test_empty_plan_and_invalid_team_id_are_rejected(context):
    assert not validate_plan(Plan(()), context).valid
    assert not validate_plan(Plan((SiteProposal("1", 10),)), replace(context, team_id="bad team")).valid


def test_legal_storage_and_same_bus_multiple_sites_are_allowed(context):
    plan = Plan((SiteProposal("1", 10, 5, 2, 8), SiteProposal("1", 20)))
    assert validate_plan(plan, context).valid


def test_export_roundtrips_through_official_parser(tmp_path, context):
    plan = Plan((SiteProposal("13", 20, 10, 2, 8), SiteProposal("14", 40)))
    path = tmp_path / "candidate.csv"
    export_plan(plan, context, path)
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        assert tuple(reader.fieldnames) == CANONICAL_CSV_COLUMNS
        rows = list(reader)
    assert [row["site_id"] for row in rows] == ["w2-s1-0001", "w2-s1-0002"]
    official = validate_csv_submission(path, artifact_dir=context.scenario_dir,
                                     max_team_connection_capacity_mw=context.connection_budget_mw)
    assert official.valid
    parsed = read_student_csv(path, bus_ids=context.bus_ids,
                              max_team_connection_capacity_mw=context.connection_budget_mw)
    assert parsed is not None
    assert float(rows[0]["storage_energy_mwh"]) == 8


def test_no_overwrite_or_invalid_export(tmp_path, context):
    path = tmp_path / "candidate.csv"
    plan = FullGeneration().propose(context)
    export_plan(plan, context, path)
    original = path.read_bytes()
    with pytest.raises(FileExistsError):
        export_plan(plan, context, path)
    assert path.read_bytes() == original
    with pytest.raises(ValueError, match="invalid plan"):
        export_plan(Plan((SiteProposal("missing", 10),)), context, tmp_path / "bad.csv")
    assert not (tmp_path / "bad.csv").exists()


def test_prior_site_id_collision_is_rejected(context):
    plan = FullGeneration().propose(context)
    duplicate = replace(context, prior_site_ids=frozenset(site_ids(plan, context)))
    report = validate_plan(plan, duplicate)
    assert not report.valid
    assert "repeat" in report.issues[0]


def test_mutated_scenario_and_rules_are_rejected(tmp_path, context):
    original_context = context
    scenario = tmp_path / "scenario"
    shutil.copytree(context.scenario_dir, scenario)
    context = replace(context, scenario_dir=scenario)
    with (scenario / "demand_bus.csv").open("a") as handle:
        handle.write("\n")
    assert "changed" in validate_plan(FullGeneration().propose(context), context).issues[0]
    rules = tmp_path / "rules.json"
    rules.write_bytes(context.rules_file.read_bytes())
    context = replace(original_context, rules_file=rules)
    assert file_fingerprint(rules) == context.rules_fingerprint
    rules.write_text(rules.read_text() + "\n")
    assert "rules changed" in validate_plan(FullGeneration().propose(context), context).issues[0]
