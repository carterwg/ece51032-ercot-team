# Strategy findings for team discussion

These results use **ten teams and 500 MW per team per submission**. Each tested field gives all nine rivals the same plan. Campaign scores sum the four graded rounds. Within each week, the evaluator carries all teams’ actual hourly S1 grid withdrawals into S2.

## S1 choice at bus 6141

| Generator | Battery power / energy | S1 capital | Lowest S1 award | Exact 500 MW fields | Mean campaign score | Worst campaign score |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 97 MW | 99 MW / 396 MWh | $332.6M | 499.901525 MW | 32/36 | — | — |
| 95 MW | 105 MW / 420 MWh | $337M | 499.915361 MW | 32/36 | $64.521B | $62.752B |
| 75 MW | 150 MW / 600 MWh | $360M | 499.933808 MW | 33/36 | $64.471B | $62.708B |
| 200 MW | — | $400M | 499.943942 MW | 35/36 | $64.386B | $62.597B |

All four builds cleared 499.9 MW in all 36 fields. The $332.6M build was evaluated in the S1-only refinement. It saved $4.4M versus the $337M build and cleared the threshold by **1.525 kW** in its tightest case, where all nine rivals chose a 50 MW generator and a 175 MW battery at bus 6141. The $337M build had the highest mean and worst-case scores among the five builds in the full campaign comparison. [1 MW results](../findings/Battery_S1_1MW_local_search.md) · [Four-round comparison](../findings/Battery_S1_targeted_optimization.md) · [Tightest dispatch for the $332.6M build](../findings/Battery_S1_G97_P99__nine_g50_b175_at_6141.md)

## Concentrating or splitting the request

The four-field portfolio comparison evaluated 96 campaigns. At equal equipment sizes, a single site at bus 6141 earned a higher mean and worst-case score than the five-site PTDF layout in the tested configurations below.

| S1 / S2 generation | Layout | Lowest S1 award | Mean campaign score | Worst campaign score |
| --- | --- | ---: | ---: | ---: |
| 125 MW / 500 MW | One site | 500 MW | $69.026B | $68.273B |
| 125 MW / 500 MW | Five sites | 500 MW | $68.872B | $67.857B |
| 500 MW / 500 MW | One site | 500 MW | $67.501B | $66.773B |
| 500 MW / 500 MW | Five sites | 500 MW | $67.332B | $66.357B |

Against nine grid-only rivals at 6141, splitting a grid-only S1 request lifted our award from **300.419 MW to 302.430 MW**. The grid’s shared generation ceiling limited the gain. The portfolio and S1 sizing tables use different matched sets of rival plans. [Ten-team portfolio comparison](../findings/Ten_teams_500_MW_comparison.md) · [Comparison data](../analysis/strategy/ten-teams-500mw/comparison.csv)

## Grid constraints and S2 carryover

Part 1 screened **101 buses** and identified **35 overlapping signed bottleneck groups**. At period 109 the native grid has **3,024.604 MW** of aggregate spare generation. Standalone hosting capacities share that supply, and simultaneous loads can introduce new binding lines. The five-site electrical layout tested buses 6141, 5395, 6342, 5451, and 6004. [Bottleneck groups and PTDF interactions](../findings/Part1_groups_and_interactions.md)

Across the 36-field campaign comparison, our new 500 MW S2 sites with matching generation kept the full award after carrying forward all ten teams’ S1 withdrawals. The earlier portfolio comparison found a minimum S2 award of 0 MW in its grid-only configurations. The admission and net grid draw of the S1 field determine the S2 base load. [Carryover and residual headroom](Saket_Second_Round_Findings.md)

The discussion can focus on the S1 admission margin the team wants to retain, which rival equipment cases merit the most weight, and whether to run the $332.6M build through a matched four-round comparison.

[Saket’s full sizing notes](Saket_Findings_11-19-2026.md) · [Full findings and reproducible study on Saket](https://github.com/carterwg/ece51032-ercot-team/tree/9ad5075b1ecdb501fd063f56a328d9cbcd4a972f/findings)
