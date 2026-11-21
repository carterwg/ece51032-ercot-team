"""Persistent Markdown findings for completed experiment cells.

python -m team_strategy.experiments.findings
python -m team_strategy.experiments.findings --bundle runs/NEW_EXPERIMENT

Only Markdown is written to findings/. Numerical diagnostic caches stay under
runs/findings-diagnostics/. Saved scores are never replaced by diagnostic scores.
"""
import argparse
from collections import defaultdict
from dataclasses import asdict
import csv
from functools import lru_cache
import hashlib
import io
import json
import math
import os
from pathlib import Path
import re
import shutil

from ..context import file_fingerprint, scenario_fingerprint
from ..evaluation.campaign import save_json
from .findings_diagnostics import SnapshotDiagnostics, added_generators, make_period, TOL_MW

ROOT = Path(__file__).resolve().parents[3]
ON_MW = 1e-6
SCHEMA = 1
META = '<!-- findings-record: '
USER = '<!-- USER_NOTES -->'
RECORD_PATHS = ('bundle', 'campaign_output', 'diagnostic_cache')
REPO_LINK = re.compile(r'\]\(<(' + re.escape(str(ROOT)) + r'/[^>]+)>\)')


def table(headers, rows):
    escape = lambda v: str(v).replace('|','\\|').replace('\n',' ')
    return '\n'.join(['| '+' | '.join(map(escape,headers))+' |',
                      '| '+' | '.join('---' for _ in headers)+' |']+
                     ['| '+' | '.join(escape(x) for x in row)+' |' for row in rows])+'\n'


def number(value, places=3):
    return 'N/A' if value is None else f'{value:,.{places}f}'


def link(path, label):
    return f'[{label}](<{Path(path).resolve()}>)'


def repo_path(path):
    absolute = Path(path).resolve()
    return str(absolute.relative_to(ROOT) if absolute.is_relative_to(ROOT) else absolute)


def portable_report_links(path, text):
    return REPO_LINK.sub(lambda match: '](<' + os.path.relpath(match[1], path.parent) + '>)', text)


def read_record(path):
    text = path.read_text()
    line = next((l for l in text.splitlines() if l.startswith(META)),None)
    if line is None:
        return None
    record = json.loads(line[len(META):-4])
    for key in RECORD_PATHS:
        if record.get(key):
            record[key] = str(ROOT / record[key])
    return record


def write_note(path, text, record=None):
    path.parent.mkdir(parents=True,exist_ok=True)
    personal = ''
    if path.exists() and USER in path.read_text(): personal = path.read_text().split(USER,1)[1]
    if record:
        record = {key: repo_path(value) if key in RECORD_PATHS and value else value
                  for key, value in record.items()}
    metadata = META+json.dumps(record,separators=(',',':'),allow_nan=False)+' -->\n' if record else ''
    temporary = path.with_name('.'+path.stem+'.tmp.md')
    generated = re.sub(r'[ \t]+\n', '\n', portable_report_links(path, text)).rstrip()
    content=metadata+generated+'\n\n## Personal notes\n\n'+USER+(personal if personal.strip() else '')
    temporary.write_text(content if content.endswith('\n') else content+'\n')
    temporary.replace(path)


def checked_bytes(output, relative, hashes):
    data = (output/relative).read_bytes()
    if relative not in hashes or hashlib.sha256(data).hexdigest()!=hashes[relative]:
        raise ValueError(f'finding evidence changed or is unhashed: {output/relative}')
    return data


def verify_cached_evidence(output, hashes):
    """A cached calculation never bypasses validation of its raw evidence."""
    for relative in hashes:
        path = Path(relative)
        if ((path.parent.name=='canonical' and path.name in {'evaluation.json','site_net_withdrawal.csv'})
                or (path.parent.name=='inputs' and path.suffix=='.csv')
                or (path.parent.name.endswith('-s2-base') and path.name in {
                    'demand_bus.csv','generator_catalog.csv','branch_limits.csv','dcline.csv'})):
            checked_bytes(output,relative,hashes)


def csv_data(data):
    return list(csv.DictReader(io.StringIO(data.decode('utf-8-sig'))))


def policy(config, portfolio):
    schedule = portfolio.get('generation_schedule', config.get('generation_schedule'))
    if schedule:
        first, second = schedule['1'], schedule['2']
        if first == second == 1: return 'C_eq_G_S1_S2'
        if first == second == 0: return 'G_eq_0_S1_S2'
        if second == 1:
            capacity = f'{config["capacity_per_submission_mw"]*first:g}'.replace('.', 'p')
            return f'G_eq_{capacity}_S1_C_eq_G_S2'
        return f'G_fraction_{first:g}_S1_{second:g}_S2'.replace('.', 'p')
    g = portfolio['generator_fraction']
    if g==0.: return 'G_eq_0_S1_S2'
    if g==1.: return 'C_eq_G_S1_S2'
    return 'G_eq_'+str(g).replace('.','p')+'_C_S1_S2'


def stem_for(config, portfolio):
    weights = portfolio['weights']
    buses = '_'.join(portfolio['bus_ids'])
    if len(weights)>1 and max(weights)-min(weights)>1e-12:
        buses = '_'.join(f'{b}_w{w:g}'.replace('.','p') for b,w in zip(portfolio['bus_ids'],weights,strict=True))
    return policy(config,portfolio)+'_'+f'{config["capacity_per_submission_mw"]:g}'+'_'+buses


@lru_cache(maxsize=6)
def native_profiles(directory):
    """Static representative package: retain full-horizon generation bounds."""
    from tools.activsg2000.dcopf import load_prepared_artifact
    artifact = load_prepared_artifact(str(directory))
    if artifact.scenario_year is not None: raise ValueError('calendar availability needs a period-specific findings loader')
    capacity = math.fsum(float(g['p_max_mw']) for g in artifact.generators_raw if g.get('status','1')=='1')
    fixed = math.fsum(float(r['Pt']) for r in artifact.dcline_raw if r.get('status','1')=='1')
    ids = [b['bus_id'] for b in artifact.buses_raw]
    return tuple(capacity+fixed-math.fsum(float(row[b]) for b in ids) for row in artifact.demand_rows)


def summarize_energy(site_rows, annual_weights, horizon, step_hours):
    by_period = defaultdict(list)
    by_site = defaultdict(list)
    for r in site_rows:
        if r['team_id']=='our-team':
            by_period[int(r['period_index'])].append(r);by_site[r['site_id']].append(r)
    series=[]
    for i in range(horizon):
        ours=by_period[i]
        series.append({'period':i,'load':math.fsum(float(r['load_mw']) for r in ours),
            'generation':math.fsum(float(r['generation_mw']) for r in ours),
            'grid':math.fsum(max(0.,float(r['net_withdrawal_mw'])) for r in ours),
            'charge':math.fsum(float(r['storage_charge_mw']) for r in ours),
            'discharge':math.fsum(float(r['storage_discharge_mw']) for r in ours)})
    energy = {k:math.fsum(r[k]*annual_weights[r['period']] for r in series)
              for k in ['load','generation','grid','charge','discharge']}
    if abs(energy['grid']+energy['generation']+energy['discharge']-energy['load']-energy['charge'])>1e-3:
        raise ValueError('annual energy accounting does not balance')
    active = [r['period'] for r in series if r['generation']>ON_MW]
    return {'series':series,'annual_energy_mwh':energy,'generator_active_periods':active,
            'modeled_generator_hours':len(active)*step_hours,
            'annual_generator_hours':math.fsum(annual_weights[i] for i in active),
            'grid_share':energy['grid']/energy['load'] if energy['load'] else None,
            'peak_generation_mw':max(r['generation'] for r in series),
            'peak_grid_mw':max(r['grid'] for r in series),'sites':dict(by_site)}


