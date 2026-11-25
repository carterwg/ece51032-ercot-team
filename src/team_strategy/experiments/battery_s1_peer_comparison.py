"""Compare S1 builds in matched four-round campaigns."""

import argparse
import csv
from math import fsum
from pathlib import Path
from statistics import mean

from ercot_game.csv_submission import STORAGE_DURATION_HOURS

from ..evaluation.campaign import save_json
from .battery_s1 import BUS, CAPACITY_MW, FIELDS, ROOT, BatteryPlan, read
from .battery_s1_optimization import (
    CAPITAL_LIMIT_M, OUTPUT, THRESHOLD, capital_cost, exact_tasks, stored_results, validation_fields,
)
from .battery_s1_optimization_report import minimum_s1, verified_finding
from .findings import link, number, repo_path, table, write_note

PLANS = {
    'Carter battery-only': BatteryPlan(0, 125),
    'Garcia generator-only': BatteryPlan(225, 0, s1_bus='2054'),
    '97/99 hybrid': BatteryPlan(97, 99),
    '95/105 hybrid': BatteryPlan(95, 105),
    '200 MW generator-only': BatteryPlan(200, 0),
    '210 MW generator-only': BatteryPlan(210, 0),
}
REPORT = 'Battery_S1_peer_campaign_comparison.md'


def report(output, destination, analysis):
    config = read(ROOT / FIELDS)
    fields = validation_fields(config)
    rates = read(ROOT / config['rules_file'])
    campaigns = stored_results(output, 'campaign')
    keys = {label: {field['name']: f"{plan.key}/{field['name']}" for field in fields}
            for label, plan in PLANS.items()}
    pending = [key for group in keys.values() for key in group.values() if key not in campaigns]
    if pending:
        raise ValueError(f'{len(pending)} campaigns remain unresolved, beginning with {pending[:5]}')
    with (ROOT / config['scenario_directory'] / 'branch_limits.csv').open(newline='') as handle:
        ratings = {row['branch_id']: float(row['thermal_limit_mva'])
                   for row in csv.DictReader(handle) if row['status'] == '1'}

    destination.mkdir(parents=True, exist_ok=True)
    analysis.mkdir(parents=True, exist_ok=True)
    cases = {}
    for field in fields:
        name = field['name']
        field_cases = {}
        reference = None
        for label, plan in PLANS.items():
            raw = campaigns[keys[label][name]]
            if raw.get('s1_bus', BUS) != plan.s1_bus or raw['sizes'] != [plan.generator_mw, plan.battery_mw]:
                raise ValueError(f'Unexpected own plan in {keys[label][name]}')
            rival_hashes = [
                {team: digest for team, digest in row['input_sha256_by_team'].items() if team != 'our-team'}
                for row in raw['rounds']
            ]
            if reference is None:
                reference = rival_hashes
            elif reference != rival_hashes:
                raise ValueError(f'Rival inputs differ in {name}')
            finding = verified_finding(raw, field, config, rates, ratings, destination)
            s2 = min(CAPACITY_MW * row['service_fraction'] for row in raw['rounds'] if row['round'].endswith('2'))
            field_cases[label] = {'s1_mw': minimum_s1(raw['rounds']), 's2_mw': s2,
                                  'score_usd': raw['campaign_score_usd'], 'finding': repo_path(finding),
                                  's1_score_usd': fsum(row['score_usd'] for row in raw['rounds']
                                                      if row['round'].endswith('1')),
                                  's2_score_usd': fsum(row['score_usd'] for row in raw['rounds']
                                                      if row['round'].endswith('2'))}
        cases[name] = field_cases
        print(f'Verified all {len(PLANS)} plans in {name}', flush=True)

    summary = {}
    for label, plan in PLANS.items():
        own = {name: cell[label] for name, cell in cases.items()}
        s2_rounds = [[row for row in campaigns[key]['rounds'] if row['round'].endswith('2')]
                     for key in keys[label].values()]
        lowest = min(own, key=lambda name: own[name]['s1_mw'])
        worst = min(own, key=lambda name: own[name]['score_usd'])
        summary[label] = {
            'bus': plan.s1_bus, 'generator_mw': plan.generator_mw, 'storage_mw': plan.battery_mw,
            'storage_mwh': STORAGE_DURATION_HOURS * plan.battery_mw,
            'capital_m': capital_cost((plan.generator_mw, plan.battery_mw)),
            'min_s1_mw': own[lowest]['s1_mw'], 'min_s1_field': lowest,
            'mean_s1_mw': mean(row['s1_mw'] for row in own.values()),
            'full_s1_fields': sum(row['s1_mw'] == CAPACITY_MW for row in own.values()),
            'near_firm_fields': sum(row['s1_mw'] >= THRESHOLD for row in own.values()),
            'min_s2_mw': min(row['s2_mw'] for row in own.values()),
            'mean_score_usd': mean(row['score_usd'] for row in own.values()),
            'mean_s1_score_usd': mean(row['s1_score_usd'] for row in own.values()),
            'mean_s2_score_usd': mean(row['s2_score_usd'] for row in own.values()),
            **{f'mean_s2_{cost}': mean(fsum(row['score_breakdown'][cost] for row in rounds)
                                      for rounds in s2_rounds)
               for cost in ('generator_operating_cost_usd', 'grid_energy_cost_usd')},
            'worst_score_usd': own[worst]['score_usd'], 'worst_score_field': worst,
            'fields_tied_for_best_score': sum(
                own[name]['score_usd'] == max(row['score_usd'] for row in field_cases.values())
                for name, field_cases in cases.items()),
        }
    write_note(destination / REPORT, report_text(summary, cases, fields))
    save_json(analysis / 'peer_comparison.json', {'fields': len(fields), 'summary': summary, 'cases': cases})
    return destination / REPORT


