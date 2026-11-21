# Headroom and Neighbor-Bus Interaction Report

This report synthesizes existing hosting-capacity, network, reserve-margin, and joint-test artifacts. It uses no new optimization or simulation.

**Source files reviewed**

- [hosting_capacity_all_buses.csv](carter_week1_material/hosting_capacity_all_buses.csv)
- [bus_screening_metrics.csv](carter_week1_material/bus_screening_metrics.csv)
- [diversified_top20.csv](carter_week1_material/diversified_top20.csv)
- [bottleneck_diversity_analysis.csv](carter_week1_material/bottleneck_diversity_analysis.csv)
- [system_reserve_margin_study.md](../notes/carter_week1_notes/system_reserve_margin_study.md)
- [1079/2054 joint test](../notes/carter_week1_notes/1079_2054_joint_test.md)
- [6062/6298 joint test](../notes/carter_week1_notes/6062_6298_joint_test.md)
- [portfolio comparison](../notes/carter_week1_notes/portfolio_comparison.md)

## 1. What headroom means

In this game, headroom is the maximum additional IT load that can be added at a location or set of locations while the DCOPF remains feasible across the relevant operating periods.

There are three different meanings that must not be conflated:

1. **Single-bus hosting capacity, \(HC_k\)**  
   Maximum constant additional load that bus \(k\) can accept alone in every studied period:

   ```text
   HC_k = minimum over periods t of the maximum feasible load at bus k
   ```

   This is the value in `hosting_capacity_all_buses.csv`.

2. **Regional or simultaneous hosting region**  
   The set of feasible load vectors at multiple buses. This is smaller than the individual headroom rectangle when buses compete for generation or transmission capacity.

3. **Residual headroom after an observed load**  
   How much more load can be added at bus \(k\) when \(X\) MW is already connected at nearby bus \(j\). This is the interaction quantity that matters for competition but is not reported for every pair in the existing artifacts.

For the representative game data:

- Active generation is 81,201.890 MW.
- Peak representative period 109 has a system load of 78,177.286 MW.
- Arithmetic generation reserve/headroom is 3,024.604 MW.
- The highest single-bus hosting capacities meet that ceiling within numerical precision.

Thus, “headroom” is not one universal local number. It can be aggregate generation headroom, a deliverability corridor, or a nearby branch limit.

## 2. Local, regional, corridor, or system-wide?

The evidence shows all four forms:

| Headroom type | Verified result | Interpretation |
|---|---|---|
| System-wide generation | 3,024.604 MW at peak period 109 | All available active generation reaches Pmax |
| Regional or multi-bus generation | 1079 and 2054 jointly reach 3,024.604 MW | They share the same aggregate generation ceiling |
| Corridor-based | 6062, 6298, 5413, 5317, 5015, 8043, 7414, and others | Network branches limit delivery before generation |
| Local/deliverability | Some buses have a lower HC than the system ceiling | A bus-specific injection encounters a local corridor or network constraint |

### Verified conclusions

- The 3,024.604 MW ceiling is the same as the aggregate period-109 reserve margin.
- 1079 and 2054 are verified generation-limited at their individual and joint limits, with no verified branch thermal limit in the joint solution.
- 6062/6298 jointly reveal a corridor interaction at b02136 that was not the limit in their separate one-bus tests.
- b02579 limits 5413 and 5317 in the individual shortlist tests and also appears in multiple competition previews.
- 6062, 6298, and 7414 show three distinct corridor patterns in the 20-bus diversity list.

### Hypotheses

- Generation-ceiling buses outside the existing 20-bus bottleneck table may or may not be individually free of transmission limits. Their exact ceiling makes generation competition highly plausible, but the branch binding is not recorded for each one.
- Sharing an electrical region or many top-100 neighboring members does not prove that two buses share a binding constraint.
- Directly connected top-50 buses do not automatically interact more than geographically distant buses on the same major corridor.

## 3. Top-50 hosting-capacity classification