def analyze_round(root, config, portfolio, cell, r, rules, signatures, branches):
    from tools.hosting_capacity import prepared_artifact_period_provider
    output=Path(cell['output']);hashes=cell['artifact_sha256'];name=r['round'];prefix=name+'/'
    rows=csv_data(checked_bytes(output,prefix+'canonical/site_net_withdrawal.csv',hashes))
    evaluation=json.loads(checked_bytes(output,prefix+'canonical/evaluation.json',hashes))
    if evaluation['competition_scope'] not in {'joint','joint_projection'}: raise ValueError('unmatched fallback cannot become findings')
    requests={}
    for path in sorted((output/name/'inputs').glob('*.csv')):
        data=checked_bytes(output,str(path.relative_to(output)),hashes);records=csv_data(data)
        for row in records:
            if hashlib.sha256(data).hexdigest()!=r['input_sha256_by_team'][row['team_id']]:
                raise ValueError('request hash differs from the recorded round')
            requests[(row['team_id'],row['site_id'])]=row
    annual=[float(w)/rules['present_value_annuity_factor'] for w in rules['period_weight_hours']]
    horizon=r['horizon'];step=rules['time_step_hours']
    metrics=summarize_energy(rows,annual,horizon,step)
    if abs(metrics['annual_energy_mwh']['load']-next(s['served_load_mwh'] for s in r['team_scores'] if s['team_id']=='our-team'))>1.:
        raise ValueError('recorded served MWh and annual findings disagree')
    submission=int(name[-1]);week=int(name[5]);directory=(root/config['scenario_directory'] if submission==1 else output/f'week-{week}-s2-base')
    if submission==2:
        for relative in ['demand_bus.csv','generator_catalog.csv','branch_limits.csv','dcline.csv']:
            checked_bytes(output,f'week-{week}-s2-base/{relative}',hashes)
    headroom=native_profiles(str(directory));provider=prepared_artifact_period_provider(directory)
    snapshots=defaultdict(list)
    for row in rows:snapshots[int(row['period_index'])].append(row)
    potential=set().union(*(set(signatures.get(b,())) for b in portfolio['bus_ids']))
    diagnostics=SnapshotDiagnostics(root,potential)
    bindings={};periods=[];required=[];optional=[];unknown=[];probes=[]
    has_storage=any(float(v.get('storage_power_mw',0.)) or float(v.get('storage_energy_mwh',0.)) for v in requests.values())
    binding_data=evaluation['aggregate_diagnostics']['binding_diagnostics_by_period']
    if set(binding_data)!={str(i) for i in range(horizon)}:raise ValueError('full-horizon flow evidence is missing')
    for i,s in enumerate(metrics['series']):
        actual=snapshots[i];d=binding_data[str(i)];tight=[];candidate_near=[]
        for bid,flow in d['flow_mw_by_branch'].items():
            if bid not in branches:continue
            b=branches[bid];limit=b['limit_mw'];flow=float(flow);direction='upper' if flow>=0 else 'lower'
            signature=f'{bid}:{direction}';margin=limit-abs(flow)
            if margin < -TOL_MW: raise ValueError(f'recorded flow exceeds branch limit: {bid}')
            if margin<=TOL_MW:
                tight.append(signature)
                item=bindings.setdefault(signature,{'branch_id':bid,'direction':direction,'limit_mw':limit,
                    'from_bus':b['from_bus'],'to_bus':b['to_bus'],'periods':[],'generator_on_periods':[],
                    'maximum_abs_flow_mw':0.,'part1_candidate':signature in potential})
                item['periods'].append(i);item['maximum_abs_flow_mw']=max(item['maximum_abs_flow_mw'],abs(flow))
                if s['generation']>ON_MW:item['generator_on_periods'].append(i)
            if signature in potential and limit>0 and abs(flow)>=.95*limit:
                candidate_near.append({'signature':signature,'flow_mw':flow,'limit_mw':limit,'margin_mw':margin})
        private,_=added_generators(requests,actual)
        other_cap=math.fsum(g.p_max_mw for g in private if not g.generator_id.startswith('findings:our-team:'))
        total_load=math.fsum(float(x['load_mw'])+float(x['storage_charge_mw'])-float(x['storage_discharge_mw']) for x in actual)
        lower=max(0.,total_load-headroom[i]-other_cap)
        total_net=math.fsum(float(x['net_withdrawal_mw']) for x in actual)
        native_remaining=headroom[i]-total_net
        full_request_lower=max(0.,total_load-s['load']+config['capacity_per_submission_mw']-headroom[i]-other_cap)
        prices={b:max(0.,float(d['balance_dual_by_bus'][b])) for b in portfolio['bus_ids']}
        grid_bill=math.fsum(max(0.,float(x['net_withdrawal_mw']))*prices[x['bus_id']] for x in actual if x['team_id']=='our-team')*rules['period_weight_hours'][i] if r['energy_cost_enabled'] else 0.
        item={**s,'annual_hours':annual[i],'base_generation_headroom_mw':headroom[i],
            'native_remaining_mw':native_remaining,'generation_lower_bound_mw':lower,
            'full_request_generation_lower_bound_mw':full_request_lower,'tight_lines':sorted(tight),
            'candidate_near_lines':candidate_near,'grid_bill_usd':grid_bill,'lmp_by_own_bus':prices,
            'requirement_status':'no_output_needed_in_recorded_dispatch','minimum_private_mw':0.}
        if s['generation']>ON_MW:
            if lower>s['generation']+TOL_MW:raise ValueError('generation lower bound exceeds recorded feasible output')
            if not has_storage and abs(lower-s['generation'])<=TOL_MW:
                item.update(requirement_status='certified_by_generation_bound_and_feasible_witness',minimum_private_mw=lower)
            elif not has_storage:
                period,own=make_period(provider(i),actual,requests)
                probe=diagnostics.probe(period,'minimum_private',own_ids=own,generation_lower_bound=lower)
                probes.append(probe);item['diagnostic_evidence']=probe['evidence_path']
                if probe['status']=='verified':
                    if probe['value_mw']>s['generation']+TOL_MW:raise ValueError('minimum-generation replay exceeds the recorded feasible output')
                    item.update(requirement_status='verified_minimum_private_replay',minimum_private_mw=probe['value_mw'])
                else:item.update(requirement_status='unresolved',minimum_private_mw=None)
            else:item.update(requirement_status='storage_counterfactual_not_replayed',minimum_private_mw=None)
            if item['minimum_private_mw'] is None:unknown.append(i)
            elif item['minimum_private_mw']>TOL_MW:required.append(i)
            else:optional.append(i)
        periods.append(item)
    # Curtailed requests get a local counterfactual at the generation-critical
    # snapshot and the Part 1 critical hour. Never pretend this is a full game rerun.
    curtailed=r['service_fraction']<1-1e-6
    if curtailed and not has_storage:
        chosen={min(range(horizon),key=lambda i:headroom[i]), min(109,horizon-1)}
        for i in sorted(chosen):
            for bus in portfolio['bus_ids']:
                period,_=make_period(provider(i),snapshots[i],requests,mode='hosting',target_bus=bus)
                probe=diagnostics.probe(period,'hosting',target_bus=bus)
                probes.append(probe)
    metrics.pop('series');metrics.pop('sites')
    metrics.update(round=name,score_usd=r['score_usd'],score_breakdown=r['score_breakdown'],
        requested_load_mw=math.fsum(float(x['connection_capacity_mw']) for k,x in requests.items() if k[0]=='our-team'),
        requested_generation_mw=math.fsum(float(x['generator_capacity_mw']) for k,x in requests.items() if k[0]=='our-team'),
        allocated_load_mw=math.fsum(a['allocated_connection_mw'] for a in r['site_allocations']),
        service_fraction=r['service_fraction'],site_allocations=r['site_allocations'],
        required_generator_periods=required,optional_generator_periods=optional,unresolved_generator_periods=unknown,
        annual_required_generator_hours=math.fsum(annual[i] for i in required),
        annual_unresolved_generator_hours=math.fsum(annual[i] for i in unknown),
        periods=periods,bindings=list(bindings.values()),probes=probes,potential_signatures=sorted(potential),
        scenario_directory=str(directory),has_storage=has_storage,competition_scope=r['competition_scope'])
    return metrics


