# Current State of the Project

**Purpose:** a 10-minute handoff for a teammate joining the team. This is a synthesis of existing analyses, notes, reports, notebooks, and generated artifacts; it does not report or perform any new simulations.

## Executive summary

The project has moved past standalone bus ranking. The evidence establishes three central facts:

1. **Period 109 is the representative-grid bottleneck.** Active generation is 81,201.890 MW and peak representative load is 78,177.286 MW, leaving only 3,024.604 MW of arithmetic generation headroom.
2. **Hosting capacities are not additive.** Joint loads create shared generation or transmission constraints that do not appear in separate one-bus tests.
3. **The tested competitive previews are dominated by system allocation, not by small bus differences.** Five-rival cases serve about 50.4% of a 1,000 MW request; ten-rival cases serve about 27.5%, and the four tested candidates are tied within numerical precision.

For the officially evaluated **500 MW, solo, finalized campaign**, Carter's rank-1 C=G strategy at bus 6141 is substantially better than the bus-1001 baseline:

- Carter rank-1: **$67.955 billion** combined across the four graded rounds
- Full-generation baseline: **$55.271 billion**
- Difference: **$12.684 billion**, or **22.95%**
- Normalized scores: **78.20** versus **23.96**

This comparison proves the relative result only in the **matched solo campaign**; it does not establish that bus 6141 beats the field in competition or under unknown opponents.

## 1. What has been conclusively proven

The following are proven within their stated representative-grid or matched-campaign scope.

### Grid and hosting-capacity facts

- **The representative system reserve ceiling is 3,024.604 MW.** The all-bus hosting result agrees with the period-109 arithmetic reserve margin to numerical precision.
- **The ceiling is system headroom, not a guarantee of bus availability.** Some buses reach it without a transmission branch binding, while other buses encounter a transmission limit first.
- **Hosting capacities are not additive.**
  - Buses 1079 and 2054 each have about 3,024.604 MW individually, but together have only 3,024.604 MW of equal-load joint capacity, not 6,049.208 MW.
  - Buses 6062 and 6298 have separate capacities totaling 5,472.673 MW, but their equal-load joint capacity is 3,007.890 MW.
- **Joint loads can reveal new constraints.** The 6062/6298 joint test is limited by branch b02136, even though that branch was not the individual bottleneck for these buses.
- **Shared bottlenecks exist.** Eight buses in the short-listing analysis are limited by branch b02579, and buses 7095/7414 share b02136.
- **Period 109 is the main stress period.** It is the limiting period for the reserve margin and for the key hosting-capacity and joint-hosting experiments.

### Site-size and competition facts from the student preview

- In the **standalone, no-storage, no-opponent preview**, 500 MW and 1,000 MW plans at the five study buses are fully served. At a given size, all candidate buses have the same preview score.
- The valid 1,000 MW plan earns **$36.5266 billion** in that standalone Week-2 preview; a 500 MW plan earns **$18.2633 billion**.
- The previously proposed 1,500 MW and 2,000 MW plans are invalid under the 1,000 MW per-team/per-submission cap.
- In the preview's five-rival and ten-rival fallback scenarios, all four candidate buses are effectively tied:
  - Five rivals: about 50.405% served
  - Ten rivals: about 27.494% served
- Concentrated crowding at 1079, crowding at 5131, and diversified rival siting all produce essentially the same 27.494% allocation for the 1079/6062/6298/7414 candidates. They are not measurably different in the tested preview scenarios.
- The preview competition cases are principally transmission-limited; branch b02579 dominates.

### C=G campaign facts

- The Carter rank-1 strategy and the full-generation baseline were each evaluated for all 120 periods in all four graded rounds with the 500 MW finalized cap.
- Both campaigns were valid and feasible in every round, with full service in the solo campaign.
- Bus 6141 is a proven advantage over bus 1001 in this exact solo campaign.
- The bus-6141 C=G design avoids generator operating cost and uses only grid generation; it does not outperform the bus-1001 design through private generation in this campaign. It wins mainly because its grid-only dispatch removes the baseline's generator operating cost.

### Workflow facts

