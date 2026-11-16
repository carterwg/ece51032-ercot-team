# Project strategy interpretation: bottleneck diversity

This note interprets the 20-bus shortlist in
[`analysis/bus_rankings/bottleneck_diversity_analysis.csv`](../analysis/bus_rankings/bottleneck_diversity_analysis.csv)
as a strategic screening result. Capacities are one-bus-at-a-time results on
the representative grid, not a simultaneous allocation to teams.

## Buses that appear most independent

**Bus 6062** and **bus 6298** are the strongest choices if the goal is to avoid
a transmission corridor that is also limiting other shortlisted choices.
Bus 6062 is limited by branch `b01773` (6075–6062, 2,020 MVA), while bus 6298
is limited by `b01758` (6298–6056, 2,020 MVA). Each corridor appears for only
one of the 20 buses, so both have the highest corridor-uniqueness result.
Their individual minimum hosting capacities are about 2,958.841 MW and
2,513.833 MW, respectively.

This is relative independence within this shortlist, not immunity from
competition: other teams can choose buses outside the shortlist, and a
different joint dispatch can change the limiting constraints.

## Buses most exposed to shared congestion

The clearest shared-congestion group consists of **5413, 5317, 5015, 8043,
5384, 5295, 2002, and 8126**. Each is limited by branch `b02579`
(8004–7150, 647 MVA), which is shared by all eight in their individual
hosting-limit tests. These buses span minimum hosting capacities from
2,722.552 MW (8126) to 3,022.548 MW (5413), but their high individual values
should not be mistaken for eight independent blocks of capacity: they all
encounter the same corridor limit.

**7095** and **7414** share a second bottleneck, branch `b02136` (6294–6293,
217.8 MVA). The CSV reports that this branch limits both buses and no other
shortlisted bus.

## Buses that are generation-limited

**6197, 6021, 6038, 5131, 8155, 1079, 3088, and 2054** have no binding
transmission branch in their hosting-limit solutions. Instead, all **432
generators** are at Pmax for each of these buses. Their minimum hosting
capacities are essentially identical, about 3,024.604 MW.

Strategically, moving among these eight buses does not avoid the reported
limiting resource: their individual tests all run into the same system-wide
generation ceiling. Their results do not indicate that each bus has a
separate local generation constraint.

## Unique transmission corridors

The two shortlist choices with unique limiting corridors are:

| Bus | Limiting branch | Individual minimum hosting capacity |
|---:|---|---:|
| 6062 | `b01773` (6075–6062, 2,020 MVA) | 2,958.841 MW |
| 6298 | `b01758` (6298–6056, 2,020 MVA) | 2,513.833 MW |

These are the most differentiated transmission-limited options in this set.
Uniqueness means no other shortlisted bus had that same branch bind in its
own test; it does not mean the corridor is uncongested under other plans or
that these sites can jointly use their full individual capacities.

## Where a popular analysis may crowd the game

If many teams use this same shortlist, the eight buses limited by `b02579`
are the most obvious candidates for a common-corridor pile-up. The generation-
limited group is another natural magnet: all eight buses have nearly the same
top-of-list capacity, so a strategy that simply selects the largest individual
hosting value could send teams to the same apparent options.

The CSV cannot predict how many teams will choose each bus. It does show why
copying a ranking can concentrate plans: `b02579` is shared by eight
transmission-limited candidates, while the eight generation-limited candidates
depend on the same system supply ceiling. Diversifying across the two unique
corridors may reduce exposure to those specific shared constraints, but
capacity and risk still need to be evaluated jointly.

## Strategy caveat

The reported hosting capacity is the maximum additional load at one bus while
other loads remain at the representative base. Separate bus results cannot
be added: placing multiple teams' loads on the grid changes dispatch and
flows, potentially binding corridors or exhausting generation sooner. The
official game evaluates all teams together, so these results are useful for
forming hypotheses and alternatives, not guarantees of served load or score.
