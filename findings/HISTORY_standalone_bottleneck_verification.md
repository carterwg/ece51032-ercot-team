# Standalone bottleneck reproduction and verification

| Measurement | Result |
| --- | --- |
| Candidates | 101 |
| Periods | 120 |
| Candidate-period solves | 12120 |
| Maximum HC difference from screening MW | 0.000000646 |
| Carter shortlist groups checked | 20 |
| Top 100 material transmission-limited buses | 71 |
| Scores / IT value / grid/private MWh / generator hours | N/A — capacity diagnostics, not scored operation |

| Independent physical/optimality check | Maximum error MW |
| --- | --- |
| max_balance_error_mw | 0.0000000754 |
| max_limit_violation_mw | 0.0000000013 |
| duality_gap_mw | 0.0000000205 |

| Bus | Line | Rating increase MW | Measured HC gain MW | Shadow prediction MW |
| --- | --- | --- | --- | --- |
| 5413 | b02579 | 0.01 | 0.07619872 | 0.07619872 |
| 5317 | b02579 | 0.01 | 0.07585004 | 0.07585006 |
| 5015 | b02579 | 0.01 | 0.07384260 | 0.07384260 |
| 8043 | b02579 | 0.01 | 0.07359169 | 0.07359169 |
| 5384 | b02579 | 0.01 | 0.07295352 | 0.07295352 |
| 5295 | b02579 | 0.01 | 0.07246437 | 0.07246437 |
| 2002 | b02579 | 0.01 | 0.07138783 | 0.07138783 |
| 8126 | b02579 | 0.01 | 0.06863579 | 0.06863580 |
| 7095 | b02136 | 0.01 | 0.30512675 | 0.30512675 |
| 7414 | b02136 | 0.01 | 0.30473150 | 0.30473150 |
| 6062 | b01773 | 0.01 | 0.01236202 | 0.01236203 |
| 6298 | b01758 | 0.01 | 0.01091986 | 0.01091986 |
| 6141 | b02136 | 0.01 | 0.32750703 | 0.32750703 |
| 7346 | b01775 | 0.01 | 0.35091738 | 0.35091738 |
| 7346 | b02136 | 0.01 | 0.07475370 | 0.07475370 |

The standalone capacity results reproduced the screening values closely. Material line limits require positive capacity shadows and perturbation checks; simply observing a tight line can misclassify a generation-limited bus. Standalone groups do not prove independent corridors or quantify electrical interaction under rival load. The later Part 1 findings address those gaps. [complete verification evidence](<../runs/part1-stage2/verification.json>).

| Recorded reproduction | Solver | Candidates | Evidence |
| --- | --- | --- | --- |
| part1-stage2 | highs | 101 | [saved capacities / diagnoses](<../runs/part1-stage2/bottlenecks.json>) |
| part1-stage2-current | gurobi | 101 | [saved capacities / diagnoses](<../runs/part1-stage2-current/bottlenecks.json>) |
| part1-stage2-gurobi | gurobi | 101 | [saved capacities / diagnoses](<../runs/part1-stage2-gurobi/bottlenecks.json>) |

## Personal notes

<!-- USER_NOTES -->