The 50 buses are ranked by the minimum single-bus hosting capacity in `hosting_capacity_all_buses.csv`.

### A. Buses that appear to share the generation headroom

The strongest group is the **29-bus exact ceiling plateau**: all have about 3,024.604 MW and bind in period 109.

```text
6349, 5131, 5279, 5120, 5236, 5045, 5018, 6292, 6045,
6197, 6234, 6254, 6056, 6107, 6038, 6118, 6021, 6003,
6210, 5451, 5358, 8082, 8155, 1079, 3048, 3046, 3088,
2054, 2127
```

**Verified:**

- All 29 reach the same numerical headroom ceiling and period 109.
- The reserve-margin study proves the numerical ceiling corresponds to the period-109 aggregate active-generation headroom.
- The 1079/2054 joint test proves that two buses on this plateau compete for the same 3,024.604 MW resource.

**Hypothesis:**

- Most or all of the remaining plateau buses share the aggregate generation pool. Exact equality alone does not prove every bus is individually free of a branch; however, eight buses in the diversity list are explicitly verified to have no transmission branch binding and are generation-limited.

The explicitly generation-limited 20-bus subset is:

```text
6197, 6021, 6038, 5131, 8155, 1079, 3088, 2054
```

They are therefore the highest-confidence group for generation interaction among the top-50 ranking.

### B. Buses that appear to share transmission bottlenecks

The strongest verified shared-corridor groups are:

| Group | Verified binding branch | Evidence |
|---|---|---|
| 5413, 5317, 5015, 8043, 5384, 5295, 2002, 8126 | b02579, 8004--7150, 647 MVA | Individual bottleneck-diversity results |
| 7095, 7414 | b02136, 6294--6293, 217.8 MVA | Individual bottleneck-diversity results |
| 6062 | b01773, 6075--6062, 2,020 MVA | Unique in the 20-bus shortlist |
| 6298 | b01758, 6298--6056, 2,020 MVA | Unique in the 20-bus shortlist |

Within the top-50 table, the branches explicitly identified in the 20-bus diversity analysis are:

| Top-50 bus | Binding branch |
|---|---|
| 5413 | b02579 |
| 5317 | b02579 |
| 6062 | b01773 |
| 5015 | b02579 |
| 8043 | b02579 |

The other top-50 buses have lower or ceiling capacities but do not have a binding branch attached in the reviewed artifacts.

Important note: a shared branch list is not needed to show every regional interaction. The 6062/6298 pair has different individual bottlenecks but acquires b02136 when loaded jointly.

### C. Buses that appear relatively independent

The most defensible relative-independence candidates are:

1. **6062**  
   Individually limited by b01773, a branch unique among the 20-bus diversity shortlist.

2. **6298**  
   Individually limited by b01758, also unique among the 20-bus shortlist.

3. **7414**  
   Limited by b02136, which is shared only with 7095 in the 20-bus shortlist.

4. **Bus pairs drawn from different verified resource groups**  
   For example, 6062 plus 6298 appears promising only by individual data; the joint test disproves simple independence because b02136 becomes binding.

Relative independence is not absolute:

- Any bus can interact through a new aggregate flow pattern.
- Buses outside the shortlist can create the actual bottleneck.
- A new corridor can emerge only when loads are combined.
- The 6062/6298 joint test is direct evidence of this risk.

## 4. Practical residual-headroom metric

For a fast existing-data screen, define a unit-load interaction fraction:

\[
\rho_{kj} =
1 - (1-\rho^{G}_{kj})(1-\rho^{T}_{kj})
\]

where:

- \(\rho^{G}_{kj}\) is the probability-weighted generation-resource overlap
- \(\rho^{T}_{kj}\) is the probability-weighted transmission-resource overlap

Use these initial components:

| Relationship | Proposed \(\rho\) |
|---|---:|
| Both reach the exact 3,024.604 MW ceiling | \(\rho^G=1.0\) |
| Neither is a known ceiling bus | \(\rho^G=0.0\) |
| Same verified bottleneck branch | \(\rho^T=1.0\) |
| Different known bottlenecks, but one or both directly share an incident branch | \(\rho^T=0.5\) |
| Same two-hop branch neighborhood or same electrical region | \(\rho^T=0.25\) |
| No known shared resource | \(\rho^T=0.0\) |

