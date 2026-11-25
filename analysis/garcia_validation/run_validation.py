"""Run Garcia candidate hardware through the unchanged instructor evaluator.

Run from the repository root with:
PYTHONPATH=src:ercot-connection-game/src:ercot-connection-game .venv/bin/python \
    analysis/garcia_validation/run_validation.py --case CASE --candidate CANDIDATE

Every result is a full 120-period Submission 1 evaluation, not a campaign.
No allocation, dispatch, numerical-tolerance, or scoring monkeypatch is used.
"""
from __future__ import annotations

import argparse
import csv
from contextlib import nullcontext
from dataclasses import asdict
import json
from pathlib import Path
import subprocess
import sys
import time

from team_strategy.context import file_fingerprint, load_context
from team_strategy.contracts import NamedPlan, Plan, RoundKey, Scenario, SiteProposal
from team_strategy.evaluation.campaign import BatchEvaluator, save_json
from ercot_game.batch_evaluation import _score_team, load_scoring_rules

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / 'runs/garcia-validation'
HOSTING_BUSES = ['1079', '2054', '2127', '3046', '3048']
CANDIDATES = {
    'garcia_g0_2054': ['2054', 0, 0],
    'garcia_g100_2054': ['2054', 100, 0],
    'garcia_g150_2054': ['2054', 150, 0],
    'garcia_g225_2054': ['2054', 225, 0],
    'location_g225_6141': ['6141', 225, 0],
    'ours_g200_6141': ['6141', 200, 0],
    'ours_b196_6141': ['6141', 0, 196],
    'ours_g97_b99_6141': ['6141', 97, 99],
    'ours_b35_6141': ['6141', 0, 35],
}


def case(count, connection, generator, buses, *, battery=0, provenance):
    return {'rival_count': count, 'connection_mw': connection,
            'generator_mw': generator, 'battery_mw': battery,
            'rival_bus_assignment': [buses[i % len(buses)] for i in range(count)],
            'provenance': provenance}


CASES = {
    'garcia11_colocated_g0': case(10, 500, 0, ['2054'], provenance='Garcia colocated case, exact stated equipment and bus'),
    'garcia11_colocated_g200': case(10, 500, 200, ['2054'], provenance='Garcia colocated case, exact stated equipment and bus'),
    **{f'garcia11_diverse_g{g}': case(10, 500, g, HOSTING_BUSES,
       provenance='Reconstruction: Garcia rival equipment/count; explicit cyclic siting at our five hosting buses, absent from his upload')
       for g in (0, 100, 200, 250)},
    'garcia11_diverse_c300g200': case(10, 300, 200, HOSTING_BUSES,
       provenance='Reconstruction: Garcia rival equipment/count; explicit cyclic siting at our five hosting buses, absent from his upload'),
    **{f'ours10_same6141_g{g}': case(9, 500, g, ['6141'],
       provenance='Exact existing ten-team field: nine_grid_at_6141' if not g else 'Exact existing ten-team field: nine_g200_at_6141')
       for g in (0, 200)},
    'ours10_same6141_g50_b175': case(9, 500, 50, ['6141'], battery=175,
       provenance='Exact existing adverse ten-team field: nine_g50_b175_at_6141'),
}
CASES.update({name.replace('garcia11_', 'garcia10_'):{**field,
    'rival_count':9,'rival_bus_assignment':field['rival_bus_assignment'][:9],
    'provenance':'Corrected ten-team game: nine rivals, Garcia equipment assumptions; '
                 + ('all rivals at 2054' if 'colocated' in name else
                    'explicit cyclic placement at 1079, 2054, 2127, 3046, 3048 (his assignments were not uploaded)')}
    for name,field in list(CASES.items()) if name.startswith('garcia11_')})


def plan(bus, connection, generator, battery):
    return Plan((SiteProposal(bus, connection, generator, battery, battery * 4),))


