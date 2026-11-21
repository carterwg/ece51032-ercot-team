"""Preserve earlier baseline campaigns and intermediate verification history."""
from collections import defaultdict
import csv
import json
from pathlib import Path

from ..context import file_fingerprint, scenario_fingerprint
from ..evaluation.campaign import save_json
from .findings import (ON_MW, USER, csv_data, link, native_profiles, number,
                       summarize_energy, table, write_note)
from .findings_diagnostics import SnapshotDiagnostics, TOL_MW, make_period, solve_snapshot


def export_earlier_runs(root, destination):
    from tools.hosting_capacity import prepared_artifact_period_provider
    root=Path(root);destination=Path(destination)
    source=root/'runs/finalized-500mw/summary.json'
    if source.exists():
        summary=json.loads(source.read_text())
        for campaign in summary['campaigns']:
            variant=campaign['strategy_variant'];bus='1001' if variant=='full_generation' else '6141'
            output=source.parent/variant/'finalized-500mw'
            native=root/'ercot-connection-game/data/processed/activsg2000_representative_v1'
            if scenario_fingerprint(native)!=campaign['source_scenario_sha256']:
                raise ValueError('earlier baseline physical inputs changed')
            fingerprint={'summary':file_fingerprint(source)}
            scores=[];energy=[];details=''
            for result in campaign['rounds']:
                name=result['round'];folder=output/name
                ev_path=folder/'results/evaluation.json';csv_path=folder/'results/site_net_withdrawal.csv'
                request_path=folder/'submissions/baseline.csv'
                ev=json.loads(ev_path.read_text());rows=csv_data(csv_path.read_bytes());requests=csv_data(request_path.read_bytes())
                for path in (ev_path,csv_path,request_path):fingerprint[str(path)]=file_fingerprint(path)
                if ev['competition_scope']!='joint' or not ev['team_scores'][0]['feasible']:
                    raise ValueError('earlier campaign is not an accepted joint evaluation')
                if file_fingerprint(request_path)!=ev['input_sha256_by_team'][campaign['team_id']]:
                    raise ValueError('earlier request changed')
                if abs(float(result['score'])-ev['team_scores'][0]['score'])>.01:
                    raise ValueError('earlier score differs from official evaluation')
                # Normalize ownership only in memory; historical files stay intact.
                rows=[{**r,'team_id':'our-team'} for r in rows]
                requests={('our-team',r['site_id']):{**r,'team_id':'our-team'} for r in requests}
                rules=ev['rules'];annual=[w/rules['present_value_annuity_factor'] for w in rules['period_weight_hours']]
                m=summarize_energy(rows,annual,len(annual),rules['time_step_hours'])
                directory=folder/'planning_base_load' if name.endswith('2') else native
                for path in directory.glob('*.csv'):fingerprint[str(path)]=file_fingerprint(path)
                provider=prepared_artifact_period_provider(directory);headroom=native_profiles(str(directory))
                grouped=defaultdict(list)
                for row in rows:grouped[int(row['period_index'])].append(row)
                required=[];unknown=[];minimum={};probes=[]
                diagnostics=SnapshotDiagnostics(root,set())
                for i in m['generator_active_periods']:
                    period,ours=make_period(provider(i),grouped[i],requests)
                    try:
                        check=solve_snapshot(period,'minimum_private',ours)
                        if check['value_mw']>m['series'][i]['generation']+TOL_MW:
                            raise ValueError('minimum exceeds recorded feasible generation')
                        minimum[i]=check['value_mw']
                        if check['value_mw']>TOL_MW:required.append(i)
                    except Exception as error:
                        unknown.append(i);minimum[i]=None
                    if i in {109,max(m['generator_active_periods'],key=lambda j:m['series'][j]['generation'])}:
                        probes.append(diagnostics.probe(period,'minimum_private',own_ids=ours))
                e=m['annual_energy_mwh']
                if abs(e['load']-float(result['served_load_mwh']))>1.:
                    raise ValueError('earlier annual served energy differs from official score')
                score=float(result['score']);value=float(result['it_value'])
                costs=sum(float(result[k]) for k in ['energy_cost','generator_operating_cost','generator_capital_cost','site_cost','storage_capital_cost'])
                if abs(value-costs-score)>.01:raise ValueError('earlier economic accounting does not balance')
                scores.append([name,500,500,number(value/1e9,6),number(score/1e9,6),number(float(result['service_fraction'])*100,6)+'%'])
                energy.append([name,number(e['grid']),number(e['generation']),number(100*m['grid_share'],6)+'%',
                    number(m['modeled_generator_hours']),number(m['annual_generator_hours']),
                    number(sum(annual[i] for i in required)),number(sum(annual[i] for i in unknown))])
                with (directory/'branch_limits.csv').open() as f:
                    branches={b['branch_id']:b for b in csv.DictReader(f) if b.get('status','1')=='1'}
                bindings=defaultdict(list)
                for index,values in ev['aggregate_diagnostics']['binding_diagnostics_by_period'].items():
                    for bid,flow in values['flow_mw_by_branch'].items():
                        if bid in branches and abs(abs(flow)-float(branches[bid]['thermal_limit_mva']))<=TOL_MW:
                            bindings[bid+(' upper' if flow>=0 else ' lower')].append(int(index))
                details+='\n## '+name+'\n\n'+table(['Actual tight branch / direction','Binding periods'],[(b,', '.join(map(str,ps))) for b,ps in sorted(bindings.items())])
                selected=sorted(set(m['generator_active_periods']) if bus=='1001' else {109})
                details+='\n'+table(['Period','Actual private MW','Actual grid MW','Verified minimum private MW'],[
                    [i,number(m['series'][i]['generation'],6),number(m['series'][i]['grid'],6),number(minimum.get(i,0.),6)] for i in selected])
                for probe in probes:
                    details+=f'\nPeriod {probe["period_index"]} targeted diagnostic: **{probe["status"]}**. '+link(probe['evidence_path'],'independently checked snapshot')+'.\n'
                    details+='\n'+table(['Rating +1 MW on','Status','Minimum before MW','Minimum after MW','Reduction MW'],[
                        [', '.join(t['branch_ids']),t['status'],number(t.get('value_before_mw'),6),number(t.get('value_after_mw'),6),number(t.get('improvement_mw'),6)] for t in probe['line_relaxations']])
                details+='\n'+link(ev_path,'official score and flows')+' · '+link(csv_path,'hourly energy ledger')+'.\n'
                print(f'Earlier findings: {variant}/{name}',flush=True)
            if abs(sum(float(r['score']) for r in campaign['rounds'])-campaign['combined_score_usd'])>.01:
                raise ValueError('earlier campaign total does not balance')
            cache=root/'runs/findings-diagnostics/earlier-baselines'/variant
            cache.mkdir(parents=True,exist_ok=True);save_json(cache/'consumed_evidence_sha256.json',fingerprint)
            text=f'# Earlier solo baseline: C = G, 500 MW, bus {bus}\n\n'+table(['Round','Requested C MW','Requested G MW','Gross IT value $B','Net score $B','Admission'],scores+
                [['Campaign','—','—',number(sum(float(r['it_value']) for r in campaign['rounds'])/1e9,6),number(campaign['combined_score_usd']/1e9,6),'—']])
            text+='\n'+table(['Round','Grid MWh/year','Private MWh/year','Grid share','Modeled gen h','Annual gen h','Verified required annual h','Unresolved annual h'],energy)
            text+='\nThis earlier solo campaign is preserved separately from the 119 matched Part 2 campaigns. It is not an additional competitive hypothesis. C and G are new capacity per submission; S1 remains in S2 and weeks reset. Scores/energy describe new sites. Annual MWh/hours use representative-day weights. Private output above one watt counts as on. Required hours come from minimum-private-generation replays for every active period; failures stay unresolved. Tight lines alone do not establish causality; the targeted +1 MW tests hold admitted loads fixed and do not change saved scores.\n'
            if bus=='1001':text+='\nThe bus-1001 plan uses substantial private energy despite being solo. The minimum-generation and finite-relaxation results below test the local transmission explanation rather than assuming every dispatched MWh was indispensable.\n'
            else:text+='\nBus 6141 needed no private generation in these solo evaluations. Installed capacity still incurs capital cost. Crowded-case results are recorded separately.\n'
            text+=details+'\n## Provenance\n\n'+link(source,'original campaign summary')+' · '+link(cache/'consumed_evidence_sha256.json','hashes of consumed evidence')+'. Historical inputs and evaluation files are preserved; this fingerprint inventory was created when backfilling findings, not frozen as a historical complete artifact manifest.\n'
            write_note(destination/f'LEGACY_C_eq_G_S1_S2_500_{bus}__solo.md',text)
    export_intermediate_history(root,destination)


