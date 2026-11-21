# Joint hosting-capacity experiment: buses 6062 and 6298

## Setup

I maximized the total additional load at buses 6062 and 6298, constrained to
receive equal load increments. The joint problem was solved for each of the
120 periods in the ACTIVSg2000 representative dataset; the joint hosting
capacity is the minimum feasible total across periods.

## Results

| Result | Value |
|---|---:|
| Joint hosting capacity | 3,007.890 MW total |
| Additional load at bus 6062 | 1,503.945 MW |
| Additional load at bus 6298 | 1,503.945 MW |
| Limiting period | 109 |
| Binding branch | `b02136`, buses 6294–6293 |
| Branch flow at limit | -217.800 MW (217.8 MVA thermal limit) |
| Total generation at the limit | 81,185.176 MW |
| Total active generator Pmax | 81,201.890 MW |
| Generator utilization | 99.979% |
| Generators at Pmax | 431 of 432 |

The sign on branch flow follows the dataset's from/to direction: negative
means flow from bus 6293 toward bus 6294. The joint result is transmission-
limited by `b02136` at period 109.

## Comparison with individual hosting capacities

| Quantity | Value |
|---|---:|
| HC(6062) | 2,958.841 MW |
| HC(6298) | 2,513.833 MW |
| Sum of individual hosting capacities | 5,472.673 MW |
| Joint hosting capacity with equal loads | 3,007.890 MW |

Using the requested definition:

```text
interaction ratio
= joint HC / (HC(6062) + HC(6298))
= 3,007.889568679 / (2,958.840537157 + 2,513.832888856)
= 0.549620  (about 54.96%)
```

Thus, under the equal-load joint constraint, the total feasible load is about
54.96% of the sum of the two separate one-bus-at-a-time capacities. The
individual capacities are not additive because the combined load changes
network flows and dispatch; here the shared system encounters the `b02136`
thermal limit before the individual capacities can be reached together.