def execute(case_name, candidate_name, week, workers, backend, storage_solver, allocation_solver='course'):
    field, candidate = CASES[case_name], CANDIDATES[candidate_name]
    suffix='' if allocation_solver=='course' else '-gurobi-allocation-qp'
    destination = OUTPUT / case_name / candidate_name / f'week-{week}-{backend}-{storage_solver}{suffix}'
    destination.mkdir(parents=True, exist_ok=False)
    job = {'case': case_name, 'field': field, 'candidate': candidate_name,
           'equipment': candidate, 'week': week, 'workers': workers,
           'solver_backend': backend, 'storage_solver': storage_solver,
           'evaluator_overrides': [] if allocation_solver=='course' else ['Fairness QP backend only: Gurobi, same objective and constraints'], 'horizon': 120,
           'git_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
           'source_sha256': {str(p.relative_to(ROOT)): file_fingerprint(p) for p in (
               Path(__file__).resolve(), ROOT/'ercot-connection-game/src/ercot_game/batch_evaluation.py',
               ROOT/'ercot-connection-game/tools/activsg2000/allocation.py',
               ROOT/'ercot-connection-game/tools/activsg2000/dcopf.py')}}
    save_json(destination/'job.json', job)
    selection=ROOT/'analysis/garcia_validation/selected_pairs.json'
    if selection.exists() and [case_name,candidate_name] not in json.loads(selection.read_text())['pairs']:
        save_json(destination/'result.json',{**job,'status':'not_selected',
                  'reason':'Outside the targeted winners and matched benchmark comparison'})
        print(json.dumps({'case':case_name,'candidate':candidate_name,'status':'not_selected'}),flush=True)
        return
    if allocation_solver=='course' and storage_solver=='benders':
        other=destination.parent/f'week-{week}-{backend}-monolithic'/'result.json'
        if other.exists():
            saved=json.loads(other.read_text())
            if saved['status']=='complete' and not saved['evaluator_overrides']:
                save_json(destination/'result.json',{**job,'status':'resolved_elsewhere',
                          'result_path':str(other),'reason':'Already completed with the supported official monolithic solver'})
                print(json.dumps({'case':case_name,'candidate':candidate_name,'status':'resolved_elsewhere'}),flush=True)
                return
    start = time.monotonic()
    context = load_context(release_file=ROOT/'configs/rounds/finalized_release_500mw.json',
        rules_file=ROOT/'configs/scoring/dispatch_scoring_rules_500mw.json',
        scenario_dir=ROOT/'ercot-connection-game/data/processed/activsg2000_representative_v1',
        round=RoundKey(week, 1), team_id='our-team', seed=20261121)
    opponents = tuple(NamedPlan(f'rival-{i:02d}', plan(bus, field['connection_mw'],
                      field['generator_mw'], field['battery_mw']))
                      for i, bus in enumerate(field['rival_bus_assignment'], 1))
    try:
        solver=nullcontext([])
        if allocation_solver=='gurobi':
            from team_strategy.experiments.no_storage_allocation import alternate_quadratic_solver
            solver=alternate_quadratic_solver()
            save_json(destination/'alternate_solver_source.json', {
                'source':'src/team_strategy/experiments/no_storage_allocation.py',
                'sha256':file_fingerprint(ROOT/'src/team_strategy/experiments/no_storage_allocation.py')})
        with solver as qp_audit:
            try:
                outcome = BatchEvaluator(destination/'evaluation', workers=workers,
                    solver_backend=backend, storage_solver=storage_solver).evaluate_round(
                        context=context, our_plan=plan(*[candidate[0], 500, candidate[1], candidate[2]]),
                        scenario=Scenario(case_name, opponents, 20261121))
            finally:
                if allocation_solver=='gurobi':save_json(destination/'allocation_qp_audit.json',qp_audit)
        summary = outcome.summary
        assert summary['horizon'] == 120
        assert len(summary['team_scores']) == field['rival_count'] + 1
        assert all(s['valid'] and s['feasible'] for s in summary['team_scores'])
        scores = summary['team_scores']
        ours = next(s for s in scores if s['team_id']=='our-team')
        allocated_plan = next(p for p in outcome.evaluation.evaluated_plans if p.team_id=='our-team')
        rules = load_scoring_rules(context.rules_file, artifact_dir=context.scenario_dir, horizon=context.horizon)
        week3_score = _score_team(allocated_plan, outcome.evaluation.dispatch, rules,
                                 submission_number=1, energy_cost_enabled=True)
        assert abs(week3_score.score + week3_score.energy_cost - energy_off_score_if(ours, week)) < 1.
        save_json(destination/'week3_same_dispatch_score.json', asdict(week3_score))
        trace = []
        for period in outcome.evaluation.dispatch.periods:
            generator = sum(period.generator_dispatch_mw_by_team['our-team'].values())
            trace.append({'period':period.period_index,
                'load_mw':period.submitted_load_mw_by_team['our-team'],
                'generator_mw':generator,
                'grid_mw':period.grid_purchase_mw_by_team.get('our-team', 0),
                'battery_charge_mw':sum((period.storage_charge_mw_by_team or {}).get('our-team',{}).values()),
                'battery_discharge_mw':sum((period.storage_discharge_mw_by_team or {}).get('our-team',{}).values()),
                'battery_soc_mwh':sum((period.storage_soc_mwh_by_team or {}).get('our-team',{}).values()),
                'lmp_usd_per_mwh':period.dcopf.balance_dual_by_bus.get(candidate[0]),
                'weight_hours':rules.weight_for(period.period_index)})
        with (destination/'our_dispatch.csv').open('w',newline='') as handle:
            writer=csv.DictWriter(handle,fieldnames=trace[0]);writer.writeheader();writer.writerows(trace)
        # This is the exact energy-off score identity when week=3; not a new physical run.
        energy_off_score = ours['score'] + (ours['energy_cost'] if week==3 else 0)
        result = {**job, 'status': 'complete', 'elapsed_seconds': time.monotonic()-start,
                  'score_usd': summary['score_usd'], 'energy_off_score_usd': energy_off_score,
                  'week3_score_usd':week3_score.score, 'week3_grid_cost_usd':week3_score.energy_cost,
                  'week3_method':'Unchanged official _score_team on the same full-horizon joint dispatch, energy_cost_enabled=True',
                  'our_admitted_mw': sum(a['allocated_connection_mw'] for a in summary['site_allocations']),
                  'score_breakdown': summary['score_breakdown'],
                  'scenario_sha256':summary['scenario_sha256'], 'rules_sha256':summary['rules_sha256'],
                  'generator_peak_mw':max(p['generator_mw'] for p in trace),
                  'generator_active_periods':[p['period'] for p in trace if p['generator_mw']>1e-5],
                  'generator_active_annual_hours':sum(p['weight_hours']/rules.present_value_factor for p in trace if p['generator_mw']>1e-5),
                  'result_path': str(destination/'evaluation'/context.round.key/'round.json'),
                  'artifact_sha256': {str(p.relative_to(destination)):file_fingerprint(p)
                                      for p in destination.rglob('*') if p.is_file()}}
    except Exception as exc:
        save_json(destination/'result.json', {**job, 'status':'failed',
            'elapsed_seconds':time.monotonic()-start, 'error':f'{type(exc).__name__}: {exc}'})
        raise
    save_json(destination/'result.json', result)
    print(json.dumps({k:result[k] for k in ('case','candidate','status','elapsed_seconds',
                                         'score_usd','our_admitted_mw')}), flush=True)


def energy_off_score_if(score, week):
    return score['score'] + (score['energy_cost'] if week==3 else 0)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case', choices=CASES)
    parser.add_argument('--candidate', choices=CANDIDATES)
    parser.add_argument('--week', type=int, choices=(2,3), default=2)
    parser.add_argument('--workers', type=int, default=2)
    parser.add_argument('--backend', choices=('highs','gurobi'), default='highs')
    parser.add_argument('--storage-solver', choices=('benders','monolithic'), default='benders')
    parser.add_argument('--allocation-solver', choices=('course','gurobi'),default='course')
    parser.add_argument('--design', action='store_true')
    args = parser.parse_args()
    if args.design:
        print(json.dumps({'candidates':CANDIDATES,'cases':CASES},indent=2))
        return
    if not args.case or not args.candidate:
        parser.error('--case and --candidate are required')
    execute(args.case,args.candidate,args.week,args.workers,args.backend,args.storage_solver,args.allocation_solver)


if __name__ == '__main__':
    main()
