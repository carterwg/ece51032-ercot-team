"""Verify the ten-team matrix, write a comparison, and record each campaign."""
import argparse
from collections import defaultdict
import csv
import math
from pathlib import Path
import shutil

from ..context import file_fingerprint
from ..evaluation.campaign import save_json
from .findings import (csv_data, export_findings, link, native_profiles, number, read_record,
                       table, write_note, write_strategy_indexes)
from .pool_comparisons import verify_matrix
from .ten_teams import ROOT, read


def validate_requests(config, cells):
    portfolios = {p['name']: p for p in config['portfolios']}
    scenarios = {s['name']: s for s in config['scenarios']}
    expected_teams = {'our-team'} | {f'rival-{i:02d}' for i in range(1, 10)}
    matched = {}
    for key, cell in cells.items():
        if cell['status'] != 'complete':
            continue
        our_name, field = key.split('/')
        portfolio, scenario = portfolios[our_name], scenarios[field]
        if cell.get('execution_audit') and file_fingerprint(Path(cell['execution_audit'])) != cell['execution_audit_sha256']:
            raise ValueError(f'Execution audit changed for {key}')
        if cell['result']['generation_schedule'] != portfolio['generation_schedule']:
            raise ValueError(f'Generation schedule mismatch in {key}')
        for r in cell['result']['rounds']:
            round_name = r['round']
            submission = round_name[-1]
            inputs = Path(cell['output']) / round_name / 'inputs'
            owners = set()
            rivals = {}
            for csv_file in sorted(inputs.glob('*.csv')):
                rows = csv_data(csv_file.read_bytes())
                owner, = {row['team_id'] for row in rows}
                if owner in owners or file_fingerprint(csv_file) != r['input_sha256_by_team'][owner]:
                    raise ValueError(f'Duplicate or altered input for {owner} in {key}/{round_name}')
                owners.add(owner)
                spec = portfolio if owner == 'our-team' else scenario['rival_plan']
                if owner != 'our-team':
                    rivals[owner] = tuple(sorted(tuple((k,float(v) if k.endswith(('_mw','_mwh')) else v)
                                                      for k,v in row.items() if k not in {'team_id','site_id'})
                                                  for row in rows))
                sites = dict(zip(spec['bus_ids'], spec['weights'], strict=True))
                if len(rows) != len(sites) or {x['bus_id'] for x in rows} != sites.keys():
                    raise ValueError(f'Unexpected site geometry for {owner} in {key}/{round_name}')
                for row in rows:
                    demand = 500 * sites[row['bus_id']]
                    generation = demand * spec['generation_schedule'][submission]
                    if (not math.isclose(float(row['connection_capacity_mw']), demand, abs_tol=1e-8)
                            or not math.isclose(float(row['generator_capacity_mw']), generation, abs_tol=1e-8)
                            or float(row['storage_power_mw']) != 0 or float(row['storage_energy_mwh']) != 0):
                        raise ValueError(f'Wrong requested resources for {owner} in {key}/{round_name}')
            if owners != expected_teams or {x['team_id'] for x in r['team_scores']} != expected_teams:
                raise ValueError(f'Expected ten requesting and scored teams in {key}/{round_name}')
            if matched.setdefault((field, round_name), rivals) != rivals:
                raise ValueError(f'Rival submissions differ across portfolios in {field}/{round_name}')
    return len(matched)


def aggregate(portfolio, cases, scenario_count):
    details = [r for case in cases for r in case['details']]
    first = [r for r in details if r['round'].endswith('1')]
    second = [r for r in details if r['round'].endswith('2')]
    scores = [case['score_usd'] for case in cases]
    return {'portfolio': portfolio['name'], 'count': len(cases), 'complete': len(cases) == scenario_count,
            'mean_usd': math.fsum(scores)/len(scores) if scores else None,
            'worst_usd': min(scores, default=None),
            's1_min_mw': min((r['allocated_load_mw'] for r in first), default=None),
            's2_min_mw': min((r['allocated_load_mw'] for r in second), default=None),
            's1_required_h_max': max((r['annual_required_generator_hours'] for r in first), default=None),
            's2_required_h_max': max((r['annual_required_generator_hours'] for r in second), default=None)}


