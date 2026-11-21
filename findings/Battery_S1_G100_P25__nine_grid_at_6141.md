# 500 MW at bus 6141, S1 generator 100 MW and battery 25 MW / 100 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,129.232964 | 17.471787 | 30.763287 | 0.556390 | 0.000110 | 0.200000 | 0.035000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,900.262 | 99.738 | 53,762.117 | 53,762.117 | 1.000 | 2,284.737 | 2,270.775 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 50.000 | 50.000 | 0.000 | 100.000 | 139.196 | 139.196 |
| 2 | 50.000 | 50.000 | 0.000 | 100.000 | 125.000 | 125.000 |
| 3 | 50.000 | 50.000 | 0.000 | 100.000 | 150.000 | 150.000 |
| 4 | 50.000 | 50.000 | 0.000 | 100.000 | 175.000 | 175.000 |
| 5 | 50.000 | 50.000 | 0.000 | 100.000 | 117.059 | 117.059 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 525.000000 | 0.000000 | 25.000000 | 0.000000 | 75.000000 | 16,705.591948 | none |
| 8 | 475.000000 | 0.000000 | 0.000000 | 25.000000 | 75.000000 | 11,686.890844 | none |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 100.000000 | 2,879.775176 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 100.000000 | 1,908.647394 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 100.000000 | 1,074.721058 | none |
| 107 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 100.000000 | 434.826858 | b02136:lower |
| 108 | 475.000000 | 0.000000 | 0.000000 | 25.000000 | 75.000000 | 57.572548 | b02136:lower |
| 109 | 375.262011 | 99.737989 | 0.000000 | 25.000000 | 50.000000 | 20.109084 | b02136:lower |
| 110 | 475.000000 | 0.000000 | 0.000000 | 25.000000 | 25.000000 | 57.572548 | b02136:lower |
| 111 | 475.000000 | 0.000000 | 0.000000 | 25.000000 | 0.000000 | 459.826858 | b02136:lower |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,074.721058 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,908.647394 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,879.775176 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g100_p25/nine_grid_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g100_p25/nine_grid_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
