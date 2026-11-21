# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.901525 | 4,946.414283 | 17.341682 | 30.757228 | 0.584666 | 0.000808 | 0.193962 | 0.138573 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,381.809 | 755.551 | 270,227.656 | 270,227.656 | 9.000 | 2,922.989 | 2,910.027 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 50 MW of S1 generation and 175 MW / 700 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,556.279 | 3,789,546.431 | 3,789,546.431 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 197.961 | 197.961 | -0.000 | 395.922 | 692.864 | 692.864 |
| 2 | 197.961 | 197.961 | -0.000 | 395.922 | 989.805 | 989.805 |
| 3 | 197.961 | 197.961 | 197.961 | 395.922 | 791.844 | 791.844 |
| 4 | 197.961 | 197.961 | -0.000 | 395.922 | 484.289 | 484.289 |
| 5 | 197.961 | 197.961 | -0.000 | 395.922 | 603.992 | 603.992 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 598.882027 | 0.000000 | 98.980502 | 0.000000 | 296.941506 | 766.676236 | 518.759822 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 3 | 400.921023 | 0.000000 | 0.000000 | 98.980502 | 214.578415 | 749.195649 | 345.839881 | 14,069.579627 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 499.901525 | 0.000000 | 0.000000 | 0.000000 | 395.922008 | 0.000000 | 0.000000 | 1,062.593857 | b02136:lower |
| 105 | 461.342294 | 38.559232 | 0.000000 | 0.000000 | 395.922008 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 359.873748 | 96.980896 | 0.000000 | 43.046881 | 352.875127 | 0.000000 | 345.839881 | 188.058673 | b02136:lower |
| 107 | 303.940127 | 96.980896 | 0.000000 | 98.980502 | 253.894625 | 0.000000 | 838.674017 | 96.932230 | b02136:lower |
| 108 | 303.940127 | 96.980896 | 0.000000 | 98.980502 | 154.914123 | 0.000000 | 1,183.643840 | 39.647743 | b02136:lower |
| 109 | 445.967510 | 96.980896 | 43.046881 | 0.000000 | 197.961004 | 0.000000 | 1,443.334017 | 20.109084 | b02136:lower |
| 110 | 303.940127 | 96.980896 | 0.000000 | 98.980502 | 98.980502 | 0.000000 | 1,183.643840 | 39.647743 | b02136:lower |
| 111 | 304.373702 | 96.547322 | 0.000000 | 98.980502 | -0.000000 | 43.046881 | 884.142383 | 96.932230 | b02136:lower |
| 112 | 402.920629 | 96.980896 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 388.886762 | 188.058673 | b02136:lower |
| 113 | 461.342294 | 38.559232 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 499.901525 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 1,062.593857 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g50_b175_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g50_b175_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
