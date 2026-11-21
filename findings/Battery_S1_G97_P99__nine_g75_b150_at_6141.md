# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.343985 | 30.763287 | 0.585995 | 0.000707 | 0.194000 | 0.138600 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,305.543 | 694.457 | 256,876.348 | 256,876.348 | 9.000 | 3,257.071 | 2,908.027 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 75 MW of S1 generation and 150 MW / 600 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,350.000 | 3,140,999.401 | 3,140,999.401 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 198.000 | 198.000 | 0.000 | 396.000 | 755.021 | 755.021 |
| 2 | 198.000 | 198.000 | -0.000 | 396.000 | 833.482 | 833.482 |
| 3 | 198.000 | 198.000 | 99.000 | 396.000 | 792.000 | 792.000 |
| 4 | 198.000 | 198.000 | 0.000 | 396.000 | 454.375 | 454.375 |
| 5 | 198.000 | 198.000 | 0.000 | 396.000 | 545.868 | 545.868 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 599.000000 | 0.000000 | 99.000000 | 0.000000 | 297.000000 | 644.311199 | 450.000000 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 3 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 233.172443 | 750.000000 | 400.210451 | 14,069.579627 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |
| 105 | 466.208745 | 33.791255 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 403.000000 | 97.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 212.104651 | 188.058673 | b02136:lower |
| 107 | 304.000000 | 97.000000 | 0.000000 | 99.000000 | 297.000000 | 16.819291 | 678.691699 | 96.932230 | b02136:lower |
| 108 | 304.000000 | 97.000000 | 0.000000 | 99.000000 | 198.000000 | 0.000000 | 1,006.842231 | 39.647743 | b02136:lower |
| 109 | 317.390323 | 97.000000 | 0.000000 | 85.609677 | 112.390323 | 0.000000 | 1,137.895349 | 20.109084 | b02136:lower |
| 110 | 393.235415 | 93.374261 | 0.000000 | 13.390323 | 99.000000 | 0.000000 | 1,121.308301 | 39.647743 | b02136:lower |
| 111 | 328.250000 | 72.750000 | 0.000000 | 99.000000 | 0.000000 | 105.104651 | 959.977060 | 96.932230 | b02136:lower |
| 112 | 427.250000 | 72.750000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 405.104651 | 188.058673 | b02136:lower |
| 113 | 466.208745 | 33.791255 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g75_b150_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g75_b150_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
