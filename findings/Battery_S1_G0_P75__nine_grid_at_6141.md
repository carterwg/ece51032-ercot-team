# 500 MW at bus 6141, S1 generator 0 MW and battery 75 MW / 300 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,079.238770 | 17.603303 | 30.763287 | 0.554984 | 0.000000 | 0.000000 | 0.105000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,380,000.000 | 0.000 | 143,685.546 | 143,685.546 | 0.000 | 1,992.540 | 2,075.310 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 150.000 | 150.000 | 0.000 | 300.000 | 457.196 | 457.196 |
| 2 | 150.000 | 150.000 | 0.000 | 300.000 | 375.000 | 375.000 |
| 3 | 150.000 | 150.000 | 0.000 | 300.000 | 375.000 | 375.000 |
| 4 | 150.000 | 150.000 | 0.000 | 300.000 | 375.000 | 375.000 |
| 5 | 150.000 | 150.000 | -0.000 | 300.000 | 300.000 | 300.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 575.000000 | 0.000000 | 75.000000 | 0.000000 | 225.000000 | 16,568.384697 | none |
| 8 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 225.000000 | 11,786.885038 | none |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 2,929.769370 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 1,958.641588 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 1,124.715252 | none |
| 107 | 442.919691 | 0.000000 | 0.000000 | 57.080309 | 242.919691 | 541.901362 | b02136:lower |
| 108 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 167.919691 | 157.566742 | b02136:lower |
| 109 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 92.919691 | 20.365289 | b02136:lower |
| 110 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 17.919691 | 157.566742 | b02136:lower |
| 111 | 482.080309 | 0.000000 | 0.000000 | 17.919691 | -0.000000 | 502.740743 | b02136:lower |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,124.715252 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,958.641588 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 2,929.769370 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p75/nine_grid_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p75/nine_grid_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
