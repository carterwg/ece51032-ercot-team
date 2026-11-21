"""Independent snapshot diagnostics for findings, without changing saved scores.

Minimize our private generation at the recorded admitted loads, allowing native
and rival generation to redispatch within their admitted caps. For curtailed
sites, maximize grid-only load at one site, holding our other sites' recorded
net withdrawals fixed. These are hourly diagnostics, not new game allocations.
"""
from dataclasses import replace
import hashlib
import json
import math
from pathlib import Path

from ..clustering.bottlenecks import HostingLP
from ..context import file_fingerprint
from ..evaluation.campaign import save_json

TOL_MW = 1e-4


def check_solution(model, own_ids=()):
    """Independently check the diagnostic's nodal balance, bounds, and duality."""
    period = model.period
    values, _, shadows, dual = model._snapshot()
    balance = {b.bus_id: period.fixed_injection_mw_by_bus.get(b.bus_id, 0.)-b.demand_mw for b in period.buses}
    angles = {b: 0. if col is None else values[int(col.index)]/model.model._angle_scale
              for b,col in model.model._angle_columns.items()}
    bound_error, objective = 0., 0.
    for g in period.generators:
        output = values[int(model.model._generator_columns[g.generator_id].index)]
        balance[g.bus_id] += output
        bound_error = max(bound_error, g.p_min_mw-output, output-g.p_max_mw)
        if g.generator_id in own_ids: objective += output
    lines = []
    for i,b in enumerate(period.branches):
        flow = b.susceptance_pu*(angles[b.from_bus_id]-angles[b.to_bus_id])
        balance[b.from_bus_id] -= flow; balance[b.to_bus_id] += flow
        bound_error = max(bound_error, abs(flow)-b.thermal_limit_mw)
        for direction, sign, shadow in [('upper',1.,shadows[i][0]),('lower',-1.,shadows[i][1])]:
            if abs(flow-sign*b.thermal_limit_mw) <= TOL_MW:
                lines.append({'branch_id': b.branch_id, 'direction': direction, 'flow_mw': flow,
                              'limit_mw': b.thermal_limit_mw, 'shadow_mw_per_mw': max(0.,shadow)})
    error = max(abs(v) for v in balance.values())
    gap = abs(objective-dual)
    if max(error,bound_error,gap) > TOL_MW:
        raise ValueError(f'diagnostic solution failed independent checks: {error}, {bound_error}, {gap}')
    return {'value_mw': max(0.,objective), 'tight_lines': lines, 'max_balance_error_mw': error,
            'max_limit_violation_mw': max(0.,bound_error), 'duality_gap_mw': gap}


def solve_snapshot(period, mode, own_ids=(), target_bus=None):
    model = HostingLP(period, solver_backend='highs')
    tolerance = 1e-9
    try:
        model.set_period(period)
    except RuntimeError as error:
        if 'Infeasible' not in str(error): raise
        # Zero-headroom snapshots can be rejected by simplex presolve with the
        # stricter tolerance. Retry identical equations/bounds; accept only if
        # the independent physical and duality checks still pass at 1e-4 MW.
        tolerance = 1e-5
        model = HostingLP(period, solver_backend='highs')
        model.solver.setOptionValue('primal_feasibility_tolerance',tolerance)
        model.set_period(period)
    if mode == 'hosting':
        d = model.diagnose(target_bus)
        return {'solver_primal_tolerance_mw':tolerance,
                'value_mw': d.hosting_capacity_mw, 'generation_headroom_mw': d.generation_headroom_mw,
                'limiting_resource': d.limiting_resource,
                'tight_lines': [{'branch_id':l.branch_id,'direction':l.direction,'flow_mw':l.flow_mw,
                                 'limit_mw':l.limit_mw,'shadow_mw_per_mw':l.capacity_shadow_mw_per_mw}
                                for l in d.tight_lines],
                'max_balance_error_mw':d.max_balance_error_mw,
                'max_limit_violation_mw':d.max_limit_violation_mw,'duality_gap_mw':d.duality_gap_mw}
    if mode != 'minimum_private': raise ValueError('unknown diagnostic objective')
    for g in own_ids:
        model.solver.changeColCost(int(model.model._generator_columns[g].index),1.)
    model._run()
    return {**check_solution(model, own_ids),'solver_primal_tolerance_mw':tolerance}


