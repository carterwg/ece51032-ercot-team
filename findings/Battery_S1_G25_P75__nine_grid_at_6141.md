# 500 MW at bus 6141, S1 generator 25 MW and battery 75 MW / 300 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,104.235767 | 17.552564 | 30.763287 | 0.555696 | 0.000027 | 0.050000 | 0.105000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,975.259 | 24.741 | 157,761.947 | 157,761.947 | 1.000 | 2,369.504 | 2,370.501 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 150.000 | 150.000 | 0.000 | 300.000 | 414.193 | 414.193 |
| 2 | 150.000 | 150.000 | 0.000 | 300.000 | 375.000 | 375.000 |
| 3 | 150.000 | 150.000 | -0.000 | 300.000 | 410.966 | 410.966 |
| 4 | 150.000 | 150.000 | 0.000 | 300.000 | 525.000 | 525.000 |
| 5 | 150.000 | 150.000 | 0.000 | 300.000 | 342.056 | 342.056 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 575.000000 | 0.000000 | 75.000000 | 0.000000 | 225.000000 | 16,680.589145 | none |
| 8 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 225.000000 | 11,761.888041 | none |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 2,904.772373 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 1,933.644591 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 1,099.718255 | none |
| 107 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 459.824055 | b02136:lower |
| 108 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 225.000000 | 132.569745 | b02136:lower |
| 109 | 400.259208 | 24.740792 | 0.000000 | 75.000000 | 150.000000 | 20.109084 | b02136:lower |
| 110 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 75.000000 | 132.569745 | b02136:lower |
| 111 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 0.000000 | 534.824055 | b02136:lower |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,099.718255 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,933.644591 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,904.772373 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g25_p75/nine_grid_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g25_p75/nine_grid_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
