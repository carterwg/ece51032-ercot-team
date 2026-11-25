"""Size four-hour S1 storage and generation at bus 6141 in the ten-team game."""
import argparse
import itertools
import math
from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import ExitStack, contextmanager, nullcontext
from dataclasses import dataclass, replace
import fcntl
from pathlib import Path
from random import Random
import subprocess
import sys
import time

from ercot_game.csv_submission import STORAGE_DURATION_HOURS

from ..context import file_fingerprint, load_context, scenario_fingerprint
from ..contracts import NamedPlan, Plan, RoundKey, Scenario, SiteProposal
from ..evaluation.allocation_roundoff import (correct_zero_anchor_cuts, omit_zero_generator_columns,
                                              presolve_exact_self_supply, zero_allocation_roundoff)
from ..evaluation.campaign import BatchEvaluator, run_campaign, save_json
from .bulk_storage_model import bulk_storage_model
from .findings import native_profiles
from .matched_weeks import reuse_identical_week_physics
from .no_storage_allocation import alternate_quadratic_solver, separate_independent_hours
from .ten_teams import ROOT, ScheduledPortfolio, read

BUS = '6141'
CAPACITY_MW = 500
INITIAL = ((0, 125), (50, 75), (75, 50), (100, 25), (125, 0), (200, 0),
           (0, 200), (0, 75), (0, 25), (25, 75), (50, 50), (75, 25), (100, 0), (0, 0))
FIELDS = 'analysis/strategy/ten-teams-500mw/experiment.json'
RIVAL_STORAGE_SEED = 20261120


@dataclass(frozen=True)
class BatteryPlan:
    generator_mw: int
    battery_mw: int
    s1_bus: str = BUS

    @property
    def key(self):
        suffix = '' if self.s1_bus == BUS else f'_bus{self.s1_bus}'
        return f'g{self.generator_mw}_p{self.battery_mw}{suffix}'

    def propose(self, context):
        if context.round.submission == 2:
            return Plan((SiteProposal(BUS, CAPACITY_MW, CAPACITY_MW),))
        return Plan((SiteProposal(self.s1_bus, CAPACITY_MW, self.generator_mw, self.battery_mw,
                                  self.battery_mw * STORAGE_DURATION_HOURS),))


class RivalPortfolio(ScheduledPortfolio):
    def __init__(self, spec):
        super().__init__(spec)
        self.storage_schedule = spec.get('storage_power_schedule', {})

    def propose(self, context):
        plan = super().propose(context)
        total_power = self.storage_schedule.get(str(context.round.submission), 0.)
        sites = []
        for site in plan.sites:
            power = total_power * site.connection_mw / context.connection_budget_mw
            sites.append(replace(site, storage_power_mw=power, storage_energy_mwh=power*STORAGE_DURATION_HOURS))
        return Plan(tuple(sites))


def has_storage(sizes, field):
    return bool(sizes[1] or any(field['rival_plan'].get('storage_power_schedule', {}).values()))


@contextmanager
def storage_slot(output, count=4):
    """Limit simultaneous large daily LPs across concurrent sweep phases."""
    slots = output/'solver-slots'
    slots.mkdir(exist_ok=True)
    while True:
        for index in range(count):
            with (slots/str(index)).open('a') as handle:
                try:
                    fcntl.flock(handle,fcntl.LOCK_EX|fcntl.LOCK_NB)
                except BlockingIOError:
                    continue
                yield
                return
        time.sleep(2)


def native_interval_cuts(sites, blocks, period_indices, spare):
    """Bound net withdrawals using native generation and daily storage cycles."""
    for day in blocks:
        for start in range(len(day)):
            for end in range(start + 1, len(day) + 1):
                hours = day[start:end]
                periods = tuple(period_indices[i] for i in hours)
                rhs = math.fsum(spare[period] for period in periods)
                gradient = []
                for site in sites:
                    power, energy = site.storage_power_mw, site.storage_energy_mwh
                    usable = 0. if len(hours) == len(day) else min(
                        len(hours)*power, energy, energy/2+start*power, energy/2+(len(day)-end)*power
                    )
                    gradient.append(math.fsum(site.load_mw_by_period[i] for i in hours)
                                    - len(hours)*site.generator_mw - usable)
                yield periods, rhs, gradient


