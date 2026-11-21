# 500 MW at bus 6141, S1 generator 75 MW and battery 50 MW / 200 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,129.232964 | 17.487348 | 30.763287 | 0.555857 | 0.000083 | 0.150000 | 0.070000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,925.262 | 74.738 | 105,824.187 | 105,824.187 | 1.000 | 2,284.737 | 2,453.274 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 100.000 | 100.000 | 0.000 | 200.000 | 264.196 | 264.196 |
| 2 | 100.000 | 100.000 | 0.000 | 200.000 | 250.000 | 250.000 |
| 3 | 100.000 | 100.000 | 0.000 | 200.000 | 294.034 | 294.034 |
| 4 | 100.000 | 100.000 | 0.000 | 200.000 | 350.000 | 350.000 |
| 5 | 100.000 | 100.000 | 0.000 | 200.000 | 217.059 | 217.059 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 550.000000 | 0.000000 | 50.000000 | 0.000000 | 150.000000 | 16,680.591948 | none |
| 8 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 150.000000 | 11,711.890844 | none |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 2,879.775176 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 1,908.647394 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 1,074.721058 | none |
| 107 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 434.826858 | b02136:lower |
| 108 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 150.000000 | 82.572548 | b02136:lower |
| 109 | 375.262011 | 74.737989 | 0.000000 | 50.000000 | 100.000000 | 20.109084 | b02136:lower |
| 110 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 50.000000 | 82.572548 | b02136:lower |
| 111 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 0.000000 | 484.826858 | b02136:lower |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,074.721058 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,908.647394 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,879.775176 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g75_p50/nine_grid_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g75_p50/nine_grid_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