def period_label(i):return f'{i} (day {i//24+1}, h{i%24:02d})'


def render_case(record, metrics, config, scenario, cell, destination):
    title=record['stem']+' — '+record['scenario']
    rounds=metrics['rounds'];total=cell['result']['campaign_score_usd'];last_by_week={};score_rows=[];energy_rows=[];cost_rows=[]
    for r in rounds:
        week=r['round'][5];s2=r['round'].endswith('2');old=last_by_week.get(week)
        total_c=r['allocated_load_mw']+(old['allocated_load_mw'] if s2 and old else 0.)
        b=r['score_breakdown'];e=r['annual_energy_mwh']
        score_rows.append([r['round'],number(r['requested_load_mw']),number(r['requested_generation_mw']),
            number(r['allocated_load_mw'],6),number(total_c,6),number(b['it_value_usd']/1e9,6),number(r['score_usd']/1e9,6)])
        energy_rows.append([r['round'],number(e['grid']),number(e['generation']),
            'N/A' if r['grid_share'] is None else number(100*r['grid_share'],6)+'%',
            number(r['modeled_generator_hours']),number(r['annual_generator_hours']),
            number(r['annual_required_generator_hours']),number(r['annual_unresolved_generator_hours']),number(r['peak_generation_mw'],6)])
        cost_rows.append([r['round'],*(number(b[k]/1e9,6) for k in ['grid_energy_cost_usd','generator_operating_cost_usd',
            'generator_capital_cost_usd','site_cost_usd','storage_capital_cost_usd'])])
        if not s2:last_by_week[week]=r
    score_rows.append(['Campaign total','—','—','—','—',number(sum(r['score_breakdown']['it_value_usd'] for r in rounds)/1e9,6),number(total/1e9,6)])
    text=f'# {title}\n\n'+table(['Round','Requested C MW','Requested G MW','Admitted new C MW','Own operating C incl. S1 MW','Gross IT value $B','Net score $B'],score_rows)
    text+='\n'+table(['Round','Grid MWh/year','Private gen MWh/year','Grid energy share','Gen on: modeled h','Gen on: annual h','Verified required-on annual h','Unresolved-on annual h','Peak private MW'],energy_rows)
    text+='\n'+table(['Round','Grid energy $B','Generator operation $B','Generator capital $B','Site capital $B','Storage capital $B'],cost_rows)
    text+='\n**Scope:** Score and energy tables refer to the **new sites in each submission**. S1 sites remain operating in S2; the operating-capacity column includes them, but their value/capital is not scored again. Each year-energy column describes that build’s represented annual operation; four builds are not one continuous year. Scores are the game’s ten-year present-value economics. Weeks reset.\n'
    text+='\n**Hours:** A generator is counted on when our combined output exceeds 0.000001 MW. Modeled hours count distinct periods, not the number of generator units. Annual hours use representative-day weights; they are not 120 equally weighted hours. Required-on hours are verified for the **admitted load**, allowing rival generation to redispatch. Zero required hours for a curtailed plan does not mean the original 500 MW request could be served without backup. Unresolved hours are not counted as unnecessary.\n'
    text+=f'\n## Test setup\n\n- Policy: `{record["policy"]}`.\n- Layout: '+', '.join(f'{b}: {config["capacity_per_submission_mw"]*w:g} MW per submission' for b,w in zip(record['buses'],record['weights'],strict=True))+'.\n'
    if 'rival_plan' in scenario:
        plan = scenario['rival_plan']
        loads = ', '.join(f'{bus} ({config["capacity_per_submission_mw"]*weight:g} MW)' for bus,weight in zip(plan['bus_ids'],plan['weights'],strict=True))
        text += f'- Opponents: {scenario["rival_count"]}. Each uses {loads} per submission. G/C is {plan["generation_schedule"]["1"]:g} in S1 and {plan["generation_schedule"]["2"]:g} in S2.\n'
    else:
        text+=f'- Opponents: {len(scenario["rival_bus_ids"])}; each requests 500 MW per submission at '+(', '.join(scenario['rival_bus_ids']) or 'no buses (solo reference)')+f'; rival G/C = {scenario["rival_generator_fraction"]:g}.\n'
    text+=f'- Seed: {cell["result"]["seed"]}. Included in competitive means: {scenario["include_in_risk"]}. No calibrated probability is assigned to this hypothesis.\n'
    text+='- Full 120-period joint evaluation; S1 actual withdrawals of **all** teams carry into S2.\n'
    if record.get('exploratory'):text+='- Exploratory duplicate probe; excluded from strategy-comparison means. Original full artifact fingerprints were not frozen for this probe; current consumed files are hashed when logged.\n'
    text+='\n## What happened and why\n'
    for r in rounds:
        e=r['annual_energy_mwh'];name=r['round'];gen_on=r['generator_active_periods']
        text+=f'\n### {name}\n\nRequested {r["requested_load_mw"]:g} MW load and {r["requested_generation_mw"]:g} MW generation; admitted **{r["allocated_load_mw"]:.6f} MW** ({100*r["service_fraction"]:.6f}%). '
        if r['service_fraction']<1-1e-6:
            text+='The unadmitted capacity does not operate or earn IT value; this is firm-capacity allocation, not a 500 MW site suffering outages in only a few hours. '
            shortage=[p for p in r['periods'] if p['full_request_generation_lower_bound_mw']>TOL_MW]
            text+=f'Holding other admitted loads/caps fixed, aggregate generation alone rules out full grid-only service at {len(shortage)} modeled periods; the largest own backup lower bound is {max((p["full_request_generation_lower_bound_mw"] for p in shortage),default=0.):.6f} MW. Local line restrictions can be stronger. '
        else:text+='All requested load was admitted. '
        if gen_on:
            text+=f'Private generation ran at periods {", ".join(map(str,gen_on))}; represented annual output was {e["generation"]:,.3f} MWh. '
            if r['required_generator_periods']:text+=f'Own generation was physically necessary for admitted load at verified periods {", ".join(map(str,r["required_generator_periods"]))}. '
            if r['optional_generator_periods']:text+=f'At periods {", ".join(map(str,r["optional_generator_periods"]))}, a feasibility replay found our own generation could be zero if other generators redispatched; observed use there is not proof that our generator was indispensable. '
            if r['unresolved_generator_periods']:text+=f'Necessity remains unresolved at {r["unresolved_generator_periods"]}. '
        else:text+='No own private output was dispatched. '
        if name.startswith('week-2'):text+='Week 2 does not charge grid purchases, but network constraints still apply. '
        text+='\n'
        selected=set(gen_on)
        selected.add(min(r['periods'],key=lambda p:p['base_generation_headroom_mw'])['period'])
        selected.add(min(109,len(r['periods'])-1))
        if r['score_breakdown']['grid_energy_cost_usd']:
            selected.update(p['period'] for p in sorted(r['periods'],key=lambda p:p['grid_bill_usd'],reverse=True)[:3])
        critical=[r['periods'][i] for i in sorted(selected)]
        text+='\n'+table(['Period (zero-based)','Annual h represented','Actual private MW','Actual grid MW','Native spare after admitted net loads MW','Generation-only min own MW','Verified min own MW','Weighted grid bill $M','Actual tight lines'],[
            [period_label(p['period']),number(p['annual_hours']),number(p['generation'],6),number(p['grid'],6),number(p['native_remaining_mw'],6),
             number(p['generation_lower_bound_mw'],6),number(p['minimum_private_mw'],6),number(p['grid_bill_usd']/1e6,6),', '.join(p['tight_lines']) or 'none'] for p in critical])
        text+='\nThe generation-only lower bound uses native Pmax plus all admitted rival private capacity. If it matches observed private output, the aggregate limit and the recorded feasible solution certify the minimum. A line touching its limit is an observation, not proof that it caused generator use.\n'
        text+='\n'+table(['Observed binding branch','Endpoints','Direction','Rating MW','Max absolute flow MW','Binding periods','Binding while our gen on','Part 1 candidate'],[
            [b['branch_id'],b['from_bus']+' → '+b['to_bus'],b['direction'],number(b['limit_mw']),number(b['maximum_abs_flow_mw'],6),
             ', '.join(map(str,b['periods'])),', '.join(map(str,b['generator_on_periods'])) or 'none',b['part1_candidate']] for b in sorted(r['bindings'],key=lambda b:b['branch_id'])])
        text+='\n### Snapshot counterfactuals for this round\n\n'
        if not r['probes']:text+='No additional LP replay was needed: private output was zero or its minimum was certified by the aggregate generation bound. No line-relaxation claim is made.\n'
        for p in r['probes']:
            goal=('minimum total own private generation, allowing native/rival redispatch' if p['objective']=='minimum_private'
                  else f'maximum grid-only load at {p["target_bus"]}, keeping our other sites’ recorded net withdrawals fixed')
            text+=f'- Period {p["period_index"]}: {goal}. Status **{p["status"]}**. '
            if p['status']=='verified':
                text+=f'Objective = **{p["value_mw"]:.6f} MW**; maximum nodal residual {p["max_balance_error_mw"]:.3g} MW. '
                if p.get('solver_primal_tolerance_mw',1e-9)>1e-9:
                    text+='The identical LP required a solver feasibility-tolerance retry at 0.00001 MW; independent balance, limit, and duality errors still passed the 0.0001 MW acceptance threshold. '
                if p['objective']=='hosting':text+=f'Generation-only capacity ceiling = {p["generation_headroom_mw"]:.6f} MW; limiting-resource diagnosis: {p["limiting_resource"]}. '
            else:text+=f'Unresolved: {p.get("error", "no independently checked solution")}. '
            text+=link(p['evidence_path'],'diagnostic evidence')+'.\n'
            if p['line_relaxations']:
                text+='\n'+table(['Rating increased by 1 MW on','Status','Objective before MW','Objective after MW','Improvement MW','Causal effect observed'],[
                    [', '.join(t['branch_ids']),t['status'],number(t.get('value_before_mw'),6),number(t.get('value_after_mw'),6),
                     number(t.get('improvement_mw'),6),t.get('causal_effect_observed','unresolved')] for t in p['line_relaxations']])+'\n'
        text+='\nThese are selected **hourly** physical counterfactuals at fixed admitted loads/resources. They do not rerun allocation across the horizon and do not change this campaign’s score. Up to three likely binding branches, prioritized using Part 1 and diagnostic shadows, are tested individually and together. No improvement from a single-line test does not rule out other or jointly binding lines.\n'
    text+='\n## Part 1 hypotheses and interpretation limits\n\n'
    potentials=sorted(set().union(*(set(r['potential_signatures']) for r in rounds)))
    text+='Potential signatures from the electrical grouping: '+(', '.join('`'+x+'`' for x in potentials) or 'none retained')+'. These are screening hypotheses; only the observed-flow and finite-relaxation evidence above pertains to this run.\n'
    if set(record['buses'])=={'6062','6298'}:text+='6062 and 6298 share `b02136:lower` under stress; the split is not evidence of independent corridors.\n'
    text+='This is one fixed opponent hypothesis. It supplies no competitor probability estimate, no global optimum over all buses/resources, and no evidence that S1 generation is unnecessary in a stronger untested field.\n'
    text+='\n## Reproducibility and numerical history\n\n'
    override=cell.get('execution_override')
    text+=('This accepted campaign used a recorded numerical retry: `'+override['kind']+'`. '+link(override.get('audit_path',override.get('audit_file',Path(cell['output'])/'campaign.json')),'retry audit')+'.\n' if override else 'No per-cell numerical retry is recorded in this cell.\n')
    if cell.get('execution_audit'):
        audit = json.loads(Path(cell['execution_audit']).read_text())
        if audit.get('matched_week_reuse'):
            text += '\nThe evaluator reused identical physical inputs across weeks and applied each week’s scoring rules. Any changed network or plan required a separate solve. '+link(cell['execution_audit'],'execution audit')+'.\n'
    if cell.get('prior_attempts'):
        text += '\n'+table(['Earlier attempt','Outcome','Log'],[[a['method'],a['error'],link(a['log'],'evaluation log')] for a in cell['prior_attempts']])
    text+=f'Campaign SHA-256: `{record["campaign_sha256"]}`.\n\n'+link(Path(cell['output'])/'campaign.json','accepted campaign')+' · '+link(record['bundle'],'experiment bundle')+' · '+link(Path(record['bundle'])/'manifest.json','source/input manifest')+'\n'
    for r in rounds:
        folder=Path(cell['output'])/r['round']
        text+='\n- '+r['round']+': '+link(folder/'canonical/evaluation.json','official evaluation and flows')+'; '+link(folder/'canonical/site_net_withdrawal.csv','hourly energy ledger')+'; '+link(folder/'inputs','requested CSVs')+'.'
    return text


