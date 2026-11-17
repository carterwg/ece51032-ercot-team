# Full-generation baseline

`FullGeneration.propose(context)` requests the whole available connection budget,
sets G = C at every site, and uses no storage. It works for all six submissions;
the four graded submissions contribute to our comparison campaign.

Parameters:

- `site_count`: positive integer, default 1.
- `bus_ids`: optional distinct source bus IDs, one per site. When omitted, choose
  the first `site_count` catalog IDs in lexical order for deterministic behaviour.

The connection budget is split equally, with the final site receiving the
floating-point remainder. Bus choice is intentionally simple; this baseline
establishes a generator-backed capacity comparison rather than a siting claim.

C = G permits full private supply. It does not force off-grid dispatch: the
operator may prefer cheaper grid electricity. Actual scores therefore remain
separate from the analytical full-output lower comparison anchor.

The [executed baseline report](../../notebooks/01_full_generation_baseline.ipynb)
interprets the saved solo campaigns at the default bus 1001, with overviews of
the finalized 500 MW per-submission case.

## Add a teammate's strategy

1. Add a class in `src/team_strategy/strategies/my_strategy.py` whose constructor
   takes parameters and whose `propose(context)` returns a `Plan`.
2. Add it to `STRATEGIES` in `strategies/__init__.py`.
3. Add `configs/strategies/my_strategy.json` with `strategy` and `params` keys.
4. Add focused tests for algorithm-specific assumptions. The common contract
   test automatically exercises every registered strategy with default parameters.
   Keep defaults usable on the small teaching network; load larger inputs explicitly.
5. Explain assumptions, parameters, and observed findings in `docs/strategies/`.

Use the shared validator and CSV exporter. Do not copy the official scoring or
allocation logic into a strategy. For stochastic choices, instantiate an RNG
from `context.seed`; avoid process-global random state.
