# Concentrated-crowding study

## Method and assumptions

Each candidate was evaluated as a 1,000 MW site with ten rival teams, also
requesting 1,000 MW each. Scenario A puts every rival at bus 1079; Scenario B
puts every rival at bus 5131; Scenario C puts one rival at each of the top ten
buses by minimum hosting capacity. The top ten, ordered by minimum capacity
with bus ID as the tie-breaker, are:

`6349, 5045, 5120, 5131, 5236, 5279, 5018, 6045, 6056, 6197`.

The four candidate buses were evaluated separately in each scenario, so
candidates did not compete against each other. Every preview checked all 120
periods (`preview_stride=1`), used Week 2 scoring (no grid-energy charge), and
had no private generation or storage. The allocation factor is the preview's
projected fraction of the candidate's request that can be served; with one
1,000 MW site, it equals the served fraction. Curtailment is
`1,000 MW × (1 − allocation factor)`.

All full-request joint dispatches required the preview's allocation projection.
The branch constraints below are lines that reached their thermal limits in
at least one allocated dispatch period. The most stressed period was index
119 in every run; system generation was approximately 90.75% of active Pmax
(81,201.89 MW) there, so the common competition outcome is transmission-
limited rather than generation-limited.

## Results

Scores are shown in billions of preview score units. Small differences in the
last digits are solver tolerances, not meaningful strategic differences.

| Scenario | Candidate bus | Score (billion) | Served fraction | Allocation factor | Allocated MW | Curtailed MW | Binding transmission constraints |
|---|---:|---:|---:|---:|---:|---:|---|
| A: ten rivals at 1079 | 1079 | 10.0425 | 27.4937% | 0.274937 | 274.94 | 725.06 | b02579, 8004–7150 (647 MVA) |
| A: ten rivals at 1079 | 6062 | 10.0425 | 27.4937% | 0.274937 | 274.94 | 725.06 | b02579, 8004–7150 (647 MVA) |
| A: ten rivals at 1079 | 6298 | 10.0425 | 27.4937% | 0.274937 | 274.94 | 725.06 | b02579, 8004–7150 (647 MVA) |
| A: ten rivals at 1079 | 7414 | 10.0425 | 27.4937% | 0.274937 | 274.94 | 725.06 | b02579, 8004–7150 (647 MVA) |
| B: ten rivals at 5131 | 1079 | 10.0425 | 27.4937% | 0.274937 | 274.94 | 725.06 | b01854, 6108–6192 (523 MVA); b02104, 6262–6319 (98 MVA); b02579, 8004–7150 (647 MVA) |
| B: ten rivals at 5131 | 6062 | 10.0425 | 27.4937% | 0.274937 | 274.94 | 725.06 | b02104, 6262–6319 (98 MVA); b02579, 8004–7150 (647 MVA) |
| B: ten rivals at 5131 | 6298 | 10.0425 | 27.4937% | 0.274937 | 274.94 | 725.06 | b01854, 6108–6192 (523 MVA); b02579, 8004–7150 (647 MVA) |
| B: ten rivals at 5131 | 7414 | 10.0425 | 27.4937% | 0.274937 | 274.94 | 725.06 | b02579, 8004–7150 (647 MVA) |
| C: one rival at each top-ten bus | 1079 | 10.0425 | 27.4937% | 0.274937 | 274.94 | 725.06 | b02579, 8004–7150 (647 MVA) |
| C: one rival at each top-ten bus | 6062 | 10.0425 | 27.4937% | 0.274937 | 274.94 | 725.06 | b02579, 8004–7150 (647 MVA) |
| C: one rival at each top-ten bus | 6298 | 10.0425 | 27.4937% | 0.274937 | 274.94 | 725.06 | b02355, 7058–7095 (2,295 MVA); b02579, 8004–7150 (647 MVA) |
| C: one rival at each top-ten bus | 7414 | 10.0425 | 27.4937% | 0.274937 | 274.94 | 725.06 | b02355, 7058–7095 (2,295 MVA); b02579, 8004–7150 (647 MVA) |

No generator reached Pmax in the most stressed period. Branch b02579 was
binding in every run; the other binding lines varied with the crowding
locations. In Scenario A, the candidate at 1079 is co-located with the ten
rivals; it received essentially the same allocation fraction as candidates at
other buses.

## Candidate resilience ranking

| Rank | Candidate bus | Mean served fraction across scenarios | Assessment |
|---:|---:|---:|---|
| 1 (tie) | 1079 | 27.4937% | No meaningful advantage |
| 1 (tie) | 6062 | 27.4937% | No meaningful advantage |
| 1 (tie) | 6298 | 27.4937% | No meaningful advantage |
| 1 (tie) | 7414 | 27.4937% | No meaningful advantage |

**Conclusion:** none of these candidate sites is measurably more resilient to
the tested concentrated crowding. All receive about 274.94 MW of their
1,000 MW request in each scenario, with the shared b02579 corridor limiting
the allocated dispatch. The displayed score and fraction differences are
below meaningful precision and should be treated as a four-way tie.

## Preview caveat and reproducibility

These are conservative, non-authoritative student-preview results, not
official game scores. The preview does not dispatch storage. It applied
capacity allocation because the full requests were infeasible; in Scenario C
with candidate 1079, the initial full-request solver returned an unresolved
status and the preview's allocation fallback still produced the reported
result. Treat the results as screening evidence rather than a guarantee of
official evaluator outcomes.

Detailed per-candidate results are in
[`crowding_study_results.csv`](../analysis/crowding_study_results.csv), with the raw
preview and allocation diagnostics in
[`crowding_study_preview_details.json`](../analysis/crowding_study_preview_details.json).