@contextmanager
def storage_feasibility_bounds():
    """Certify some infeasible proposals before assembling the official daily LPs."""
    from ercot_game import batch_evaluation
    from tools.activsg2000 import allocation, dcopf

    dispatch = batch_evaluation._dispatch_plans
    pool_type = allocation._DayPool
    audit = {'full_dispatch_shortcuts': [], 'interval_cuts': 0, 'days_solved': 0}

    def bounded_dispatch(directory, plans, period_indices, **kwargs):
        sites = batch_evaluation._allocation_sites(plans, period_indices)
        if any(site.storage_power_mw > 0 for site in sites):
            source = kwargs.get('source_period_indices') or period_indices
            spare = native_profiles(str(directory))
            for offset, period in enumerate(source):
                lower_bound = math.fsum(site.load_mw_by_period[offset] - site.generator_mw - site.storage_power_mw
                                        for site in sites)
                if lower_bound > spare[period] + 1e-4:
                    audit['full_dispatch_shortcuts'].append({'period': period, 'grid_mw_lower_bound': lower_bound,
                                                              'native_spare_mw': spare[period]})
                    raise dcopf.DCOPFInfeasible('Full requests exceed generation even at maximum battery discharge')
            if (kwargs.get('storage_boundary_mode') == 'daily_exact_cycle'
                and kwargs.get('time_step_hours', 1.) == 1. and len(source) % 24 == 0):
                blocks = [tuple(range(start, start+24)) for start in range(0, len(source), 24)]
                for periods, rhs, gradient in native_interval_cuts(sites, blocks, source, spare):
                    required = math.fsum(gradient)
                    if required-rhs > allocation.SHED_TOLERANCE_MWH:
                        audit['full_dispatch_shortcuts'].append({'interval': periods, 'grid_mwh_lower_bound': required,
                                                                  'native_spare_mwh': rhs})
                        raise dcopf.DCOPFInfeasible('Full requests exceed available daily storage energy')
        return dispatch(directory, plans, period_indices, **kwargs)

    class StorageDayPool:
        def __init__(self, directory, sites, period_indices, blocks, time_step_hours, workers):
            self.fallback = None
            if not (workers == 1 and time_step_hours == 1 and any(s.storage_power_mw for s in sites)):
                self.fallback = pool_type(directory, sites, period_indices, blocks, time_step_hours, workers)
                return
            self.directory, self.sites, self.period_indices = directory, sites, period_indices
            self.blocks = blocks
            self.models = {}
            spare = native_profiles(str(directory))
            self.priority = sorted(range(len(blocks)), key=lambda d: min(spare[period_indices[i]] for i in blocks[d]))
            self.cuts = [(rhs, gradient) for _, rhs, gradient in
                         native_interval_cuts(sites, blocks, period_indices, spare)]

        def shed(self, alphas):
            if self.fallback is not None:
                return self.fallback.shed(alphas)
            # Summing nodal balances over a contiguous interval gives a valid
            # lower bound on that day's shed, even with perfect transmission.
            best, gradient = max(((math.fsum(a*g for a,g in zip(alphas, gradient, strict=True))-rhs, gradient)
                                  for rhs,gradient in self.cuts), key=lambda cut: cut[0])
            if best > allocation.SHED_TOLERANCE_MWH:
                audit['interval_cuts'] += 1
                return [(best, gradient)]
            results = []
            for day in self.priority:
                if day not in self.models:
                    self.models[day] = allocation._build_day(self.directory, self.sites, self.period_indices,
                                                             self.blocks[day], 1.)
                result = self.models[day].shed(alphas)
                audit['days_solved'] += 1
                if result[0] > allocation.SHED_TOLERANCE_MWH:
                    return [result]
                results.append(result)
            return results

        def close(self):
            if self.fallback is not None:
                self.fallback.close()
            else:
                self.models.clear()

    batch_evaluation._dispatch_plans = bounded_dispatch
    allocation._DayPool = StorageDayPool
    try:
        yield audit
    finally:
        batch_evaluation._dispatch_plans = dispatch
        allocation._DayPool = pool_type


def run_job(path):
    job = read(path)
    if has_storage(job['sizes'], job['field']) and not job.get('parent_holds_storage_slot'):
        with storage_slot(path.parents[4]):
            run_locked_job(path,job)
    else:
        run_locked_job(path,job)


