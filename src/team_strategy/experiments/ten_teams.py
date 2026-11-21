"""Run matched ten-team campaigns with the instructor evaluator."""
from argparse import ArgumentParser, SUPPRESS
from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import ExitStack
import itertools
import json
import math
from pathlib import Path
import subprocess
import sys

from ..context import file_fingerprint, scenario_fingerprint
from ..evaluation.allocation_roundoff import (correct_zero_anchor_cuts, omit_zero_generator_columns,
                                              presolve_exact_self_supply, zero_allocation_roundoff)
from ..evaluation.campaign import run_campaign, save_json
from ..strategies.corridor_portfolio import CorridorPortfolio
from .concentration import verify_cell
from . import matched_weeks
from . import no_storage_allocation

ROOT = Path(__file__).resolve().parents[3]
PRIMARY_POLICIES = {'grid': (0., 0.), 's2_cg': (0., 1.), 'both_cg': (1., 1.)}
PARTIAL_POLICIES = {'s1_125_s2_cg': (.25, 1.), 's1_250_s2_cg': (.5, 1.), 's1_375_s2_cg': (.75, 1.)}


def read(path):
    return json.loads(Path(path).read_text())


def define_experiment(root):
    part1 = root / 'analysis/clustering/part1'
    manifest = read(part1 / 'manifest.json')
    verification = part1 / 'verification.json'
    if manifest['verification_status'] != 'passed' or file_fingerprint(verification) != manifest['verification_sha256']:
        raise ValueError('Part 1 verification is missing or changed')
    for name, digest in read(verification)['artifact_sha256'].items():
        if file_fingerprint(part1 / name) != digest:
            raise ValueError(f'Part 1 evidence changed: {name}')
    pools = {b['bus_id']: b for b in manifest['candidate_pool']['candidates']}
    hosting = sorted((b for b in pools if pools[b]['hosting_rank']), key=lambda b: pools[b]['hosting_rank'])[:5]
    group_data = read(part1 / 'groups.json')
    signed = {b: set(signatures) for b, signatures in group_data['signatures'].items()}
    distance = group_data['normalized_ptdf_distances']
    indices = {b: i for i, b in enumerate(group_data['ptdf']['bus_ids'])}
    stress = [s['candidates'] for s in read(part1 / 'stress.json')['scenarios'] if s['status'] == 'valid']
    residual = {b: min(s[b]['minimum_hosting_capacity_mw'] for s in stress) for b in pools}
    eligible = {b for b in pools if residual[b] >= 500.}
    composite_rank = lambda b: (pools[b]['screening_rank'] or math.inf, b)
    diversified = [min(eligible, key=composite_rank)]
    while len(diversified) < 5:
        def separation(bus):
            return (max(len(signed[bus] & signed[old]) / max(1, len(signed[bus] | signed[old]))
                        for old in diversified),
                    -min(distance[indices[bus]][indices[old]] for old in diversified),
                    composite_rank(bus))
        diversified.append(min(eligible.difference(diversified), key=separation))

    def layout(buses):
        return {'bus_ids': buses, 'weights': [1 / len(buses)] * len(buses)}

    def schedule(fractions):
        return dict(zip(('1', '2'), fractions, strict=True))

    layouts = {f'{method}_{count}': layout(buses[:count])
               for (method, buses), count in itertools.product(
                   (('hosting', hosting), ('bottleneck_ptdf', diversified)), (1, 2, 5))}
    scenarios = []
    for name, layout_name, fractions in [
        ('nine_grid_at_6141', 'bottleneck_ptdf_1', (0., 0.)),
        ('nine_grid_at_hosting_1', 'hosting_1', (0., 0.)),
        ('nine_s2_cg_hosting_2', 'hosting_2', (0., 1.)),
        ('nine_both_cg_ptdf_5', 'bottleneck_ptdf_5', (1., 1.)),
    ]:
        rival = {**layouts[layout_name], 'generation_schedule': schedule(fractions)}
        scenarios.append({'name': name, 'rival_count': 9, 'rival_plan': rival,
                          'rival_bus_ids': rival['bus_ids'], 'rival_generator_fraction': fractions[1],
                          'include_in_risk': True})
    portfolios = []
    for name, geometry in layouts.items():
        policies = dict(PRIMARY_POLICIES)
        if name in {'bottleneck_ptdf_1', 'bottleneck_ptdf_5'}:
            policies.update(PARTIAL_POLICIES)
        for policy, fractions in policies.items():
            portfolios.append({'name': f'{name}_{policy}', 'layout': name, 'policy': policy, **geometry,
                               'role': 'primary' if policy in PRIMARY_POLICIES else 'sizing',
                               'generation_schedule': schedule(fractions), 'generator_fraction': fractions[1]})
    return {'schema_version': 1, 'team_count': 10, 'capacity_per_submission_mw': 500, 'seed': 17,
            'part1_directory': str(part1.relative_to(root)),
            'release_file': 'configs/rounds/finalized_release_500mw.json',
            'scenario_directory': 'ercot-connection-game/data/processed/activsg2000_representative_v1',
            'rules_file': 'configs/scoring/dispatch_scoring_rules_500mw.json',
            'candidate_selection': {b: {'minimum_stress_hc_mw': residual[b], 'signed_constraints': sorted(signed[b])}
                                    for b in hosting + diversified},
            'layouts': layouts, 'scenarios': scenarios, 'portfolios': portfolios}


