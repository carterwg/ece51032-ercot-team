# Saket’s findings for November 19, 2026

## S1 battery and generator sizing

In the **original seven fields, where rivals used no storage**, the lowest-cost plan tested that kept **500 MW of firm S1 admission** was one site at bus **6141** with **zero local generation and a 196 MW / 784 MWh battery**. The 200 MW generator benchmark also kept the full award. The follow-up below tests what happens when rivals bring batteries. This study follows the [November 18 findings](Saket_Second_Round_Findings.md).

| S1 equipment at bus 6141 | Capital per S1 build | Minimum S1 admission | Mean campaign score | Worst campaign score |
| --- | ---: | ---: | ---: | ---: |
| 200 MW generator, no battery | $400.0M | 500 MW | $67.056B | $62.597B |
| 196 MW / 784 MWh battery, no generator | $274.4M | 500 MW | $67.342B | $62.929B |

Each field had ten teams requesting 500 MW per submission. The study included 93 S1 sizing runs and 14 four-round finalist campaigns. Those campaigns held our S2 plan at a new 500 MW site with 500 MW of generation and carried forward all ten teams’ actual S1 grid withdrawals. Both finalists kept 500 MW in every S1 and S2 round. The battery saved **$125.6M per S1 build** and raised the four-round score in every field, by **$285M on average**. Means weight the seven tested fields equally. [Full sizing and score comparison](../findings/Battery_S1_comparison.md)

## Why the battery worked

The native grid fell below the full 5,000 MW field request in **seven of the 120 modeled hours**, periods 106–112. These represent seven annual hours. The evaluator assigns one firm capacity for the entire horizon, so a short peak can reduce the award and IT value for the whole year.

With nine rivals at bus 6141 each carrying 200 MW of generation, serving all ten full requests required about **195.5 MW of support from our site** at the tightest hour. The three-hour minimum discharge under that full-field calculation totaled **351.2 MWh**. Holding enough energy and delivering it fast enough were separate requirements. The joint evaluator awarded **499.15 MW** with a 195 MW battery and **500 MW** with a 196 MW battery. At period 109, the 196 MW battery supplied 196 MW, the grid supplied 304 MW, and line `b02136` was binding. The recorded schedule satisfied the game’s four-hour battery rule and returned to 50% state of charge at the end of each modeled day. [Tightest-field dispatch](../findings/Battery_S1_G0_P196__nine_g200_at_6141.md)

## How much the rival assumptions matter

- In the **original four fields**, the cheapest tested plan with exactly 500 MW of S1 admission used a **35 MW / 140 MWh battery** and zero generation. It cost **$49M**. A 25 MW / 100 MWh battery had a slightly higher mean W3S1 score, with a minimum award of **499.944 MW**. These smaller plans were evaluated in S1 only.
- In the same-bus field with nine 125 MW rival generators, our **125 MW / 500 MWh battery** received only **400.56 MW**. Smaller equipment sizes depend on which rival plans are in the field and how the evaluator allocates capacity.
- The **25 MW generator plus 175 MW / 700 MWh battery** and the **75 MW generator plus 125 MW / 500 MWh battery** both passed the nine-rival, 200 MW same-bus S1 test. They cost **$295M** and **$325M**, respectively, versus **$274.4M** for the battery-only finalist. The 196 MW choice cleared that field’s estimated power requirement by about **0.5 MW**. [Admission matrix and case records](../findings/Battery_S1_comparison.md)

## Follow-up with rival batteries

Each field has nine rivals with identical S1 plans. The table gives the equipment **per rival**, and each rival splits its 500 MW load and equipment equally across the listed buses. In S2, each team builds new 500 MW sites with matching generation and zero new storage. The evaluator carries the hourly S1 net grid withdrawals of all ten teams, including their charging and discharging, into S2.

