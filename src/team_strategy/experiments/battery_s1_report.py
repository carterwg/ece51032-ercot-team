"""Verify storage operation and write the S1 sizing findings."""
import argparse
from collections import defaultdict
import csv
import json
import math
from pathlib import Path

from ercot_game.csv_submission import STORAGE_DURATION_HOURS

from ..context import file_fingerprint, scenario_fingerprint
from ..evaluation.campaign import save_json
from .battery_s1 import BUS, CAPACITY_MW, FIELDS, RIVAL_STORAGE_SEED, ROOT, challenge_fields, read, rival_storage_fields
from .findings import (checked_bytes, csv_data, link, native_profiles, number, summarize_energy, table,
                       write_note, write_strategy_indexes)

EPS_MW = 1e-4
ACTIVE_MW = 1e-5


def storage_trace(series, power, energy, day_length=24, step=1.):
    """Reconstruct end-of-hour SOC from independent charge and discharge evidence."""
    if len(series) % day_length:
        raise ValueError('Battery trace must cover complete representative days')
    states, days = [], []
    for start in range(0,len(series),day_length):
        half = energy/2
        soc, low, high, charge, discharge = half,half,half,0.,0.
        for row in series[start:start+day_length]:
            into, out = row['charge'],row['discharge']
            if min(into,out) < -EPS_MW or max(into,out) > power+EPS_MW:
                raise ValueError('Recorded battery power exceeds allocated bounds')
            if out*step > soc+EPS_MW:
                raise ValueError('Battery discharged more energy than it held')
            soc += (into-out)*step
            if not -EPS_MW <= soc <= energy+EPS_MW:
                raise ValueError('Recorded battery SOC exceeds allocated bounds')
            low,high = min(low,soc),max(high,soc)
            charge,discharge = charge+into*step,discharge+out*step
            states.append(soc)
        if abs(soc-half)>EPS_MW:
            raise ValueError('Battery did not return to half full at the daily boundary')
        days.append({'day':start//day_length+1,'start_mwh':half,'end_mwh':soc,'min_mwh':low,'max_mwh':high,
                     'charged_mwh':charge,'discharged_mwh':discharge})
    return states, days


def verify_requests(output, name, artifact_hashes, request_hashes, sizes, field, *, s1_bus=BUS):
    rivals = field['rival_plan']
    submission = name[-1]
    csv_paths = sorted((output/name/'inputs').glob('*.csv'))
    owners = set()
    requests = {}
    for path in csv_paths:
        relative = str(path.relative_to(output))
        rows = csv_data(checked_bytes(output,relative,artifact_hashes))
        team, = {r['team_id'] for r in rows}
        if team in owners or artifact_hashes[relative] != request_hashes[team]:
            raise ValueError('Input CSVs differ from the evaluated roster')
        owners.add(team)
        if team=='our-team':
            generation,power = sizes if submission=='1' else (CAPACITY_MW,0)
            bus = s1_bus if submission == '1' else BUS
            expected = {bus:(CAPACITY_MW,generation,power,power*STORAGE_DURATION_HOURS)}
        else:
            power = rivals.get('storage_power_schedule', {}).get(submission, 0.)
            expected = {b:(CAPACITY_MW*w,CAPACITY_MW*w*rivals['generation_schedule'][submission],
                           power*w,power*w*STORAGE_DURATION_HOURS)
                        for b,w in zip(rivals['bus_ids'],rivals['weights'],strict=True)}
        if len(rows)!=len(expected) or {r['bus_id'] for r in rows}!=expected.keys():
            raise ValueError('Input site layout differs from the matched case')
        columns = ('connection_capacity_mw','generator_capacity_mw','storage_power_mw','storage_energy_mwh')
        for row in rows:
            if any(abs(float(row[column])-value)>1e-8
                   for column,value in zip(columns,expected[row['bus_id']],strict=True)):
                raise ValueError('Input resources differ from the specified case')
            requests[team,row['site_id']] = expected[row['bus_id']]
    teams = {'our-team'}|{f'rival-{i:02d}' for i in range(1,10)}
    if teams != owners:
        raise ValueError('Expected all ten teams in each evaluated round')
    return requests


