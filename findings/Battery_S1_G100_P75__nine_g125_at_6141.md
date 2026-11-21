# 500 MW at bus 6141, S1 generator 100 MW and battery 75 MW / 300 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 4,072.305347 | 17.390290 | 30.763287 | 0.567605 | 0.000392 | 0.200000 | 0.105000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,598.089 | 401.911 | 172,054.745 | 172,054.745 | 7.000 | 3,232.140 | 3,299.962 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 150.000 | 150.000 | 0.000 | 300.000 | 331.559 | 331.559 |
| 2 | 150.000 | 150.000 | 0.000 | 300.000 | 495.247 | 495.247 |
| 3 | 150.000 | 150.000 | -0.000 | 300.000 | 514.814 | 514.814 |
| 4 | 150.000 | 150.000 | 0.000 | 300.000 | 529.901 | 529.901 |
| 5 | 150.000 | 150.000 | -0.000 | 300.000 | 490.545 | 490.545 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 195.209122 | 7,946.615810 | b01921:upper |
| 22 | 575.000000 | 0.000000 | 75.000000 | 0.000000 | 106.559314 | 14,533.169614 | b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 1,936.702793 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 965.575011 | b02136:lower |
| 106 | 494.319671 | 5.680329 | 0.000000 | 0.000000 | 300.000000 | 188.058673 | b02136:lower |
| 107 | 439.060298 | 60.939702 | 0.000000 | 0.000000 | 300.000000 | 96.932230 | b02136:lower |
| 108 | 336.875095 | 88.124905 | 0.000000 | 75.000000 | 225.000000 | 39.647743 | b02136:lower |
| 109 | 325.026782 | 99.973218 | 0.000000 | 75.000000 | 150.000000 | 20.109084 | b02136:lower |
| 110 | 336.875095 | 88.124905 | 0.000000 | 75.000000 | 75.000000 | 39.647743 | b02136:lower |
| 111 | 371.612588 | 53.387412 | 0.000000 | 75.000000 | -0.000000 | 96.932230 | b02136:lower |
| 112 | 494.319671 | 5.680329 | 0.000000 | 0.000000 | -0.000000 | 188.058673 | b02136:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 965.575011 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,936.702793 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g100_p75/nine_g125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g100_p75/nine_g125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
