# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.344116 | 30.763287 | 0.586364 | 0.000207 | 0.194000 | 0.138600 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,704.157 | 295.843 | 298,685.880 | 298,685.880 | 9.000 | 3,271.036 | 3,370.762 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 125 MW of S1 generation and 200 MW / 800 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,800.000 | 4,612,314.574 | 4,612,314.574 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 198.000 | 198.000 | 0.000 | 396.000 | 891.000 | 891.000 |
| 2 | 198.000 | 198.000 | 143.355 | 396.000 | 945.645 | 945.645 |
| 3 | 198.000 | 198.000 | 198.000 | 396.000 | 838.918 | 838.918 |
| 4 | 198.000 | 198.000 | 0.000 | 396.000 | 608.914 | 608.914 |
| 5 | 198.000 | 198.000 | 0.000 | 396.000 | 792.000 | 792.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 599.000000 | 0.000000 | 99.000000 | 0.000000 | 297.000000 | 794.311199 | 600.000000 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 2 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 297.000000 | 992.311199 | 600.000000 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |
| 105 | 478.652333 | 21.347667 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 376.750000 | 24.250000 | 0.000000 | 99.000000 | 297.000000 | 0.000000 | 579.604651 | 188.058673 | b02136:lower |
| 107 | 376.750000 | 24.250000 | 0.000000 | 99.000000 | 198.000000 | 0.000000 | 1,128.372408 | 96.932230 | b02136:lower |
| 108 | 376.750000 | 24.250000 | 0.000000 | 99.000000 | 99.000000 | 0.000000 | 1,473.342231 | 39.647743 | b02136:lower |
| 109 | 526.250000 | 72.750000 | 99.000000 | 0.000000 | 198.000000 | 38.961045 | 1,216.966070 | 20.109084 | b02136:lower |
| 110 | 376.750000 | 24.250000 | 0.000000 | 99.000000 | 99.000000 | 107.977060 | 1,581.319291 | 39.647743 | b02136:lower |
| 111 | 376.750000 | 24.250000 | 0.000000 | 99.000000 | 0.000000 | 0.000000 | 1,128.372408 | 96.932230 | b02136:lower |
| 112 | 440.851940 | 59.148060 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 238.961045 | 188.058673 | b02136:lower |
| 113 | 478.652333 | 21.347667 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 49.281810 | 0.000000 | 959.726330 | b02090:lower, b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g125_b200_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g125_b200_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
