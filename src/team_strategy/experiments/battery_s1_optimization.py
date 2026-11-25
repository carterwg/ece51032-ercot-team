"""Targeted sizing and four-round validation of the bus 6141 S1 hybrid."""

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import product
from math import fsum
from pathlib import Path

from ..context import scenario_fingerprint
from ..evaluation.campaign import save_json
from .battery_s1 import (
    BUS, CAPACITY_MW, FIELDS, ROOT, BatteryPlan, challenge_fields, execute, read, rival_storage_fields,
)

OUTPUT = ROOT / 'runs/battery-s1-500mw'
BENCHMARKS = ((75, 150), (200, 0))
THRESHOLD = 499.9
CAPITAL_LIMIT_M = 360


def capital_cost(sizes):
    g, p = sizes
    return (10 * g + 7 * p) / 5


def prior_fields(config):
    return (config['scenarios'] + challenge_fields(config) + rival_storage_fields(config)
            + rival_storage_fields(config, randomized=True))


def adversarial_fields(config):
    template = next(field for field in config['scenarios'] if field['name'] == 'nine_grid_at_6141')
    return [
        dict(template, name=f'nine_g{g}_b{p}_at_6141', rival_generator_fraction=1.,
             rival_plan=dict(template['rival_plan'], generation_schedule={'1': g/CAPACITY_MW, '2': 1.},
                             storage_power_schedule={'1': p, '2': 0.}))
        for g, p in product((50, 75, 100, 125), (125, 150, 175, 200))
    ]


def validation_fields(config):
    fields = {field['name']: field for field in prior_fields(config) + adversarial_fields(config)}
    return list(fields.values())


def hosting_profile(config):
    directory = ROOT / config['part1_directory']
    source = read(directory / 'manifest.json')['scenario_sha256']
    if source != scenario_fingerprint(ROOT / config['scenario_directory']):
        raise ValueError('Hosting profile and evaluator use different scenarios')
    baseline = read(directory / 'baseline.json')
    return next(row['capacity_by_period_mw'] for row in baseline if row['bus_id'] == BUS)


def storage_envelope(hosting):
    """Reduce all intraday battery constraints to half-planes in load and power.

    For a constant gross withdrawal D, net charging in hour t is at most
    min(P, hosting[t] - D). In every contiguous interval that upper bound must
    let SOC stay nonnegative or reach the specified terminal SOC. Sorting the
    interval capacities gives each linear piece of the sum of the minima.
    """
    tightest = {(1, -1): min(hosting)}  # D - P <= hosting[t].
    for offset in range(0, len(hosting), 24):
        day = hosting[offset:offset + 24]
        for start in range(24):
            for end in range(start + 1, 25):
                width = end - start
                free_energy = 4 - 2 * (start == 0) - 2 * (end == 24)
                capacities = sorted(day[start:end])
                for count in range(1, width + 1):
                    key = (count, -(width - count + free_energy))
                    rhs = fsum(capacities[:count])
                    tightest[key] = min(tightest.get(key, float('inf')), rhs)
    return [(hours, power, rhs) for (hours, power), rhs in tightest.items()]