class ScheduledPortfolio:
    def __init__(self, spec):
        self.by_submission = {int(s): CorridorPortfolio(spec['bus_ids'], spec['weights'], fraction)
                              for s, fraction in spec['generation_schedule'].items()}

    def propose(self, context):
        return self.by_submission[context.round.submission].propose(context)


def run_cell(jobfile):
    job = read(jobfile)
    portfolio, scenario = job['portfolio'], job['scenario']
    target = jobfile.parent
    source_order = job['method'] == 'reverse_own_sites'
    if source_order:
        portfolio = {**portfolio, 'bus_ids': portfolio['bus_ids'][::-1], 'weights': portfolio['weights'][::-1]}
    with ExitStack() as stack:
        audit = {'source_sha256': {str(path.relative_to(ROOT)): file_fingerprint(path)
                                  for path in (Path(__file__).resolve(),Path(matched_weeks.__file__).resolve(),
                                               Path(no_storage_allocation.__file__).resolve())}}
        if job['method'] != 'official':
            audit['alternate_quadratic_solver'] = stack.enter_context(no_storage_allocation.alternate_quadratic_solver())
            audit.update({'cut_corrections': stack.enter_context(correct_zero_anchor_cuts()),
                     'exact_presolve': stack.enter_context(presolve_exact_self_supply()),
                     'roundoff': stack.enter_context(zero_allocation_roundoff()),
                     'omitted_zero_columns': stack.enter_context(omit_zero_generator_columns())})
        audit['matched_week_reuse'] = stack.enter_context(matched_weeks.reuse_identical_week_physics())
        audit['hourly_allocation_separation'] = stack.enter_context(
            no_storage_allocation.separate_independent_hours(alternate_dispatch=job['method']!='official'))
        rivals = tuple((f'rival-{i:02d}', ScheduledPortfolio(scenario['rival_plan']))
                       for i in range(1, scenario['rival_count'] + 1))
        try:
            result = run_campaign(strategy=ScheduledPortfolio(portfolio), opponent_strategies=rivals,
                                  scenario_name=scenario['name'], seed=job['seed'], output_dir=target/'campaign',
                                  release_file=ROOT/job['release_file'], scenario_dir=ROOT/job['scenario_directory'],
                                  rules_file=ROOT/job['rules_file'], workers=1, solver_backend='highs')
        finally:
            save_json(target/'execution.json', {'kind': job['method'], **audit})
    output = target/'campaign'
    result.update(portfolio=portfolio['name'], role=portfolio['role'], generation_schedule=portfolio['generation_schedule'],
                  generator_fraction=portfolio['generator_fraction'], include_in_risk=True)
    save_json(output/'campaign.json', result)
    cell = {'status': 'complete', 'output': str(output), 'result': result,
            'artifact_sha256': {str(p.relative_to(output)): file_fingerprint(p) for p in output.rglob('*') if p.is_file()},
            'execution_audit': str(target/'execution.json'),
            'execution_audit_sha256': file_fingerprint(target/'execution.json')}
    if job['method'] != 'official':
        cell['execution_override'] = {'kind': job['method'], 'audit_path': str(target/'execution.json')}
    save_json(target/'cell.json', cell)


