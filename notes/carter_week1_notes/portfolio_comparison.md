# Equal-site portfolio hosting-capacity comparison

## Method

Each plan was evaluated on all 120 periods in the ACTIVSg2000 representative
dataset. Added load at the plan's sites was constrained to be equal, and the
sum of added load was maximized. The reported joint hosting capacity is the
minimum optimized total over the 120 periods; binding constraints and
generation utilization are reported for that limiting period.

The interaction ratio is:

```text
joint hosting capacity / sum of the individual minimum hosting capacities
```

Individual capacities are from the single-bus hosting-capacity results:

| Bus | Individual minimum hosting capacity (MW) |
|---:|---:|
| 1079 | 3,024.604 |
| 2054 | 3,024.604 |
| 6062 | 2,958.841 |
| 6298 | 2,513.833 |
| 7414 | 2,795.556 |

## Comparison

| Plan | Sites (equal added load per site) | Joint hosting capacity | Limiting period | Binding constraints at limit | Sum of individual HCs | Interaction ratio |
|---|---|---:|---:|---|---:|---:|
| A | 1079: 3,024.604 MW | 3,024.604 MW | 109 | All 432 active generators at Pmax; no branch at thermal limit | 3,024.604 MW | 1.0000 (100.00%) |
| B | 1079, 2054: 1,512.302 MW each | 3,024.604 MW | 109 | All 432 active generators at Pmax; no branch at thermal limit | 6,049.208 MW | 0.5000 (50.00%) |
| C | 6062, 6298: 1,503.945 MW each | 3,007.890 MW | 109 | Branch `b02136` (6294–6293) at 217.8 MVA; 431 of 432 active generators at Pmax | 5,472.673 MW | 0.5496 (54.96%) |
| D | 1079, 6062, 6298, 7414: 756.151 MW each | 3,024.604 MW | 109 | All 432 active generators at Pmax; no branch at thermal limit | 11,292.834 MW | 0.2678 (26.78%) |

At Plan C's limit, flow on `b02136` is -217.800 MW in the dataset's
from/to orientation (from bus 6293 toward bus 6294). Total generation is
81,185.176 MW out of 81,201.890 MW of active Pmax, or 99.979% utilization.
Plans A, B, and D use the full 81,201.890 MW of active generation, or 100%
utilization.

## Interpretation

Plan A's joint result is effectively its individual hosting capacity, so its
ratio is 1. Plan B's two buses compete for the same generation ceiling; with
equal allocations, the total remains about one bus's capacity and the
interaction ratio is 0.5. Plan C is limited by the shared transmission
constraint `b02136` before all generators reach Pmax; its ratio is about
0.550. Plan D spreads the same generation-limited total over four sites, so
the equal site allocation falls to about 756.151 MW per bus and its ratio is
about 0.268.

These are equal-share, joint-feasibility experiments on the representative
base case. Individual hosting capacities are not additive: simultaneous added
loads alter dispatch and network flows, and can compete for common generation
or transmission capacity.
