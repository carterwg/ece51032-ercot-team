"""Accounting, causal replay, provenance, and durable Markdown findings."""
from dataclasses import replace
import hashlib
import json

import pytest

from team_strategy.experiments import findings
from team_strategy.experiments import findings_diagnostics
from team_strategy.experiments.findings_diagnostics import SnapshotDiagnostics, added_generators, solve_snapshot
from tools.activsg2000.dcopf import Branch, Bus, Generator
from tools.hosting_capacity import HostingCapacityPeriod


def row(period, site, load, generation, team='our-team'):
    return dict(period_index=str(period), site_id=site, team_id=team, bus_id='B',
                load_mw=str(load), generation_mw=str(generation), net_withdrawal_mw=str(load-generation),
                storage_charge_mw='0', storage_discharge_mw='0')


def test_energy_and_runtime_use_representative_weights_without_counting_units():
    rows=[row(0,'s1',10,2),row(0,'s2',10,3),row(1,'s1',10,0),row(1,'s2',10,0),
          row(0,'other',100,100,team='rival')]
    r=findings.summarize_energy(rows,[7.,365.],2,1.)
    assert r['annual_energy_mwh']==dict(load=7440., generation=35., grid=7405., charge=0.,discharge=0.)
    assert r['modeled_generator_hours']==1
    assert r['annual_generator_hours']==7
    assert r['grid_share']==pytest.approx(7405/7440)


def test_no_admitted_load_has_no_energy_share():
    r=findings.summarize_energy([row(0,'s',0,0)],[8760.],1,1.)
    assert r['grid_share'] is None
    assert r['annual_generator_hours']==0


def test_broken_energy_ledger_is_rejected():
    bad=row(0,'s',10,2);bad['net_withdrawal_mw']='10'
    with pytest.raises(ValueError,match='does not balance'):
        findings.summarize_energy([bad],[8760.],1,1.)


def toy_period(load=50, own_cap=20):
    return HostingCapacityPeriod(0,(Bus('A',0,True),Bus('B',load)),
        (Generator('native','A',0,100,10),Generator('own','B',0,own_cap,100)),
        (Branch('L','A','B',10,40),),{}, {})


def test_private_generation_is_required_by_line_despite_ample_total_generation(tmp_path):
    result=SnapshotDiagnostics(tmp_path,{'L:upper'}).probe(toy_period(),'minimum_private',own_ids=('own',))
    assert result['status']=='verified'
    assert result['value_mw']==pytest.approx(10)
    relaxed=result['line_relaxations'][0]
    assert relaxed['branch_ids']==['L']
    assert relaxed['value_after_mw']==pytest.approx(9)
    assert relaxed['improvement_mw']==pytest.approx(1)
    assert relaxed['causal_effect_observed']
    assert relaxed['max_balance_error_mw']<1e-7


def test_dispatching_a_generator_does_not_prove_it_is_required():
    result=solve_snapshot(toy_period(load=20),'minimum_private',('own',))
    assert result['value_mw']==pytest.approx(0)


def test_hosting_counterfactual_and_finite_line_relief(tmp_path):
    p=toy_period(load=10,own_cap=0)
    result=SnapshotDiagnostics(tmp_path,{'L:upper'}).probe(p,'hosting',target_bus='B')
    assert result['status']=='verified'
    assert result['value_mw']==pytest.approx(30)
    assert result['generation_headroom_mw']==pytest.approx(90)
    assert result['line_relaxations'][0]['value_after_mw']==pytest.approx(31)
    # Period labels are presentation, not part of an otherwise identical model.
    again=SnapshotDiagnostics(tmp_path,{'L:upper'}).probe(replace(p,period_index=3),'hosting',target_bus='B')
    assert again['evidence_path']==result['evidence_path']
    assert again['period_index']==3


def test_infeasible_replay_remains_unknown_instead_of_becoming_zero(tmp_path):
    result=SnapshotDiagnostics(tmp_path,set()).probe(toy_period(own_cap=5),'minimum_private',own_ids=('own',))
    assert result['status']=='unresolved'
    assert 'value_mw' not in result
    assert result['line_relaxations']==[]


def test_numerical_retry_keeps_equations_and_checks_physics(monkeypatch):
    original=findings_diagnostics.HostingLP
    calls=[]
    def construct(period,**kwargs):
        model=original(period,**kwargs);calls.append(period)
        if len(calls)==1:
            def fail(_):raise RuntimeError('LP did not solve optimally (Infeasible)')
            model.set_period=fail
        return model
    monkeypatch.setattr(findings_diagnostics,'HostingLP',construct)
    p=toy_period()
    result=solve_snapshot(p,'minimum_private',('own',))
    assert calls==[p,p]
    assert result['value_mw']==pytest.approx(10)
    assert result['solver_primal_tolerance_mw']==1e-5
    assert result['max_balance_error_mw']<1e-7
    assert result['duality_gap_mw']<1e-7