| Rival buses | S1 generator | S1 battery power / energy | Our S1 award with 196 MW battery | Our S1 award with 200 MW generator |
| --- | ---: | ---: | ---: | ---: |
| 6141 | 0 MW | 125 MW / 500 MWh | 500.00 MW | 500.00 MW |
| 6141 | 0 MW | 196 MW / 784 MWh | 445.74 MW | 500.00 MW |
| 6141, 5395, 6342, 5451, 6004 | 0 MW | 150 MW / 600 MWh | 499.94 MW | 500.00 MW |
| 6141 | 75 MW | 125 MW / 500 MWh | 357.09 MW | 500.00 MW |

We ran five of our S1 equipment plans across the four new fields for 20 campaigns and 80 scored rounds. All five plans received 500 MW in both S2 rounds of every new campaign. The 200 MW generator also kept the full 500 MW in S1 across all eleven fields.

Energy over the tight window explains the loss in the same-bus fields. When all ten teams use 196 MW batteries at 6141, their combined capacity is **7,840 MWh**. Serving all 5,000 MW over periods 106–112 would require **10,785 MWh** of net battery discharge at that bus. The seven-hour energy balance puts the equal award at no more than about **445.8 MW** per team, close to the **445.74 MW** measured. In the hybrid-rival field, the nine generators and all ten batteries have enough combined discharge power at the tightest hour. Even with rival generators at maximum output, the full field would need **6,060 MWh** of net discharge over the window, compared with **5,284 MWh** of storage. [Comparison and run records](../findings/Battery_S1_comparison.md)

The **75 MW generator plus 150 MW / 600 MWh battery** cost **$360M** per S1 build and received **500 MW** in three of the four new fields and **499.938 MW** against the same-bus hybrid rivals. It scored **$64.598B** on average and **$62.861B** in the worst case across the four fields. The 200 MW generator scored **$64.490B** on average and **$62.724B** in the worst case. The hybrid is a lower-cost option if a **0.062 MW** shortfall is acceptable.

The **300 MW / 1,200 MWh battery** also received **500 MW** in three fields and **499.943 MW** against the same-bus hybrid rivals. It cost **$420M** per S1 build, with a mean score of **$64.463B** and a worst score of **$62.701B**. The 75 MW generator plus 125 MW battery cost **$325M** and averaged **$64.496B**, with a minimum S1 award of **489.140 MW**.

## S1-only check across all eleven fields

With a **75 MW generator and 150 MW / 600 MWh battery at bus 6141**, our 500 MW request received **exactly 500 MW in 10 of 11 fields**. It cleared all seven fields without rival storage and three of the four with rival storage. The sole exception was the field where all nine rivals applied at bus 6141 with **75 MW generation and 125 MW / 500 MWh of storage each**. Our award there was **499.937844 MW**, a shortfall of **0.062156 MW**. [All eleven S1 results](../findings/Battery_S1_comparison.md)

In that field, line `b02136` was binding throughout periods 106–112, and our battery reached **0 MWh** at the end of period 111. Serving all ten 500 MW requests through those seven periods would require at least **5,535.1 MWh** of battery discharge given the bus's hosting limit, even with all ten generators running at full output. The field had **5,100 MWh** of battery energy at full nameplate. [S1 dispatch and line limits](../findings/Battery_S1_G75_P150__nine_g75_b125_at_6141.md)

