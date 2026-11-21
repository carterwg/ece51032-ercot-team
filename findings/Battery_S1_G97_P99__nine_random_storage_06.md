# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.344170 | 30.763287 | 0.586342 | 0.000176 | 0.194000 | 0.138600 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,738.369 | 261.631 | 297,350.786 | 297,350.786 | 9.000 | 3,272.033 | 3,088.537 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 165 MW of S1 generation and 185 MW / 740 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,665.000 | 4,137,756.414 | 4,137,756.414 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 198.000 | 198.000 | -0.000 | 396.000 | 851.286 | 851.286 |
| 2 | 198.000 | 198.000 | 99.000 | 396.000 | 864.357 | 864.357 |
| 3 | 198.000 | 198.000 | 198.000 | 396.000 | 861.636 | 861.636 |
| 4 | 198.000 | 198.000 | 0.000 | 396.000 | 693.000 | 693.000 |
| 5 | 198.000 | 198.000 | 0.000 | 396.000 | 792.000 | 792.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 599.000000 | 0.000000 | 99.000000 | 0.000000 | 297.000000 | 749.311199 | 555.000000 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 1 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 198.000000 | 776.814540 | 370.000000 | 14,552.010372 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |
| 105 | 483.510209 | 16.489791 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 376.750000 | 24.250000 | 0.000000 | 99.000000 | 297.000000 | 0.000000 | 489.604651 | 188.058673 | b02136:lower |
| 107 | 376.750000 | 24.250000 | 0.000000 | 99.000000 | 198.000000 | 0.000000 | 1,038.372408 | 96.932230 | b02136:lower |
| 108 | 376.750000 | 24.250000 | 0.000000 | 99.000000 | 99.000000 | 0.000000 | 1,383.342231 | 39.647743 | b02136:lower |
| 109 | 526.250000 | 72.750000 | 99.000000 | 0.000000 | 198.000000 | 162.333453 | 1,070.338478 | 20.109084 | b02136:lower |
| 110 | 376.750000 | 24.250000 | 0.000000 | 99.000000 | 99.000000 | 0.000000 | 1,383.342231 | 39.647743 | b02136:lower |
| 111 | 376.750000 | 24.250000 | 0.000000 | 99.000000 | 0.000000 | 48.961045 | 1,087.333453 | 96.932230 | b02136:lower |
| 112 | 465.348338 | 34.651662 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 418.961045 | 188.058673 | b02136:lower |
| 113 | 483.510209 | 16.489791 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 3.199407 | 0.000000 | 1,005.808733 | b02090:lower, b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_random_storage_06/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_random_storage_06/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