def case_record(root, bundle, config, portfolio, scenario, cell, destination, *, exploratory=False):
    output=Path(cell['output']);hashes=cell['artifact_sha256']
    data=checked_bytes(output,'campaign.json',hashes);result=json.loads(data)
    if result!=cell['result'] or result['status']!='complete' or len(result['rounds'])!=4:
        raise ValueError('campaign is incomplete or differs from its saved evidence')
    if not math.isclose(result['campaign_score_usd'],math.fsum(r['score_usd'] for r in result['rounds']),abs_tol=.01,rel_tol=1e-12):
        raise ValueError('campaign score differs from its four rounds')
    rules_path=root/config['rules_file'];rules=json.loads(rules_path.read_text())
    if any(r['rules_sha256']!=file_fingerprint(rules_path) for r in result['rounds']):raise ValueError('historical scoring rules changed')
    groups=json.loads((root/config['part1_directory']/'groups.json').read_text())
    with (root/config['scenario_directory']/'branch_limits.csv').open(newline='') as f:
        branches={b['branch_id']:{'from_bus':b['from_bus_id'],'to_bus':b['to_bus_id'],'limit_mw':float(b['thermal_limit_mva'])}
                  for b in csv.DictReader(f) if b.get('status','1')=='1' and float(b['reactance_pu'])!=0}
    source_digest=hashlib.sha256(data).hexdigest();stem=stem_for(config,portfolio)
    cache=root/'runs/findings-diagnostics/cases';cache.mkdir(parents=True,exist_ok=True)
    code=file_fingerprint(Path(__file__))
    from . import findings_diagnostics
    version=hashlib.sha256((code+file_fingerprint(Path(findings_diagnostics.__file__))+file_fingerprint(rules_path)+file_fingerprint(root/config['part1_directory']/'groups.json')).encode()).hexdigest()
    cache_path=cache/(source_digest+'-'+version[:12]+'.json')
    if cache_path.exists():
        verify_cached_evidence(output,hashes)
        metrics=json.loads(cache_path.read_text())
    else:
        metrics={'rounds':[analyze_round(root,config,portfolio,cell,r,rules,groups['signatures'],branches) for r in result['rounds']]}
        save_json(cache_path,metrics)
    filename=stem+'__'+scenario['name']+('.md' if not exploratory else '__probe_'+source_digest[:10]+'.md')
    path=destination/filename
    if path.exists():
        existing=read_record(path)
        if existing and existing.get('campaign_sha256')!=source_digest:path=destination/(path.stem+'__'+source_digest[:10]+'.md')
    rs=metrics['rounds'];record={'schema':SCHEMA,'kind':'campaign','stem':stem,'policy':policy(config,portfolio),
        'portfolio':portfolio['name'],'buses':portfolio['bus_ids'],'weights':portfolio['weights'],'scenario':scenario['name'],
        'risk':scenario['include_in_risk'],'exploratory':exploratory,'bundle':str(bundle),'campaign_output':str(output),
        'campaign_sha256':source_digest,'score_usd':result['campaign_score_usd'],
        'it_value_usd':sum(r['score_breakdown']['it_value_usd'] for r in rs),
        'grid_mwh':sum(r['annual_energy_mwh']['grid'] for r in rs),'generation_mwh':sum(r['annual_energy_mwh']['generation'] for r in rs),
        'modeled_generator_hours':sum(r['modeled_generator_hours'] for r in rs),
        'annual_generator_hours':sum(r['annual_generator_hours'] for r in rs),
        'required_annual_hours':sum(r['annual_required_generator_hours'] for r in rs),
        'minimum_admission':min(r['service_fraction'] for r in rs),
        'scenario_count_in_bundle':len(config['scenarios']),'bundle_status':json.loads((bundle/'manifest.json').read_text()).get('status'),
        'diagnostic_cache':str(cache_path)}
    # An identical cell may occur in a component run and the pooled report.
    # Retain the broader source cohort instead of replacing it with a subset.
    if path.exists():
        previous=read_record(path)
        if previous and previous.get('scenario_count_in_bundle',0)>record['scenario_count_in_bundle']:
            record['bundle']=previous['bundle'];record['scenario_count_in_bundle']=previous['scenario_count_in_bundle'];record['bundle_status']=previous['bundle_status']
    write_note(path,render_case(record,metrics,config,scenario,cell,destination),record)
    return path


