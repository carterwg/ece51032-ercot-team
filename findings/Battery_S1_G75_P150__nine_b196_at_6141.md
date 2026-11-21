# 500 MW at bus 6141, S1 generator 75 MW and battery 150 MW / 600 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 4,520.193209 | 17.326025 | 30.763287 | 0.576685 | 0.000577 | 0.150000 | 0.210000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,477.167 | 522.833 | 312,253.776 | 312,253.776 | 7.000 | 2,371.499 | 2,358.537 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 0 MW of S1 generation and 196 MW / 784 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,575.916 | 3,766,529.800 | 3,766,529.800 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 300.000 | 300.000 | 0.000 | 600.000 | 900.000 | 900.000 |
| 2 | 300.000 | 300.000 | 0.000 | 600.000 | 900.000 | 900.000 |
| 3 | 300.000 | 300.000 | -0.000 | 600.000 | 883.965 | 883.965 |
| 4 | 300.000 | 300.000 | 0.000 | 600.000 | 750.000 | 750.000 |
| 5 | 300.000 | 300.000 | 0.000 | 600.000 | 640.793 | 640.793 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 650.000000 | 0.000000 | 150.000000 | 0.000000 | 450.000000 | 1,046.295923 | 525.305246 | 14,531.439582 | b01921:upper, b02355:lower |
| 9 | 350.000000 | 0.000000 | 0.000000 | 150.000000 | 450.000000 | 0.000000 | 195.050175 | 9,644.852975 | b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 0.000000 | 1,488.814931 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 0.000000 | 517.687149 | b02136:lower |
| 106 | 425.000000 | 75.000000 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 429.297860 | 188.058673 | b02136:lower |
| 107 | 425.000000 | 75.000000 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 978.065617 | 96.932230 | b02136:lower |
| 108 | 425.000000 | 75.000000 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 1,323.035440 | 39.647743 | b02136:lower |
| 109 | 275.000000 | 75.000000 | 0.000000 | 150.000000 | 450.000000 | 0.000000 | 1,290.698234 | 20.109084 | b02136:lower |
| 110 | 277.166885 | 72.833115 | 0.000000 | 150.000000 | 300.000000 | 0.000000 | 1,175.202324 | 39.647743 | b02136:lower |
| 111 | 275.000000 | 75.000000 | 0.000000 | 150.000000 | 150.000000 | 0.000000 | 828.065617 | 96.932230 | b02136:lower |
| 112 | 275.000000 | 75.000000 | 0.000000 | 150.000000 | 0.000000 | 0.000000 | 279.297860 | 188.058673 | b02136:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 517.687149 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,488.814931 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g75_p150/nine_b196_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g75_p150/nine_b196_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