def colocalized_award(sizes, rival, envelope):
    """Solve the two-fraction allocation on a single bus before full reevaluation."""
    from ercot_game.batch_evaluation import _ALLOCATION_MARGIN
    from highspy import Highs, HighsModelStatus, kHighsInf
    from tools.activsg2000.allocation import TOTAL_RELATIVE_TOLERANCE

    g, p = sizes
    rg, rp = rival
    coefficients = [(h * (CAPACITY_MW-g) + b*p, 9 * (h * (CAPACITY_MW-rg) + b*rp), rhs)
                    for h, b, rhs in envelope]
    if all(a + b <= rhs for a, b, rhs in coefficients):
        return float(CAPACITY_MW)

    model = Highs()
    model.setOptionValue('output_flag', False)
    model.setOptionValue('threads', 1)
    model.addVariable(0., 1., -1.)
    model.addVariable(0., 1., -9.)
    for a, b, rhs in coefficients:
        model.addRow(-kHighsInf, rhs, 2, [0, 1], [a, b])
    model.run()
    if model.getModelStatus() != HighsModelStatus.kOptimal:
        raise RuntimeError('The co-located capacity LP failed')
    best_total = -model.getObjectiveValue()
    # At the tie-break floor, the least-squares optimum is the equal award
    # clipped to the feasible interval. Above the floor the same decreasing
    # objective might prefer more throughput, so evaluate the polygon vertices
    # and the projection of (1,1) onto each feasible edge.
    planes = coefficients + [(1., 0., 1.), (0., 1., 1.), (-1., 0., 0.), (0., -1., 0.),
                             (-1., -9., -best_total*(1.-TOTAL_RELATIVE_TOLERANCE))]
    best, alpha = float('inf'), 0.
    for a, b, rhs in planes:
        normal = a*a + b*b/9
        if not normal:
            continue
        x = 1 - a * (a+b-rhs) / normal
        y = 1 - b * (a+b-rhs) / (9*normal)
        low, high = -float('inf'), float('inf')
        # Parameterize the edge by (x,y) + t*(-b,a). Normalize the tangent
        # to avoid a scale-dependent slack test.
        scale = max(abs(a), abs(b))
        dx, dy = -b/scale, a/scale
        for c, d, limit in planes:
            rate, remaining = c*dx+d*dy, limit-c*x-d*y
            if abs(rate) < 1e-9:
                if remaining < -1e-7:
                    low, high = 1., 0.
                    break
            elif rate > 0:
                high = min(high, remaining/rate)
            else:
                low = max(low, remaining/rate)
        if low <= high + 1e-10:
            step = min(high, max(low, 0.))
            ours, theirs = x+step*dx, y+step*dy
            loss = (1-ours)**2 + 9*(1-theirs)**2
            if loss < best:
                best, alpha = loss, min(1., max(0., ours))
    if best == float('inf'):
        raise RuntimeError('The co-located allocation tie-break found no feasible edge')
    return CAPACITY_MW if alpha >= 1.-1e-5 else CAPACITY_MW * alpha * _ALLOCATION_MARGIN


def screen_awards(sizes, fields, envelope):
    awards = {}
    for field in fields:
        rival = field['rival_plan']
        g = CAPACITY_MW * rival['generation_schedule']['1']
        p = rival.get('storage_power_schedule', {}).get('1', 0)
        awards[field['name']] = colocalized_award(sizes, (g, p), envelope)
    return awards


def screen(output, config):
    envelope = storage_envelope(hosting_profile(config))
    at_6141 = [field for field in rival_storage_fields(config) if field['rival_plan']['bus_ids'] == [BUS]]
    prior = [field for field in prior_fields(config) if field['rival_plan']['bus_ids'] == [BUS]]
    adverse = adversarial_fields(config)
    sizes_grid = sorted((pair for pair in product(range(0, 181, 5), range(0, 261, 5))
                         if capital_cost(pair) <= CAPITAL_LIMIT_M), key=lambda pair: (capital_cost(pair), pair))
    rows = []
    for sizes in sizes_grid:
        first = screen_awards(sizes, at_6141, envelope)
        row = {'sizes': sizes, 'capital_m': capital_cost(sizes), 'initial_colocated_mw': first}
        if min(first.values()) >= THRESHOLD - .01:
            row['adversarial_mw'] = screen_awards(sizes, adverse, envelope)
            if min(row['adversarial_mw'].values()) >= THRESHOLD - .01:
                row['prior_colocated_mw'] = screen_awards(sizes, prior, envelope)
        rows.append(row)
    benchmark = [{'sizes': sizes, 'initial_colocated_mw': screen_awards(sizes, at_6141, envelope),
                  'adversarial_mw': screen_awards(sizes, adverse, envelope)} for sizes in BENCHMARKS]
    save_json(output / 'targeted_screen.json', {'grid_step_mw': 5, 'rows': rows, 'benchmarks': benchmark})
    eligible = [row for row in rows if 'adversarial_mw' in row]
    print(f'{len(rows)} under-budget pairs, {len(eligible)} pass or are near the co-located first screen', flush=True)
    print('Lowest-cost initial screen pairs', [(r['sizes'], r['capital_m']) for r in eligible[:12]], flush=True)
    validated = [row for row in eligible if min(row['adversarial_mw'].values()) >= THRESHOLD - .01]
    print('Lowest-cost adversarial screen pairs', [(r['sizes'],r['capital_m']) for r in validated[:16]], flush=True)
    shortlist = [row for row in validated if min(row['prior_colocated_mw'].values()) >= THRESHOLD - .01]
    print('Lowest-cost broader screen pairs', [(r['sizes'],r['capital_m']) for r in shortlist[:16]], flush=True)


