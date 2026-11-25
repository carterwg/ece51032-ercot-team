# Bottleneck diversity analysis guide

This guide describes
[`analysis/bus_rankings/bottleneck_diversity_analysis.csv`](../analysis/bus_rankings/bottleneck_diversity_analysis.csv).
The file contains one row for each of the 20 buses in the diversified shortlist.
Each bus is analyzed on its own: the solver adds load at that candidate bus,
holds the representative-period base demand at other buses, and finds the
maximum additional load that the grid can serve.

The results use the ACTIVSg2000 representative package: 2,000 buses and 120
zero-based hourly periods. The binding-period index comes from the
all-bus hosting-capacity results. The shortlisted buses in this file all bind
at period 109.

## Column reference

| Column | Definition, computation, interpretation, and relevance to the game |
|---|---|
| `uniqueness_order` | **Definition:** Row position in the report's bottleneck-uniqueness ordering. **Computation:** Rows with a binding transmission branch come first, ordered by `bottleneck_uniqueness_rank` (fewer shortlisted buses sharing a branch ranks higher), then by hosting capacity descending; buses without a binding transmission branch follow, ordered by hosting capacity. **Power-system meaning:** It is a presentation order, not a physical grid quantity. **Game relevance:** Brings buses with less-shared corridor constraints to the top for comparing alternative siting locations. |
| `bus_id` | **Definition:** ACTIVSg2000 bus identifier for the load candidate. **Computation:** Copied from `diversified_top20.csv`. **Power-system meaning:** The network node where the additional data-center demand is modeled. **Game relevance:** Identifies where a proposed connection would be made; the bus number alone does not encode a geographic location. |
| `minimum_hosting_capacity_mw` | **Definition:** Maximum extra load at this bus in its most restrictive one of the 120 periods. **Computation:** Copied from the all-bus hosting-capacity results and checked by rerunning the hosting-limit solve at the recorded period. The LP maximizes candidate demand while enforcing generator bounds and branch thermal limits. **Power-system meaning:** The largest single-bus demand increment that remains feasible in that modeled hour, with other base loads unchanged. **Game relevance:** A high value indicates substantial modeled room for an individual connection, but it does not guarantee that this capacity remains available when other teams add load. |
| `binding_period_index` | **Definition:** Zero-based index of the period in which the bus reaches its minimum hosting capacity. **Computation:** Read from the all-bus results; the saved capacity was verified by solving that period. **Power-system meaning:** Identifies the hourly operating condition that is most restrictive for that bus. **Game relevance:** Helps connect a siting limit to the scenario hour the grid operator must accommodate. Period 109 is in the representative peak-load day. |
| `bottleneck_group` | **Definition:** Label for the constraint group identified at the bus's hosting limit. **Computation:** The binding branch IDs joined by `+`; when no branch is binding, the label is `SYSTEM_GENERATION_CAPACITY`. **Power-system meaning:** Names the transmission corridor constraint or the system-wide generation-capacity ceiling limiting the modeled solution. **Game relevance:** Helps compare whether candidate sites depend on the same scarce grid resource. |
| `binding_branch` | **Definition:** IDs of branches at their thermal limit in the hosting-limit solution. **Computation:** A branch is included when the absolute modeled flow is within 0.0001 MW of its thermal limit; multiple IDs, if present, are separated by semicolons. **Power-system meaning:** These are the transmission elements whose flow limits are reached in that dispatch. The candidate does not need to be directly connected to the branch: power flows redistribute over the network. **Game relevance:** Shortlisted sites that hit the same branch may be exposed to a common transmission bottleneck. Blank means no branch is at its limit in that solution. |
| `binding_branch_details` | **Definition:** Human-readable description of each branch in `binding_branch`. **Computation:** Each semicolon-separated item has the form `branch_id:from_bus-to_bus@thermal_limitMVA`. **Power-system meaning:** Gives the constrained line's endpoints and rating; the endpoint order follows the dataset's from/to orientation. **Game relevance:** Makes a shared corridor easier to recognize and communicate without looking up another file. Example: `b02579:8004-7150@647MVA`. |
| `binding_branch_flow_mw` | **Definition:** Signed flow on each branch listed in `binding_branch`, in the same order. **Computation:** Reconstructed from the solved DC power-flow bus angles; positive means from the branch's `from_bus_id` toward its `to_bus_id`, negative means the reverse. **Power-system meaning:** Shows the direction and magnitude of flow at the hosting limit. Its magnitude is approximately the branch's thermal rating in this solution. **Game relevance:** Indicates which way the candidate's limiting dispatch loads the shared corridor. Example: bus 6062 has `2020.000000` MW on `b01773`; bus 6298 has `-2020.000000` MW on `b01758`. |
| `shortlisted_buses_sharing_branch` | **Definition:** For each listed binding branch, the number of the 20 shortlisted buses whose individual hosting-limit solution also binds that branch. **Computation:** Counted over the shortlist, in the same semicolon-separated order as `binding_branch`. **Power-system meaning:** Measures how many candidate tests encounter the same constrained transmission element; it is not a simultaneous-flow calculation. **Game relevance:** A high count flags a corridor that may be a common source of competition among teams. For example, `b02579` is shared by 8 shortlisted buses. |
| `max_shortlisted_buses_sharing_bottleneck` | **Definition:** Largest sharing count among the row's binding branches. **Computation:** Maximum of the branch-specific counts; zero when no branch is binding. **Power-system meaning:** A summary of how widely the bus's most-shared limiting corridor appears in the shortlist. **Game relevance:** Supports sorting by bottleneck concentration. Buses 7095 and 7414 have value 2 for `b02136`; the eight `b02579`-limited buses have value 8. |
| `bottleneck_uniqueness_rank` | **Definition:** Dense rank for how uncommon a bus's binding branch is among the shortlist; smaller is more unique. **Computation:** Rank the distinct branch-sharing counts in ascending order, assigning rank 1 to count 1, rank 2 to count 2, and rank 3 to count 8 in these results. For multiple binding branches, the row uses the best (smallest) rank among them. Blank when no transmission branch binds. **Power-system meaning:** A relative shortlist statistic, not a reliability or contingency metric. **Game relevance:** Helps find sites that may avoid the same transmission corridor constraints as other shortlisted sites. |
| `bottleneck_uniqueness` | **Definition:** Text interpretation of the uniqueness rank. **Computation:** `unique corridor` for a branch shared by one shortlisted bus, `shared by N shortlisted buses` otherwise, and `N/A - no binding transmission branch` when the solution is not branch-limited. **Power-system meaning:** Describes sharing within this 20-bus sample only. **Game relevance:** Makes the distinction between uncommon and common shortlisted corridors easy to scan. “Unique” does not mean the branch is unique in the grid or immune to other loads. |
| `binding_generator_pmax_count` | **Definition:** Number of generators at their maximum active-power output in the hosting-limit solution. **Computation:** Counts generators whose solved output is within 0.00001 MW of `p_max_mw`. **Power-system meaning:** These units have no additional upward output headroom in that dispatch. **Game relevance:** When nearly all generators are at Pmax and no branch binds, the candidate is generation-capacity-limited rather than transmission-limited. |
| `binding_generator_pmax_ids` | **Definition:** IDs of the generators counted in `binding_generator_pmax_count`. **Computation:** Semicolon-separated generator IDs in dataset order, using the same Pmax tolerance as the count. **Power-system meaning:** Identifies the units whose upper generation bounds are active. **Game relevance:** Provides a traceable view of which modeled generators have exhausted their dispatch capacity at the candidate's hosting limit. |
| `binding_generator_pmin_count` | **Definition:** Number of generators at their minimum active-power output in the hosting-limit solution. **Computation:** Counts generators whose solved output is within 0.00001 MW of `p_min_mw`. **Power-system meaning:** These units cannot be dispatched lower under the modeled generator bounds. **Game relevance:** Minimum-output constraints can affect dispatch flexibility and can matter when assessing how the modeled system responds to new load or changing conditions. |
| `binding_generator_pmin_ids` | **Definition:** IDs of the generators counted in `binding_generator_pmin_count`. **Computation:** Semicolon-separated generator IDs in dataset order, using the same Pmin tolerance as the count. **Power-system meaning:** Identifies units at their lower generation bounds. **Game relevance:** Lets analysts inspect which units have no downward flexibility in the modeled solution. |

