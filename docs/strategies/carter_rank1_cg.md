# Carter rank-1 bus, C = G

This is a second named strategy configuration using the existing `FullGeneration`
implementation. It changes only the site location from the baseline's default
bus `1001` to Carter's selected bus `6141`; C = G and batteries remain zero.

The checked-in [screening analysis](../../analysis/bus_screening_metrics.csv)
ranks `6141` first by composite score (94.084542). Its recorded minimum hosting
capacity is 3,004.494975 MW. These are screening observations, not a guarantee
of capacity after competitors submit or after S1 changes the S2 base load.
The analysis does not record a scenario fingerprint. This strategy therefore
uses the selected bus as a fixed hypothesis and evaluates it on current inputs;
it does not treat that hosting-capacity figure as a certified limit.

In every submission, request the context's full connection budget at one new
site on bus `6141`, with matching generator capacity and no storage. The official
operator still decides how much generation and grid electricity to use.

From the team root with the project environment active:

```bash
team-strategy propose \
  --config configs/strategies/carter_rank1_cg.json \
  --team-id YOUR_TEAM_ID --week 2 --submission 1 \
  --seed 0 --output-dir runs/carter-rank1-w2s1-001
```

The finalized cap is **500 MW per submission**. The CLI uses the finalized team
profile; batch evaluation must use `configs/scoring/dispatch_scoring_rules_500mw.json`.
The imported instructor code and original files remain unchanged.

## Finalized 500 MW solo evaluation

One new 500 MW C = G site was built at bus `6141` in each graded submission.
All 120 periods were evaluated, with validated S1-to-S2 carryover, weekly resets,
and no opponents. Every new site received 100% allocation.

| Strategy | Combined score | Normalized Q |
| --- | --- | --- |
| Baseline, bus 1001 | $55.271B | 23.96 |
| Carter rank 1, bus 6141 | $67.955B | 78.20 |

The gain is $12.684B (22.95%). The grid supplied all
energy in Carter's four submissions, so private-generator operating cost was
zero; generator capital was still charged. This is a solo comparison, not a
competitive robustness estimate.

Evidence:

- [Executed strategy report](../../notebooks/02_carter_rank1_cg.ipynb)
- [Per-round scores and energy shares](../../analysis/carter_rank1_cg_500mw.csv)
- [Baseline comparison](../../analysis/cg_bus_comparison_500mw.csv)
- [Campaign totals and verification](../../analysis/carter_rank1_cg_500mw.json)