def report_text(summary, cases, fields):
    count = len(fields)
    usd_b = lambda dollars: number(dollars / 1e9, 6)
    mean_leader = max(summary, key=lambda label: summary[label]['mean_score_usd'])
    worst_leader = max(summary, key=lambda label: summary[label]['worst_score_usd'])
    text = '# Matched S1 and campaign comparison\n\n'
    if mean_leader == worst_leader:
        text += f'**{mean_leader}** led on both equal-weight mean and worst-field campaign score. '
    else:
        text += (f'**{mean_leader}** led on equal-weight mean campaign score. '
                 f'**{worst_leader}** led on worst-field campaign score. ')
    text += f'The results cover **{count * len(summary)} campaigns and {count * len(summary) * 4} scored rounds**.\n\n'
    text += table(['S1 build', 'S1 bus', 'Generator MW', 'Battery MW / MWh', 'Capital $M', 'Minimum S1 MW',
                   'Exact 500 MW fields', 'At least 499.9 MW fields', 'Minimum S2 MW',
                   'Mean score $B', 'Worst score $B'], [
        [label, row['bus'], row['generator_mw'], f"{row['storage_mw']} / {row['storage_mwh']}",
         number(row['capital_m'], 1), number(row['min_s1_mw'], 6), f"{row['full_s1_fields']}/{count}",
         f"{row['near_firm_fields']}/{count}", number(row['min_s2_mw'], 6),
         usd_b(row['mean_score_usd']), usd_b(row['worst_score_usd'])] for label, row in summary.items()
    ])
    text += '\n## Findings\n\n'
    qualified = [label for label, row in summary.items() if row['near_firm_fields'] == count]
    if qualified:
        cheapest = min(qualified, key=lambda label: summary[label]['capital_m'])
        text += f'**{cheapest}** had the lowest S1 capital cost among builds that cleared 499.9 MW in every field.\n\n'
    most_full = max(row['full_s1_fields'] for row in summary.values())
    top_full = [label for label, row in summary.items() if row['full_s1_fields'] == most_full]
    text += (f'The highest exact 500 MW count was **{most_full} of {count} fields**, '
             f'reached by {", ".join(top_full)}.\n\n')
    cheap, baseline = (summary[label] for label in ('97/99 hybrid', '95/105 hybrid'))
    text += table(['97/99 relative to 95/105', 'Change'], [
        ['S1 build capital $M', f"{cheap['capital_m'] - baseline['capital_m']:+.1f}"],
        ['Minimum S1 kW', f"{1000 * (cheap['min_s1_mw'] - baseline['min_s1_mw']):+.3f}"],
        ['Mean campaign score $M', f"{(cheap['mean_score_usd'] - baseline['mean_score_usd']) / 1e6:+.3f}"],
        ['Worst campaign score $M', f"{(cheap['worst_score_usd'] - baseline['worst_score_usd']) / 1e6:+.3f}"],
    ])
    text += '\nThe average score contributions below sum the two graded weeks for each submission.\n\n'
    text += table(['S1 build', 'Mean S1 award MW', 'Mean S1 score $B', 'Mean S2 score $B'], [
        [label, number(row['mean_s1_mw'], 6), usd_b(row['mean_s1_score_usd']), usd_b(row['mean_s2_score_usd'])]
        for label, row in summary.items()
    ])
    text += '\n### What drove the score differences\n\n'
    generator_label = '200 MW generator-only'
    generator = summary[generator_label]
    generator_210 = summary['210 MW generator-only']
    garcia = summary['Garcia generator-only']
    carter_label = 'Carter battery-only'
    carter = summary[carter_label]

    generator_limit = generator['min_s1_field']
    generator_link = link(ROOT / cases[generator_limit][generator_label]['finding'], '200 MW limiting field')
    text += (
        f"**The 200 MW generator at bus 6141** cleared 499.9 MW in all {count} fields and reached "
        f"500 MW in {generator['full_s1_fields']}. In its lowest-award field, nine rivals each used "
        f"50 MW generation and 125 MW / 500 MWh storage at bus 6141. The evaluator awarded "
        f"{number(generator['min_s1_mw'], 6)} MW in both S1 rounds. Line b02136 was at its lower "
        f"flow limit during the seven modeled hours when our generator ran. {generator_link}\n\n"
        f"At the same S1 bus, the **97/99 hybrid** saved "
        f"${generator['capital_m'] - cheap['capital_m']:.1f}M per S1 build and earned "
        f"${(cheap['mean_score_usd'] - generator['mean_score_usd']) / 1e6:.1f}M more on average. "
        f"The hybrid’s worst-case score was ${(cheap['worst_score_usd'] - generator['worst_score_usd']) / 1e6:.1f}M higher. "
        f"The 200 MW build provided {1000 * (generator['min_s1_mw'] - cheap['min_s1_mw']):.1f} kW "
        f"more minimum S1 allocation. Across both graded weeks, the hybrid gained "
        f"${(cheap['mean_s1_score_usd'] - generator['mean_s1_score_usd']) / 1e6:.1f}M in S1 and "
        f"${(cheap['mean_s2_score_usd'] - generator['mean_s2_score_usd']) / 1e6:.1f}M in S2 on average.\n\n"
        f"**Garcia’s 225 MW generator at bus 2054** cost ${garcia['capital_m'] - generator['capital_m']:.1f}M "
        f"more per S1 build than the 200 MW generator at bus 6141. Garcia earned "
        f"${(garcia['mean_score_usd'] - generator['mean_score_usd']) / 1e6:.1f}M more on average and "
        f"${(garcia['worst_score_usd'] - generator['worst_score_usd']) / 1e6:.1f}M more in the worst field. "
        f"The two generator-only builds differ in S1 bus and generator size.\n\n"
        f"Compared with 97/99, Garcia earned "
        f"${(cheap['mean_s1_score_usd'] - garcia['mean_s1_score_usd']) / 1e6:.1f}M less in S1 and "
        f"${(garcia['mean_s2_score_usd'] - cheap['mean_s2_score_usd']) / 1e6:.1f}M more in S2 on average. "
        f"All {len(summary)} plans received 500 MW in every S2 round. Garcia’s S1 carryover "
        f"was followed by ${(cheap['mean_s2_generator_operating_cost_usd'] - garcia['mean_s2_generator_operating_cost_usd']) / 1e6:.1f}M "
        f"less S2 generator operating cost and "
        f"${(garcia['mean_s2_grid_energy_cost_usd'] - cheap['mean_s2_grid_energy_cost_usd']) / 1e6:.1f}M "
        f"more S2 grid energy cost. The net mean campaign advantage was "
        f"${(garcia['mean_score_usd'] - cheap['mean_score_usd']) / 1e6:.1f}M.\n\n"
    )
    carter_limit = carter['min_s1_field']
    carter_link = link(ROOT / cases[carter_limit][carter_label]['finding'], 'Carter’s limiting field')
    text += (
        f"Carter’s battery earned the highest campaign score in {carter['fields_tied_for_best_score']} fields. "
        f"In its weakest field, nine rivals each used a 196 MW / 784 MWh battery at bus 6141. "
        f"The evaluator awarded Carter {number(carter['min_s1_mw'], 6)} MW and each rival about "
        f"495.263 MW in S1, for a field total of about 4,457 MW. {carter_link}\n"
    )
    text += '\n### Increasing generation from 200 to 210 MW at bus 6141\n\n'
    text += table(['Measure', '210 MW relative to 200 MW'], [
        ['S1 capital cost ($M)', f"{generator_210['capital_m'] - generator['capital_m']:+.1f}"],
        ['Minimum S1 award (kW)', f"{1000 * (generator_210['min_s1_mw'] - generator['min_s1_mw']):+.3f}"],
        ['Fields with exact 500 MW', f"{generator_210['full_s1_fields'] - generator['full_s1_fields']:+d}"],
        ['Mean S1 score across both weeks ($M)',
         f"{(generator_210['mean_s1_score_usd'] - generator['mean_s1_score_usd']) / 1e6:+.3f}"],
        ['Mean S2 score across both weeks ($M)',
         f"{(generator_210['mean_s2_score_usd'] - generator['mean_s2_score_usd']) / 1e6:+.3f}"],
        ['Mean campaign score ($M)',
         f"{(generator_210['mean_score_usd'] - generator['mean_score_usd']) / 1e6:+.3f}"],
        ['Worst-case campaign score ($M)',
         f"{(generator_210['worst_score_usd'] - generator['worst_score_usd']) / 1e6:+.3f}"],
    ])
    text += '\n## Methods\n\n'
    text += (
        'Each field uses the same ten 500 MW requests, with the nine rivals following the saved field definition. '
        'The 36 fields include the 21 existing cases and 16 same-bus adversarial combinations with one overlap. '
        'The course evaluator dispatches 120 periods with four-hour storage and daily state-of-charge cycles. '
        'The graded rounds are W2S1, W2S2, W3S1, and W3S2. Each week resets, then the net hourly S1 withdrawals '
        'of all ten teams enter that week’s S2 base load. Each plan requests a new 500 MW site with 500 MW of '
        'generation at bus 6141 in S2. The 200 MW generator-only results reuse the official campaigns from the '
        'targeted sizing study. The 210 MW build ran through the same four rounds for every field. '
        'The report rechecks artifact hashes, matching rival submissions, round scores, and each weekly carryover. '
        'Campaign scores sum the four rounds. The exact and near-firm field counts require the corresponding S1 '
        'award in both graded weeks. The capital column shows the requested S1 build cost.\n')
    text += '\n## Limiting fields\n\n'
    text += table(['S1 build', 'Lowest S1 field', 'Minimum S1 MW', 'Worst score field', 'Worst score $B',
                   'Fields with top score'], [
        [label, link(ROOT / cases[row['min_s1_field']][label]['finding'], row['min_s1_field']),
         number(row['min_s1_mw'], 6),
         link(ROOT / cases[row['worst_score_field']][label]['finding'], row['worst_score_field']),
         usd_b(row['worst_score_usd']), f"{row['fields_tied_for_best_score']}/{count}"]
        for label, row in summary.items()
    ])
    text += '\n## S1 award by field\n\n'
    text += table(['Field', 'Rival buses', 'G per rival MW', 'P per rival MW', *summary], [
        [field['name'], ', '.join(field['rival_plan']['bus_ids']),
         number(CAPACITY_MW * field['rival_plan']['generation_schedule']['1'], 0),
         field['rival_plan'].get('storage_power_schedule', {}).get('1', 0),
         *[link(ROOT / row['finding'], number(row['s1_mw'], 6)) for row in cases[field['name']].values()]]
        for field in fields
    ])
    text += '\n## Campaign score by field in billions of dollars\n\n'
    text += table(['Field', *summary], [
        [name, *[link(ROOT / row['finding'], usd_b(row['score_usd'])) for row in field.values()]]
        for name, field in cases.items()
    ])
    text += '\n## Recommended strategy\n\n'
    recommended = summary[worst_leader]
    storage = (f"{recommended['storage_mw']} MW / {recommended['storage_mwh']:.0f} MWh of storage"
               if recommended['storage_mw'] else 'no battery')
    text += (
        f"In **S1**, request {CAPACITY_MW} MW at bus {recommended['bus']} with "
        f"{recommended['generator_mw']} MW of local generation and {storage}. "
        f"In **S2**, request a new {CAPACITY_MW} MW site at bus {BUS} with "
        f"{CAPACITY_MW} MW of local generation and no battery.\n\n"
        f"This plan had the highest worst-case campaign score at ${usd_b(recommended['worst_score_usd'])}B"
    )
    if worst_leader == mean_leader:
        text += f" and the highest mean at ${usd_b(recommended['mean_score_usd'])}B"
    text += (f". The evaluator recorded exact 500 MW S1 awards in "
             f"{recommended['full_s1_fields']} of {count} fields.\n\n")
    if recommended['capital_m'] > CAPITAL_LIMIT_M:
        budget_options = [label for label in qualified if summary[label]['capital_m'] <= CAPITAL_LIMIT_M]
        if budget_options:
            fallback_label = max(budget_options, key=lambda label: summary[label]['mean_score_usd'])
            fallback = summary[fallback_label]
            text += (
                f"If the earlier ${CAPITAL_LIMIT_M}M sizing ceiling is binding for us, use the **{fallback_label}** "
                f"at bus {fallback['bus']} in S1 with {fallback['generator_mw']} MW of generation and "
                f"{fallback['storage_mw']} MW / {fallback['storage_mwh']:.0f} MWh of storage. "
                f"It costs ${fallback['capital_m']:.1f}M per S1 build and cleared {THRESHOLD} MW "
                f"in all {count} fields. Use the same S2 plan.\n\n"
            )
    rival_locations = [field['rival_plan']['bus_ids'] for field in fields]
    at_6141 = rival_locations.count(['6141'])
    with_2054 = sum('2054' in buses for buses in rival_locations)
    text += (
        f"In {at_6141} of {count} fields all nine rivals requested S1 at bus 6141. "
        f"Bus 2054 appeared in {with_2054} fields, with rivals split across 1079 and 2054. "
        f"The recommendation applies to these tested fields, with less evidence for concentrated competition at 2054.\n"
    )
    return text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--jobs', type=int, default=9)
    parser.add_argument('--timeout', type=int, default=720)
    parser.add_argument('--report-only', action='store_true')
    parser.add_argument('--output', type=Path, default=OUTPUT)
    parser.add_argument('--findings', type=Path, default=ROOT / 'findings')
    parser.add_argument('--analysis', type=Path, default=ROOT / 'analysis/strategy/battery-s1-500mw')
    args = parser.parse_args()
    if args.jobs < 1 or args.timeout < 1:
        parser.error('jobs and timeout must be positive')
    if not args.report_only:
        config = read(ROOT / FIELDS)
        tasks = [(plan, field) for field in validation_fields(config) for plan in PLANS.values()]
        exact_tasks(args.output, config, {'campaign': tasks}, jobs=args.jobs, slots=args.jobs,
                    timeout=args.timeout, group='targeted_peer')
    print(report(args.output, args.findings, args.analysis))


if __name__ == '__main__':
    main()
