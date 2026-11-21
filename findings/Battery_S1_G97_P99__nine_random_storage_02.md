# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.343653 | 30.763287 | 0.586592 | 0.000442 | 0.194000 | 0.138600 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,478.706 | 521.294 | 290,809.491 | 290,809.491 | 9.000 | 3,173.304 | 3,173.304 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 70 MW of S1 generation and 195 MW / 780 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,755.000 | 4,531,716.343 | 4,531,716.343 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 198.000 | 198.000 | 0.000 | 396.000 | 891.000 | 891.000 |
| 2 | 198.000 | 198.000 | 198.000 | 396.000 | 756.595 | 756.595 |
| 3 | 198.000 | 198.000 | 99.252 | 396.000 | 989.748 | 989.748 |
| 4 | 198.000 | 198.000 | 0.000 | 396.000 | 594.000 | 594.000 |
| 5 | 198.000 | 198.000 | 0.000 | 396.000 | 741.855 | 741.855 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 599.000000 | 0.000000 | 99.000000 | 0.000000 | 297.000000 | 779.311199 | 585.000000 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 1 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 198.000000 | 796.814540 | 390.000000 | 14,552.010372 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |
| 105 | 464.117127 | 35.882873 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 378.395349 | 72.750000 | 0.000000 | 48.854651 | 347.145349 | 0.000000 | 390.000000 | 188.058673 | b02136:lower |
| 107 | 376.339025 | 24.660975 | 0.000000 | 99.000000 | 248.145349 | 0.000000 | 1,249.042214 | 96.932230 | b02136:lower |
| 108 | 328.250000 | 72.750000 | 0.000000 | 99.000000 | 149.145349 | 0.000000 | 1,233.592231 | 39.647743 | b02136:lower |
| 109 | 476.104651 | 72.750000 | 48.854651 | 0.000000 | 198.000000 | 49.663647 | 1,548.773324 | 20.109084 | b02136:lower |
| 110 | 328.250000 | 72.750000 | 0.000000 | 99.000000 | 99.000000 | 0.000000 | 1,233.592231 | 39.647743 | b02136:lower |
| 111 | 328.250000 | 72.750000 | 0.000000 | 99.000000 | 0.000000 | 136.041239 | 1,024.663647 | 96.932230 | b02136:lower |
| 112 | 427.250000 | 72.750000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 438.854651 | 188.058673 | b02136:lower |
| 113 | 475.750000 | 24.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 87.186588 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 13.817096 | 0.000000 | 995.191044 | b02090:lower, b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_random_storage_02/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_random_storage_02/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
