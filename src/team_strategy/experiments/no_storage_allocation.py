"""Solve the instructor's no-storage allocation with hour-by-hour separation.

The instructor day LP separates into hourly LPs when storage is absent. A
positive partial-day sum is already a valid cut. Candidate acceptance still
checks every hour and applies the original per-day shed threshold. The original
capacity objective, quadratic tie-break, scaling, redispatch and scores apply.
"""
from collections import defaultdict
from contextlib import contextmanager
from dataclasses import replace
from functools import lru_cache
import math
from pathlib import Path


@contextmanager
def alternate_quadratic_solver():
    """Retry the same allocation tie-break with an independent QP backend."""
    from tools.activsg2000 import allocation, dcopf

    original = allocation._solve_master
    audit = []
    try:
        import gurobipy as gp
    except ImportError:
        yield audit
        return
    try:
        env = gp.Env(empty=True)
        env.setParam('OutputFlag',0)
        env.start()
    except gp.GurobiError:
        yield audit
        return

    def master(capacities, cuts, *, minimum_total):
        if minimum_total is None:
            return original(capacities,cuts,minimum_total=None)
        with gp.Model(env=env) as model:
            model.Params.Threads = 1
            model.Params.FeasibilityTol = 1e-9
            model.Params.OptimalityTol = 1e-9
            model.Params.BarConvTol = 1e-14
            model.Params.TimeLimit = 15
            fractions = model.addVars(len(capacities),lb=0,ub=1)
            scale = max(capacities)
            weights = [c/scale for c in capacities]
            model.addConstr(gp.quicksum(w*fractions[i] for i,w in enumerate(weights)) >= minimum_total/scale)
            for gradient,rhs in cuts:
                magnitude = max(max(map(abs,gradient),default=0.),abs(rhs),1.)
                model.addConstr(gp.quicksum(g/magnitude*fractions[i] for i,g in enumerate(gradient) if g) <= rhs/magnitude)
            model.setObjective(gp.quicksum(w*(1-fractions[i])*(1-fractions[i]) for i,w in enumerate(weights)))
            model.optimize()
            audit.append({'cuts':len(cuts),'minimum_total_mw':minimum_total,'gurobi_status':model.Status})
            if model.Status == gp.GRB.INFEASIBLE:
                return None
            if model.Status != gp.GRB.OPTIMAL:
                raise dcopf.DCOPFUnresolved(f'Alternate allocation QP status {model.Status}')
            values = [min(1.,max(0.,fractions[i].X)) for i in range(len(capacities))]
            if math.fsum(w*a for w,a in zip(weights,values)) < minimum_total/scale-1e-8:
                raise dcopf.DCOPFUnresolved('Alternate QP failed the allocated capacity floor')
            return values

    allocation._solve_master = master
    try:
        yield audit
    finally:
        allocation._solve_master = original
        env.dispose()