Then estimate residual headroom at bus \(k\) after \(X\) MW is already connected at bus \(j\):

\[
\widehat{HC}_{k|j}(X)
= \max(0,\; HC_k - X\rho_{kj})
\]

This is intentionally a screening approximation. It is not a feasible-region boundary.

### Interpreting the estimate

- \(\rho=1.0\): treat the buses as fully competing for the same resource.
- \(\rho=0.5\): direct or likely coupled corridor interaction.
- \(\rho=0.25\): weak or uncertain regional interaction.
- \(\rho=0.0\): no evidence of interaction in the existing data.

Example:

- \(1079\) and \(2054\): both on the exact generation plateau, so \(\rho=1.0\).
- Starting with 2,000 MW at 2054, the simple proxy predicts no residual generation headroom for 1079:

  ```text
  max(0, 3024.604 - 2000 x 1) = 1024.604 MW
  ```

  This agrees directionally with the verified equal-load joint result; it is not a precise joint allocation.

- \(6062\) and \(6298\): known individually different bottlenecks, but direct network neighborhood and joint evidence indicate interaction. \(\rho^G=0\) because neither is on the exact 3024.604 ceiling. \(\rho^T\) is initially 0.5--1.0, not 0, until a suitable joint constraint result exists.

### More robust practical metric: interaction ratio

For every pair, calculate:

\[
IR(k,j)=
\frac{HC_k+HC_j-\widehat{HC}_{k,j}^{\text{joint}}}{HC_k+HC_j}
\]

In existing data:

- 1079/2054 joint capacity 3,024.604 versus individual sum 6,049.208:

  ```text
  interaction loss = 49.999%, IR = 0.500
  ```

- 6062/6298 joint capacity 3,007.890 versus individual sum 5,472.673:

  ```text
  interaction loss = 45.0%, IR = 0.550
  ```

These are the only pair-level interaction ratios that are directly established in the existing joint artifacts.

## 5. Methodology without every pairwise optimization

The proposed method uses the existing tables to cluster buses, then optimizes only representatives.

### Phase 1: cluster by verified resource

Create resource groups:

1. **Generation plateau**  
   Minimum HC is approximately 3,024.604 MW.

2. **Known generation-limited short list**  
   No binding branch in the existing 20-bus diversity test.

3. **Known b02579 corridor**

4. **Known b02136 corridor**

5. **Known unique-corridor buses**

6. **Unknown/non-ceiling buses**  
   Require cluster or branch analysis before a resource conclusion.

### Phase 2: build topology features without solving

For each bus calculate:

- minimum and period-specific hosting capacity
- binding period
- direct incident branches
- branch thermal limits
- direct and second-hop branch intersections
- nearby active-generator capacity
- base load
- electrical region and top-100 region members
- number of shared bottleneck branches with a candidate cluster

The existing `bus_screening_metrics.csv` supplies the first coarse ranking inputs, but its `nearby_generation_capacity_mw` and `connected_branch_thermal_limit_mva` need to be interpreted as screening metrics rather than exact feasible headroom.

### Phase 3: select cluster representatives

Instead of every pair, select:

- 3--5 generation-ceiling representatives
- 3--5 b02579 representatives
- 6062
- 6298
- 7414
- 7095
- 2--3 unknown/high-HC buses

For a 20-50 candidate set, this produces tens of selected experiments rather than thousands of pairwise optimizations.

### Phase 4: test one dimension at a time

First test:

- one load bus
- two buses at once
- one bus plus one representative rival bus
- one bus plus a cluster of rival loads

Use equal-load and fixed-load forms, but do not average the exact result into an additive HC sum.

### Phase 5: update group interactions

After each representative joint result:

1. assign the group a verified shared-generation or shared-corridor label
2. update the interaction coefficient \(\rho_{kj}\)
3. leave untested pairings marked “hypothesis”
4. apply the metric to new buses only within the same cluster

This method is hierarchy-based:

```text
exact joint test
  -> updates only the resource cluster it proves
  -> closes for representative buses
  -> does not prove every unseen pair
```

## 6. Important constraints for the named buses

### 1079

**Verified**

- Minimum HC: 3,024.604 MW
- Binding period: 109
- No binding branch in the existing individual or 1079/2054 joint test
- All 432 active generators are at Pmax in the 1079/2054 joint solution
- 1079 shares the generation ceiling with 2054 and other plateau buses

**Primary constraint:** system aggregate generation at period 109.

**Hypothesis:** 1079's apparent deliverability advantage may disappear in a full joint plan because 1079 and nearby generation-limited buses compete for the same Pmax resource.

### 2054

**Verified**

- Minimum HC: 3,024.604 MW
- Binding period: 109
- No branch at thermal limit in the individual/joint 1079/2054 test
- All 432 active generators reach Pmax in the joint test

**Primary constraint:** system aggregate generation at period 109.

**Hypothesis:** 2054 is not a geographically independent alternative to 1079 or the rest of the generation-ceiling plateau.

### 6062

**Verified**

- Minimum HC: 2,958.841 MW
- Binding period: 109
- Individual bottleneck: b01773, 6075--6062, 2,020 MVA
- Unique limiting corridor among the 20-bus shortlist
- In joint operation with 6298, b02136 becomes the binding constraint

**Primary constraint:** individual delivery is corridor-based; the joint constraint can move to b02136.

**Hypothesis:** 6062 is not simply independent of nearby 6298 loads despite having a unique individual bottleneck.

### 6298

**Verified**

- Minimum HC: 2,513.833 MW
- Binding period: 109
- Individual bottleneck: b01758, 6298--6056, 2,020 MVA
- Unique limiting corridor among the 20-bus shortlist
- Jointly with 6062, b02136 limits the pair at 3,007.890 MW

**Primary constraint:** its individual local corridor b01758.

**Hypothesis:** b02136 is a high-risk emergent constraint in any plan that combines 6298 with 6062 or similarly located loads.

### 7414

**Verified**

- Minimum HC: 2,795.556 MW
- Binding period: 109
- Individual bottleneck: b02136, 6294--6293, 217.8 MVA
- b02136 is shared with 7095 among the 20-bus diversity shortlist

**Primary constraint:** low-capacity b02136 delivery corridor.

**Hypothesis:** 7414 is relative to 7095; it has no proven independence from the rest of the network or from hidden rival plans.

## 7. Confidence summary

| Finding | Confidence |
|---|---|
| 3,024.604 MW equals period-109 generation reserve | Verified |
| 1079/2054 compete for generation | Verified by joint test |
| 6062/6298 are non-additive | Verified by joint test |
| 6062 individual bottleneck is b01773 | Verified |
| 6298 individual bottleneck is b01758 | Verified |
| 7414 individual bottleneck is b02136 | Verified |
| b02579 is shared by many screened buses | Verified in shortlist data |
| Every exact-ceiling bus shares generation | Hypothesis, with strong aggregate evidence |
| Two-hop or region similarity predicts residual headroom | Hypothesis / screening metric |
| A corridor-unique bus remains independent under real competition | Hypothesis, disproved for 6062/6298 under their joint test |

## 8. Practical week-level conclusion

- Treat the exact 3,024.604 MW plateau as **one shared system-generation resource** for screening.
- Treat b02579, b02136, b01773, and b01758 as verified transmission-resource clusters.
- Use 6062 and 6298 for corridor diversity as hypotheses, not as guaranteed independent locations.
- Use 1079 and 2054 as strong candidates for studying aggregate generation constraints.
- Use 7414 for studying a low-capacity shared corridor.
- Do not estimate residual headroom by subtracting independent bus hosting capacities. Use cluster interaction coefficients and representative joint tests instead.