def summarize(config, cells, records, destination, identity):
    specs = {p['name']: p for p in config['portfolios']}
    by_portfolio = defaultdict(list)
    by_field = defaultdict(list)
    for path, r in records:
        r['details'] = read(r['diagnostic_cache'])['rounds']
        r['path'] = path
        result = cells[r['portfolio']+'/'+r['scenario']]['result']
        totals = defaultdict(float)
        for round_result in result['rounds']:
            for team in round_result['team_scores']:
                totals[team['team_id']] += team['score']
        ours = totals.pop('our-team')
        r['rank'] = 1 + sum(other > ours + 1 for other in totals.values())
        r['lead_usd'] = ours - max(totals.values())
        by_portfolio[r['portfolio']].append(r)
        by_field[r['scenario']].append(r)
    fields = [s['name'] for s in config['scenarios']]
    rows = [aggregate(p, by_portfolio[p['name']], len(fields)) for p in config['portfolios']]
    rows.sort(key=lambda r: (not r['complete'], -(r['worst_usd'] if r['worst_usd'] is not None else -math.inf),
                             -(r['mean_usd'] if r['mean_usd'] is not None else -math.inf), r['portfolio']))
    dollars = lambda v: number(v/1e9 if v is not None else None, 6)
    g_plan = lambda p: ' / '.join(f'{500*p["generation_schedule"][s]:g}' for s in ('1', '2'))
    layouts = config['layouts']
    total = len(cells)
    accepted = len(records)
    text = '# Ten-team comparison at 500 MW per submission\n\n'
    text += table(['Our layout and policy', 'Sites', 'S1 / S2 G MW', 'Fields complete', 'Mean score $B', 'Worst score $B',
                   'Minimum S1 admitted MW', 'Minimum S2 admitted MW', 'Max S1 required h/year', 'Max S2 required h/year'],
                  [[r['portfolio'], len(specs[r['portfolio']]['bus_ids']), g_plan(specs[r['portfolio']]),
                    f"{r['count']}/{len(fields)}", dollars(r['mean_usd']), dollars(r['worst_usd']),
                    number(r['s1_min_mw']), number(r['s2_min_mw']), number(r['s1_required_h_max']),
                    number(r['s2_required_h_max'])] for r in rows])
    text += f'\nAccepted {accepted} of {total} campaigns ({4*accepted} scored rounds). Mean scores weight the tested fields equally. Each campaign evaluates four 120-period graded submissions. W2 and W3 start from the same base. Actual S1 grid withdrawals from all ten teams carry into S2.\n'
    text += '\n## Evaluation checks\n\nEvery accepted result uses the instructor allocation, joint dispatch, and scoring rules. Fixed plans with identical physical inputs can reuse the physical solve between weeks while the evaluator recomputes the score for each week. Later runs solve no-storage feasibility one hour at a time, with the same allocation objectives and checks across all 120 periods. Each case links any numerical retry and its audit.\n'
    complete = [r for r in rows if r['complete']]
    if complete:
        best_worst = complete[0]
        best_mean = max(complete, key=lambda r: r['mean_usd'])
        text += f"\n`{best_worst['portfolio']}` leads on worst-case score at **${dollars(best_worst['worst_usd'])}B**. `{best_mean['portfolio']}` leads on equal-weight mean at **${dollars(best_mean['mean_usd'])}B**.\n"
        policies = sorted({specs[r['portfolio']]['policy'] for r in complete})
        policy_rows = []
        for policy in policies:
            options = [r for r in complete if specs[r['portfolio']]['policy'] == policy]
            best = max(options,key=lambda r:r['mean_usd'])
            policy_rows.append([policy,best['portfolio'],dollars(best['mean_usd']),dollars(best['worst_usd']),
                                number(min(r['s1_min_mw'] for r in options)),number(min(r['s2_min_mw'] for r in options))])
        text += '\n'+table(['Generation policy','Best mean layout','Mean $B','Worst $B for that layout',
                            'Lowest S1 MW across complete layouts','Lowest S2 MW across complete layouts'],policy_rows)
    text += '\n## Opponent plans and site selection\n\n'
    text += table(['Field', 'Identical layout for each of nine rivals', 'S1 / S2 G MW per rival'],
                  [[s['name'], ', '.join(s['rival_plan']['bus_ids']), g_plan(s['rival_plan'])] for s in config['scenarios']])
    text += '\nThe hosting-capacity layouts take the first 1, 2, or 5 buses in standalone hosting rank. The electrical layouts start with the best composite-ranked bus that retained at least 500 MW across the Part 1 stress screens. They add buses by minimizing worst signed bottleneck overlap, then maximizing minimum PTDF distance. Loads are equally split within each layout.\n\n'
    text += table(['Layout', 'Buses', 'Per-site MW'], [[name, ', '.join(p['bus_ids']), number(500/len(p['bus_ids']))] for name,p in layouts.items()])
    headroom = min(native_profiles(str(ROOT/config['scenario_directory'])))
    text += f'\n## Why S1 can need generation\n\nAt the tightest native hour, aggregate generation has **{headroom:,.3f} MW** of spare supply. For the full **5,000 MW** S1 field to be admitted at zero storage, at least **{5000-headroom:,.3f} MW** must come from new private generation in that hour. Local transmission limits can tighten the result. The game admits one firm capacity per site for the entire modeled horizon, so the limiting hour can reduce IT value across the year.\n'
    text += '\nThe partial S1 tests hold S2 at 500 MW of generation. They bracket the tested cost and admission trade-off at 0, 125, 250, 375, and 500 MW of S1 generation for the one-site and five-site electrical layouts.\n\n'
    sizing = [r for r in rows if specs[r['portfolio']]['layout'] in {'bottleneck_ptdf_1','bottleneck_ptdf_5'}
              and specs[r['portfolio']]['generation_schedule']['2'] == 1.]
    sizing.sort(key=lambda r: (specs[r['portfolio']]['layout'], specs[r['portfolio']]['generation_schedule']['1']))
    text += table(['Electrical layout', 'S1 G MW', 'Mean score $B', 'Worst score $B', 'Minimum S1 admitted MW', 'Fields complete'],
                  [[specs[r['portfolio']]['layout'], int(500*specs[r['portfolio']]['generation_schedule']['1']),
                    dollars(r['mean_usd']), dollars(r['worst_usd']), number(r['s1_min_mw']), f"{r['count']}/{len(fields)}"] for r in sizing])
    sizing_by_field = []
    for layout in ('bottleneck_ptdf_1','bottleneck_ptdf_5'):
        for field in fields:
            options = sorted([(int(500*specs[r['portfolio']]['generation_schedule']['1']),r) for r in by_field[field]
                              if specs[r['portfolio']]['layout']==layout and specs[r['portfolio']]['generation_schedule']['2']==1.],
                             key=lambda item:item[0])
            if not options:
                continue
            admitted = lambda r: min(x['allocated_load_mw'] for x in r['details'] if x['round'].endswith('1'))
            full = next((g for g,r in options if admitted(r)>=500-1e-4),None)
            most, best = max(options,key=lambda pair:pair[1]['score_usd'])
            sizing_by_field.append([layout,field,len(options),number(full,0),most,number(admitted(best),6),dollars(best['score_usd'])])
    text += '\n'+table(['Layout','Rival field','S1 sizes tested','Smallest tested G for full S1 MW',
                        'Highest scoring tested S1 G MW','S1 MW at highest score','Score $B'],sizing_by_field)
    text += '\n## Matched scores by field\n\n'
    text += table(['Our strategy', *fields], [[r['portfolio'], *[
        dollars(next((x['score_usd'] for x in by_portfolio[r['portfolio']] if x['scenario']==field), None)) for field in fields]] for r in rows])
    for field in fields:
        text += f'\n### {field}\n\n'
        text += table(['Case', 'Score $B', 'Rank of 10', 'Lead over best rival $B', 'Gross IT value $B', 'Grid MWh across build-years',
                       'Private MWh across build-years', 'Generator on h across build-years', 'Verified required h'],
                      [[link(r['path'], r['portfolio']), dollars(r['score_usd']), r['rank'], dollars(r['lead_usd']), dollars(r['it_value_usd']),
                        number(r['grid_mwh']), number(r['generation_mwh']), number(r['annual_generator_hours']),
                        number(r['required_annual_hours'])] for r in sorted(by_field[field], key=lambda r: -r['score_usd'])])
    if accepted != total:
        missing = [(key, cell['error']) for key, cell in cells.items() if cell['status']!='complete']
        text += '\n## Missing results\n\n'+table(['Campaign', 'Evaluation status'], missing)
    write_note(destination/'Ten_teams_500_MW_comparison.md', text)
    return rows, by_portfolio


