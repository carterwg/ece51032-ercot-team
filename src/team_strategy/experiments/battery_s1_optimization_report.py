"""Validate and report the targeted S1 sizing study after campaigns complete."""

import argparse
import csv
from math import fsum
from pathlib import Path
from statistics import mean

from ercot_game.csv_submission import STORAGE_DURATION_HOURS

from ..context import file_fingerprint, scenario_fingerprint
from ..evaluation.campaign import save_json
from .battery_s1 import CAPACITY_MW, FIELDS, ROOT, BatteryPlan, read, rival_storage_fields
from .battery_s1_optimization import (
    BENCHMARKS, OUTPUT, THRESHOLD, adversarial_fields, capital_cost, prior_fields, stored_results, validation_fields,
)
from .battery_s1_report import analyze_round, render_case
from .findings import link, number, repo_path, table, write_note, write_strategy_indexes


def minimum_s1(rounds):
    return min(CAPACITY_MW * row['service_fraction'] for row in rounds if row['round'].endswith('1'))


def pair_key(sizes, field):
    return f"{BatteryPlan(*sizes).key}/{field['name']}"


def verified_finding(raw, field, config, rates, ratings, destination):
    rounds = raw['rounds']
    if raw['phase'] == 'campaign':
        expected = [f'week-{week}-submission-{submission}' for week in (2, 3) for submission in (1, 2)]
        if [row['round'] for row in rounds] != expected:
            raise ValueError('Expected all four graded rounds')
        if abs(fsum(row['score_usd'] for row in rounds) - raw['campaign_score_usd']) > .02:
            raise ValueError('Campaign score does not reconcile')
        carries = raw['carryovers']
        if sorted(carry['week'] for carry in carries) != [2, 3]:
            raise ValueError('Expected validated S1 carryover for both weeks')
        for carry in carries:
            output = Path(raw['output'])
            week = carry['week']
            if (carry['validation']['passed_period_count'] != 120 or len(carry['team_ids']) != 10
                or scenario_fingerprint(output/f'week-{week}-s2-base') != carry['carried_scenario_sha256']
                or file_fingerprint(output/f'week-{week}-s1-withdrawal.csv') != carry['withdrawal_sha256']):
                raise ValueError('Invalid carryover of the ten S1 withdrawals')
    if raw['phase'] == 'sweep' and [row['round'] for row in rounds] != ['week-3-submission-1']:
        raise ValueError('Expected an S1-only screening run')
    entry = {**raw, 'metrics': [analyze_round(raw, row, config, field, rates, ratings) for row in rounds]}
    return render_case(entry, destination, field)


