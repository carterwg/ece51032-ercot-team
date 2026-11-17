from dataclasses import replace
import csv
import json

import pytest

from team_strategy.experiments.interpretation import (
    ResultSource, assert_comparable, campaign_records, load_result_records,
)

from conftest import ROOT


@pytest.fixture
def source():
    return ResultSource('full_generation', 'Baseline', ROOT / 'analysis/baseline_cg_500mw.json')


def modified_source(source, tmp_path, mutate):
    payload = json.loads(source.summary_json.read_text())
    mutate(payload)
    path = tmp_path / 'summary.json'
    path.write_text(json.dumps(payload))
    return replace(source, summary_json=path)


def test_saved_campaigns_reproduce_existing_totals_and_q(source):
    carter = ResultSource('carter_rank1_cg', 'Carter', ROOT / 'analysis/carter_rank1_cg_500mw.json',
                          ROOT / 'analysis/carter_rank1_cg_500mw.csv')
    records = load_result_records([source, carter])
    selected = [row for row in records if row['experiment'] == 'finalized-500mw']
    assert_comparable(selected)
    totals = {row['strategy']: row for row in campaign_records(selected)}
    assert totals['full_generation']['score_billions'] == pytest.approx(55.27141599407376)
    assert totals['carter_rank1_cg']['normalized_score'] == pytest.approx(78.20051739483006)
    assert len(records) == 8


def test_incomplete_campaign_is_not_normalized(source, tmp_path):
    source = modified_source(source, tmp_path, lambda p: p['campaigns'][0]['rounds'].pop())
    result = next(row for row in campaign_records(load_result_records([source]))
                  if row['experiment'] == 'finalized-500mw')
    assert result['completed_rounds'] == 3
    assert not result['complete']
    assert result['normalized_score'] is None


def test_duplicate_rounds_are_rejected(source, tmp_path):
    def duplicate(payload):
        payload['campaigns'][0]['rounds'].append(payload['campaigns'][0]['rounds'][0].copy())
    with pytest.raises(ValueError, match='duplicate'):
        load_result_records([modified_source(source, tmp_path, duplicate)])


def test_storage_capital_comes_from_primary_summary(source, tmp_path):
    def add_storage(payload):
        row = payload['campaigns'][0]['rounds'][0]
        row['storage_capital_cost'] = '1000000'
        row['score'] = float(row['score']) - 1000000
    records = load_result_records([modified_source(source, tmp_path, add_storage)])
    row = next(row for row in records if row['experiment'] == 'finalized-500mw'
               and row['round'] == 'week-2-submission-1')
    assert row['storage_capital_cost_usd'] == 1000000
    assert campaign_records([row])[0]['normalized_score'] is None


def test_unreconciled_costs_are_rejected(source, tmp_path):
    def wrong_score(payload):
        payload['campaigns'][0]['rounds'][0]['score'] = 0
    with pytest.raises(ValueError, match='reconcile'):
        load_result_records([modified_source(source, tmp_path, wrong_score)])


def test_different_budgets_cannot_be_pooled(source):
    rows = load_result_records([source])
    rows[0]['capacity_per_submission_mw'] = 250
    with pytest.raises(ValueError, match='one experiment/budget'):
        assert_comparable(rows)


def test_changed_rules_are_not_comparable(source):
    rows = [row for row in load_result_records([source]) if row['experiment'] == 'finalized-500mw']
    rows[0]['effective_rules_sha256'] = 'different'
    with pytest.raises(ValueError, match='matching'):
        assert_comparable(rows)


@pytest.mark.parametrize('invalid_score', [None, float('nan'), float('inf')])
def test_missing_or_nonfinite_score_is_not_zero(source, tmp_path, invalid_score):
    def mutate(payload):
        payload['campaigns'][0]['rounds'][0]['score'] = invalid_score
    with pytest.raises(ValueError, match='finite'):
        load_result_records([modified_source(source, tmp_path, mutate)])


def test_mismatched_csv_and_summary_are_rejected(source, tmp_path):
    original = ROOT / 'analysis/baseline_cg_500mw.csv'
    with original.open() as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames
        rows = list(reader)
    rows[0]['score_billions'] = '0'
    path = tmp_path / 'details.csv'
    with path.open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    with pytest.raises(ValueError, match='disagree'):
        load_result_records([replace(source, details_csv=path)])


def test_genuine_rejected_submission_remains_a_scored_zero(source, tmp_path):
    def reject(payload):
        row = payload['campaigns'][0]['rounds'][0]
        row.update(valid='False', feasible='False', service_fraction='')
        for field in ('score', 'it_value', 'energy_cost', 'generator_operating_cost',
                      'generator_capital_cost', 'storage_capital_cost', 'site_cost'):
            row[field] = 0
    rows = load_result_records([modified_source(source, tmp_path, reject)])
    first = next(row for row in rows if not row['valid'])
    assert first['score_usd'] == 0
    assert first['service_fraction'] is None
    campaign = next(row for row in campaign_records(rows) if row['experiment'] == 'finalized-500mw')
    assert campaign['complete']
    assert not campaign['all_valid']
    assert campaign['normalized_score'] is not None