def case_evidence_summary(path, record):
    """Keep the important physical findings inside the requested strategy file."""
    if not record.get('diagnostic_cache'):return ''
    title=record['scenario']+(' (exploratory probe; excluded)' if record['exploratory'] else '')
    text='\n### '+title+'\n\n'+link(path,'Full run record, energy tables, and raw evidence')+'.\n\n'
    cache = Path(record['diagnostic_cache'])
    if not cache.is_file():
        return text
    rounds=json.loads(cache.read_text())['rounds']
    rows=[]
    for r in rounds:
        if r['required_generator_periods']:
            periods=[r['periods'][i] for i in r['required_generator_periods']]
            if all(p['requirement_status']=='certified_by_generation_bound_and_feasible_witness' for p in periods):
                reason=f'Aggregate generation shortage certifies backup; peak minimum {max(p["minimum_private_mw"] for p in periods):.6f} MW.'
            else:reason='Minimum-private-generation replays verify backup is necessary at the recorded admitted load.'
        elif r['unresolved_generator_periods']:reason='Generator necessity remains unresolved for some active hours.'
        elif r['generator_active_periods']:reason='Redispatch can avoid our private output in the tested active hours.'
        else:reason='Admitted load was supplied without own private output.'
        if r['service_fraction']<1-1e-6:
            shortage=[p for p in r['periods'] if p['full_request_generation_lower_bound_mw']>TOL_MW]
            reason+=f' Full grid-only request fails the generation bound in {len(shortage)} modeled periods; peak backup lower bound {max((p["full_request_generation_lower_bound_mw"] for p in shortage),default=0.):.6f} MW. Unadmitted capacity earns no IT value.'
        tight=', '.join(sorted(b['branch_id']+':'+b['direction'] for b in r['bindings'])) or 'none'
        rows.append([r['round'],number(r['allocated_load_mw'],6),number(r['annual_required_generator_hours']),tight,reason])
    text+=table(['Round','Admitted new MW','Verified required annual gen h','Actual tight lines across all periods','Physical finding'],rows)
    text+='\nTight lines above are observations; the finite-relaxation results below establish only the stated hourly causal effects.\n'
    for r in rounds:
        for p in r['probes']:
            if p['status']!='verified':
                text+=f'\n- {r["round"]}, period {p["period_index"]}: diagnostic unresolved; see the full run record.\n'
                continue
            if p['objective']=='hosting':
                text+=f'\n- {r["round"]}, period {p["period_index"]}: maximum grid-only load at bus {p["target_bus"]} = **{p["value_mw"]:.6f} MW**; generation-only ceiling = {p["generation_headroom_mw"]:.6f} MW; resource diagnosis: {p["limiting_resource"]}.\n'
            for t in p['line_relaxations']:
                if t['status']=='verified' and t['causal_effect_observed']:
                    effect='increases hosting capacity' if p['objective']=='hosting' else 'reduces minimum own private generation'
                    text+=f'\n- {r["round"]}, period {p["period_index"]}: increasing the rating of '+', '.join(t['branch_ids'])+f' by 1 MW each **{effect} by {t["improvement_mw"]:.6f} MW** ({t["value_before_mw"]:.6f} → {t["value_after_mw"]:.6f} MW).\n'
    return text


