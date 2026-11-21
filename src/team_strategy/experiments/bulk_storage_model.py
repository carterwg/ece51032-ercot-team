"""Batch-load the instructor's monolithic storage LP in its original order."""

from contextlib import contextmanager
from types import SimpleNamespace


@contextmanager
def bulk_storage_model():
    """Reduce Python-to-HiGHS calls without changing the LP or solver options."""
    from highspy import Highs, HighsStatus
    from tools.activsg2000 import dcopf

    audit = []
    original_factory = dcopf._highs
    original_solve = dcopf.solve_dcopf_horizon

    class BufferedModel(Highs):
        def __init__(self):
            super().__init__()
            self.columns = []
            self.row_bounds = []
            self.starts = []
            self.indices = []
            self.values = []

        def addVariable(self, *, lb, ub, obj, name=None):
            column = SimpleNamespace(index=len(self.columns))
            self.columns.append((obj, lb, ub))
            return column

        def addRow(self, lb, ub, count, indices, values):
            self.row_bounds.append((lb, ub))
            self.starts.append(len(self.indices))
            self.indices.extend(indices)
            self.values.extend(values)

        def getNumRow(self):
            return len(self.row_bounds) if self.row_bounds is not None else super().getNumRow()

        def run(self):
            if self.row_bounds is not None:
                costs, lower, upper = zip(*self.columns, strict=True)
                rows_lower, rows_upper = zip(*self.row_bounds, strict=True)
                columns, rows = len(costs), len(rows_lower)
                if super().addCols(columns, costs, lower, upper, 0, [], [], []) != HighsStatus.kOk:
                    raise RuntimeError('Could not load storage LP columns')
                if super().addRows(rows, rows_lower, rows_upper, len(self.indices),
                                   self.starts, self.indices, self.values) != HighsStatus.kOk:
                    raise RuntimeError('Could not load storage LP rows')
                audit.append({'columns': columns, 'rows': rows})
                self.columns = self.row_bounds = self.starts = self.indices = self.values = None
            return super().run()

    def solve(*args, **kwargs):
        if kwargs.get('_return_model'):
            return original_solve(*args, **kwargs)
        _, status, kind, inf = original_factory()
        dcopf._highs = lambda: (BufferedModel, status, kind, inf)
        try:
            return original_solve(*args, **kwargs)
        finally:
            dcopf._highs = original_factory

    dcopf.solve_dcopf_horizon = solve
    try:
        yield audit
    finally:
        dcopf.solve_dcopf_horizon = original_solve