def write_notebook_inputs(directory, by_portfolio, identity):
    cost_fields = {'it_value': 'it_value_usd', 'energy_cost': 'grid_energy_cost_usd',
                   'generator_operating_cost': 'generator_operating_cost_usd',
                   'generator_capital_cost': 'generator_capital_cost_usd', 'site_cost': 'site_cost_usd',
                   'storage_capital_cost': 'storage_capital_cost_usd'}
    for name, cases in by_portfolio.items():
        campaigns = []
        energy_rows = []
        for case in cases:
            rounds = [{'round': r['round'], 'score': r['score_usd'], 'service_fraction': min(1.,r['service_fraction']),
                       'valid': True, 'feasible': True, **{k:r['score_breakdown'][v] for k,v in cost_fields.items()}}
                      for r in case['details']]
            campaigns.append({'experiment': 'ten-teams-500mw', 'capacity_per_submission_mw': 500,
                              'hypothetical_capacity_override': False, 'scenario_id': case['scenario'],
                              'source_scenario_sha256': identity['scenario_sha256'],
                              'effective_rules_sha256': identity['rules_sha256'],
                              'effective_release_sha256': identity['release_sha256'], 'rounds': rounds})
            for r in case['details']:
                energy = r['annual_energy_mwh']
                energy_rows.append({'experiment':'ten-teams-500mw', 'capacity_per_submission_mw':500,
                                    'scenario_id':case['scenario'], 'round':r['round'], 'score_billions':r['score_usd']/1e9,
                                    'bus_id':' / '.join(case['buses']), 'grid_supply_share':r['grid_share'],
                                    'private_generation_share':energy['generation']/energy['load'] if energy['load'] else None})
        if campaigns:
            save_json(directory/f'{name}.json', {'campaigns': campaigns})
            with (directory/f'{name}.csv').open('w',newline='') as out:
                writer = csv.DictWriter(out,fieldnames=list(energy_rows[0]))
                writer.writeheader()
                writer.writerows(energy_rows)