The evaluator settings explain our entire **62.156 kW** shortfall. The fairness tie-break allows a **0.000491 MW** reduction in total field admission. Because our larger battery frees more hosting capacity per MW of admission, that allowance moves our own award down by **12.157 kW**, to **499.987843 MW**. The evaluator then applies a **0.01%** margin to reduced awards, taking off another **49.999 kW**. The energy bound for the first pass matches the saved maximum total field award within **0.000001 MW** when our site takes its full 500 MW. [Tie-break tolerance](../ercot-connection-game/tools/activsg2000/allocation.py#L441) · [Dispatch margin](../ercot-connection-game/src/ercot_game/batch_evaluation.py#L973)

## November 20 randomized rival equipment in S1

Our **75 MW generator and 150 MW / 600 MWh battery at bus 6141** received **exactly 500 MW in all ten additional fields**, bringing the total to **20 exact full awards across 21 fields**. Each new field had nine rivals using the same 500 MW plan. Seed `20261120` draws generator and four-hour battery power in 5 MW increments from preset ranges for six same-bus fields, two fields split across buses 1079 and 2054, and two fields split across the five PTDF-selected buses. Our S1 score averaged **$17.327B**, with a range of **$17.314B to $17.340B**. [Ten-case table and run records](../findings/Battery_S1_comparison.md#randomized-rival-equipment-in-s1)

Eight of the ten new fields admitted the full 5,000 MW. In the other two, our site retained 500 MW while rival awards fell.

| Case | Rival equipment per 500 MW request | Field award | Award per rival | Binding line during periods 106–112 |
| --- | --- | ---: | ---: | --- |
| [01](../findings/Battery_S1_G75_P150__nine_random_storage_01.md) | 55 MW generator and 70 MW / 280 MWh battery at bus 6141 | 4,138.964 MW | 404.329 MW | `b02136` in all seven periods |
| [07](../findings/Battery_S1_G75_P150__nine_random_storage_07.md) | 50 MW generator and 145 MW / 580 MWh battery split across buses 1079 and 2054 | 4,829.753 MW | 481.084 MW | `b02579` in two periods |

## November 20 targeted S1 cost optimization

On the 5 MW grid, the lowest-cost build verified at **499.9 MW or more across all 36 distinct fields** was **95 MW generation and a 105 MW / 420 MWh battery** for **$337M**. It received exactly 500 MW in 32 fields, with a minimum of **499.915361 MW**. Its four-round campaign score averaged **$64.520754B**, with a worst field score of **$62.751587B**. The original $360M hybrid averaged **$64.471011B** and had a worst field score of **$62.707614B**. The $400M generator-only benchmark received exactly 500 MW in 35 fields, with **499.943942 MW** against nine 50 MW generator / 125 MW battery rivals. Every candidate and benchmark received 500 MW in both S2 rounds of every field. [Full comparison and case records](../findings/Battery_S1_targeted_optimization.md)

The 5 MW grid contained **973 pairs** under the $360M budget. The first four storage-rival fields passed with **145 MW generation and a 10 MW / 40 MWh battery** for **$304M**, with a minimum of **499.909596 MW**. That build fell to **384.852389 MW** against nine 50 MW generator / 125 MW battery rivals. The $300M, 150 MW generator-only build received **432.043086 MW** in the five-site storage field. Broader screening eliminated cheaper pairs. The **$334M 90/110 MW pair** received **499.889419 MW** against nine 50/175 MW rivals, while the **$333M 100/95 MW pair** received **499.152164 MW** against nine 200 MW generator-only rivals. The result applies to the tested 5 MW equipment grid and field set.

The **50 MW generator / 175 MW battery** rival plan produced the lowest S1 award for all three finalists and the original hybrid. For the $337M build, all ten full requests would have required about **6,970 MWh** of net discharge through periods 106–112, compared with **6,720 MWh** of combined storage energy. The 50/125 MW rivals caused more curtailment across the field while leaving a larger award for our site.

### 1 MW refinement

Within the 1 MW grid of **85–105 MW generation** and **95–115 MW battery power**, the lowest-cost build verified across all 36 fields was **97 MW generation and a 99 MW / 396 MWh battery** at **$332.6M**. It received exactly 500 MW in 32 fields and at least 499.9 MW in all 36. The lowest award was **499.901525 MW**, or **1.525 kW** above the threshold, against nine 50 MW generator / 175 MW battery rivals. The cheaper **96 MW generator + 100 MW / 400 MWh battery** at **$332.0M** received **499.894922 MW** against those rivals. [1 MW search and exact S1 records](../findings/Battery_S1_1MW_local_search.md)
