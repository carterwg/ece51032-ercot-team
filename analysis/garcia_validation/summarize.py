"""Audit saved official jobs and export the matched S1 comparison."""
import csv
from dataclasses import asdict
import importlib.util
import json
from pathlib import Path

from run_validation import ROOT, OUTPUT, CASES, CANDIDATES
from team_strategy.context import file_fingerprint

HERE=Path(__file__).resolve().parent


def load_results():
    records=[]
    for path in sorted(OUTPUT.glob('*/*/*/result.json')):
        record=json.loads(path.read_text())
        if record['field']['rival_count']!=9:continue
        record['saved_result']=str(path.relative_to(ROOT))
        if record['status']=='complete':
            assert record['horizon']==120
            for name,expected in record['artifact_sha256'].items():
                assert file_fingerprint(path.parent/name)==expected, (path,name)
            result=json.loads(Path(record['result_path']).read_text())
            assert len(result['team_scores'])==record['field']['rival_count']+1
            assert all(score['valid'] and score['feasible'] for score in result['team_scores'])
            assert result['horizon']==120
            record['field_admitted_mw']=sum(score['served_load_mwh']/8760 for score in result['team_scores'])
        records.append(record)
    return records


def export():
    records=load_results()
    records=[r for r in records if r['field']['rival_count']==9]
    complete=[r for r in records if r['status']=='complete' and not r.get('evaluator_overrides')]
    alternate=[r for r in records if r.get('evaluator_overrides')]
    # A rerun may provide independent W3 verification or a successful official retry.
    by_pair={}
    for r in complete:
        key=(r['case'],r['candidate'])
        if key not in by_pair or ('week3_score_usd' in r and 'week3_score_usd' not in by_pair[key]):
            by_pair[key]=r
    fields=['case','candidate','team_count','our_bus','our_generator_mw','our_battery_mw',
            'our_battery_mwh','full_build_equipment_capital_usd','our_admitted_mw',
            'field_admitted_mw','week2_s1_score_usd','week3_s1_score_usd',
            'generator_fuel_usd','week3_grid_cost_usd','elapsed_seconds','result_file','case_scope']
    rows=[]
    for (case,candidate),r in sorted(by_pair.items()):
        bus,g,p=r['equipment']
        rows.append(dict(zip(fields,[case,candidate,r['field']['rival_count']+1,bus,g,p,4*p,
            2e6*g+1.4e6*p,r['our_admitted_mw'],r['field_admitted_mw'],r['energy_off_score_usd'],
            r.get('week3_score_usd'),r['score_breakdown']['generator_operating_cost_usd'],
            r.get('week3_grid_cost_usd'),r['elapsed_seconds'],r['saved_result'],r['field']['provenance']])))
    with (HERE/'comparison.csv').open('w',newline='') as handle:
        writer=csv.DictWriter(handle,fieldnames=fields);writer.writeheader();writer.writerows(rows)
    reference=[]
    reference_cases={
        'ours10_same6141_g0': 'nine_grid_at_6141',
        'ours10_same6141_g200': 'nine_g200_at_6141',
        'ours10_same6141_g50_b175': 'nine_g50_b175_at_6141',
    }
    for case,old_field in reference_cases.items():
        for candidate in ('ours_g200_6141','ours_b196_6141','ours_g97_b99_6141'):
            new=by_pair.get((case,candidate))
            if not new:continue
            _,g,p=CANDIDATES[candidate]
            old_folder=ROOT/'runs/battery-s1-500mw/sweep'/f'g{g}_p{p}'/old_field
            old_paths=sorted(old_folder.glob('attempt-*/result.json'))
            if not old_paths:continue
            old=json.loads(old_paths[-1].read_text())
            old_round=next(r for r in old['rounds'] if r['round']=='week-3-submission-1')
            old_mw=sum(a['allocated_connection_mw'] for a in old_round['site_allocations'])
            old_w2=old_round['score_usd']+old_round['score_breakdown']['grid_energy_cost_usd']
            reference.append({'case':case,'candidate':candidate,'previous_result':str(old_paths[-1].relative_to(ROOT)),
                'previous_admitted_mw':old_mw,'new_admitted_mw':new['our_admitted_mw'],
                'admission_difference_mw':new['our_admitted_mw']-old_mw,
                'previous_week2_s1_score_usd':old_w2,
                'week2_score_difference_usd':new['energy_off_score_usd']-old_w2,
                'previous_week3_s1_score_usd':old_round['score_usd'],
                'new_week3_s1_score_usd':new.get('week3_score_usd')})
    screens=list(csv.DictReader(open(HERE/'sources/screen_results.csv')))
    paired=[]
    for case,policy in [('garcia11_colocated_g0','rivals_500C_0G_colocated'),
                        ('garcia11_colocated_g200','rivals_500C_200G_colocated')]:
        for candidate in [c for c in CANDIDATES if c.startswith('garcia_')]:
            new=by_pair.get((case,candidate))
            if not new:continue
            bus,g,_=CANDIDATES[candidate]
            old=next(r for r in screens if r['policy']==policy and r['our_bus']==bus and float(r['our_generator_mw'])==g)
            paired.append({'case':case,'candidate':candidate,
                'screen_admitted_mw':float(old['our_allocated_load_mw_screen']),
                'official_admitted_mw':new['our_admitted_mw'],
                'screen_week2_s1_score_usd':float(old['our_score_week1_2_usd_screen']),
                'official_week2_s1_score_usd':new['energy_off_score_usd'],
                'official_minus_screen_usd':new['energy_off_score_usd']-float(old['our_score_week1_2_usd_screen']),
                'screen_generator_fuel_usd':float(old['our_generator_operating_usd_screen']),
                'official_generator_fuel_usd':new['score_breakdown']['generator_operating_cost_usd']})
    selection=HERE/'selected_pairs.json'
    expected={tuple(p) for p in json.loads(selection.read_text())['pairs']} if selection.exists() else {(case,candidate) for case in CASES for candidate in CANDIDATES}
    failed=[{k:r.get(k) for k in ('case','candidate','saved_result','error')} for r in records if r['status'] not in ('complete','not_selected','resolved_elsewhere') and not r.get('evaluator_overrides')]
    for path in sorted(OUTPUT.glob('*/*/*/timeout.json')):
        if (path.parent/'result.json').exists():continue
        job=json.loads((path.parent/'job.json').read_text());timeout=json.loads(path.read_text())
        if job['field']['rival_count']!=9:continue
        failed.append({'case':job['case'],'candidate':job['candidate'],'saved_result':str(path.relative_to(ROOT)),
                       'error':f"Process timeout after {timeout['timeout_seconds']} seconds; no joint score returned"})
    alternate_parity=[]
    for r in alternate:
        standard=by_pair.get((r['case'],r['candidate']))
        if r['status']=='complete' and standard:
            difference=r['our_admitted_mw']-standard['our_admitted_mw']
            score_difference=r['energy_off_score_usd']-standard['energy_off_score_usd']
            assert abs(difference)<1e-3 and abs(score_difference)<1000, (r['case'],r['candidate'],difference,score_difference)
            alternate_parity.append({'case':r['case'],'candidate':r['candidate'],
                'admission_difference_mw':difference,'week2_score_difference_usd':score_difference})
    alt_completed={(r['case'],r['candidate']) for r in alternate if r['status']=='complete'}
    summary={'completed_pairs':len(set(by_pair)&expected),'planned_pairs':len(expected),
        'additional_completed_pairs':len(set(by_pair)-expected),
        'all_completed_pairs':len(by_pair),
        'resolved_with_alternate_qp_only':[list(k) for k in sorted((alt_completed-set(by_pair))&expected)],
        'unresolved_after_all_methods':[list(k) for k in sorted(expected-set(by_pair)-alt_completed)],
        'alternate_qp_parity':alternate_parity,
        'missing_pairs':[list(k) for k in sorted(expected-set(by_pair))],
        'failed_attempts':failed,
        'alternate_qp_attempts':[{k:r.get(k) for k in ('case','candidate','status','our_admitted_mw',
            'energy_off_score_usd','week3_score_usd','error','evaluator_overrides','saved_result')} for r in alternate],
        'results':rows,'matched_previous_results':reference,'exact_garcia_screen_pairs':paired,
        'source_fingerprints':sorted({tuple(sorted(r['source_sha256'].items())) for r in complete}),
        'source_note':'All primary results use exactly nine rivals (ten total teams). Garcia used ten rivals; these are corrected-count tests. Diverse placements are explicit reconstructions.',
        'comparison_scope':'Submission 1 only; these are not four-round campaign scores.'}
    (HERE/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:summary[k] for k in ('completed_pairs','planned_pairs','failed_attempts')}))
    for r in reference:
        print('previous',r['case'],r['candidate'],'delta MW',r['admission_difference_mw'],'delta W2 USD',r['week2_score_difference_usd'])
    return summary


if __name__=='__main__':
    export()