def export_intermediate_history(root,destination):
    verification=root/'runs/part1-stage2/verification.json'
    if verification.exists():
        v=json.loads(verification.read_text())
        text='# Standalone bottleneck reproduction and verification\n\n'+table(['Measurement','Result'],[
            ['Candidates',v['candidate_count']],['Periods',v['period_count']],['Candidate-period solves',v['candidate_period_solves']],
            ['Maximum HC difference from screening MW',number(v['max_capacity_difference_from_screening_mw'],9)],
            ['Carter shortlist groups checked',v['carter_shortlist_groups_verified']],
            ['Top 100 material transmission-limited buses',v['top100_material_transmission_limited_count']],
            ['Scores / IT value / grid/private MWh / generator hours','N/A — capacity diagnostics, not scored operation']])
        text+='\n'+table(['Independent physical/optimality check','Maximum error MW'],[(k,number(x,10)) for k,x in v['max_independent_errors'].items()])
        text+='\n'+table(['Bus','Line','Rating increase MW','Measured HC gain MW','Shadow prediction MW'],[
            [r['bus_id'],r['branch_id'],r['rating_increase_mw'],number(r['hosting_capacity_gain_mw'],8),number(r['shadow_prediction_mw'],8)] for r in v['line_rating_perturbation_checks']])
        text+='\nThe standalone capacity results reproduced the screening values closely. Material line limits require positive capacity shadows and perturbation checks; simply observing a tight line can misclassify a generation-limited bus. Standalone groups do not prove independent corridors or quantify electrical interaction under rival load. The later Part 1 findings address those gaps. '+link(verification,'complete verification evidence')+'.\n'
        rows=[]
        for path in sorted((root/'runs').glob('part1-stage2*/bottlenecks.json')):
            d=json.loads(path.read_text());rows.append([path.parent.name,d['solver'],len(d['results']),link(path,'saved capacities / diagnoses')])
        text+='\n'+table(['Recorded reproduction','Solver','Candidates','Evidence'],rows)
        write_note(destination/'HISTORY_standalone_bottleneck_verification.md',text)
    rows=[]
    for directory in ['part1-stage1','part1-initial-seven','part1-extended-backgrounds','part1-failed-gurobi',
                      'part2-cli-primary','part2-cli-benchmark','part2-scheduled-cli-s1','part2-scheduled-cli-s2']:
        folder=root/'runs'/directory
        if not folder.exists():continue
        file=folder/'manifest.json'
        d=json.loads(file.read_text()) if file.exists() else {}
        explanation=d.get('error') or ('candidate selection, no dispatch' if directory=='part1-stage1' else
            'generated and validated CSV only; no scored game run' if 'cli-' in directory else
            'component evidence reused in final Part 1; no extra independent replication')
        rows.append([directory,d.get('status','selection saved'),explanation,link(folder,'raw record')])
    text='# Intermediate runs and validation history\n\n'+table(['Run','Recorded status','Meaning','Evidence'],rows)
    text+='\nScores, value, energy, and generator hours are **not applicable** to candidate selection/CSV-only checks or physical grouping components. Failed solver attempts do not receive fabricated zero scores. The initial seven-background report and two-background extension feed the final nine-background Part 1 record; they are not counted twice. The recorded Gurobi failure is preserved, while the completed final analysis uses its documented accepted solver.\n'
    write_note(destination/'HISTORY_intermediate_and_validation_runs.md',text)
