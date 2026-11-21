# 500 MW at bus 6141, S1 generator 75 MW and battery 75 MW / 300 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.943942 | 4,038.922297 | 17.438752 | 30.759838 | 0.567228 | 0.000288 | 0.149983 | 0.104988 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,215.316 | 293.613 | 183,252.053 | 183,252.053 | 7.000 | 3,104.490 | 3,258.077 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 149.983 | 149.983 | -0.000 | 299.966 | 447.187 | 447.187 |
| 2 | 149.983 | 149.983 | 0.000 | 299.966 | 548.557 | 548.557 |
| 3 | 149.983 | 149.983 | -0.000 | 299.966 | 474.407 | 474.407 |
| 4 | 149.983 | 149.983 | -0.000 | 299.966 | 524.941 | 524.941 |
| 5 | 149.983 | 149.983 | -0.000 | 299.966 | 514.684 | 514.684 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | 424.952350 | 0.000000 | 0.000000 | 74.991591 | 214.975644 | 7,979.990452 | b01921:upper |
| 30 | 574.935533 | 0.000000 | 74.991591 | 0.000000 | 192.432313 | 15,936.160998 | b02355:lower |
| 104 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | 299.966365 | 1,970.085843 | none |
| 105 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | 299.966365 | 998.958061 | b02136:lower |
| 106 | 498.144669 | 1.799273 | 0.000000 | 0.000000 | 299.966365 | 188.058673 | b02136:lower |
| 107 | 455.265210 | 44.678731 | 0.000000 | 0.000000 | 299.966365 | 96.932230 | b02136:lower |
| 108 | 359.178137 | 65.774213 | 0.000000 | 74.991591 | 224.974774 | 39.647743 | b02136:lower |
| 109 | 349.984236 | 74.968115 | 0.000000 | 74.991591 | 149.983182 | 20.109084 | b02136:lower |
| 110 | 359.178137 | 65.774213 | 0.000000 | 74.991591 | 74.991591 | 39.647743 | b02136:lower |
| 111 | 386.133291 | 38.819060 | 0.000000 | 74.991591 | -0.000000 | 96.932230 | b02136:lower |
| 112 | 498.144669 | 1.799273 | 0.000000 | 0.000000 | -0.000000 | 188.058673 | b02136:lower |
| 113 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 998.958061 | b02136:lower |
| 114 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,970.085843 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g75_p75/nine_g125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g75_p75/nine_g125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