def write_strategy_indexes(root,destination):
    records=[]
    for path in sorted(destination.glob('*.md')):
        r=read_record(path)
        if r and r.get('kind')=='campaign':records.append((path,r))
    groups=defaultdict(list)
    for p,r in records:groups[r['stem']].append((p,r))
    indexes=[]
    for stem,cases in sorted(groups.items()):
        rows=[]
        for path,r in cases:
            rows.append([link(path,r['scenario']),number(r['score_usd']/1e9,6),number(r['it_value_usd']/1e9,6),
                number(100*r['minimum_admission'],6)+'%',number(r['grid_mwh']),number(r['generation_mwh']),
                number(r['modeled_generator_hours']),number(r['annual_generator_hours']),number(r['required_annual_hours']),
                'probe / excluded' if r['exploratory'] else ('competitive' if r['risk'] else 'solo / excluded')])
        text='# '+stem+'\n\n'+table(['Scenario / detailed finding','Net score $B','Gross IT value $B','Minimum admission','Σ grid MWh/build-year','Σ gen MWh/build-year','Σ modeled gen h','Σ annual gen h','Σ verified required annual h','Comparison role'],rows)
        text+='\nEnergy and hours are sums over four separate new-build evaluations, not one continuous year. See each linked case for per-round values, cumulative S1/S2 capacity, all observed binding lines, necessity tests, and tested line relief.\n'
        cohorts=defaultdict(list)
        for p,r in cases:
            if not r['exploratory']:cohorts[r['bundle']].append(r)
        for bundle,rs in cohorts.items():
            competitive=[r for r in rs if r['risk']]
            if competitive:
                text+=f'\nSource cohort {link(bundle,"experiment")}: {len(rs)} logged cases; competitive mean **${sum(r["score_usd"] for r in competitive)/len(competitive)/1e9:.6f}B**, worst logged competitive case **${min(r["score_usd"] for r in competitive)/1e9:.6f}B**. '
                complete=all(r['bundle_status']=='complete' for r in rs) and len(rs)==rs[0]['scenario_count_in_bundle']
                text+=('Complete source cohort.\n' if complete else '**Partial/incomplete cohort; descriptive values only, not a matched strategy recommendation.**\n')
        text+='\n## Detailed findings by scenario\n'
        for path,r in cases:text+=case_evidence_summary(path,r)
        text+='\n## Interpretation\n\nGenerator capacity is not energy output. G=C enables self-supply in constrained hours and can remain idle when grid electricity is cheaper. S1 demand remains in S2; weeks reset. Different buses can share the system generation ceiling and overlapping transmission constraints. Neither site count nor a Part 1 signature alone proves independent capacity or economic superiority. Selected hourly tests keep admitted loads/resources fixed and do not change the campaign score or prove a full-horizon allocation gain.\n'
        path=destination/(stem+'.md');write_note(path,text);indexes.append((path,len(cases)))
    text='# Findings register\n\n'+table(['Coverage','Count'],[
        ['Matched Part 2 campaign cases',sum(not r['exploratory'] for _,r in records)],['Exploratory duplicate probes',sum(r['exploratory'] for _,r in records)],
        ['Earlier baseline campaign records',len(list(destination.glob('LEGACY_*.md')))],
        ['Policy/layout summary files',len(indexes)],['Accepted scored rounds',4*sum(not r['exploratory'] for _,r in records)]])
    text+='\nThis folder contains Markdown only. Start with a policy/layout summary, then open its opponent-specific cases. Links under `runs/` refer to locally generated solver evidence. Saved game scores are separate from new hourly physical diagnostics. Failed attempts are never converted to zero scores.\n\n'
    text+=table(['Strategy summary','Scenario/probe notes'],[(link(p,p.stem),n) for p,n in indexes])
    text+='\n## How to read the measurements\n\n- C and G are requested new MW per submission; admitted capacity can be lower.\n- Dollar scores use the course’s present-value economics, summed over four graded submissions. Gross IT value is shown separately from net score and costs.\n- Modeled generator hours count distinct operating periods above 0.000001 MW output. Annual hours/MWh use the actual representative-day weights; 3 of 120 modeled hours need not mean 3/120 of a year.\n- “Required” refers to fixed admitted loads with rival generation allowed to redispatch. Actual generator use alone does not establish necessity.\n- Actual binding lines, Part 1 candidate lines, and finite-relaxation-confirmed causes are labeled separately. Observing a tight line does not prove it caused a shortage.\n- A snapshot line-relief diagnostic is not a full horizon allocation rerun or a revised campaign score.\n- Scenario means are descriptive equal-weight stress comparisons, not calibrated probabilities.\n'
    text+='\n## Other evidence\n\n'
    for p in sorted(destination.glob('*.md')):
        if p.name in {'Battery_S1_comparison.md', 'Battery_S1_targeted_optimization.md',
                      'Battery_S1_1MW_local_search.md'} or p.name.startswith(
            ('Ten_teams_', 'Part1_','HISTORY_','CONTROL_','LEGACY_')
        ):
            text+='- '+link(p,p.stem)+'\n'
    text+='\n## Updating the register\n\nCompleted experiment commands export findings automatically. Rebuild/backfill with:\n\n```bash\nPYTHONPATH=src:ercot-connection-game:ercot-connection-game/src .venv/bin/python -m team_strategy.experiments.findings\n```\n\nFor a particular saved experiment, add `--bundle runs/EXPERIMENT`. Diagnostic JSON caches remain outside this folder under `runs/findings-diagnostics/`. Text added below a file’s `Personal notes` marker is preserved on regeneration.\n'
    write_note(destination/'README.md',text)