def verify_rival_storage(ledger, requests, weights):
    """Check battery schedules at the capacities each rival site was awarded."""
    sites = defaultdict(list)
    for row in ledger:
        key = row['team_id'],row['site_id']
        if key[0]!='our-team':
            sites[key].append(row)
    total_charge = total_discharge = total_power = 0.
    hourly_charge = [0.]*len(weights)
    hourly_discharge = [0.]*len(weights)
    checked = 0
    for key, (connection, _, power, energy) in requests.items():
        if key[0]=='our-team' or power==0:
            continue
        site = sorted(sites[key],key=lambda row:int(row['period_index']))
        if [int(row['period_index']) for row in site]!=list(range(len(weights))):
            raise ValueError(f'Incomplete rival battery ledger for {key}')
        admitted = float(site[0]['load_mw'])
        if admitted < -EPS_MW or admitted > connection+EPS_MW or any(
                abs(float(row['load_mw'])-admitted)>EPS_MW for row in site):
            raise ValueError(f'Invalid rival site allocation for {key}')
        fraction = admitted/connection
        series = [{'charge':float(row['storage_charge_mw']), 'discharge':float(row['storage_discharge_mw'])}
                  for row in site]
        storage_trace(series, power*fraction, energy*fraction)
        total_power += power*fraction
        for i, (row, weight) in enumerate(zip(series, weights, strict=True)):
            total_charge += row['charge']*weight
            total_discharge += row['discharge']*weight
            hourly_charge[i] += row['charge']
            hourly_discharge[i] += row['discharge']
        checked += 1
    return {'verified_sites':checked,'allocated_power_mw':total_power,
            'annual_charged_mwh':total_charge,'annual_discharged_mwh':total_discharge,
            'hourly_charge_mw':hourly_charge,'hourly_discharge_mw':hourly_discharge}