## Interpreting the constraints

### Transmission-limited buses

A bus is transmission-limited in this report when one or more branch flows reach
their thermal ratings at its maximum additional load. Adding more demand at that
bus would require a dispatch whose flow on at least one such branch exceeds its
modeled limit. The branch may be far from the candidate bus because injections
and withdrawals affect flows across multiple paths.

For example, bus 6062 is limited by `b01773` (6075–6062, 2,020 MVA), while bus
6298 is limited by `b01758` (6298–6056, 2,020 MVA). Each appears as a unique
corridor among the 20 shortlisted buses. In contrast, `b02579` (8004–7150,
647 MVA) binds for eight shortlisted candidates, including buses 5413, 5317,
5015, and 8043.

### Generation-capacity-limited buses

When no transmission branch binds, but the total remaining load is limited by
generators reaching their Pmax, the solution is generation-capacity-limited.
The eight such buses in this report each use the system's available generation
to its upper bounds at period 109; their binding-branch fields are blank. This
does **not** mean every bus has a separate local generator shortage. The
limiting resource is the system-wide supply available to serve the additional
load under this model.

### Why buses can share a bottleneck

Power does not travel along a single designated path from a generator to a
load. In the network model, changing load at different buses changes flows
across shared transmission corridors. Thus, separate one-bus-at-a-time
hosting-capacity solves can reach the same branch's thermal limit even when
the candidate buses are not endpoints of that branch. A shared branch count in
this CSV means those separate tests each bind that branch; it is not the
number of buses that can all be added simultaneously.

### Why hosting capacities do not add across buses

Each reported hosting capacity is an independent maximum against the same
representative base case. If loads were added at several buses together, their
combined injections would change generation dispatch and network flows. They
could jointly exceed a shared branch rating or the system's total generation
capacity even if each individual result is feasible. A combined plan therefore
requires a joint dispatch/evaluation; summing these individual maxima does not
give a feasible total.

## Reading the shortlist results

- **Bus 6062:** minimum hosting capacity is about 2,958.841 MW; `b01773` binds
  at +2,020 MW and is shared by one shortlisted bus. It is ranked as a unique
  shortlisted corridor.
- **Bus 6298:** minimum hosting capacity is about 2,513.833 MW; `b01758` binds
  at -2,020 MW and is also unique among the shortlist.
- **Buses 7095 and 7414:** both bind `b02136` (6294–6293, 217.8 MVA), so each
  records a sharing count of 2.
- **Bus 5413:** minimum hosting capacity is about 3,022.548 MW and `b02579`
  binds at -647 MW; seven other shortlisted buses share that same branch.
- **Bus 1079:** minimum hosting capacity is about 3,024.604 MW, with no binding
  branch and all 432 active generators at Pmax. Its bottleneck is generation
  capacity, so transmission-corridor uniqueness is not applicable.

All uniqueness and sharing statements are relative to this particular
20-bus shortlist and this representative dataset. They are screening evidence,
not a guarantee of available capacity in the game: the official evaluation
dispatches teams' plans together, and competition for network capacity can
change each site's served load.
