# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.940265 | 4,772.043132 | 17.345534 | 30.759612 | 0.582253 | 0.000759 | 0.193977 | 0.138583 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,783.087 | 693.635 | 264,828.404 | 264,828.404 | 9.000 | 2,987.808 | 2,973.847 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 50 MW of S1 generation and 150 MW / 600 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,281.631 | 2,913,586.316 | 2,913,586.316 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 197.976 | 197.976 | -0.000 | 395.953 | 767.287 | 767.287 |
| 2 | 197.976 | 197.976 | -0.000 | 395.953 | 811.292 | 811.292 |
| 3 | 197.976 | 197.976 | -0.000 | 395.953 | 855.102 | 855.102 |
| 4 | 197.976 | 197.976 | -0.000 | 395.953 | 494.941 | 494.941 |
| 5 | 197.976 | 197.976 | -0.000 | 395.953 | 495.636 | 495.636 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 598.928438 | 0.000000 | 98.988172 | 0.000000 | 296.964517 | 767.367509 | 427.210287 | 14,511.434940 | b01921:upper, b02355:lower |
| 3 | 400.952093 | 0.000000 | 0.000000 | 98.988172 | 296.964517 | 574.855628 | 69.252384 | 14,141.710972 | b01921:upper, b02355:lower |
| 104 | 499.940265 | 0.000000 | 0.000000 | 0.000000 | 395.952690 | 0.000000 | 0.000000 | 1,236.965008 | b02136:lower |
| 105 | 492.358106 | 7.582159 | 0.000000 | 0.000000 | 395.952690 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 402.951854 | 96.988411 | 0.000000 | 0.000000 | 395.952690 | 0.000000 | 231.949085 | 188.058673 | b02136:lower |
| 107 | 303.963681 | 96.988411 | 0.000000 | 98.988172 | 296.964517 | 0.000000 | 681.728670 | 96.932230 | b02136:lower |
| 108 | 303.963681 | 96.988411 | 0.000000 | 98.988172 | 197.976345 | 0.000000 | 1,026.698493 | 39.647743 | b02136:lower |
| 109 | 402.951854 | 96.988411 | 0.000000 | 0.000000 | 197.976345 | 0.000000 | 1,243.349459 | 20.109084 | b02136:lower |
| 110 | 303.963681 | 96.988411 | 0.000000 | 98.988172 | 98.988172 | 0.000000 | 1,026.698493 | 39.647743 | b02136:lower |
| 111 | 304.411710 | 96.540383 | 0.000000 | 98.988172 | -0.000000 | 89.545656 | 773.695812 | 96.932230 | b02136:lower |
| 112 | 402.951854 | 96.988411 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 231.949085 | 188.058673 | b02136:lower |
| 113 | 492.358106 | 7.582159 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 499.940265 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 1,236.965008 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g50_b150_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g50_b150_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