def execute_cell(key, job, folder, timeout):
    folder.mkdir(parents=True, exist_ok=True)
    attempts = []
    for method in ('official', 'audited_numerical_retry', 'reverse_own_sites'):
        if method == 'reverse_own_sites' and len(job['portfolio']['bus_ids']) == 1:
            continue
        previous = list(folder.glob('attempt-*'))
        attempt = folder/f'attempt-{len(previous)+1:02d}'
        attempt.mkdir()
        jobfile = attempt/'job.json'
        save_json(jobfile, {**job, 'method': method})
        with (attempt/'evaluation.log').open('w') as log:
            try:
                result = subprocess.run([sys.executable, '-m', 'team_strategy.experiments.ten_teams', '--cell', str(jobfile)],
                                        stdout=log, stderr=subprocess.STDOUT, timeout=timeout, check=False)
                error = f'evaluator exited {result.returncode}'
            except subprocess.TimeoutExpired:
                error = f'evaluator timed out after {timeout}s'
            else:
                if result.returncode == 0:
                    cell = read(attempt/'cell.json')
                    cell['prior_attempts'] = attempts
                    return key, cell
        attempts.append({'method': method, 'error': error, 'log': str(attempt/'evaluation.log')})
        print(f'Retrying {key}: {error} ({method})', flush=True)
    return key, {'status': 'failed', 'error': attempts[-1]['error'], 'prior_attempts': attempts}


def run(output, jobs, timeout, resume):
    config = define_experiment(ROOT)
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=resume)
    spec = output/'experiment.json'
    if resume and spec.exists():
        if config != read(spec): raise ValueError('resume requires the same experiment design')
    else:
        save_json(spec, config)
    identity = {'config_sha256': file_fingerprint(spec),
                'scenario_sha256': scenario_fingerprint(ROOT/config['scenario_directory']),
                'rules_sha256': file_fingerprint(ROOT/config['rules_file']),
                'release_sha256': file_fingerprint(ROOT/config['release_file']),
                'source_sha256': {str(p.relative_to(ROOT)): file_fingerprint(p) for p in (
                    Path(__file__).resolve(), ROOT/'src/team_strategy/evaluation/campaign.py',
                    ROOT/'src/team_strategy/evaluation/allocation_roundoff.py',
                    ROOT/'ercot-connection-game/tools/activsg2000/allocation.py',
                    ROOT/'ercot-connection-game/src/ercot_game/batch_evaluation.py')}}
    if identity['scenario_sha256'] != read(ROOT/config['part1_directory']/'manifest.json')['scenario_sha256']:
        raise ValueError('Part 1 and the ten-team runs must use the same physical network')
    manifest = output/'manifest.json'
    cells_path = output/'cells.json'
    if resume and manifest.exists() and read(manifest)['identity'] != identity:
        raise ValueError('resume requires identical inputs and source')
    cells = read(cells_path) if resume and cells_path.exists() else {}
    save_json(manifest, {'status': 'running', 'identity': identity})
    all_jobs = {}
    for portfolio, scenario in itertools.product(config['portfolios'], config['scenarios']):
        key = f"{portfolio['name']}/{scenario['name']}"
        if key in cells and verify_cell(cells[key]): continue
        all_jobs[key] = {'portfolio': portfolio, 'scenario': scenario, **{k: config[k] for k in (
            'seed', 'release_file', 'scenario_directory', 'rules_file')}}
    total = len(config['portfolios'])*len(config['scenarios'])
    print(f'{total} planned campaigns, {len(all_jobs)} pending, {jobs} concurrent', flush=True)
    with ThreadPoolExecutor(jobs) as pool:
        futures = [pool.submit(execute_cell, key, job, output/'campaigns'/key, timeout)
                   for key, job in all_jobs.items()]
        for future in as_completed(futures):
            key, cell = future.result()
            cells[key] = cell
            save_json(cells_path, cells)
            complete = sum(c['status'] == 'complete' for c in cells.values())
            score = f"${cell['result']['campaign_score_usd']/1e9:.6f}B" if cell['status']=='complete' else cell['error']
            print(f'{complete}/{total} complete | {key}: {score}', flush=True)
    print(f'All attempts processed at {output}', flush=True)
    save_json(manifest, {'status': 'evaluated' if all(c['status']=='complete' for c in cells.values()) else 'partial',
                        'identity': identity, 'artifact_sha256': {'cells.json': file_fingerprint(cells_path)}})


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT/'runs/ten-teams-500mw')
    parser.add_argument('--jobs', type=int, default=6)
    parser.add_argument('--timeout', type=int, default=420, help='seconds per official or retry attempt')
    parser.add_argument('--resume', action='store_true')
    parser.add_argument('--summary', type=Path, default=ROOT/'analysis/strategy/ten-teams-500mw')
    parser.add_argument('--findings', type=Path, default=ROOT/'findings')
    parser.add_argument('--evaluate-only', action='store_true')
    parser.add_argument('--cell', type=Path, help=SUPPRESS)
    args = parser.parse_args()
    if args.cell:
        run_cell(args.cell)
    else:
        run(args.output, args.jobs, args.timeout, args.resume)
        if not args.evaluate_only:
            from .ten_team_report import report
            report(args.output.resolve(),args.summary.resolve(),args.findings.resolve())


if __name__ == '__main__':
    main()
