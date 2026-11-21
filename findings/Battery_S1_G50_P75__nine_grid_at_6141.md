# 500 MW at bus 6141, S1 generator 50 MW and battery 75 MW / 300 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,129.232964 | 17.502560 | 30.763287 | 0.555672 | 0.000055 | 0.100000 | 0.105000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,950.262 | 49.738 | 154,857.658 | 154,857.658 | 1.000 | 2,284.737 | 2,553.000 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 150.000 | 150.000 | 0.000 | 300.000 | 389.196 | 389.196 |
| 2 | 150.000 | 150.000 | 0.000 | 300.000 | 374.455 | 374.455 |
| 3 | 150.000 | 150.000 | 0.000 | 300.000 | 410.966 | 410.966 |
| 4 | 150.000 | 150.000 | -0.000 | 300.000 | 517.521 | 517.521 |
| 5 | 150.000 | 150.000 | 0.000 | 300.000 | 317.059 | 317.059 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 575.000000 | 0.000000 | 75.000000 | 0.000000 | 225.000000 | 16,655.591948 | none |
| 8 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 225.000000 | 11,736.890844 | none |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 2,879.775176 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 1,908.647394 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 1,074.721058 | none |
| 107 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 434.826858 | b02136:lower |
| 108 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 225.000000 | 107.572548 | b02136:lower |
| 109 | 375.262011 | 49.737989 | 0.000000 | 75.000000 | 150.000000 | 20.109084 | b02136:lower |
| 110 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 75.000000 | 107.572548 | b02136:lower |
| 111 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 0.000000 | 509.826858 | b02136:lower |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,074.721058 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,908.647394 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,879.775176 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g50_p75/nine_grid_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g50_p75/nine_grid_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