def analyze_round(result, round_result, config, field, rates, ratings):
    name = round_result['round']
    output = Path(result['output'])
    hashes = result['artifact_sha256']
    if json.loads(checked_bytes(output,name+'/round.json',hashes))!=round_result:
        raise ValueError('Round summary changed')
    requests = verify_requests(output,name,hashes,round_result['input_sha256_by_team'],result['sizes'],field,
                               s1_bus=result.get('s1_bus', BUS))
    ev = read_evaluation(output,name,hashes)
    if len(round_result['team_scores'])!=10 or len(ev['team_scores'])!=10 or round_result['horizon']!=120:
        raise ValueError('Expected 120 periods of scores and all ten teams')
    breakdown = round_result['score_breakdown']
    if not math.isclose(breakdown['it_value_usd']-sum(v for k,v in breakdown.items() if k!='it_value_usd'),
                        round_result['score_usd'],rel_tol=0,abs_tol=.02):
        raise ValueError('Economic components fail to reconcile')
    if round_result['rules_sha256'] != file_fingerprint(ROOT/config['rules_file']):
        raise ValueError('Round economic rules changed')
    generation,power = result['sizes'] if name.endswith('1') else (CAPACITY_MW,0)
    fraction = round_result['service_fraction']
    if abs(breakdown['storage_capital_cost_usd'] - fraction*power*(rates['storage_capital_cost_per_mw']+
           STORAGE_DURATION_HOURS*rates['storage_capital_cost_per_mwh']))>.05:
        raise ValueError('Storage capital differs from allocated MW and MWh')
    weights = [weight/rates['present_value_annuity_factor'] for weight in rates['period_weight_hours']]
    ledger = csv_data(checked_bytes(output,name+'/canonical/site_net_withdrawal.csv',hashes))
    rival_storage = verify_rival_storage(ledger,requests,weights)
    metrics = summarize_energy(ledger,weights,120,1.)
    if len([r for r in ledger if r['team_id']=='our-team']) !=120:
        raise ValueError('Each of our 120 hours must have one site ledger row')
    series = metrics['series']
    if any(abs(row['load']-CAPACITY_MW*fraction)>EPS_MW for row in series):
        raise ValueError('The hourly load differs from the firm admission')
    if any(row['generation'] > generation*fraction+EPS_MW for row in series):
        raise ValueError('Generation exceeds the allocated label')
    states, days = storage_trace(series,power*fraction,power*fraction*STORAGE_DURATION_HOURS)
    all_grid = defaultdict(float)
    for row in ledger:
        all_grid[int(row['period_index'])] += float(row['net_withdrawal_mw'])
    network = ROOT/config['scenario_directory'] if name.endswith('1') else output/f'week-{name[5]}-s2-base'
    headroom = native_profiles(str(network))
    flows = ev['aggregate_diagnostics']['binding_diagnostics_by_period']
    if set(flows)!={str(i) for i in range(120)}:
        raise ValueError('Missing flow evidence')
    own_score = next(s for s in round_result['team_scores'] if s['team_id']=='our-team')
    field_mw = sum(t['served_load_mwh'] for t in round_result['team_scores'])/sum(weights)
    if abs(metrics['annual_energy_mwh']['load']-own_score['served_load_mwh'])>1.:
        raise ValueError('Served load does not match the hourly energy ledger')
    for i,row in enumerate(series):
        binding = []
        for branch,flow in flows[str(i)]['flow_mw_by_branch'].items():
            if branch in ratings:
                margin = ratings[branch]-abs(flow)
                if margin < -EPS_MW:
                    raise ValueError(f'Line {branch} exceeds the recorded limit')
                if margin <= EPS_MW:
                    binding.append(branch+(':upper' if flow>=0 else ':lower'))
        row.update({'soc_mwh':states[i], 'tight_lines':sorted(binding), 'remaining_native_mw':headroom[i]-all_grid[i]})
    return {'name':name,'admitted_mw':CAPACITY_MW*fraction,'field_mw':field_mw,'score_usd':round_result['score_usd'],
            'rival_storage':rival_storage,
            'scope':round_result['competition_scope'],'costs':breakdown,'energy':metrics['annual_energy_mwh'],
            'annual_generator_hours':metrics['annual_generator_hours'], 'generator_periods':metrics['generator_active_periods'],
            'battery_discharge_hours':math.fsum(weights[i] for i,r in enumerate(series) if r['discharge']>ACTIVE_MW),
            'battery_charge_hours':math.fsum(weights[i] for i,r in enumerate(series) if r['charge']>ACTIVE_MW),
            'battery_discharge_periods':sum(r['discharge']>ACTIVE_MW for r in series),
            'battery_charge_periods':sum(r['charge']>ACTIVE_MW for r in series),
            'peak_generator_mw':max(r['generation'] for r in series),'peak_discharge_mw':max(r['discharge'] for r in series),
            'peak_charge_mw':max(r['charge'] for r in series), 'minimum_native_spare_mw':min(r['remaining_native_mw'] for r in series),
            'days':days,'series':series}


def read_evaluation(output,name,hashes):
    evaluation = json.loads(checked_bytes(output,name+'/canonical/evaluation.json',hashes))
    if evaluation['competition_scope'] not in {'joint','joint_projection'}:
        raise ValueError('Only the joint ten-team cases qualify')
    return evaluation


