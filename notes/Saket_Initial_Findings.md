# Saket Initial Findings for the 500 MW Game

**Prepared by:** Saket  
**Date:** November 16, 2026  
**Scope:** Full instructor-evaluator runs for two solo strategies at the finalized
500 MW per-team, per-submission limit.

Moving the same C = G plan from bus 1001 to Carter's rank-1 bus 6141 increased
the combined graded score from **$55.271B to $67.955B**, a **22.95% improvement**.
Both strategies received full allocation. The gain came from lower operating
costs, showing that siting matters even when private generation can cover the
entire requested load. These runs establish a solo benchmark; competition is
the next question to test.

## 1. Experiment setup

| Setting | Value |
| --- | --- |
| Network | ACTIVSg2000 representative package |
| Horizon | All 120 periods, comprising five representative days |
| Connection request | One new 500 MW site in each graded submission |
| Private generation | G = C = 500 MW at each new site |
| Batteries | None |
| Competing teams | None |
| Graded scores included | W2S1, W2S2, W3S1, W3S2 |
| Submission 2 base | Original base plus the corresponding S1 hourly net grid withdrawal |
| Weekly reset | Week 3 starts again from the original representative base |
| Grid-energy charge | None in Week 2; joint-dispatch LMP settlement in Week 3 |
| Solver | HiGHS through the instructor evaluator |

The baseline used **bus 1001**, the first catalog ID in lexical order. It was a
simple reference, not an optimized siting decision. The second strategy used
**bus 6141**, which ranks first by composite score in Carter's
[bus-screening analysis](../analysis/bus_screening_metrics.csv). Capacity,
generation, battery size, and evaluation settings were held constant. Each
strategy's S2 base followed its own S1 dispatch.

Every submission contained a new site ID. S1 sites were carried as fixed net
withdrawals, not redispatched or rescored during S2. Physical assets were not
carried from Week 2 into Week 3.

The active team profiles are
[finalized_release_500mw.json](../configs/rounds/finalized_release_500mw.json) and
[dispatch_scoring_rules_500mw.json](../configs/scoring/dispatch_scoring_rules_500mw.json).
Use the latter explicitly when running batch evaluations. The imported course
files predate capacity finalization; the team framework enforces 500 MW while
leaving those instructor files unchanged.

## 2. Measured scores

Scores below are ten-year present values in **billions of USD**.

| Submission | Baseline at bus 1001 | Carter variant at bus 6141 | Gain from moving the site |
| --- | ---: | ---: | ---: |
| Week 2 Submission 1 | 16.584 | 17.263 | 0.680 |
| Week 2 Submission 2 | 12.419 | 17.263 | 4.844 |
| Week 3 Submission 1 | 13.850 | 16.715 | 2.865 |
| Week 3 Submission 2 | 12.418 | 16.714 | 4.296 |
| **Combined** | **55.271** | **67.955** | **12.684** |

Combined scores use unrounded results; displayed rows are rounded independently.
The source is the [saved comparison](../analysis/cg_bus_comparison_500mw.csv),
supported by the [baseline](../analysis/baseline_cg_500mw.csv) and
[Carter variant](../analysis/carter_rank1_cg_500mw.csv) per-round results.

## 3. Full allocation did not mean full grid supply

Every new site received **100% of its requested 500 MW** in every submission.
No capacity-reduction step was needed. All sites were served across the full
120-period horizon.

Electricity supply was different. The table reports **weighted energy shares**,
not installed capacities or constant hourly dispatch fractions. The measured
shares were the same in Weeks 2 and 3; settlement costs differed.

| New sites evaluated | Bus 1001 grid share | Bus 1001 private generation | Bus 6141 grid share | Bus 6141 private generation |
| --- | ---: | ---: | ---: | ---: |
| Submission 1 | 74.0387% | 25.9613% | 100% | 0% |
| Submission 2 | 0.0170% | 99.9830% | 100% | 0% |

At bus 1001, the new S2 site relied almost entirely on its private generator
after S1's grid withdrawal became fixed base load. At bus 6141, the grid supplied
all energy for both new builds. This is why S2 contributed a large part of the
score difference.

**C = G is a capacity choice, not a generator operating instruction.** The
operator can use cheaper grid electricity while the team still pays generator
capital. The two full-allocation results also do not establish how either site
would behave under competing teams' submissions.

## 4. Operating costs explain the score difference

Both campaigns earned the same IT value and paid the same site and generator
capital costs. The measured difference is entirely in operating costs.

| Campaign component | Bus 1001 | Bus 6141 |
| --- | ---: | ---: |
| IT value | 123.053B | 123.053B |
| Site capital | 50.000B | 50.000B |
| Generator capital | 4.000B | 4.000B |
| Private-generator operation | 11.047B | 0.000B |
| Grid-energy settlement | 2.735B | 1.098B |
| Storage capital | 0.000B | 0.000B |
| **Net score** | **55.271B** | **67.955B** |

