# 500 MW at bus 6141, S1 generator 135 MW and battery 35 MW / 140 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.915361 | 4,948.454894 | 17.355275 | 30.758080 | 0.584857 | 0.001118 | 0.269954 | 0.048992 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,213.073 | 1,045.488 | 99,585.288 | 99,585.288 | 9.000 | 3,006.759 | 2,909.027 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 50 MW of S1 generation and 175 MW / 700 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,556.989 | 3,698,846.767 | 3,698,846.767 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 69.988 | 69.988 | -0.000 | 139.976 | 314.947 | 314.947 |
| 2 | 69.988 | 69.988 | -0.000 | 139.976 | 334.512 | 334.512 |
| 3 | 69.988 | 69.988 | 69.988 | 139.976 | 279.953 | 279.953 |
| 4 | 69.988 | 69.988 | 0.000 | 139.976 | 168.355 | 168.355 |
| 5 | 69.988 | 69.988 | -0.000 | 139.976 | 216.695 | 216.695 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 534.909436 | 0.000000 | 34.994075 | 0.000000 | 104.982226 | 828.858508 | 518.996279 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 2 | 464.921286 | 0.000000 | 0.000000 | 34.994075 | 104.982226 | 864.993798 | 485.143418 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 499.915361 | 0.000000 | 0.000000 | 0.000000 | 139.976301 | 0.000000 | 0.000000 | 1,060.553246 | b02136:lower |
| 105 | 449.309448 | 50.605913 | 0.000000 | 0.000000 | 139.976301 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 358.207288 | 134.977147 | 0.000000 | 6.730926 | 133.245375 | 0.000000 | 345.997519 | 188.058673 | b02136:lower |
| 107 | 329.944138 | 134.977147 | 0.000000 | 34.994075 | 98.251300 | 0.000000 | 866.502127 | 96.932230 | b02136:lower |
| 108 | 329.944138 | 134.977147 | 0.000000 | 34.994075 | 63.257225 | 0.000000 | 1,211.471949 | 39.647743 | b02136:lower |
| 109 | 371.669139 | 134.977147 | 6.730926 | 0.000000 | 69.988151 | 0.000000 | 1,370.859745 | 20.109084 | b02136:lower |
| 110 | 329.944138 | 134.977147 | 0.000000 | 34.994075 | 34.994075 | 0.000000 | 1,211.471949 | 39.647743 | b02136:lower |
| 111 | 330.507829 | 134.413457 | 0.000000 | 34.994075 | -0.000000 | 6.730926 | 875.654538 | 96.932230 | b02136:lower |
| 112 | 364.938213 | 134.977147 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 352.728445 | 188.058673 | b02136:lower |
| 113 | 449.309448 | 50.605913 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 499.915361 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 1,060.553246 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g135_p35/nine_g50_b175_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g135_p35/nine_g50_b175_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