def test_private_capacity_scales_with_admitted_load():
    request={('our-team','s'):dict(bus_id='B',connection_capacity_mw='500',generator_capacity_mw='250')}
    gens,own=added_generators(request,[row(0,'s',100,20)])
    assert gens[0].p_max_mw==50
    assert own==(gens[0].generator_id,)


def test_regeneration_preserves_personal_notes_and_only_creates_markdown(tmp_path):
    path=tmp_path/'case.md'
    findings.write_note(path,'# Original',{'kind':'test'})
    path.write_text(path.read_text()+'My observation.\n')
    findings.write_note(path,'# Updated',{'kind':'test'})
    assert 'My observation.' in path.read_text()
    assert '# Original' not in path.read_text()
    assert findings.read_record(path)=={'kind':'test'}
    assert all(p.suffix=='.md' for p in tmp_path.iterdir())
    before=path.read_bytes()
    findings.write_note(path,'# Updated',{'kind':'test'})
    assert path.read_bytes()==before


def test_cached_metrics_do_not_hide_changed_raw_evidence(tmp_path):
    path=tmp_path/'week-2-submission-1/canonical/evaluation.json';path.parent.mkdir(parents=True)
    path.write_text('original')
    key=str(path.relative_to(tmp_path));hashes={key:hashlib.sha256(path.read_bytes()).hexdigest()}
    findings.verify_cached_evidence(tmp_path,hashes)
    path.write_text('changed')
    with pytest.raises(ValueError,match='evidence changed'):
        findings.verify_cached_evidence(tmp_path,hashes)


def test_missing_artifact_fingerprint_is_rejected(tmp_path):
    (tmp_path/'x').write_text('untrusted')
    with pytest.raises(ValueError,match='unhashed'):
        findings.checked_bytes(tmp_path,'x',{})


def test_exact_requested_filename_and_distinct_submission_policies():
    p=dict(bus_ids=['6141'],weights=[1.],generator_fraction=1.)
    config={'capacity_per_submission_mw':500}
    assert findings.stem_for(config,p)=='C_eq_G_S1_S2_500_6141'
    assert findings.stem_for({**config,'generation_schedule':{'1':0.,'2':1.}},p)=='G_eq_0_S1_C_eq_G_S2_500_6141'
    assert findings.stem_for({**config,'capacity_per_submission_mw':250},p)=='C_eq_G_S1_S2_250_6141'


def test_summary_excludes_solo_and_duplicate_probes_from_mean(tmp_path):
    base=dict(kind='campaign',stem='C_eq_G_S1_S2_500_6141',score_usd=10e9,it_value_usd=20e9,
              minimum_admission=1.,grid_mwh=100.,generation_mwh=1.,modeled_generator_hours=1.,
              annual_generator_hours=1.,required_annual_hours=1.,exploratory=False,risk=True,
              bundle=str(tmp_path/'source'),bundle_status='complete',scenario_count_in_bundle=3)
    for name,delta in [('a',{}),('b',{'score_usd':12e9}),('solo',{'score_usd':100e9,'risk':False}),
                       ('probe',{'score_usd':1000e9,'exploratory':True})]:
        findings.write_note(tmp_path/(name+'.md'),'# case',{**base,'scenario':name,**delta})
    findings.write_strategy_indexes(tmp_path,tmp_path)
    summary=(tmp_path/(base['stem']+'.md')).read_text()
    assert 'competitive mean **$11.000000B**' in summary
    assert 'Complete source cohort' in summary
    (tmp_path/'b.md').unlink()
    findings.write_strategy_indexes(tmp_path,tmp_path)
    assert 'Partial/incomplete cohort' in (tmp_path/(base['stem']+'.md')).read_text()


def test_failed_campaign_gets_a_finding_without_a_fabricated_score(tmp_path,monkeypatch):
    bundle=tmp_path/'run';bundle.mkdir()
    p=dict(name='p',bus_ids=['6141'],weights=[1.],generator_fraction=0.)
    config=dict(capacity_per_submission_mw=500,scenario_directory='network',portfolios=[p],scenarios=[{'name':'s'}])
    (bundle/'experiment.json').write_text(json.dumps(config))
    (bundle/'manifest.json').write_text(json.dumps({'status':'failed','identity':{'scenario_sha256':'network'}}))
    (bundle/'cells.json').write_text(json.dumps({'p/s':{'status':'failed','error':'infeasible evaluator'}}))
    monkeypatch.setattr(findings,'scenario_fingerprint',lambda _: 'network')
    assert findings.export_findings(bundle,root=tmp_path)==[]
    failed=next((tmp_path/'findings').glob('*FAILED*.md')).read_text()
    assert 'Unavailable — not zero' in failed
    assert 'infeasible evaluator' in failed
