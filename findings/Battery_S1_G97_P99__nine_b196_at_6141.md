# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 4,510.990027 | 17.353428 | 30.763287 | 0.576511 | 0.000747 | 0.194000 | 0.138600 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,323.159 | 676.841 | 201,802.452 | 201,802.452 | 7.000 | 2,539.041 | 2,340.584 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 0 MW of S1 generation and 196 MW / 784 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,572.308 | 3,659,846.969 | 3,659,846.969 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 198.000 | 198.000 | 0.000 | 396.000 | 556.315 | 556.315 |
| 2 | 198.000 | 198.000 | 0.000 | 396.000 | 505.843 | 505.843 |
| 3 | 198.000 | 198.000 | 0.000 | 396.000 | 675.282 | 675.282 |
| 4 | 198.000 | 198.000 | 0.000 | 396.000 | 495.000 | 495.000 |
| 5 | 198.000 | 198.000 | 0.000 | 396.000 | 482.341 | 482.341 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 599.000000 | 0.000000 | 99.000000 | 0.000000 | 297.000000 | 1,048.205394 | 467.011536 | 14,531.439582 | b01921:upper, b02355:lower |
| 9 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 297.000000 | 0.000000 | 236.846993 | 9,644.852975 | b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 1,498.018113 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 526.890331 | b02136:lower |
| 106 | 403.000000 | 97.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 398.094678 | 188.058673 | b02136:lower |
| 107 | 403.000000 | 97.000000 | 0.000000 | 0.000000 | 396.000000 | 48.692880 | 995.555316 | 96.932230 | b02136:lower |
| 108 | 304.000000 | 97.000000 | 0.000000 | 99.000000 | 297.000000 | 0.000000 | 1,192.832258 | 39.647743 | b02136:lower |
| 109 | 304.000000 | 97.000000 | 0.000000 | 99.000000 | 198.000000 | 0.000000 | 1,310.495053 | 20.109084 | b02136:lower |
| 110 | 306.158566 | 94.841434 | 0.000000 | 99.000000 | 99.000000 | 0.000000 | 1,194.990824 | 39.647743 | b02136:lower |
| 111 | 352.692880 | 97.000000 | 0.000000 | 50.307120 | 48.692880 | 0.000000 | 896.555316 | 96.932230 | b02136:lower |
| 112 | 354.307120 | 97.000000 | 0.000000 | 48.692880 | 0.000000 | 0.000000 | 349.401798 | 188.058673 | b02136:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 526.890331 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,498.018113 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_b196_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_b196_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