- Week 1 is practice only. Neither Week-1 submission counts toward the final score.
- Week 2 has no grid-energy charge.
- Week 3 charges grid purchases at joint-dispatch LMP.
- Each week starts from the representative base; assets do not carry between weeks.
- Within a week, Week-S1 sites enter Week-S2 as base load. A Week-S2 file lists only new sites.
- The final score is the sum of four graded rounds: W2S1, W2S2, W3S1, and W3S2.
- The team per-submission connection cap is 1,000 MW.
- The notebooks read saved results and do not rerun the game.

## 2. What hypotheses were disproven

1. **“Choose the highest hosting-capacity bus and you maximize the score.”** Disproven as a general strategy: standalone top-HC buses share the same generation ceiling, and all five 1,000 MW candidates tie in the standalone and tested competition previews.
2. **“Hosting capacities for separate buses add.”** Disproved by the 1079/2054, 6062/6298, and four-location joint tests.
3. **“Bus 6062 and bus 6298 are independent because they have unique individual bottlenecks.”** Disproved for simultaneous equal-load operation: they jointly encounter b02136.
4. **“A larger standalone site will always be feasible and useful.”** Disproved for 1,500 MW and 2,000 MW requests, which exceed the released 1,000 MW cap.
5. **“The concentration of rivals around bus 1079 or 5131 proves that one candidate bus is more crowded/resilient than the others.”** The existing concentrated-crowding preview showed no meaningful difference among 1079, 6062, 6298, and 7414.
6. **“The composite screening rank is a direct score ranking.”** It is a heuristic for diversity and bottleneck exposure, not a game score. It should not be used alone to choose a final submission.
7. **“Bus 6298 is expected to outperform the other tested candidates.”** It was deliberately treated as a high-risk, unique-corridor option, but no existing preview showed such an advantage.

## 3. What hypotheses are still open

### Immediate Week-1 questions

- How does the **actual joint evaluator**, under the full class plan, allocate connection capacity?
- Which branches bind at Week 1, and are the binding constraints the same at every representative period?
- What is the real allocation fraction and curtailment for the proposed diverse portfolio?
- Does the carried base load for Submission 2 reveal the same bottlenecks as the prior standalone analyses?

### Bus-selection questions

- Do less-obvious buses outperform bus 6141 or 2054 under real competition?
- Are buses ranked 20–100 genuinely less crowded, or do they simply expose different but equally scarce corridors?
- Which buses are truly independent under an actual eight-team or full-class joint plan?
- Do top-ranked generation-limited buses always share the 3,024.604 MW resource pool, or can resources differ by allocation period?

### Generator questions

- How much does onsite generation improve real score and allocation?
- Is there a generator-size threshold beyond which marginal benefit disappears or operating/capital cost dominates?
- Is the C=G relationship still the best generator choice under competition and Week-3 LMP?

### Battery questions

- Does storage materially improve allocated service or score?
- Can storage shift demand away from the actual binding period and thereby improve allocation?
- What are the useful storage power and energy sizes, and does a four-hour battery add enough value to justify its capital cost?
- The student preview **does not dispatch storage**; no current artifact proves a storage benefit.

### Campaign questions

- How do matched opponent scenarios change bus ranking?
- Is the 6141 solo advantage robust under competition and the Week-3 energy charge?
- How sensitive is the rank of a strategy to rival siting, rival resource mix, and joint allocation?
- Is downside risk estimated at all? The current solo notebooks explicitly lack matched multi-scenario risk campaigns, so no real Pareto-risk conclusion exists.

## 4. Which findings are most important for Week 1

1. **Use Week 1 to observe crowding and allocation, not to repeat hosting-screening studies.** The key unknown is actual joint behavior.
2. **The current information-screen recommendation is the spatial portfolio at buses 2054, 6062, 6298, and 7414, using four grid-only 250 MW sites in Submission 1.** It simultaneously tests:
   - a generation-limited bus: 2054
   - unique corridor buses: 6062 and 6298
   - a shared corridor: 7414
3. **Submission 2 should be adaptive.** Place two matched 250 MW sites at the most informative Submission-1 bus:
   - a no-resource control
   - one treatment only: a 125 MW generator or a 62.5 MW/250 MWh four-hour battery
4. **Choose the resource treatment according to the S1 binding behavior:**
   - choose generation if S1 shows generation scarcity
   - choose storage if S1 shows transmission congestion with generation headroom
   - never combine both in the treatment site, because the effect will be ambiguous
