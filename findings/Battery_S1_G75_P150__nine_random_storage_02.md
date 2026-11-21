# 500 MW at bus 6141, S1 generator 75 MW and battery 150 MW / 600 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.316396 | 30.763287 | 0.586559 | 0.000332 | 0.150000 | 0.210000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,606.062 | 393.938 | 444,236.252 | 444,236.252 | 9.000 | 3,355.803 | 3,358.797 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 70 MW of S1 generation and 195 MW / 780 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,755.000 | 4,596,334.754 | 4,596,334.754 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 300.000 | 300.000 | 0.000 | 600.000 | 1,418.889 | 1,418.889 |
| 2 | 300.000 | 300.000 | 224.145 | 600.000 | 1,275.855 | 1,275.855 |
| 3 | 300.000 | 300.000 | 150.000 | 600.000 | 1,350.000 | 1,350.000 |
| 4 | 300.000 | 300.000 | 0.000 | 600.000 | 872.613 | 872.613 |
| 5 | 300.000 | 300.000 | -0.000 | 600.000 | 1,115.355 | 1,115.355 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 650.000000 | 0.000000 | 150.000000 | 0.000000 | 450.000000 | 728.311199 | 585.000000 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 1 | 350.000000 | 0.000000 | 0.000000 | 150.000000 | 300.000000 | 847.814540 | 390.000000 | 14,552.010372 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |
| 105 | 471.389725 | 28.610275 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 378.395349 | 56.250000 | 0.000000 | 65.354651 | 534.645349 | 0.000000 | 390.000000 | 188.058673 | b02136:lower |
| 107 | 331.250000 | 18.750000 | 0.000000 | 150.000000 | 384.645349 | 0.000000 | 1,206.622408 | 96.932230 | b02136:lower |
| 108 | 293.750000 | 56.250000 | 0.000000 | 150.000000 | 234.645349 | 0.000000 | 1,199.092231 | 39.647743 | b02136:lower |
| 109 | 509.104651 | 56.250000 | 65.354651 | 0.000000 | 300.000000 | 0.000000 | 1,532.109677 | 20.109084 | b02136:lower |
| 110 | 303.422320 | 46.577680 | 0.000000 | 150.000000 | 150.000000 | 0.000000 | 1,290.012037 | 39.647743 | b02136:lower |
| 111 | 293.750000 | 56.250000 | 0.000000 | 150.000000 | -0.000000 | 158.041239 | 1,012.163647 | 96.932230 | b02136:lower |
| 112 | 443.750000 | 56.250000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 455.354651 | 188.058673 | b02136:lower |
| 113 | 481.250000 | 18.750000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 92.686588 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 57.948491 | 0.000000 | 951.059649 | b02090:lower, b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g75_p150/nine_random_storage_02/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g75_p150/nine_random_storage_02/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