def run_locked_job(path, job):
    config, field = job['config'], job['field']
    plan = BatteryPlan(*job['sizes'], s1_bus=job.get('s1_bus', BUS))
    rivals = tuple((f'rival-{i:02d}', RivalPortfolio(field['rival_plan'])) for i in range(1, 10))
    target = path.parent
    output = target/'evaluation'
    inputs = dict(release_file=ROOT/config['release_file'], scenario_dir=ROOT/config['scenario_directory'],
                  rules_file=ROOT/config['rules_file'], seed=config['seed'])
    audit = {'method': job['method'], 'source_sha256': file_fingerprint(Path(__file__))}
    with ExitStack() as stack:
        try:
            if job['method'] != 'plain':
                audit['tie_break'] = stack.enter_context(alternate_quadratic_solver())
                audit['cuts'] = stack.enter_context(correct_zero_anchor_cuts())
                audit['roundoff'] = stack.enter_context(zero_allocation_roundoff())
                audit['pruned_zero_generators'] = stack.enter_context(omit_zero_generator_columns())
                audit['exact_presolve'] = stack.enter_context(presolve_exact_self_supply())
            audit['week_reuse'] = stack.enter_context(reuse_identical_week_physics())
            audit['no_storage'] = stack.enter_context(separate_independent_hours(alternate_dispatch=job['method'] != 'plain'))
            if job['method'] == 'audited':
                audit['batched_storage_matrix'] = stack.enter_context(bulk_storage_model())
            if job['method'] != 'original_day_order':
                audit['storage'] = stack.enter_context(storage_feasibility_bounds())
            if job['phase'] == 'campaign':
                result = run_campaign(strategy=plan, opponent_strategies=rivals, scenario_name=field['name'],
                                      output_dir=output, storage_solver='monolithic', **inputs)
            else:
                context = load_context(**inputs, round=RoundKey(3, 1), team_id='our-team')
                opponents = tuple(NamedPlan(team, rival.propose(replace(context, team_id=team))) for team,rival in rivals)
                round_result = BatchEvaluator(output, storage_solver='monolithic').evaluate_round(
                    context=context, our_plan=plan.propose(context), scenario=Scenario(field['name'],opponents,config['seed']))
                result = {'status':'complete', 'rounds':[round_result.summary]}
        finally:
            save_json(target/'execution.json', audit)
    result.update({'sizes':job['sizes'], 's1_bus':plan.s1_bus, 'field':field['name'],
                   'phase':job['phase'], 'output':str(output),
                   'execution':str(target/'execution.json'),
                   'artifact_sha256': {str(p.relative_to(output)):file_fingerprint(p) for p in output.rglob('*') if p.is_file()}})
    save_json(target/'result.json', result)


def challenge_fields(config):
    """Check whether the apparent benefit survives rivals with partial backup."""
    return [
        {**scenario, 'name': name, 'rival_plan': {**scenario['rival_plan'], 'generation_schedule': {'1':gen/500, '2':1.}},
         'rival_generator_fraction':1.}
        for source,name,gen in [('nine_grid_at_6141','nine_g125_at_6141',125),
                                ('nine_both_cg_ptdf_5','nine_g150_ptdf_5',150),
                                ('nine_grid_at_6141','nine_g200_at_6141',200)]
        for scenario in config['scenarios'] if scenario['name'] == source
    ]


def rival_storage_fields(config, *, randomized=False):
    """Matched rivals with four-hour S1 batteries and new C = G sites in S2."""
    sources = {scenario['name']:scenario for scenario in config['scenarios']}
    shared_bus = 'nine_grid_at_6141'
    five_sites = 'nine_both_cg_ptdf_5'
    cases = (
        ('nine_b125_at_6141', shared_bus, 0, 125),
        ('nine_b196_at_6141', shared_bus, 0, 196),
        ('nine_b150_ptdf_5', five_sites, 0, 150),
        ('nine_g75_b125_at_6141', shared_bus, 75, 125),
    )
    if randomized:
        two_sites = 'nine_s2_cg_hosting_2'
        # Sample one pair from each band so the draw covers weak and strong
        # backups in both clustered and dispersed layouts.
        bands = (
            (shared_bus, (20, 65), (25, 90)),
            (shared_bus, (30, 90), (135, 225)),
            (shared_bus, (65, 120), (100, 155)),
            (shared_bus, (130, 185), (25, 80)),
            (shared_bus, (160, 225), (90, 155)),
            (shared_bus, (150, 225), (155, 220)),
            (two_sites, (40, 90), (80, 145)),
            (two_sites, (150, 220), (100, 200)),
            (five_sites, (20, 80), (120, 205)),
            (five_sites, (90, 180), (45, 110)),
        )
        rng = Random(RIVAL_STORAGE_SEED)
        cases = [
            (f'nine_random_storage_{index:02d}', source,
             rng.randrange(g_min, g_max + 1, 5), rng.randrange(p_min, p_max + 1, 5))
            for index, (source, (g_min, g_max), (p_min, p_max)) in enumerate(bands, 1)
        ]
    fields = []
    for name, source, generator, power in cases:
        template = sources[source]
        rival = dict(template['rival_plan'], generation_schedule={'1':generator/CAPACITY_MW,'2':1.},
                     storage_power_schedule={'1':power,'2':0.})
        fields.append(dict(template, name=name, rival_plan=rival, rival_generator_fraction=1.))
        if randomized:
            fields[-1]['rival_storage_seed'] = RIVAL_STORAGE_SEED
    return fields


