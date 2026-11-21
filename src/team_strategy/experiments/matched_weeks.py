"""Reuse identical physical inputs across weeks while re-running official scoring."""
from contextlib import contextmanager
from functools import lru_cache
from pathlib import Path

from ..context import file_fingerprint


@contextmanager
def reuse_identical_week_physics():
    """For fixed portfolios only. S1 and S2 still get distinct site IDs.

    Cache native solve/redispatch calls only if physical CSVs, plans, and
    evaluator options compare equal. The evaluator still reads the actual
    submissions, follows the original projection path, and scores each week.
    """
    from ercot_game import base_load, batch_evaluation
    from tools.activsg2000.dcopf import DCOPFInfeasible, DCOPFUnresolved
    from ..evaluation import campaign
    from ..submissions import csv_export

    def stable_ids(plan, context):
        return tuple(f's{context.round.submission}-{i:04d}' for i in range(1,len(plan.sites)+1))

    @lru_cache(maxsize=4)
    def physics(directory):
        files = tuple(sorted(Path(directory).glob('*.csv')))
        return tuple((path.name,file_fingerprint(path)) for path in files)

    cache = {}
    audit = []

    def share(function, *, is_validation=False):
        def wrapped(directory, *args, **kwargs):
            signature = physics(str(Path(directory).resolve()))
            bucket = cache.setdefault((function.__name__,signature),[])
            for saved_args,saved_kwargs,source,value in bucket:
                if saved_args == args and saved_kwargs == kwargs:
                    audit.append({'operation':function.__name__,'source':str(source),'destination':str(directory)})
                    if isinstance(value,(DCOPFInfeasible,DCOPFUnresolved)):
                        raise type(value)(str(value))
                    return value
            try:
                result=function(directory,*args,**kwargs)
            except (DCOPFInfeasible,DCOPFUnresolved) as error:
                bucket.append((args,kwargs,directory,type(error)(str(error))))
                raise
            if not is_validation or result == ([],[]):
                bucket.append((args,kwargs,directory,result))
            return result
        return wrapped

    originals = [(campaign,'site_ids',campaign.site_ids),(csv_export,'site_ids',csv_export.site_ids),
                 (batch_evaluation,'_dispatch_plans',batch_evaluation._dispatch_plans),
                 (batch_evaluation,'_utilitarian_allocation',batch_evaluation._utilitarian_allocation),
                 (base_load,'_validate_base_load',base_load._validate_base_load)]
    for index,(module,name,function) in enumerate(originals):
        setattr(module,name,stable_ids if index<2 else share(function,is_validation=module is base_load))
    try:
        yield audit
    finally:
        for module,name,function in originals:
            setattr(module,name,function)