Moving to bus 6141 saved approximately **$11.047B in generator operation** and
**$1.637B in grid-energy settlement**, totaling **$12.684B**. Week 2 grid energy
was uncharged; the grid-settlement totals above come from Week 3.

Carter's generators were idle in all four submissions, but their capital still
cost **$1B per submission**, or **$4B across the campaign**. This makes generator
sizing worth testing next. That capital figure alone does not establish the
score or allocation of a plan with smaller generators; it needs another full
evaluation, especially under competition.

## 5. Normalized score and comparison anchors

For the finalized capacity, use:

```text
S = W2S1 + W2S2 + W3S1 + W3S2, in billions of USD
Q(S) = 100 * (S - 49.67) / (73.0525 - 49.67)
```

| Strategy | Combined score | Normalized Q |
| --- | ---: | ---: |
| Baseline at bus 1001 | $55.271B | 23.96 |
| Carter variant at bus 6141 | $67.955B | 78.20 |

The **$49.67B anchor** represents full private generation throughout all four
graded new-build submissions. It is an analytical comparison case, not the
measured score of every plan with C = G. Economic dispatch explains why the
observed baseline can score above it.

The **$73.0525B anchor** assumes full allocation, grid-only supply, zero energy
prices, and no private-asset capital. It is an idealized scoring bound, not a
promised feasible network outcome. Actual Week 3 prices are dispatch LMPs.

The rounded anchors are retained consistently. Negative Q values and values
above 100 remain visible. Q is computed from the complete campaign, never from
one submission. See [scoring definitions](../docs/SCORING.md) for the exact
rounding convention and the distinction from the instructor's grading reference.

## 6. How this connects to Carter's screening findings

Carter's notes emphasize that individual hosting capacities are not additive
and that attractive buses can share system generation headroom or transmission
bottlenecks. Our experiment adds a full-evaluator economic comparison for two
specific site choices at the finalized team capacity.

Bus 6141's composite rank was useful for forming a hypothesis, and the solo
comparison supports that choice over the arbitrary bus 1001 reference. It does
not prove that bus 6141 is the best bus, that its individual hosting capacity is
available independently of other teams, or that concentrating all requests there
is the best competitive strategy.

Some team notes retain recommendations based on older capacity assumptions.
Use the 500 MW profiles above for current experiments.

## 7. What remains unknown

Only one solo campaign scenario was evaluated for each strategy. We therefore
have measured returns but no estimate of competitive downside risk. In
particular:

- Full allocation in these runs does not measure relative allocation resilience
  when other teams add load.
- Neither strategy used storage, so these results say nothing about battery
  value or the trade-off between batteries and private generation.
- The same bus and resource choice was repeated in S2; adaptive S2 siting has
  not been compared.

Once matched opponent scenarios exist, compare **average normalized score
against downside risk**, retaining worst-case Q and the frequency below the
analytical baseline. Use a Pareto frontier rather than selecting a weighted
composite score. One solo run must not be plotted as an observed zero-risk point.

## 8. Next experiments to discuss

1. **Competition at bus 6141:** compare concentrated and dispersed rival plans,
   using the same opponent assumptions and seeds for every candidate.
2. **Generator sizing at a fixed bus:** vary only generator capacity, keeping
   the 500 MW connection request and battery size fixed. Include C = G as the
   reference and check allocation as well as score.
3. **Adaptive Submission 2:** choose the next bus using the corresponding S1
   outcome instead of automatically repeating the S1 location.
4. **Diversification:** compare a single 500 MW site with two 250 MW sites in
   different electrical regions. Evaluate the joint plan rather than adding
   individual hosting-capacity figures.
5. **Storage when a constraint is identified:** test a battery separately from
   a generator change so their effects can be distinguished. Use the full
   evaluator; the fast preview omits battery operating benefits.

These are proposed tests, not additional implemented strategies or measured
outcomes.

## 9. Evidence and reusable interpretation

The shared framework had **89 passing tests** at the initial merge, including
an integration check through the instructor evaluator. The template and both
strategy notebooks execute against the saved 500 MW evidence.

| Artifact | Purpose |
| --- | --- |
| [Baseline campaign summary](../analysis/baseline_cg_500mw.json) | Settings, scores, input fingerprints, and verification |
| [Carter campaign summary](../analysis/carter_rank1_cg_500mw.json) | Matching evidence for bus 6141 |
| [Comparison CSV](../analysis/cg_bus_comparison_500mw.csv) | Combined scores, gains, and normalized scores |
| [Main template](../notebooks/main_template.ipynb) | Common plots and comparison conventions |
| [Baseline notebook](../notebooks/01_full_generation_baseline.ipynb) | Baseline plots and calculated findings |
| [Carter notebook](../notebooks/02_carter_rank1_cg.ipynb) | Bus 6141 plots and calculated findings |
| [Strategy development guide](../docs/STRATEGY_DEVELOPMENT.md) | How to add, validate, evaluate, and compare a strategy |

Large raw runs remain local under `runs/finalized-500mw/` and are ignored by Git.
The committed summaries and notebooks provide the shared results for the team.