def execute(output, config, field, sizes, phase, timeout, *, storage_slots=4, s1_bus=BUS):
    key = BatteryPlan(*sizes, s1_bus=s1_bus).key+'/'+field['name']
    directory = output/phase/key
    directory.mkdir(parents=True, exist_ok=True)
    attempts = []
    storage = has_storage(sizes, field)
    for method in ('audited', 'original_day_order'):
        attempt = directory/f'attempt-{len(list(directory.glob("attempt-*")))+1:02d}'
        attempt.mkdir()
        job = attempt/'job.json'
        save_json(job, {'config':config, 'field':field, 'sizes':list(sizes), 's1_bus':s1_bus,
                        'phase':phase, 'method':method,
                        'parent_holds_storage_slot':storage})
        log = attempt/'evaluation.log'
        # Start the solver timeout after acquiring a slot so queued cases have
        # the same evaluation time budget as cases that start immediately.
        slot = storage_slot(output, storage_slots) if storage else nullcontext()
        with slot, log.open('w') as handle:
            try:
                proc = subprocess.run([sys.executable, '-m', 'team_strategy.experiments.battery_s1', '--job', str(job)],
                                      stdout=handle, stderr=subprocess.STDOUT, timeout=timeout, check=False)
                if proc.returncode == 0:
                    return key, {**read(attempt/'result.json'), 'prior_attempts':attempts}
                error = f'exit {proc.returncode}'
            except subprocess.TimeoutExpired:
                error = f'timeout after {timeout}s'
        attempts.append({'method':method, 'log':str(log), 'error':error})
        print(f'Retry {phase} {key}: {error}', flush=True)
    return key, {'status':'failed', 'sizes':list(sizes), 's1_bus':s1_bus, 'field':field['name'],
                 'phase':phase, 'prior_attempts':attempts}


def run(output, candidates, phase, jobs, timeout, fields=None):
    config = read(ROOT/FIELDS)
    if phase in {'stress','stress_campaign','refined','finalists'}:
        challenge = challenge_fields(config)
        config['scenarios'] = challenge if phase.startswith('stress') else config['scenarios']+challenge
    if phase.startswith('rival_storage'):
        config['scenarios'] = rival_storage_fields(config, randomized=phase=='rival_storage_randomized')
    if fields:
        names = {s['name'] for s in config['scenarios']}
        if not set(fields)<=names:
            raise ValueError(f'Unknown field: {set(fields)-names}')
        config['scenarios'] = [s for s in config['scenarios'] if s['name'] in fields]
    runtime_phase = 'campaign' if phase.endswith('campaign') or phase=='finalists' else 'sweep'
    output.mkdir(parents=True, exist_ok=True)
    identity = {'config_sha256':file_fingerprint(ROOT/FIELDS),
                'scenario_sha256':scenario_fingerprint(ROOT/config['scenario_directory']),
                'rules_sha256':file_fingerprint(ROOT/config['rules_file']),
                'release_sha256':file_fingerprint(ROOT/config['release_file'])}
    manifest = output/'manifest.json'
    if manifest.exists():
        if read(manifest) != identity:
            raise ValueError('experiment inputs changed')
    else:
        save_json(manifest, identity)
    results = output/f'{phase}.json'
    cells = read(results) if results.exists() else {}
    pending = [(sizes, field) for sizes,field in itertools.product(candidates,config['scenarios'])
               if cells.get(BatteryPlan(*sizes).key+'/'+field['name'],{}).get('status') != 'complete']
    print(f'{phase}: {len(pending)} cases pending', flush=True)
    with ThreadPoolExecutor(jobs) as pool:
        futures = [pool.submit(execute,output,config,field,sizes,runtime_phase,timeout) for sizes,field in pending]
        for future in as_completed(futures):
            key, cell = future.result()
            cells[key] = cell
            save_json(results, cells)
            message = (f"S1 {500*next(x for x in cell['rounds'] if x['round'].endswith('1'))['service_fraction']:.6f} MW"
                       if cell['status']=='complete' else 'failed')
            print(f'{phase} {key} {message}', flush=True)
    return cells


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT/'runs/battery-s1-500mw')
    parser.add_argument('--phase', choices=('sweep','campaign','stress','stress_campaign','refined','finalists',
                                           'rival_storage','rival_storage_campaign','rival_storage_sizing_campaign',
                                           'rival_storage_randomized'), default='sweep')
    parser.add_argument('--candidate', nargs=2, type=int, action='append', metavar=('GEN_MW','BATTERY_MW'))
    parser.add_argument('--field', action='append')
    parser.add_argument('--jobs', type=int, default=6)
    parser.add_argument('--timeout', type=int, default=360)
    parser.add_argument('--job', type=Path, help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.job:
        run_job(args.job)
    else:
        if args.phase != 'sweep' and not args.candidate:
            parser.error('this phase requires explicit candidates')
        run(args.output.resolve(), tuple(map(tuple,args.candidate)) if args.candidate else INITIAL,
            args.phase,args.jobs,args.timeout,args.field)


if __name__ == '__main__':
    main()