def report(run, summary, destination):
    config, manifest, cells = (read(run/name) for name in ('experiment.json','manifest.json','cells.json'))
    if manifest['status'] not in {'evaluated', 'partial', 'complete'}:
        raise ValueError('Campaign attempts are still running')
    identity = manifest['identity']
    expected = {p['name']+'/'+s['name'] for p in config['portfolios'] for s in config['scenarios']}
    if config['team_count'] != 10 or config['capacity_per_submission_mw'] != 500 or set(cells) != expected:
        raise ValueError('Expected the exact ten-team campaign matrix')
    if file_fingerprint(run/'cells.json') != manifest['artifact_sha256']['cells.json']:
        raise ValueError('Saved campaign matrix fingerprint differs')
    accepted = {key: cell for key, cell in cells.items() if cell['status'] == 'complete'}
    matched = validate_requests(config,cells)
    if len(accepted) == len(cells):
        checks = verify_matrix(config,cells,identity,match_rival_hashes=False)
    else:
        portfolios = {p['name']:p for p in config['portfolios']}
        scenarios = {s['name']:s for s in config['scenarios']}
        for key, cell in accepted.items():
            p,s = key.split('/')
            verify_matrix({**config, 'portfolios':[portfolios[p]], 'scenarios':[scenarios[s]]}, {key:cell}, identity)
        checks = {'campaign_count': len(accepted), 'evaluation_count': 4*len(accepted)}
    summary.mkdir(parents=True,exist_ok=True)
    for name in ('cells.json','experiment.json'):
        shutil.copyfile(run/name,summary/name)
    save_json(summary/'manifest.json', {**manifest, **checks, 'status':'complete' if len(accepted)==len(cells) else 'partial',
                                       'verified_matched_rival_rounds':matched, 'verified_all_csv_requests':True})
    paths = export_findings(summary, root=ROOT, destination=destination)
    rows, by_portfolio = summarize(config,cells,[(p,read_record(p)) for p in paths],destination,identity)
    save_json(summary/'comparison.json', {'strategies': rows})
    with (summary/'comparison.csv').open('w',newline='') as out:
        writer=csv.DictWriter(out,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    notebook_directory = summary/'notebook'
    notebook_directory.mkdir(exist_ok=True)
    write_notebook_inputs(notebook_directory, by_portfolio, identity)
    write_strategy_indexes(ROOT,destination)
    print(f'Comparison ready: {destination / "Ten_teams_500_MW_comparison.md"}', flush=True)


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run',type=Path,default=ROOT/'runs/ten-teams-500mw')
    parser.add_argument('--summary',type=Path,default=ROOT/'analysis/strategy/ten-teams-500mw')
    parser.add_argument('--findings',type=Path,default=ROOT/'findings')
    args=parser.parse_args()
    report(args.run.resolve(),args.summary.resolve(),args.findings.resolve())