@contextmanager
def separate_independent_hours(*, alternate_dispatch=False):
    from tools.activsg2000 import allocation, dcopf
    from ercot_game import batch_evaluation

    original_pool = allocation._DayPool
    original_dispatch = batch_evaluation._dispatch_plans
    original_solve = dcopf.solve_dcopf
    audit = []

    @lru_cache(maxsize=8)
    def dispatch_model(nodes, generators, branches, base_mva):
        return dcopf.ReusableDCOPFModel(buses=nodes,generators=generators,branches=branches,base_mva=base_mva)

    @lru_cache(maxsize=8)
    def fallback_model(nodes, generations, branches, base_mva):
        model = dcopf.GurobiReusableDCOPFModel(buses=nodes,generators=generations,branches=branches,base_mva=base_mva)
        model._model.Params.FeasibilityTol = 1e-7
        model._model.Params.OptimalityTol = 1e-8
        model._model.Params.Method = 1
        model._model.Params.TimeLimit = 15
        return model

    def solve(*, buses, generators, branches, fixed_injection_mw_by_bus=None, base_mva=1.):
        nodes = tuple(replace(bus,demand_mw=0.) for bus in buses)
        model = dispatch_model(nodes,generators,branches,base_mva)
        # Reuse only matrix construction, with a fresh solve and basis each hour.
        model._highs.clearSolver()
        try:
            return model.solve(buses,fixed_injection_mw_by_bus)
        except (dcopf.DCOPFInfeasible,dcopf.DCOPFUnresolved):
            try:
                return original_solve(buses=buses,generators=generators,branches=branches,
                                      fixed_injection_mw_by_bus=fixed_injection_mw_by_bus,base_mva=base_mva)
            except (dcopf.DCOPFInfeasible,dcopf.DCOPFUnresolved) as original_error:
                if not alternate_dispatch:
                    raise
                fixed = fixed_injection_mw_by_bus or {}
                slack = math.fsum(g.p_max_mw for g in generators)+math.fsum(fixed.values())-math.fsum(b.demand_mw for b in buses)
                if slack < -1e-4:
                    raise
                method = 'HiGHS alternate presolve'
                try:
                    model._highs.clearSolver()
                    model._highs.setOptionValue('presolve','off')
                    model._highs.setOptionValue('primal_feasibility_tolerance',1e-5)
                    alternative = model.solve(buses,fixed)
                except (dcopf.DCOPFInfeasible,dcopf.DCOPFUnresolved):
                    method = 'Gurobi'
                    try:
                        alternative = fallback_model(nodes,generators,branches,base_mva).solve(buses,fixed)
                    except Exception as error:
                        raise original_error from error
                finally:
                    model._highs.setOptionValue('presolve','on')
                    model._highs.setOptionValue('primal_feasibility_tolerance',1e-7)
                balance = {b.bus_id:fixed.get(b.bus_id,0.)-b.demand_mw for b in buses}
                violation = 0.
                for g in generators:
                    p = alternative.generation_mw[g.generator_id]
                    balance[g.bus_id] += p
                    violation = max(violation,g.p_min_mw-p,p-g.p_max_mw)
                for b in branches:
                    flow = alternative.flow_mw_by_branch[b.branch_id]
                    balance[b.from_bus_id] -= flow
                    balance[b.to_bus_id] += flow
                    violation = max(violation,abs(flow)-b.thermal_limit_mw)
                error = max(map(abs,balance.values()))
                if max(error,violation) > 1e-4:
                    raise original_error
                audit.append({'proof':'alternate_physical_dispatch','solver':method,'maximum_balance_error_mw':error,
                              'maximum_limit_violation_mw':violation})
                return alternative

    @lru_cache(maxsize=8)
    def spare_generation(directory, periods):
        artifact = dcopf.load_prepared_artifact(directory)
        if artifact.scenario_year is not None:
            return None
        buses, generations, _, fixed = dcopf._prepared_period_inputs(
            directory,artifact,period_index=periods[0],validate_artifact=False)
        supply = math.fsum(g.p_max_mw for g in generations) + math.fsum(fixed.values())
        bus_ids = [b.bus_id for b in buses]
        return [supply-math.fsum(float(artifact.demand_rows[i][b]) for b in bus_ids) for i in periods]

    def dispatch(directory, plans, period_indices, **kwargs):
        sites = batch_evaluation._allocation_sites(plans,period_indices)
        if sites and not any(s.storage_power_mw or s.storage_energy_mwh for s in sites):
            periods = tuple(kwargs.get('source_period_indices') or period_indices)
            spare = spare_generation(str(Path(directory).resolve()),periods)
            if spare is not None:
                for offset,available in enumerate(spare):
                    least_net = math.fsum(s.load_mw_by_period[offset]-s.generator_mw for s in sites)
                    if least_net > available + 1e-4:
                        audit.append({'directory':str(directory),'proof':'aggregate_generation_shortage',
                                      'period':periods[offset],'native_spare_mw':available,'minimum_new_grid_mw':least_net})
                        raise dcopf.DCOPFInfeasible('Aggregate generation upper bound is below requested load')
        return original_dispatch(directory,plans,period_indices,**kwargs)

    class HourPool:
        def __init__(self, artifact_root, sites, period_indices, blocks, time_step_hours, workers):
            self.fallback = None
            if (workers != 1 or time_step_hours != 1 or any(
                    s.storage_power_mw or s.storage_energy_mwh or
                    any(load != s.load_mw_by_period[0] for load in s.load_mw_by_period) for s in sites)):
                self.fallback = original_pool(artifact_root, sites, period_indices, blocks, time_step_hours, workers)
                return
            artifact = dcopf.load_prepared_artifact(artifact_root)
            periods = [dcopf._prepared_period_inputs(artifact_root, artifact, period_index=i, validate_artifact=False)
                       for i in period_indices]
            buses, generators, branches, fixed = periods[0]
            same_network = all(g == generators and l == branches and
                               tuple((b.bus_id,b.reference) for b in bs) == tuple((b.bus_id,b.reference) for b in buses)
                               for bs,g,l,f in periods)
            if not same_network:
                self.fallback = original_pool(artifact_root, sites, period_indices, blocks, time_step_hours, workers)
                return
            self.model = allocation._DayModel([periods[0]],sites,[0],time_step_hours=1.,base_mva=100.)
            # Row order in the instructor's one-hour model: line bounds,
            # private-generator limits, bus balances, private-owner limits.
            self.row_offset = len(branches) + sum(s.generator_mw > 0 for s in sites)
            self.row_indices = list(range(self.row_offset,self.row_offset+len(buses)))
            self.rhs = [[b.demand_mw-f.get(b.bus_id,0.) for b in bs] for bs,g,l,f in periods]
            self.block_by_hour = {hour: day for day,block in enumerate(blocks) for hour in block}
            self.capacity = math.fsum(g.p_max_mw for g in generators)
            self.net = [s.load_mw_by_period[0]-s.generator_mw for s in sites]
            self.order = sorted(range(len(periods)),key=lambda i:-math.fsum(self.rhs[i]))
            self.spare = [self.capacity-math.fsum(row) for row in self.rhs]
            self.active = self.order[0]
            self.ledger = {'directory':artifact_root,'periods':len(periods),'separation_calls':0,
                           'aggregate_cuts':0,'hour_solves':0,'full_horizon_checks':0}
            audit.append(self.ledger)

        def shed(self, alphas):
            if self.fallback:
                return self.fallback.shed(alphas)
            self.ledger['separation_calls'] += 1
            tolerance = allocation.SHED_TOLERANCE_MWH
            # System balance supplies an exact cut if minimum net withdrawals
            # alone exceed spare native Pmax. This objective lower bound is
            # valid for every alpha, even when transmission is tighter.
            net = math.fsum(a*x for a,x in zip(alphas,self.net))
            critical = self.order[0]
            excess = net-self.spare[critical]
            if excess > tolerance:
                self.ledger['aggregate_cuts'] += 1
                return [(excess,self.net)]
            totals = defaultdict(float)
            gradients = {}
            for hour in (self.active,*(i for i in self.order if i!=self.active)):
                rhs = self.rhs[hour]
                self.model.highs.changeRowsBounds(len(rhs),self.row_indices,rhs,rhs)
                value, gradient = self.model.shed(alphas)
                self.ledger['hour_solves'] += 1
                day = self.block_by_hour[hour]
                if value > 0:
                    totals[day] += value
                    previous = gradients.get(day)
                    gradients[day] = gradient if previous is None else [a+b for a,b in zip(previous,gradient)]
                    if totals[day]>tolerance:
                        self.active = hour
                        return [(totals[day], gradients[day])]
            self.ledger['full_horizon_checks'] += 1
            return [(totals.get(day,0.),gradients.get(day,[0.]*len(alphas)))
                    for day in sorted(set(self.block_by_hour.values()))]

        def close(self):
            if self.fallback:
                self.fallback.close()

    allocation._DayPool = HourPool
    batch_evaluation._dispatch_plans = dispatch
    dcopf.solve_dcopf = solve
    try:
        yield audit
    finally:
        allocation._DayPool = original_pool
        batch_evaluation._dispatch_plans = original_dispatch
        dcopf.solve_dcopf = original_solve
