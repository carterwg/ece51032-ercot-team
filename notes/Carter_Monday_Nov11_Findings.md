# ECE 51032 ERCOT Connection Game
## Project Findings Summary (Through Initial Screening and Competition Studies)

**Prepared By:** Team  
**Date:** November 2026

---

# 1. Objective

The purpose of this investigation was to understand:

1. Which buses appear attractive for siting data centers
2. Whether hosting capacities are additive
3. Whether top-ranked buses are independent opportunities
4. Whether transmission or generation is the dominant constraint
5. How competition affects candidate locations
6. When generators and batteries may become strategically important

---

# 2. Data and Analysis Artifacts

The following files were generated and analyzed:

| File | Purpose |
|--------|--------|
| hosting_capacity_all_buses.csv | Minimum hosting capacity for every bus across all 120 representative periods |
| bus_screening_metrics.csv | Composite screening metrics using branch capacity, generation, load, and hosting capacity |
| diversified_top20.csv | Top candidate buses selected from different electrical neighborhoods |
| bottleneck_diversity_analysis.csv | Identification of common and unique transmission bottlenecks |
| 1079_2054_joint_test.md | Joint hosting-capacity study for two generation-limited buses |
| 6062_6298_joint_test.md | Joint hosting-capacity study for two unique-corridor buses |
| portfolio_comparison.md | Multi-bus portfolio experiments |
| site_size_and_competition_study.md | Site-size and competition sensitivity study |
| crowding_study.md | Concentrated crowding scenarios |
| system_reserve_margin_study.md | System-wide generation headroom evaluation |

---

# 3. Key Discovery #1:
## The 3024 MW Ceiling is Real

The system reserve-margin study showed:

```text
Total active generation capacity = 81,201.890 MW

Peak load period = Period 109

Peak load = 78,177.286 MW
```

Therefore:

```text
Reserve margin

81,201.890
-
78,177.286
=
3,024.604 MW
```

The largest hosting-capacity value found anywhere in the system was:

```text
3,024.604 MW
```

which matches the reserve margin to numerical precision.

### Interpretation

Many top-ranked buses are not constrained by transmission.

Instead, they simply provide access to the same remaining generation headroom available during Period 109.

---

# 4. Key Discovery #2:
## Hosting Capacities Are NOT Additive

A major assumption was:

```text
HC(1079) + HC(2054)
≈ Total Capacity
```

This turned out to be false.

### Individual Results

```text
HC(1079) = 3024.6 MW

HC(2054) = 3024.6 MW
```

Naively:

```text
6049 MW
```

would appear available.

### Actual Joint Result

```text
1079 + 2054

Joint HC = 3024.6 MW
```

with:

```text
432 / 432 generators at Pmax
```

and no transmission bottleneck.

### Conclusion

These buses compete for the same pool of generation headroom.

---

# 5. Key Discovery #3:
## Unique Buses Can Still Interact

Initially we believed:

```text
6062
6298
```

were independent opportunities.

They had different bottlenecks in single-bus hosting-capacity studies.

### Individual Values

```text
HC(6062) = 2958.8 MW

HC(6298) = 2513.8 MW
```

Expected:

```text
5472.7 MW
```

### Actual Joint Result

```text
3007.9 MW
```

Interaction ratio:

```text
54.96%
```

A new bottleneck emerged:

```text
Branch b02136
```

even though that branch was not the limiting factor in the individual studies.

### Conclusion

New constraints can emerge whenever multiple loads are introduced simultaneously.

---

# 6. Key Discovery #4:
## Shared Bottlenecks Exist

Many of the shortlisted buses depend on:

```text
Branch b02579
```

Examples:

```text
5413
5317
5015
8043
5384
5295
2002
8126
```

All were associated with:

```text
b02579
```

### Conclusion

Electrical-neighborhood diversity does not necessarily imply transmission-resource diversity.

Multiple promising buses may still depend on the same critical corridor.

---

# 7. Key Discovery #5:
## Period 109 Dominates Everything

The majority of studies were limited by:

```text
Period 109
```

This corresponds to:

```text
Peak load
Minimum reserve margin
Maximum generation utilization
```

For many candidate solutions:

```text
Period 109
=
worst-case period
```

### Implication

Any technology that reduces net demand during Period 109 may provide significant strategic value.

---

# 8. Competition Results

Competition scenarios included:

### No Competitors

```text
100% served
```

for most candidate buses.

### Five Competitors

Approximately:

```text
50%
```

served.

### Ten Competitors

Approximately:

```text
27%
```

served.

The exact bus had surprisingly little effect.

### Interpretation

At this level of congestion the allocation mechanism becomes dominant.

Differences between good buses become much smaller than differences caused by system-level scarcity.

---

# 9. Lessons Learned About Bus Selection

Initially:

```text
Choose highest HC bus.
```

Current understanding:

```text
Not necessarily.
```

Many buses near the top of the ranking:

```text
HC ≈ 3024 MW
```

appear to be accessing the same generation reserve.

Possible consequence:

```text
Many teams may select the same regions.
```

### Current View

A bus ranked 20–100 with:

```text
HC = 2800–3000 MW
```

may ultimately outperform a top-ranked bus if fewer teams are competing for the same underlying resource.

This remains a hypothesis and has not yet been proven.

---

# 10. Current Working Hypotheses

## Hypothesis A

The top-ranked generation-limited buses compete for a common generation reserve pool.

Evidence:

```text
1079 + 2054 test
```

---

## Hypothesis B

Shared transmission bottlenecks are likely to become more important as more teams enter the system.

Evidence:

```text
b02579
b02136
```

appear repeatedly.

---

## Hypothesis C

Generators may become valuable because they reduce dependence on the 3024 MW generation reserve margin.

Example:

```text
1000 MW Data Center
500 MW Onsite Generation

Net Grid Load = 500 MW
```

---

## Hypothesis D

Batteries may become valuable because most congestion is concentrated in a small number of representative periods, particularly Period 109.

A battery can:

```text
Charge during low-stress periods

Discharge during Period 109
```

thereby reducing dependence on scarce generation and transmission resources.

---

# 11. What We Have NOT Proven Yet

The following questions remain unanswered:

### Generator Questions

- How much onsite generation improves score?
- Does generation improve allocation factor?
- At what generator size does ROI become unfavorable?

### Battery Questions

- Does storage materially increase score?
- Does storage improve allocation factor?
- How large must a battery be to matter?

### Bus Selection Questions

- Are buses ranked 20–100 actually less crowded?
- Do less-obvious buses outperform top-ranked buses under competition?
- Which buses are truly independent?

---

# 12. Recommended Next Experiments

## 