def export_findings(bundle, *, root=ROOT, config_file=None, destination=None):
    root=Path(root).resolve();bundle=Path(bundle).resolve();destination=Path(destination or root/'findings')
    destination.mkdir(parents=True,exist_ok=True)
    if not (bundle/'experiment.json').exists():
        if config_file is None:raise ValueError('findings require the exact experiment configuration')
        manifest=json.loads((bundle/'manifest.json').read_text())
        if file_fingerprint(Path(config_file))!=manifest['identity']['config_sha256']:raise ValueError('experiment config fingerprint changed')
        shutil.copyfile(config_file,bundle/'experiment.json')
    config=json.loads((bundle/'experiment.json').read_text());manifest=json.loads((bundle/'manifest.json').read_text())
    expected_config=manifest['identity'].get('config_sha256')
    if expected_config and file_fingerprint(bundle/'experiment.json')!=expected_config:
        raise ValueError('frozen experiment configuration changed')
    cells=json.loads((bundle/'cells.json').read_text())
    if 'artifact_sha256' in manifest and 'cells.json' in manifest['artifact_sha256']:
        if file_fingerprint(bundle/'cells.json')!=manifest['artifact_sha256']['cells.json']:raise ValueError('experiment cell evidence changed')
    expected=manifest['identity']['scenario_sha256']
    if scenario_fingerprint(root/config['scenario_directory'])!=expected:
        raise ValueError('physical input package changed; cannot infer historical bottlenecks from new inputs')
    paths=[]
    for key,cell in sorted(cells.items()):
        pname,sname=key.split('/')
        p=next(p for p in config['portfolios'] if p['name']==pname);s=next(s for s in config['scenarios'] if s['name']==sname)
        if cell['status']!='complete':
            stem=stem_for(config,p);path=destination/(stem+'__'+sname+'__FAILED_'+hashlib.sha256((str(bundle)+str(cell)).encode()).hexdigest()[:10]+'.md')
            text=f'# Failed evaluation: {stem} — {sname}\n\n'+table(['Status','Campaign score','Gross value','Generation/grid hours'],[['REJECTED / INCOMPLETE','Unavailable — not zero','Unavailable','Not accepted as a full matched campaign']])
            text+='\nError: `'+cell.get('error','incomplete campaign')+'`.\n\nNo recommendation or physical zero-allocation conclusion can be drawn from an evaluator failure. '+link(bundle,'source experiment')+'.\n'
            write_note(path,text,{'schema':SCHEMA,'kind':'failed','bundle':str(bundle),'key':key});continue
        paths.append(case_record(root,bundle,config,p,s,cell,destination))
        print(f'Findings {len(paths)}/{sum(c["status"]=="complete" for c in cells.values())}: {paths[-1].name}',flush=True)
    write_strategy_indexes(root,destination)
    return paths


def export_part1(root,directory,destination):
    root=Path(root);directory=Path(directory);destination=Path(destination)
    manifest=json.loads((directory/'manifest.json').read_text());verified=manifest.get('verification_status')=='passed'
    if verified:
        if file_fingerprint(directory/'verification.json')!=manifest['verification_sha256']:raise ValueError('Part 1 verification changed')
        evidence=json.loads((directory/'verification.json').read_text())
        for name,h in evidence['artifact_sha256'].items():
            if file_fingerprint(directory/name)!=h:raise ValueError(f'Part 1 evidence changed: {name}')
    stress=json.loads((directory/'stress.json').read_text());groups=json.loads((directory/'groups.json').read_text())
    validation=json.loads((directory/'validation.json').read_text());interactions=json.loads((directory/'interactions.json').read_text())
    for s in stress['scenarios']:
        candidates=s.get('candidates',{});capacities=[v['minimum_hosting_capacity_mw'] for v in candidates.values()]
        bg=sum(float(mw) for t in s['scenario']['teams'] for _,mw in t['sites'])
        text='# Part 1: '+s['scenario']['name']+'\n\n'+table(['Measurement','Result'],[
            ['Status',s['status']],['Verification','passed' if verified else 'not independently verified'],
            ['Fixed background withdrawal MW',number(bg)],['Candidates',len(candidates)],['Periods',manifest['horizon']],
            ['Minimum residual HC MW',number(min(capacities),6) if capacities else 'N/A'],
            ['Maximum residual HC MW',number(max(capacities),6) if capacities else 'N/A'],
            ['Candidates supporting a full 500 MW',sum(v['full_request_feasible'] for v in candidates.values())],
            ['Game score / IT value / generator runtime','N/A — electrical diagnostic, not a scored game campaign']])
        text+='\nBackground team sites: '+('; '.join(t['team_id']+': '+', '.join(f'{b}={mw:g} MW' for b,mw in t['sites']) for t in s['scenario']['teams']) or 'none')+'.\n'
        text+='\n## Candidate findings\n\n'+table(['Bus','Residual HC MW','Supports 500 MW','Limiting periods','Material signed transmission limits','Resource diagnoses'],[
            [b,number(v['minimum_hosting_capacity_mw'],6),v['full_request_feasible'],', '.join(map(str,v['limiting_periods'])),
             ', '.join(sorted({l['branch_id']+':'+l['direction'] for d in v['diagnoses'] for l in d['tight_lines'] if l['materially_limiting']})) or 'none material',
             ', '.join(sorted({d['limiting_resource'] for d in v['diagnoses']}))] for b,v in sorted(candidates.items())])
        text+='\n## Meaning and limits\n\nThe background is fixed and uncurtailed. This test maximizes additional grid-only demand at one candidate over every operating period. A failure to support 500 MW is not an evaluator failure or a zero game score: the official game may curtail rival requests instead. Shared system generation is recorded separately from transmission groups. A binding line is material here only when the hosting LP has a positive capacity shadow; later game findings add finite line-relief checks at selected recorded snapshots.\n'
        text+='\nOperating-flow observations used periods '+str(stress['operating_periods'])+f' and a {100*stress["near_limit_fraction"]:g}% near-limit threshold. '+link(directory/'stress.json','full stress evidence')+' · '+link(directory/'manifest.json','input/source fingerprints')+'.\n'
        write_note(destination/('Part1_'+s['scenario']['name']+'.md'),text)
    validations={g['group_id']:g for g in validation['overlapping_group_validation']}
    text='# Part 1: grouping and interaction findings\n\n'+table(['Measurement','Result'],[
        ['Candidates',len(groups['system_generation_shared_by'])],['Valid backgrounds',manifest['valid_scenario_count']],
        ['Signed overlapping groups',len(groups['overlapping_groups'])],['Refined PTDF cohorts',len(groups['refined_cohorts'])],
        ['Sampled unordered pairs',len(interactions['pairs'])],['Directional/load tests',len(interactions['records'])],
        ['Campaign score / generator hours','N/A — physical grouping experiment']])
    text+='\n'+table(['Signed group','Members','Evidence status'],[(g['group_id'],', '.join(g['members']),validations[g['group_id']]['status']) for g in groups['overlapping_groups']])
    text+='\nThe groups overlap and depend on loading context. Two buses can share a stressed line despite different standalone bottlenecks. Every bus also shares the system generation ceiling. Cohort count depends on the PTDF distance cutoff, so cohort labels do not prove independent corridors.\n'
    text+='\n'+table(['Added MW','Classification','Within excess/additional MW','Across excess/additional MW','Status'],[
        [q,kind,number(v['within']['mean_excess_per_added_mw'],6),number(v['across']['mean_excess_per_added_mw'],6),v['status']]
        for q,comparisons in validation['comparisons_by_added_load_mw'].items() for kind,v in comparisons.items()])
    text+='\nThese are descriptive comparisons in a deterministic coverage-balanced pair sample; directions and load levels are dependent, not independent statistical replications. Electrical interaction does not establish competitor choice probabilities.\n'
    write_note(destination/'Part1_groups_and_interactions.md',text)
    text='# Part 1: every directional interaction test\n\n'+table(['Measurement','Result'],[
        ['Unordered pairs',len(interactions['pairs'])],['Directional tests',len(interactions['records'])],
        ['Added load levels MW',str(interactions['loads_mw'])],['Minimum shared generation headroom MW',number(interactions['minimum_generation_headroom_mw'],6)],
        ['Game scores / generator hours','N/A — hosting-capacity perturbations']])
    text+='\n'+table(['Source bus','Target bus','Added MW','Baseline HC MW','Residual HC MW','HC lost MW','Generation-forced loss MW','Extra transmission loss MW','Shared signed group'],[
        [r['source_bus'],r['target_bus'],r['added_load_mw'],number(r['baseline_hosting_capacity_mw'],6),number(r['residual_hosting_capacity_mw'],6),
         number(r['capacity_loss_mw'],6),number(r['generation_forced_loss_floor_mw'],6),number(r['transmission_excess_loss_mw'],6),r['shared_signed_bottleneck']]
        for r in interactions['records']])
    text+='\nThe generation-forced floor is separated before interpreting additional transmission competition. These experiments hold the added load fixed; they do not perform official multi-team allocation or score an investment. '+link(directory/'interactions.json','full measurement evidence')+'.\n'
    write_note(destination/'Part1_directional_tests.md',text)