class SnapshotDiagnostics:
    def __init__(self, root, potential_signatures):
        self.directory = Path(root)/'runs/findings-diagnostics/probes'
        self.directory.mkdir(parents=True,exist_ok=True)
        self.potential_signatures = set(potential_signatures)
        from ..clustering import bottlenecks
        from tools.activsg2000 import dcopf
        self.sources = {str(p):file_fingerprint(p) for p in [Path(__file__),Path(bottlenecks.__file__),Path(dcopf.__file__)]}
        self.count = 0

    def probe(self, period, mode, *, own_ids=(), target_bus=None, generation_lower_bound=0.):
        numerical = {'buses':[(b.bus_id,b.demand_mw,b.reference) for b in period.buses],
            'generators':[(g.generator_id,g.bus_id,g.p_min_mw,g.p_max_mw) for g in period.generators],
            'branches':[(b.branch_id,b.from_bus_id,b.to_bus_id,b.susceptance_pu,b.thermal_limit_mw) for b in period.branches],
            'fixed':dict(period.fixed_injection_mw_by_bus), 'mode':mode,'own_ids':sorted(own_ids),'target':target_bus,
            'sources':self.sources,'potential':sorted(self.potential_signatures)}
        key = hashlib.sha256(json.dumps(numerical,sort_keys=True,allow_nan=False).encode()).hexdigest()
        output = self.directory/(key+'.json')
        if output.exists():
            result = json.loads(output.read_text())
            return {**result,'period_index':period.period_index,'evidence_path':str(output)}
        self.count += 1
        result = {'period_index':period.period_index,'objective':mode,'target_bus':target_bus,
                  'status':'unresolved','line_relaxations':[],'model_sha256':key,'source_sha256':self.sources}
        try:
            baseline = solve_snapshot(period,mode,own_ids,target_bus)
            result.update(status='verified',**baseline)
            # A tight line alone does not prove causality. Re-solve after a
            # one-MW rating increase, holding every admitted load/cap fixed.
            improvable = (baseline['value_mw'] > generation_lower_bound+TOL_MW if mode=='minimum_private'
                          else baseline['value_mw'] < baseline['generation_headroom_mw']-TOL_MW)
            candidates = sorted(baseline['tight_lines'],key=lambda l:(
                f"{l['branch_id']}:{l['direction']}" not in self.potential_signatures,-l['shadow_mw_per_mw'],l['branch_id']))
            candidates = [l for l in candidates if l['shadow_mw_per_mw']>1e-7
                          or f"{l['branch_id']}:{l['direction']}" in self.potential_signatures]
            ids = list(dict.fromkeys(l['branch_id'] for l in candidates))[:3] if improvable else []
            batches = [[bid] for bid in ids]
            if len(ids)>1: batches.append(ids)
            for batch in batches:
                altered = replace(period,branches=tuple(replace(b,thermal_limit_mw=b.thermal_limit_mw+1.)
                    if b.branch_id in batch else b for b in period.branches))
                try:
                    relaxed = solve_snapshot(altered,mode,own_ids,target_bus)
                    gain = (baseline['value_mw']-relaxed['value_mw'] if mode=='minimum_private'
                            else relaxed['value_mw']-baseline['value_mw'])
                    if gain < -TOL_MW: raise ValueError('relaxation made objective worse beyond tolerance')
                    result['line_relaxations'].append({'branch_ids':batch,'rating_increase_mw':1.,'status':'verified',
                        'value_before_mw':baseline['value_mw'],'value_after_mw':relaxed['value_mw'],
                        'improvement_mw':max(0.,gain),'causal_effect_observed':gain>TOL_MW,
                        'max_balance_error_mw':relaxed['max_balance_error_mw'],
                        'max_limit_violation_mw':relaxed['max_limit_violation_mw'],'duality_gap_mw':relaxed['duality_gap_mw']})
                except Exception as error:
                    result['line_relaxations'].append({'branch_ids':batch,'status':'unresolved','error':str(error)})
        except Exception as error:
            result['error'] = str(error)
        save_json(output,result)
        return {**result,'evidence_path':str(output)}


def added_generators(requests, site_rows, *, include_ours=True):
    """Private caps scale with admitted C; no storage or exports are introduced."""
    from tools.activsg2000.dcopf import Generator
    by_site = {(r['team_id'],r['site_id']):r for r in site_rows}
    generators, own = [], []
    for key,request in sorted(requests.items()):
        if not include_ours and key[0]=='our-team': continue
        row = by_site.get(key)
        if row is None: continue
        c = float(row['load_mw']);requested_c = float(request['connection_capacity_mw'])
        cap = float(request['generator_capacity_mw'])*c/requested_c if requested_c else 0.
        if cap <= 0.: continue
        # Names are independent of week/site-row order, enabling exact numeric
        # cache reuse across equivalent W2 and W3 snapshots.
        identifier = f'findings:{key[0]}:{request["bus_id"]}'
        generators.append(Generator(identifier,request['bus_id'],0.,cap,0.))
        if key[0]=='our-team': own.append(identifier)
    return tuple(generators),tuple(own)


def make_period(native, site_rows, requests, *, mode='minimum_private', target_bus=None):
    extra = {}
    for r in site_rows:
        bus = r['bus_id']
        if mode=='hosting' and r['team_id']=='our-team':
            if bus==target_bus: continue
            amount = float(r['net_withdrawal_mw'])
        else: amount = float(r['load_mw'])
        if amount < -TOL_MW: raise ValueError('unexpected private export in snapshot')
        extra[bus] = extra.get(bus,0.)+max(0.,amount)
    generators, own = added_generators(requests,site_rows,include_ours=mode!='hosting')
    period = replace(native,buses=tuple(replace(b,demand_mw=b.demand_mw+extra.get(b.bus_id,0.)) for b in native.buses),
                     generators=tuple(native.generators)+generators)
    return period,own
