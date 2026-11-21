# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 4,100.301656 | 17.362484 | 30.763287 | 0.567816 | 0.000387 | 0.194000 | 0.138600 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,601.984 | 398.016 | 221,287.388 | 221,287.388 | 7.000 | 2,866.148 | 3,482.458 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 198.000 | 198.000 | -0.000 | 396.000 | 396.000 | 396.000 |
| 2 | 198.000 | 198.000 | 0.000 | 396.000 | 628.961 | 628.961 |
| 3 | 198.000 | 198.000 | 0.000 | 396.000 | 671.964 | 671.964 |
| 4 | 198.000 | 198.000 | -0.000 | 396.000 | 709.126 | 709.126 |
| 5 | 198.000 | 198.000 | -0.000 | 396.000 | 466.654 | 466.654 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 239.212814 | 7,942.619501 | b01921:upper |
| 22 | 599.000000 | 0.000000 | 99.000000 | 0.000000 | 102.563006 | 14,481.173305 | b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 1,908.706484 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 937.578702 | b02136:lower |
| 106 | 491.788573 | 8.211427 | 0.000000 | 0.000000 | 396.000000 | 188.058673 | b02136:lower |
| 107 | 438.401967 | 61.598033 | 0.000000 | 0.000000 | 396.000000 | 96.932230 | b02136:lower |
| 108 | 315.472912 | 85.527088 | 0.000000 | 99.000000 | 297.000000 | 39.647743 | b02136:lower |
| 109 | 304.026144 | 96.973856 | 0.000000 | 99.000000 | 198.000000 | 20.109084 | b02136:lower |
| 110 | 315.472912 | 85.527088 | 0.000000 | 99.000000 | 99.000000 | 39.647743 | b02136:lower |
| 111 | 349.033134 | 51.966866 | 0.000000 | 99.000000 | -0.000000 | 96.932230 | b02136:lower |
| 112 | 491.788573 | 8.211427 | 0.000000 | 0.000000 | -0.000000 | 188.058673 | b02136:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 937.578702 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,908.706484 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