def render_case(entry, destination, field):
    g,p = entry['sizes']
    s1_bus = entry.get('s1_bus', BUS)
    suffix = '' if s1_bus == BUS else f'_bus{s1_bus}'
    name = f"Battery_S1_G{g}_P{p}{suffix}__{entry['field']}"
    if entry['phase']=='campaign': name+='_campaign'
    path=destination/(name+'.md')
    if entry['status']!='complete':
        write_note(path,f'# {name}\n\n'+table(['Status','Evidence'],[
            [a['error'],link(a['log'],'Attempt log')] for a in entry['prior_attempts']]))
        return path
    rounds = entry['metrics']
    dollars = lambda amount: number(amount/1e9,6)
    text = f'# 500 MW at bus {s1_bus}, S1 generator {g} MW and battery {p} MW / {4*p} MWh\n\n'
    text += table(['Round','Our admitted MW','All teams admitted MW','Net score $B','IT value $B','Grid cost $B',
                   'Generator fuel $B','Generator capital $B','Battery capital $B'],[
        [r['name'],number(r['admitted_mw'],6),number(r['field_mw'],6),dollars(r['score_usd']),
         *[dollars(r['costs'][k]) for k in ('it_value_usd','grid_energy_cost_usd','generator_operating_cost_usd',
                                           'generator_capital_cost_usd','storage_capital_cost_usd')]] for r in rounds])
    text += '\n'+table(['Round','Grid purchased MWh/yr','Generator MWh/yr','Battery charged MWh/yr',
                          'Battery discharged MWh/yr','Gen on h/yr','Discharge h/yr','Charge h/yr'],[
        [r['name'],*[number(r['energy'][k]) for k in ('grid','generation','charge','discharge')],
         number(r['annual_generator_hours']),number(r['battery_discharge_hours']),number(r['battery_charge_hours'])] for r in rounds])
    if len(rounds)==4:
        text+=f"\nFour-round score **${dollars(entry['campaign_score_usd'])}B**. S2 uses a new 500 MW site with 500 MW generation at bus 6141 after carrying all teams’ actual S1 net withdrawals.\n"
    text += '\nBattery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.\n'
    rival = field['rival_plan']
    rival_power = rival.get('storage_power_schedule', {}).get('1',0.)
    if rival_power:
        buses = ', '.join(rival['bus_ids'])
        rival_generation = CAPACITY_MW*rival['generation_schedule']['1']
        text += (f'\nEach of the nine rivals requests 500 MW split equally across {buses}, with {rival_generation:g} MW '
                 f'of S1 generation and {rival_power:g} MW / {rival_power*STORAGE_DURATION_HOURS:g} MWh of S1 storage. '
                 'The recorded S1 battery cycles were checked site by site.\n\n')
        text += table(['Round','Rival battery sites checked','Rival storage admitted MW','Rival batteries charged MWh/yr',
                       'Rival batteries discharged MWh/yr'],[
            [r['name'],r['rival_storage']['verified_sites'],number(r['rival_storage']['allocated_power_mw']),
             number(r['rival_storage']['annual_charged_mwh']),number(r['rival_storage']['annual_discharged_mwh'])]
            for r in rounds])
    for r in rounds:
        text += f"\n## {r['name']} dispatch\n\n"
        if r['name'].endswith('1') and p:
            text+=table(['Day','Start SOC MWh','End SOC MWh','Minimum SOC MWh','Maximum SOC MWh','Charged MWh','Discharged MWh'],[
                [d['day'],*[number(d[k]) for k in ('start_mwh','end_mwh','min_mwh','max_mwh','charged_mwh','discharged_mwh')]] for d in r['days']])+'\n'
        indices = set(range(104,115))|{min(range(120),key=lambda i:r['series'][i]['remaining_native_mw'])}
        if r['name'].endswith('1'):
            for key in ('generation','charge','discharge'):
                idx = max(range(120),key=lambda i:r['series'][i][key])
                if r['series'][idx][key]>ACTIVE_MW: indices.add(idx)
        rival_headers = ['Rival charge MW','Rival discharge MW'] if rival_power else []
        text+=table(['Hour','Grid MW','Our generator MW','Charge MW','Discharge MW','End SOC MWh',
                     *rival_headers,'All-team spare native generation MW','Binding lines'],[
            [i,*[number(r['series'][i][k],6) for k in ('grid','generation','charge','discharge','soc_mwh')],
             *[number(r['rival_storage'][key][i],6) for key in ('hourly_charge_mw','hourly_discharge_mw') if rival_power],
             number(r['series'][i]['remaining_native_mw'],6),
             ', '.join(r['series'][i]['tight_lines']) or 'none'] for i in sorted(indices)])
        text+='\nThe hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.\n'
    text+='\n'+link(Path(entry['output']).parent/'result.json','Full result')+' · '+link(entry['execution'],'Solver audit')+'\n'
    if entry['prior_attempts']:
        text+='\n'+table(['Earlier attempt','Evidence'],[[a['error'],link(a['log'],'Evaluation log')] for a in entry['prior_attempts']])
    write_note(path,text)
    return path


