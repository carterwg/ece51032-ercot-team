# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.346525 | 30.763287 | 0.583729 | 0.000433 | 0.194000 | 0.138600 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,489.836 | 510.164 | 248,034.394 | 248,034.394 | 9.000 | 3,004.762 | 3,187.258 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 125 MW of S1 generation and 125 MW / 500 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,125.000 | 2,540,081.947 | 2,540,081.947 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 198.000 | 198.000 | 0.000 | 396.000 | 693.000 | 693.000 |
| 2 | 198.000 | 198.000 | 0.000 | 396.000 | 758.396 | 758.396 |
| 3 | 198.000 | 198.000 | 0.000 | 396.000 | 792.000 | 792.000 |
| 4 | 198.000 | 198.000 | -0.000 | 396.000 | 495.000 | 495.000 |
| 5 | 198.000 | 198.000 | 0.000 | 396.000 | 417.088 | 417.088 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 599.000000 | 0.000000 | 99.000000 | 0.000000 | 297.000000 | 569.311199 | 375.000000 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 3 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 297.000000 | 599.789549 | 250.000000 | 14,069.579627 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |
| 105 | 478.652333 | 21.347667 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 427.250000 | 72.750000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 67.604651 | 188.058673 | b02136:lower |
| 107 | 370.031154 | 30.968846 | 0.000000 | 99.000000 | 297.000000 | 0.000000 | 1,043.728802 | 96.932230 | b02136:lower |
| 108 | 328.250000 | 72.750000 | 0.000000 | 99.000000 | 198.000000 | 0.000000 | 862.342231 | 39.647743 | b02136:lower |
| 109 | 374.569291 | 72.750000 | 0.000000 | 52.680709 | 145.319291 | 0.000000 | 1,026.324316 | 20.109084 | b02136:lower |
| 110 | 380.930709 | 72.750000 | 0.000000 | 46.319291 | 99.000000 | 0.000000 | 915.022940 | 39.647743 | b02136:lower |
| 111 | 328.250000 | 72.750000 | 0.000000 | 99.000000 | 0.000000 | 0.000000 | 517.372408 | 96.932230 | b02136:lower |
| 112 | 427.250000 | 72.750000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 67.604651 | 188.058673 | b02136:lower |
| 113 | 478.652333 | 21.347667 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g125_b125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g125_b125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