def stored_results(output, phase):
    names = ('finalists', 'rival_storage_campaign', 'rival_storage_sizing_campaign')
    if phase == 'sweep':
        names = ('refined', 'rival_storage', 'rival_storage_randomized')
    files = [output / f'{name}.json' for name in names] + sorted(output.glob(f'targeted*_{phase}.json'))
    return {
        key: result
        for path in files if path.is_file()
        for key, result in read(path).items()
        if result['status'] == 'complete'
    }


def exact_tasks(output, config, phases, *, timeout, jobs, slots=4, group='targeted'):
    """Run only unseen cells and persist each result as soon as it finishes."""
    records = {phase: stored_results(output, phase) for phase in phases}
    paths = {phase: output / f'{group}_{phase}.json' for phase in phases}
    written = {phase: read(path) if path.is_file() else {} for phase, path in paths.items()}
    requests = [(phase, plan if isinstance(plan, BatteryPlan) else BatteryPlan(*plan), field)
                for phase, cases in phases.items() for plan, field in cases]
    tasks = [(phase, plan, field) for phase, plan, field in requests
             if f"{plan.key}/{field['name']}" not in records[phase]]
    print(f'{len(tasks)} exact evaluations pending', flush=True)
    with ThreadPoolExecutor(jobs) as pool:
        futures = {pool.submit(execute, output, config, field, (plan.generator_mw, plan.battery_mw), phase, timeout,
                               storage_slots=slots, s1_bus=plan.s1_bus): phase for phase, plan, field in tasks}
        for future in as_completed(futures):
            phase = futures[future]
            key, result = future.result()
            written[phase][key] = records[phase][key] = result
            save_json(paths[phase], written[phase])
            if result['status'] == 'complete':
                s1 = min(CAPACITY_MW * r['service_fraction'] for r in result['rounds'] if r['round'].endswith('1'))
                print(f'{phase} {key}: S1 {s1:.6f} MW', flush=True)
            else:
                print(f'{phase} {key}: unresolved', flush=True)
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--candidate', nargs=2, action='append', type=int, metavar=('G', 'P'))
    parser.add_argument('--benchmark', action='store_true')
    parser.add_argument('--adversarial-only', action='store_true')
    parser.add_argument('--screen', action='store_true')
    parser.add_argument('--initial-only', action='store_true')
    parser.add_argument('--s1-only', action='store_true')
    parser.add_argument('--field', action='append', default=[])
    parser.add_argument('--output', type=Path, default=OUTPUT)
    parser.add_argument('--jobs', type=int, default=6)
    parser.add_argument('--slots', type=int, default=4)
    parser.add_argument('--group', choices=('targeted', 'targeted_finalists', 'targeted_checks', 'targeted_adverse'),
                        default='targeted')
    parser.add_argument('--timeout', type=int, default=720)
    args = parser.parse_args()
    if min(args.jobs, args.slots, args.timeout) < 1:
        parser.error('jobs, slots, and timeout must be positive')
    config = read(ROOT / FIELDS)
    if args.screen:
        screen(args.output, config)
        return
    candidates = [*map(tuple, args.candidate or ()), *(BENCHMARKS if args.benchmark else ())]
    if not candidates:
        parser.error('provide --benchmark or at least one --candidate')
    fields = adversarial_fields(config) if args.adversarial_only else validation_fields(config)
    priority = {f['name']: i for i, f in enumerate(rival_storage_fields(config) + adversarial_fields(config))}
    fields.sort(key=lambda f: priority.get(f['name'], len(priority)))
    phase = 'sweep' if args.s1_only else 'campaign'
    if args.initial_only:
        fields, phase = rival_storage_fields(config), 'sweep'
    if args.field:
        selected = set(args.field)
        if selected - {field['name'] for field in fields}:
            parser.error('unknown field in the selected group')
        fields = [field for field in fields if field['name'] in selected]
    records = exact_tasks(args.output, config, {phase: [(sizes, field) for field in fields for sizes in candidates]},
                          jobs=args.jobs, timeout=args.timeout, slots=args.slots, group=args.group)
    if any(result['status'] != 'complete' for result in records[phase].values()):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