def report(run, summary, destination):
    config = read(ROOT/FIELDS)
    rates = read(ROOT/config['rules_file'])
    base = ROOT/config['scenario_directory']
    identity = read(run/'manifest.json')
    if identity['scenario_sha256'] != scenario_fingerprint(base) or identity['rules_sha256'] != file_fingerprint(ROOT/config['rules_file']):
        raise ValueError('Saved experiment uses a different physical or economic input')
    fields = {s['name']:s for s in (config['scenarios'] + challenge_fields(config) + rival_storage_fields(config)
                                    + rival_storage_fields(config, randomized=True))}
    with (base/'branch_limits.csv').open(newline='') as handle:
        ratings = {r['branch_id']:float(r['thermal_limit_mva']) for r in csv.DictReader(handle) if r['status']=='1'}
    entries = []
    for phase in ('sweep','stress','refined','campaign','stress_campaign','finalists','rival_storage','rival_storage_campaign',
                  'rival_storage_sizing_campaign','rival_storage_randomized'):
        path = run/f'{phase}.json'
        if not path.exists(): continue
        for key, result in sorted(read(path).items()):
            field = fields[result['field']]
            if result['status']=='complete':
                rounds = [analyze_round(result,r,config,field,rates,ratings) for r in result['rounds']]
                if result['phase']=='campaign':
                    if len(rounds)!=4 or abs(sum(r['score_usd'] for r in rounds)-result['campaign_score_usd'])>.02:
                        raise ValueError('Invalid four-round score')
                    for carry in result['carryovers']:
                        network = Path(result['output'])/f"week-{carry['week']}-s2-base"
                        if (carry['carried_scenario_sha256']!=scenario_fingerprint(network) or len(carry['team_ids'])!=10
                            or carry['validation']['passed_period_count']!=120):
                            raise ValueError('Missing validated ten-team carryover')
                entry = {**result,'metrics':rounds}
            else:
                entry = dict(result)
            entry['finding'] = str(render_case(entry,destination,field))
            entries.append(entry)
            print(f'Logged {phase} {key}',flush=True)
    summary.mkdir(parents=True,exist_ok=True)
    save_json(summary/'summary.json',{'identity':identity,'entries':[
        {k:v for k,v in e.items() if k not in {'artifact_sha256','rounds'} and k!='metrics'} |
        {'metrics':[{k:v for k,v in r.items() if k!='series'} for r in e.get('metrics',[])]} for e in entries]})
    write_comparison(entries,fields,config,rates,destination)
    write_strategy_indexes(ROOT,destination)


