from types import SimpleNamespace

import pytest

from team_strategy.experiments.battery_s1 import FIELDS, ROOT, RivalPortfolio, read, rival_storage_fields
from team_strategy.experiments.battery_s1_report import storage_trace, verify_rival_storage


def test_storage_trace_checks_each_daily_cycle():
    # A 1 MW / 4 MWh asset starts half full on each of two modeled days.
    short_day = [{'charge':1., 'discharge':0.}, {'charge':0., 'discharge':1.}]
    states, days = storage_trace(short_day + list(reversed(short_day)), 1., 4., day_length=2)
    assert states == [3.,2.,1.,2.]
    assert [d['end_mwh'] for d in days] == [2.,2.]
    with pytest.raises(ValueError, match='half full'):
        storage_trace(short_day[:1]*2 + short_day[1:]*2, 1., 4., day_length=2)


def test_storage_trace_rejects_energy_and_power_overdraw():
    with pytest.raises(ValueError, match='power'):
        storage_trace([{'charge':1.1,'discharge':0.}],1.,4.,day_length=1)
    with pytest.raises(ValueError, match='more energy'):
        storage_trace([{'charge':0.,'discharge':1.}],1.,1.,day_length=1)


def test_five_site_rival_splits_its_battery_and_builds_only_generation_in_s2():
    fields = {f['name']:f for f in rival_storage_fields(read(ROOT/FIELDS))}
    rival = RivalPortfolio(fields['nine_b150_ptdf_5']['rival_plan'])
    context = SimpleNamespace(round=SimpleNamespace(submission=1), connection_budget_mw=500.,
                              bus_ids={'6141','5395','6342','5451','6004'},max_generator_to_connection_ratio=1.)
    first = rival.propose(context).sites
    assert len(first)==5
    assert {(s.connection_mw,s.generator_mw,s.storage_power_mw,s.storage_energy_mwh) for s in first}=={
        (100.,0.,30.,120.)}
    context.round.submission = 2
    second = rival.propose(context).sites
    assert {(s.connection_mw,s.generator_mw,s.storage_power_mw,s.storage_energy_mwh) for s in second}=={
        (100.,100.,0.,0.)}


def test_rival_soc_is_checked_at_each_site_even_when_aggregate_energy_balances():
    requests = {('rival-01','a'):(100.,0.,10.,40.),('rival-02','b'):(100.,0.,10.,40.)}
    ledger = [{'team_id':team, 'site_id':site,'period_index':str(i),'load_mw':'50',
               'storage_charge_mw':str(float(team=='rival-01' and i==0)),
               'storage_discharge_mw':str(float(team=='rival-02' and i==0))}
              for team,site in requests for i in range(24)]
    with pytest.raises(ValueError,match='half full'):
        verify_rival_storage(ledger,requests,[1.]*24)