def report(output, candidates, destination, analysis):
    config = read(ROOT/FIELDS)
    rates = read(ROOT/config['rules_file'])
    fields = validation_fields(config)
    by_name = {field['name']: field for field in fields}
    existing = prior_fields(config)
    adverse = adversarial_fields(config)
    initial = rival_storage_fields(config)
    screen = read(output/'targeted_screen.json')
    all_sizes = [*candidates, *BENCHMARKS]
    campaigns = stored_results(output, 'campaign')
    initial_sweeps = stored_results(output, 'sweep')
    missing = [pair_key(sizes, field) for sizes in all_sizes for field in fields if pair_key(sizes, field) not in campaigns]
    if missing:
        raise ValueError(f'{len(missing)} campaigns still missing, starting with {missing[:4]}')
    destination.mkdir(parents=True, exist_ok=True)
    analysis.mkdir(parents=True, exist_ok=True)
    with (ROOT/config['scenario_directory']/'branch_limits.csv').open(newline='') as handle:
        ratings = {row['branch_id']: float(row['thermal_limit_mva'])
                   for row in csv.DictReader(handle) if row['status'] == '1'}

    summary = []
    for sizes in all_sizes:
        runs = []
        for field in fields:
            raw = campaigns[pair_key(sizes, field)]
            path = verified_finding(raw, field, config, rates, ratings, destination)
            runs.append(dict(field=field['name'], s1_mw=minimum_s1(raw['rounds']),
                             s2_mw=min(CAPACITY_MW * row['service_fraction'] for row in raw['rounds']
                                       if row['round'].endswith('2')),
                             score_usd=raw['campaign_score_usd'], finding=str(path)))
            print(f"Verified {pair_key(sizes, field)}", flush=True)
        summary.append(dict(sizes=sizes, capital_m=capital_cost(sizes),
                            min_s1_mw=min(row['s1_mw'] for row in runs),
                            min_s2_mw=min(row['s2_mw'] for row in runs),
                            full_s1_count=sum(row['s1_mw'] == CAPACITY_MW for row in runs),
                            near_firm_count=sum(row['s1_mw'] >= THRESHOLD for row in runs),
                            mean_score_usd=mean(row['score_usd'] for row in runs),
                            worst_score_usd=min(row['score_usd'] for row in runs),
                            cases={row['field']: row for row in runs}))

    s1_checks = read(output/'targeted_checks_sweep.json')
    check_sizes = sorted({tuple(row['sizes']) for row in s1_checks.values()}, key=capital_cost)
    check_awards = {
        sizes: {f['name']: minimum_s1(initial_sweeps[pair_key(sizes, f)]['rounds']) for f in initial}
        for sizes in check_sizes
    }
    screen_entries = {tuple(row['sizes']): row for row in screen['rows']}
    text = '# Targeted S1 generator and battery sizing at bus 6141\n\n'
    text += (f'The exact four-round comparisons use {len(fields)} distinct fields, with the {len(existing)} existing '
             f'fields and the {len(adverse)} same-bus adversarial combinations. The 75 MW generator and 125 MW battery '
             'rival combination was already in the existing set and receives one weight. Every field contains ten '
             '500 MW applicants. The campaign uses the exact daily multiperiod dispatch and carries every team’s '
             'hourly S1 net withdrawals into the same week’s S2. Our S2 request is a new 500 MW site at bus 6141 '
             'with 500 MW generation. Rival S2 plans follow the original field definitions.\n\n')
    text += table(['G MW','P MW','B MWh','S1 capital $M','Minimum S1 MW','500 MW fields','≥499.9 MW fields',
                   'Mean campaign score $B','Worst campaign score $B'], [
        [row['sizes'][0],row['sizes'][1],STORAGE_DURATION_HOURS*row['sizes'][1],number(row['capital_m'],1),
         number(row['min_s1_mw'],6),f"{row['full_s1_count']}/{len(fields)}",f"{row['near_firm_count']}/{len(fields)}",
         number(row['mean_score_usd']/1e9,6),number(row['worst_score_usd']/1e9,6)] for row in summary])
    text += ('\nExact full means the recorded S1 award is 500 MW in both graded weeks. The near-firm threshold is '
             '499.9 MW in both weeks. Scores are equal-weight descriptive comparisons across these fields.\n')
    text += '\n## Initial four storage-rival fields\n\n'
    text += (f'The search used {len(screen_entries)} under-budget 5 MW grid pairs. An analytical pre-screen uses '
             'the verified hourly hosting limit at bus 6141, daily half-full battery cycles, and the evaluator’s '
             'capacity and fairness objectives. The full evaluator checks the five-site portfolio and confirms '
             'the shortlist. The finite equipment grid determines the scope of the cost comparisons.\n\n')
    check_rows = []
    for sizes, awards in check_awards.items():
        links = []
        for field in initial:
            raw = initial_sweeps[pair_key(sizes, field)]
            path = verified_finding(raw, field, config, rates, ratings, destination)
            links.append(link(path, number(awards[field['name']],6)))
        check_rows.append([*sizes,capital_cost(sizes),*links,number(min(awards.values()),6)])
    text += table(['G MW','P MW','S1 capital $M',*[f['name'] for f in initial],'Minimum S1 MW'],check_rows)
    sensitivity = {}
    for name in ('targeted_adverse_sweep', 'targeted_boundary_sweep', 'targeted_sweep'):
        path = output/f'{name}.json'
        if path.is_file():
            sensitivity.update(read(path))
    text += '\n### Lower-cost designs under stress\n\n'
    stress_rows = []
    for key in sorted(sensitivity):
        raw = initial_sweeps[key]
        field = by_name[raw['field']]
        path = verified_finding(raw, field, config, rates, ratings, destination)
        stress_rows.append([*raw['sizes'],capital_cost(raw['sizes']),link(path,field['name']),
                            number(minimum_s1(raw['rounds']),6)])
    text += table(['G MW','P MW','S1 capital $M','Stress field','Exact S1 MW'],stress_rows)
    text += '\n## Same-bus adversarial allocation grid\n\n'
    text += table(['Rival G MW','Rival P MW',*[f"Our {g} G / {p} P" for g,p in all_sizes]],[
        [int(round(CAPACITY_MW*field['rival_plan']['generation_schedule']['1'])),
         field['rival_plan']['storage_power_schedule']['1'],
         *[link(row['cases'][field['name']]['finding'],
                 number(row['cases'][field['name']]['s1_mw'],6)) for row in summary]] for field in adverse])
    text += '\n## Full campaign records\n\n'
    text += table(['G MW','P MW','Opponent field','Minimum S1 MW','Minimum S2 MW','Campaign score $B'],[
        [*row['sizes'],link(case['finding'],case['field']),number(case['s1_mw'],6),number(case['s2_mw'],6),
         number(case['score_usd']/1e9,6)] for row in summary for case in row['cases'].values()])
    path = destination/'Battery_S1_targeted_optimization.md'
    write_note(path,text)
    for row in summary:
        for case in row['cases'].values():
            case['finding'] = repo_path(case['finding'])
    save_json(analysis/'targeted_optimization.json', dict(
        field_count=len(fields),existing_count=len(existing),adversarial_count=len(adverse),
        initial_checks=[{'sizes': sizes, 'awards': awards} for sizes, awards in check_awards.items()],summary=summary))
    write_strategy_indexes(ROOT, destination)
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--candidate', nargs=2, action='append', type=int, required=True, metavar=('G', 'P'))
    parser.add_argument('--output', type=Path, default=OUTPUT)
    parser.add_argument('--findings', type=Path, default=ROOT/'findings')
    parser.add_argument('--analysis', type=Path, default=ROOT/'analysis/strategy/battery-s1-500mw')
    args = parser.parse_args()
    print(report(args.output, list(map(tuple,args.candidate)), args.findings, args.analysis))


if __name__ == '__main__':
    main()