5. **Record binding branches, curtailed MW, per-site allocation, generator dispatch, and battery behavior from the official output.** These are more informative than the score alone.
6. **Retain bus 6141 as a scored-campaign candidate, not as a proven Week-1 choice.** The solo evidence is strong for 6141 under C=G, but competition remains untested.
7. **Do not submit 1,500 MW or 2,000 MW counterfactual plans.** They are invalid under the released cap.

## 5. Which findings likely matter only after Week 1

- **Generator and battery sizing sweeps** become more precise once actual binding constraints and allocation factors are known.
- **The final S2 resource choice** should depend on Week-1 residual congestion, and should not be fixed solely from standalone hosting data.
- **Less-obvious bus testing** becomes useful after real crowding patterns reveal which top buses the class is selecting.
- **Matched opponent campaigns** and risk/return comparisons become priority later, once Week-1 behavior supplies realistic opponent assumptions.
- **Week-3 decisions** become critical after observing LMP behavior and grid-withdrawal profiles; Week-2 results do not include energy charges.
- **Storage economics** may become important after Week-1 identifies Period-109 or transmission stress, but its unmeasured real benefit should not drive a prior submission.
- **The bus-6141 versus bus-1001 result** should inform the Week-2/Week-3 benchmark suite, but its solo advantage does not automatically generalize to competition.

## 6. Highest-information-gain analyses to run next

These are recommendations for future work; they are **not** analyses already completed.

1. **Parse the actual Week-1 joint evaluation first.**
   - identify allocated fraction per site
   - identify binding branch and period
   - distinguish generation-limited from transmission-limited cases
   - calculate actual residual headroom in the Week-2 Submission-2 base
2. **Run one matched pair of resource diagnostics at the observed bottleneck bus.**
   - control: no onsite assets
   - treatment: generator only
   - treatment: battery only
   - keep site/bus/capacity and opponent assumptions constant
3. **Build matched opponent campaigns for the strongest two or three strategies.**
   - use the same S1/S2 history
   - use the same rival plans and scenario ID
   - include W2S1, W2S2, W3S1, and W3S2
   - only then estimate downside risk or Pareto membership
4. **Create a bus-crowding sweep based on observed opponent locations.**
   - test top buses, diversified corridors, and the 6141/2054/6062/6298 candidate set
   - vary rival plans rather than varying capacity caps
5. **Quantify generator ROI.** For a fixed real bottleneck bus, compare 0, 125, 250, 500, and 750 MW of generation at matched allocations and score them across all four graded rounds.
6. **Quantify battery ROI and timing.** Compare useful P/B combinations at the actual binding bus, especially four-hour storage variants, and measure allocation change, peak grid withdrawal, and capital cost.
7. **Create an end-to-end portfolio comparison.** Evaluate diversified, single-bus, bus-6141 C=G, and resource-treatment portfolios in the same scenario rather than comparing standalone previews.

## Existing artifact map

- [Top-level project README](../README.md)
- [Architecture](../docs/ARCHITECTURE.md)
- [Official evaluation rules](OFFICIAL_EVALUATION.md)
- [Week-1 recommendation](carter_week1_notes/week1_strategy_recommendation.md)
- [Monday findings](carter_week1_notes/Carter_Monday_Nov11_Findings.md)
- [Joint 1079/2054 test](carter_week1_notes/1079_2054_joint_test.md)
- [Joint 6062/6298 test](carter_week1_notes/6062_6298_joint_test.md)
- [Portfolio comparison](carter_week1_notes/portfolio_comparison.md)
- [Site-size and competition study](carter_week1_notes/site_size_and_competition_study.md)
- [Crowding study](carter_week1_notes/crowding_study.md)
- [Reserve-margin study](carter_week1_notes/system_reserve_margin_study.md)
- [Carter study artifact index](carter_week1_notes/artifact_index.md)
- [Reusable notebook guide](../notebooks/README.md)
- [Baseline campaign report](../analysis/baseline_cg_500mw.json)
- [Carter rank-1 campaign report](../analysis/carter_rank1_cg_500mw.json)
- [Cross-strategy campaign comparison](../analysis/cg_bus_comparison_500mw.csv)
- [Carter Week-1 data manifest](../analysis/carter_week1_material/manifest.json)
