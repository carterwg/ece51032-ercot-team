# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.343976 | 30.763287 | 0.586162 | 0.000549 | 0.194000 | 0.138600 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,398.306 | 601.694 | 275,989.263 | 275,989.263 | 9.000 | 3,173.301 | 3,006.759 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 85 MW of S1 generation and 155 MW / 620 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,395.000 | 3,281,065.468 | 3,281,065.468 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 198.000 | 198.000 | -0.000 | 396.000 | 863.575 | 863.575 |
| 2 | 198.000 | 198.000 | -0.000 | 396.000 | 918.161 | 918.161 |
| 3 | 198.000 | 198.000 | 198.000 | 396.000 | 764.330 | 764.330 |
| 4 | 198.000 | 198.000 | -0.000 | 396.000 | 493.486 | 493.486 |
| 5 | 198.000 | 198.000 | 0.000 | 396.000 | 588.473 | 588.473 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 599.000000 | 0.000000 | 99.000000 | 0.000000 | 297.000000 | 659.311199 | 465.000000 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 3 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 198.000000 | 775.000000 | 425.210451 | 14,069.579627 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |
| 105 | 469.736834 | 30.263166 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 399.645349 | 72.750000 | 0.000000 | 27.604651 | 368.395349 | 0.000000 | 310.000000 | 188.058673 | b02136:lower |
| 107 | 328.250000 | 72.750000 | 0.000000 | 99.000000 | 269.395349 | 0.000000 | 787.372408 | 96.932230 | b02136:lower |
| 108 | 304.000000 | 97.000000 | 0.000000 | 99.000000 | 170.395349 | 13.157769 | 930.000000 | 39.647743 | b02136:lower |
| 109 | 447.186519 | 80.418132 | 27.604651 | 0.000000 | 198.000000 | 0.000000 | 1,308.466070 | 20.109084 | b02136:lower |
| 110 | 328.250000 | 72.750000 | 0.000000 | 99.000000 | 99.000000 | 0.000000 | 1,132.342231 | 39.647743 | b02136:lower |
| 111 | 328.250000 | 72.750000 | 0.000000 | 99.000000 | 0.000000 | 27.604651 | 814.977060 | 96.932230 | b02136:lower |
| 112 | 427.250000 | 72.750000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 337.604651 | 188.058673 | b02136:lower |
| 113 | 469.736834 | 30.263166 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_random_storage_03/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_random_storage_03/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
