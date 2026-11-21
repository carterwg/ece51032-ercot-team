# Saket Second-Round Findings for the 500 MW Game

**Prepared November 18, 2026.** This note follows the [initial solo findings](Saket_Initial_Findings.md) and focuses on ten teams requesting up to **500 MW each per submission**.

**S1 is worth testing with storage.** Before any submissions, the grid has enough aggregate spare generation to cover the ten-team 5,000 MW request for 8,753 of 8,760 represented annual hours. Seven peak-day hours put that firm request out of reach on grid power alone. A short battery discharge may help a 500 MW site retain its full allocation through that window. A **200 MW generator at bus 6141** already passed the full-load S1 check across all four named rival fields. The existing **125 MW** plan also passed, so 200 MW is a verified comparison case and the minimum required size remains open.

## 1. What the hourly grid profile shows

`H_t` denotes headroom in hour `t`. It equals the sum of the in-service generators’ maximum output, plus fixed injections, minus existing grid demand. The representative model has 81,201.89 MW of in-service generation and zero fixed injections. The S1 headroom varies with demand across the 120 modeled hours.

| S1 grid headroom before submissions | Period | MW | Annual hours represented at that exact value |
| --- | --- | ---: | ---: |
| Minimum | 109, peak day at 13:00 | 3,024.604 | 1.00 |
| Maximum | 25, day 2 at 01:00 | 23,034.479 | 99.73 |

The annual weighted median is **14.33 GW**. Aggregate headroom falls below **5 GW** in periods **106–112**, from 10:00 through 16:00 on the representative peak day. At period 109, existing demand reaches **78,177.286 MW**. The game sets one firm admitted capacity per site for all 120 hours. Those few tight hours can therefore cut capacity and IT value for the whole year. [Demand profiles](../ercot-connection-game/data/processed/activsg2000_representative_v1/demand_bus.csv) · [Representative day weights](../ercot-connection-game/data/processed/activsg2000_representative_v1/representative_days.csv)

The hosting-capacity table answers a different question. Each bus is tested separately against the same base load. **146 buses** can individually host over 2 GW, and all compete for the same 3.0246 GW of spare generation at period 109. Against nine grid-only rivals at bus 6141, our grid-only allocation rose from **300.42 MW at one site** to **302.43 MW across five electrically diverse sites**. Splitting eased the local line constraint and let the entire field use about **20 MW** more grid supply. The gain was about **2 MW for us** because the field approached the shared generation ceiling. [Hosting-capacity table](../analysis/hosting_capacity_all_buses.csv) · [Ten-team comparison](../findings/Ten_teams_500_MW_comparison.md)

## 2. S1 generation that achieved full admission

The in-memory S1 check used our single **500 MW site at bus 6141 with 200 MW of generation**, nine rivals at 500 MW each, and the instructor’s joint dispatch and allocation over all 120 hours.

| Rival S1 plans | Our admitted MW | Peak private output MW | Modeled hours with private output |
| --- | ---: | ---: | ---: |
| Nine grid-only rivals at 6141 | 500.00 | 199.73 | 3 |
| Nine grid-only rivals at 1079 | 500.00 | 199.73 | 3 |
| Nine grid-only S1 rivals split across 1079 and 2054 | 500.00 | 199.73 | 3 |
| Nine rivals with full generation across five electrical sites | 500.00 | 113.71 | 7 |

This was an S1 allocation check. The matched four-round campaign comparison already includes a **125 MW S1 / 500 MW S2** plan at bus 6141. That plan admitted our full 500 MW in every round and led the tested menu with a **$69.026B mean** and a **$68.273B worst-case score**. In the same-bus crowding case, its S1 generator was needed in three represented annual hours. At the tightest hour the generator supplied **124.74 MW**, the grid supplied **375.26 MW** to us, and the evaluator shifted some grid capacity away from rivals because our backup let it serve more total load. [125 MW S1 strategy](../findings/G_eq_125_S1_C_eq_G_S2_500_6141.md) · [Same-bus S1 dispatch](../findings/G_eq_125_S1_C_eq_G_S2_500_6141__nine_grid_at_6141.md)

## 3. What carries into S2

The residual in hour `t` is `R_t = H_t - P_S1,grid,t`, where the second term is the net hourly grid withdrawal from all S1 sites. S1 withdrawals carry forward as fixed base load. S2 adds new sites on top of that base.

For this check, our S1 plan used **125 MW of generation at bus 6141**. Each rival split its 500 MW request across the same five buses, and only its S1 generation size changed.

| Rival S1 generation per team | All teams’ admitted S1 load | Minimum S2 residual | S2 residual below 500 MW, modeled / annual hours | Longest run below 500 MW | S2 residual below 5 GW, modeled / annual hours | Longest run below 5 GW |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 MW | 3,149.34 MW | 0 MW | 5 / 5.00 | 5 h | 26 / 1,090.05 | 15 h |
| 250 MW | 5,000.00 MW | 0 MW | 12 / 302.19 | 9 h | 39 / 1,868.92 | 19 h |
| 500 MW | 5,000.00 MW | 0 MW | 12 / 302.19 | 9 h | 39 / 1,868.92 | 19 h |

With grid-only rivals, the 500 MW target had a **1,646 MWh** deficit on the peak day. With either backup-heavy rival plan, it had an **880 MWh** deficit on day 4 and a **4,424 MWh** deficit on the peak day. Both backup-heavy fields admitted the full 5 GW in S1 and had nearly identical net grid withdrawals. Installed S1 generation can reduce withdrawal when it runs, and it can increase the amount of S1 load that is admitted and carried forward. Both effects matter. [Saved full-backup rival case](../findings/G_eq_125_S1_C_eq_G_S2_500_6141__nine_both_cg_ptdf_5.md)

For our new S2 site at 6141, an hourly network check and a daily storage feasibility model found that a **500 MW / 2,000 MWh battery** could cover the grid-only-rival S1 outcome at **$700M** of capital, compared with **$1B** for a 500 MW generator. The battery’s grid draws passed the network check in all 120 hours with S1 fixed and our S2 site alone. With partial or full S1 backup among rivals, **500 MW of generation** was the least-capital solution for our site. The cost screen covered equipment capital. Joint S2 allocation, charging competition, and operating costs remain open. [Battery and capital rules](../configs/scoring/dispatch_scoring_rules_500mw.json)

## 4. Tests to run next

1. **Test batteries in S1 on a small set of matched fields.** At bus 6141, compare grid-only, 125 MW and 200 MW of generation, battery-only, and a smaller generator plus a battery. Start with the same S2 plan for each S1 candidate so the results show what S1 changed. Use the four-hour storage rule and verify that each battery starts and ends the representative day half full.
2. **Measure admission, charging, and carryover together.** For any S1 battery that retains the full 500 MW, record its charge and discharge hours, equipment and energy costs, and the residual grid profile it leaves for S2. The joint dispatch determines both the charging opportunity and how much of our request gets admitted.
3. **Use 500 MW of S2 generation as the benchmark.** Compare storage or a hybrid S2 plan against it in the short-deficit field. Keep full generation in the comparison for fields with nine-hour shortages. Check all ten teams together before using the smaller-capital result for a submission.