def export_history(root,destination):
    destination=Path(destination);bundles=[root/'analysis/strategy/part2',root/'analysis/strategy/part2-s1-grid-s2-cg']
    histories=[]
    for bundle in bundles:
        if not bundle.exists():continue
        manifest=json.loads((bundle/'manifest.json').read_text())
        recoveries=manifest.get('numerical_recoveries',[])
        if (bundle/'numerical_retries.json').exists():recoveries=json.loads((bundle/'numerical_retries.json').read_text())
        for i,r in enumerate(recoveries):
            key=r.get('key',r.get('campaign'));tag=('scheduled' if 's1-grid' in bundle.name else 'original')
            filename='HISTORY_'+tag+'_'+key.replace('/','__')+'.md'
            failure=r.get('original_failure',r.get('original_failed_cell',{}))
            audit_path=(Path(r['retry_directory'])/'execution.json')
            audit=json.loads(audit_path.read_text()) if audit_path.exists() else {}
            source_archive=Path(r['retry_directory'])/'retry_source.zip'
            text='# Numerical history: '+key+'\n\n'+table(['Item','Finding'],[
                ['Original attempt','Rejected / incomplete; no campaign score assigned'],['Failure',failure.get('error',r.get('reason','see source audit'))],
                ['Accepted retry',r['retry_directory']],['Allocation residues rounded down',len(r.get('adjustments',[]))],
                ['Tiny feasibility-cut corrections',len(r.get('corrected_cuts',[]))],['Exact-balance presolve snapshots',len(r.get('exact_presolve',[]))],
                ['Failed attempt score / generator hours','Unavailable as an accepted complete campaign — not zero']])
            text+='\nA failed numerical solve is not a physically scored zero. The accepted campaign is logged separately and must pass joint dispatch and economic/energy accounting.\n'
            text+='\n## What changed\n\n'+(r.get('method') or 'Requested load, generator capacity, bus allocation, rival requests, line ratings, and generator availability remained fixed. Numerical changes are explicitly recorded below.')+'\n'
            for name in ['adjustments','pruned_zero_generators','corrected_cuts','exact_presolve']:
                data=r.get(name,audit.get(name,[]))
                if data:text+='\n### '+name.replace('_',' ')+'\n\n```json\n'+json.dumps(data,indent=2)+'\n```\n'
            text+='\n'+link(audit_path,'execution audit')+' · '+link(bundle/'manifest.json','accepted experiment manifest')+'.\n'
            if source_archive.exists():text+='\n'+link(source_archive,'executed retry source archive')+'.\n'
            write_note(destination/filename,text);histories.append(filename)
    control=root/'analysis/strategy/part2-s1-grid-s2-cg/repair_control.json'
    if control.exists():
        c=json.loads(control.read_text());text='# Same-input repair control\n\n'+table(['Measurement','Result'],[
            ['Status',c['status']],['Same requested CSVs',c['same_requested_csvs']],['Same carried network',c['same_carried_network']],
            ['Baseline score $B',number(c['baseline_score_usd']/1e9,9)],['Repaired score $B',number(c['repaired_score_usd']/1e9,9)],
            ['Difference USD',number(c['difference_usd'],6)],['Presolved periods',len(c['fixed_periods'])]])
        text+='\nAn already-successful concentrate-at-5413, seven-rival, W3S2 evaluation was repeated with the numerical adapters. The score was unchanged; this is a numerical consistency control, not an additional independent strategy scenario. '+link(control,'control evidence')+'.\n'
        write_note(destination/'CONTROL_same_input_numerical_repair.md',text)
    # Preserve the two exploratory campaigns, outside the primary comparisons.
    template_path = root/'analysis/strategy/part2/experiment.json'
    if not template_path.exists():return
    template=json.loads(template_path.read_text())
    for probe in sorted((root/'runs').glob('part2-probe-*')):
        if not (probe/'campaign.json').exists():continue
        result=json.loads((probe/'campaign.json').read_text())
        if result.get('status')!='complete' or len(result.get('rounds',[]))!=4:continue
        p_rows=[];opponents=[];first=result['rounds'][0]['round']
        for path in sorted((probe/first/'inputs').glob('*.csv')):
            rows=csv_data(path.read_bytes())
            if rows and rows[0]['team_id']=='our-team':p_rows=rows
            elif rows:opponents.extend(rows)
        if not p_rows:continue
        p={'name':probe.name,'bus_ids':[r['bus_id'] for r in p_rows],
           'weights':[float(r['connection_capacity_mw'])/500. for r in p_rows],
           'generator_fraction':sum(float(r['generator_capacity_mw']) for r in p_rows)/500.,'role':'primary'}
        scenario={'name':re.sub(r'[^a-zA-Z0-9_-]','_',result['scenario']),'rival_bus_ids':[r['bus_id'] for r in opponents],
            'rival_generator_fraction':(float(opponents[0]['generator_capacity_mw'])/float(opponents[0]['connection_capacity_mw']) if opponents else 0.),'include_in_risk':False}
        config={**template,'portfolios':[p],'scenarios':[scenario]}
        bundle=root/'runs/findings-diagnostics/probe-bundles'/probe.name;bundle.mkdir(parents=True,exist_ok=True)
        save_json(bundle/'experiment.json',config);save_json(bundle/'manifest.json',{'status':'complete','provenance':'posthoc exploratory probe'})
        cell={'status':'complete','output':str(probe),'result':result,
              'artifact_sha256':{str(f.relative_to(probe)):file_fingerprint(f) for f in probe.rglob('*') if f.is_file()}}
        case_record(root,bundle,config,p,scenario,cell,destination,exploratory=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bundle',action='append',type=Path)
    parser.add_argument('--destination',type=Path,default=ROOT/'findings')
    args=parser.parse_args()
    bundles=args.bundle or [p for p in (ROOT/'analysis/strategy/ten-teams-500mw', ROOT/'analysis/strategy/part2',
                                       ROOT/'analysis/strategy/part2-s1-grid-s2-cg') if p.is_dir()]
    for bundle in bundles:export_findings(bundle,root=ROOT,destination=args.destination)
    export_part1(ROOT,ROOT/'analysis/clustering/part1',args.destination)
    export_history(ROOT,args.destination)
    from .findings_history import export_earlier_runs
    export_earlier_runs(ROOT,args.destination)
    write_strategy_indexes(ROOT,args.destination)
    print(f'Findings ready: {args.destination/"README.md"}',flush=True)


if __name__=='__main__':main()
