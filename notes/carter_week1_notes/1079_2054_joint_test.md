# Joint hosting-capacity experiment: buses 1079 and 2054

## Setup

Using the ACTIVSg2000 representative dataset, I added equal nonnegative load
increments to buses 1079 and 2054 and maximized their combined load. The
experiment was solved independently for all 120 representative periods; the
reported joint hosting capacity is the minimum across those periods. Existing
base demand and generator/branch constraints were retained.

## Results

| Result | Value |
|---|---:|
| Limiting period | 109 |
| Joint hosting capacity (total additional load) | 3,024.604 MW |
| Additional load at bus 1079 | 1,512.302 MW |
| Additional load at bus 2054 | 1,512.302 MW |
| Total generation at the limit | 81,201.890 MW |
| Available active generator capacity | 81,201.890 MW |
| Generator utilization | 100% |
| Active generators at Pmax | 432 of 432 |
| Generators at Pmin | 117 |
| Binding branch thermal limits | None |

At period 109, the combined load reaches the system's available generation
ceiling. No branch is at its thermal limit in this joint solution, so it is
generation-capacity-limited rather than transmission-limited. Some generators
may be at both Pmin and Pmax where those bounds are equal.

## Comparison with separate hosting capacities

The individual minimum hosting capacities are approximately 3,024.6 MW at each
bus:

```text
Separate one-bus-at-a-time sum: 3,024.6 + 3,024.6 = 6,049.2 MW
Equal-load joint maximum:                                  3,024.604 MW
Joint assignment:                       1,512.302 + 1,512.302 = 3,024.604 MW
```

The separate sum is about twice the feasible joint total. Each individual
hosting result assumes the other bus has no added load; when both are loaded
equally, they compete for the same finite generation capacity. Therefore,
individual hosting capacities are not additive.