def write_comparison(entries, fields, config, rates, destination):
    generator_rate = rates['generator_capital_cost_per_mw']/1e6
    storage_rate = (rates['storage_capital_cost_per_mw'] + STORAGE_DURATION_HOURS*rates['storage_capital_cost_per_mwh'])/1e6

    def equipment_capital(sizes):
        generation, storage = sizes
        return generator_rate*generation + storage_rate*storage

    random_fields = {name for name, field in fields.items() if 'rival_storage_seed' in field}
    benchmark_fields = [name for name in fields if name not in random_fields]
    matched = defaultdict(dict)
    for e in entries:
        if e['field'] in random_fields:
            continue
        if e['phase']=='sweep':
            matched[tuple(e['sizes'])][e['field']] = e
        elif e['status']=='complete':
            first = next(r for r in e['metrics'] if r['name']=='week-3-submission-1')
            matched[tuple(e['sizes'])].setdefault(e['field'],{**e,'metrics':[first]})
    original = [s['name'] for s in config['scenarios']]
    with_storage = [name for name in benchmark_fields if fields[name]['rival_plan'].get('storage_power_schedule')]
    storage_cases = [name for name in with_storage if any(e['field']==name for e in entries)]
    prior_fields = [name for name in benchmark_fields if name not in with_storage]
    all_fields = prior_fields+storage_cases
    text='# S1 battery and generator sizing at bus 6141\n\n'
    rows=[]
    for (g,p),cases in sorted(matched.items()):
        row=[g,p,4*p,number(equipment_capital((g,p)),2)]
        for field in all_fields:
            case = cases.get(field)
            if case and case['status']=='complete':
                row.append(link(case['finding'],number(case['metrics'][0]['admitted_mw'],3)))
            elif case:
                row.append(link(case['finding'],'Unresolved'))
            else:
                row.append('—')
        rows.append(row)
    text += table(['S1 generator MW','Battery MW','Battery MWh','Full-build private capital $M',*all_fields],rows)
    text += '\nField columns report **our firm W3S1 admission in MW**. Links open the score, energy, charge trace and line limits for each case. The four original fields reproduce the prior ten-team experiment. Later fields add rival generation or storage. All cases use ten 500 MW requests.\n'
    for label,field_names in [('original',original),('seven fields with no rival storage',prior_fields),
                              *([(f'expanded {len(all_fields)}',all_fields)] if len(all_fields)>len(prior_fields) else [])]:
        full = [(g,p) for (g,p),cases in matched.items() if all(
            cases.get(field,{}).get('status')=='complete' and cases[field]['metrics'][0]['admitted_mw']>=CAPACITY_MW-EPS_MW
            for field in field_names)]
        if full:
            g,p=min(full,key=lambda x:(equipment_capital(x),x))
            text+=f'\nThe lowest equipment capital among tested plans with full S1 admission across the {label} fields is **{g} MW generation and {p} MW / {4*p} MWh of storage** at **${equipment_capital((g,p)):g}M**.\n'
    random_entries = [entry for entry in entries if entry['field'] in random_fields]
    if random_entries:
        text += '\n## Randomized rival equipment in S1\n\n'
        text += (f'Generator and battery power were drawn in 5 MW increments from preset bands using seed `{RIVAL_STORAGE_SEED}`. '
                 'Each field has nine identical 500 MW rival requests. The table lists total equipment per rival. '
                 'Multi-site rivals split their requests and equipment equally across the listed buses.\n\n')
        random_rows = []
        for entry in sorted(random_entries, key=lambda e: (e['sizes'], e['field'])):
            rival = fields[entry['field']]['rival_plan']
            gen = CAPACITY_MW * rival['generation_schedule']['1']
            power = rival['storage_power_schedule']['1']
            metrics = entry['metrics'][0] if entry['status']=='complete' else None
            random_rows.append([link(entry['finding'], entry['field'].rsplit('_', 1)[1]), *entry['sizes'],
                                ', '.join(rival['bus_ids']), f'{gen:g}', power, STORAGE_DURATION_HOURS * power,
                                *([number(metrics['admitted_mw'], 6), number(metrics['field_mw'], 6),
                                   number(metrics['score_usd']/1e9, 6)] if metrics else ['Unresolved', '—', '—'])])
        text += table(['Case', 'Our gen MW', 'Our battery MW', 'Rival buses', 'Rival gen MW', 'Rival battery MW',
                       'Rival battery MWh', 'Our S1 award MW', 'Field S1 award MW', 'S1 score $B'], random_rows)
    base = ROOT/config['scenario_directory']
    headroom = native_profiles(str(base))
    short = [i for i,h in enumerate(headroom) if h<5000]
    weights = [p/rates['present_value_annuity_factor'] for p in rates['period_weight_hours']]
    text += '\n## Seven-hour hypothesis\n\n'
    text += f'The native grid falls below the full 5,000 MW field request in hours **{", ".join(map(str,short))}**, representing {sum(weights[i] for i in short):.0f} hours per year. The largest field deficit is **{5000-min(headroom):,.3f} MW**, before transmission limits. These are aggregate hours at full requested load. Actual dispatch follows the evaluator’s joint allocation and charging.\n\n'
    text += table(['Hour','Native spare MW','Shortfall for the full field MW'],[[i,number(headroom[i]),number(5000-headroom[i])] for i in short])
    text += (f'\nA four-hour battery costs ${storage_rate:g}M per MW and a generator costs ${generator_rate:g}M per MW. '
             'Every day starts and ends at 50% SOC. The battery shifts energy from hours with headroom and its grid '
             'charging also becomes part of S1 carryover into S2.\n')
    do_same_bus = read(ROOT/config['part1_directory']/'baseline.json')
    hosting = next(r['capacity_by_period_mw'] for r in do_same_bus if r['bus_id']==BUS)
    same_bus_import = min(hosting)
    support = 5000-9*(200)-same_bus_import
    text += (f'\nWith nine 200 MW generators at bus {BUS}, serving the entire field at that bus would still require '
             f'**{support:,.3f} MW of our own backup** at the tightest hour. Each rival can cut its grid draw to 300 MW '
             f'and the standalone line-limited grid envelope is {same_bus_import:,.3f} MW. The joint allocation '
             'can also reduce rival awards, which is why this fixed-full-field bound is paired with observed admission.\n')
    fixed_field_deficits = [(i,5000-9*200-value) for i,value in enumerate(hosting) if value < 5000-9*200]
    text += '\n'+table(['Hour','Minimum own backup MW with all rivals at full load and maximum generation'],
                         [[i,number(value,3)] for i,value in fixed_field_deficits])
    text += (f'\nThose deficits add up to **{sum(value for _,value in fixed_field_deficits):,.3f} MWh**. '
             'That energy requirement fits in a 784 MWh battery. Power at the worst hour, the timing of recharging, '
             'and the rest of the daily dispatch still determine whether the evaluator admits the site.\n')
    if storage_cases:
        text += '\n## Rival battery fields\n\n'
        text += table(['Field','Buses for each rival','S1 generator MW','S1 battery MW','S1 battery MWh'],[
            [name,', '.join(r['bus_ids']),number(500*r['generation_schedule']['1'],0),
             number(r['storage_power_schedule']['1'],0),number(STORAGE_DURATION_HOURS*r['storage_power_schedule']['1'],0)]
            for name in storage_cases for r in [fields[name]['rival_plan']]])
        text += ('\nAll nine rivals in a field use the same plan, with equal shares of their 500 MW load, '
                 'generation and battery across the buses. In S2 they add new 500 MW C = G sites with zero new storage. '
                 'All S1 battery charging and discharging carry forward through the hourly grid withdrawals.\n')
        if 'nine_b196_at_6141' in storage_cases:
            deficit = math.fsum(5000-hosting[i] for i in short)
            peak_only_award = 500*same_bus_import/(10*(500-196))
            interval_award = 500*math.fsum(hosting[i] for i in short)/(10*(len(short)*500-784))
            text += (f'\nWhen all ten sites at bus 6141 use 196 MW / 784 MWh batteries and zero generation, '
                     f'full admission would require at least **{deficit:,.1f} MWh** of net discharge during periods '
                     '106–112. Their combined energy capacity is **7,840 MWh**. Each battery could start that '
                     'interval full and the field would still fall short. With equal awards and proportional '
                     f'scaling of the batteries, the peak hour alone puts an upper bound of **{peak_only_award:.2f} MW** '
                     f'per team. The seven-hour energy balance tightens that bound to **{interval_award:.2f} MW**.\n')
        if 'nine_g75_b125_at_6141' in storage_cases:
            grid_before_storage = 5000-9*75
            peak = grid_before_storage-same_bus_import
            energy = math.fsum(grid_before_storage-hosting[i] for i in short)
            text += (f'\nWhen our plan is 196 MW / 784 MWh with zero generation and the nine same-bus rivals '
                     f'each bring 75 MW generation plus 125 MW / 500 MWh of storage, serving all ten requests '
                     f'would take **{peak:,.1f} MW** of discharge at the tightest hour. Their combined discharge '
                     f'power is **1,321 MW**. Over periods 106–112, even with rival generators at maximum output, '
                     f'the field would need **{energy:,.1f} MWh** of net discharge and the batteries can hold '
                     '**5,284 MWh**. This is also an energy shortfall.\n')
    text += '\n## S1 operating economics\n\n'
    text += table(['Generator MW','Battery MW','Opponent field','W3S1 score $B','Gen MWh/yr','Battery discharge MWh/yr',
                   'Maximum battery discharge MW','Minimum spare native MW'],[
        [g,p,link(e['finding'],field),number(r['score_usd']/1e9,6),number(r['energy']['generation']),
         number(r['energy']['discharge']),number(r['peak_discharge_mw']),number(r['minimum_native_spare_mw'],6)]
        for (g,p),cases in sorted(matched.items()) for field,e in sorted(cases.items()) if e['status']=='complete'
        for r in e['metrics'][:1]])
    campaigns = defaultdict(dict)
    for e in entries:
        if e['phase']=='campaign': campaigns[tuple(e['sizes'])][e['field']]=e
    if campaigns:
        text+='\n## Four-round follow-through with 500 MW S2 generation\n\n'
        campaign_rows=[]
        for (g,p),cases in sorted(campaigns.items()):
            for field,e in sorted(cases.items()):
                if e['status']=='complete':
                    s1=min(r['admitted_mw'] for r in e['metrics'] if r['name'].endswith('1'))
                    s2=min(r['admitted_mw'] for r in e['metrics'] if r['name'].endswith('2'))
                    s1score=sum(r['score_usd'] for r in e['metrics'] if r['name'].endswith('1'))
                    campaign_rows.append([g,p,link(e['finding'],field),number(s1,6),number(s2,6),
                                          number(s1score/1e9,6),number(e['campaign_score_usd']/1e9,6)])
                else: campaign_rows.append([g,p,link(e['finding'],field),'Unresolved','—','—','—'])
        text+=table(['S1 G MW','S1 P MW','Field','Minimum S1 MW','Minimum S2 MW','S1 scores $B','Campaign score $B'],campaign_rows)
        groups = [('Original four fields',original),('Seven fields with no rival storage',prior_fields)]
        if storage_cases:
            groups += [('Fields with rival storage',storage_cases),('All tested fields',all_fields)]
        for label, names in groups:
            aggregate=[]
            for (g,p),cases in sorted(campaigns.items()):
                if not all(cases.get(field,{}).get('status')=='complete' for field in names):
                    continue
                scores = [cases[field]['campaign_score_usd'] for field in names]
                s1loads = [r['admitted_mw'] for field in names for r in cases[field]['metrics'] if r['name'].endswith('1')]
                s2loads = [r['admitted_mw'] for field in names for r in cases[field]['metrics'] if r['name'].endswith('2')]
                aggregate.append([g,p,number(sum(scores)/len(scores)/1e9,6),number(min(scores)/1e9,6),
                                  number(min(s1loads),6),number(min(s2loads),6)])
            if aggregate:
                text+=f'\n### {label}\n\n'+table(['S1 G MW','S1 Battery MW','Mean score $B','Worst score $B',
                                                      'Minimum S1 admitted MW','Minimum S2 admitted MW'],aggregate)
    write_note(destination/'Battery_S1_comparison.md',text)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run',type=Path,default=ROOT/'runs/battery-s1-500mw')
    parser.add_argument('--summary',type=Path,default=ROOT/'analysis/strategy/battery-s1-500mw')
    parser.add_argument('--findings',type=Path,default=ROOT/'findings')
    options=parser.parse_args()
    report(options.run,options.summary,options.findings)
