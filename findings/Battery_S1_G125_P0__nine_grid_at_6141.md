# 500 MW at bus 6141, S1 generator 125 MW and battery 0 MW / 0 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,129.232964 | 17.456205 | 30.763287 | 0.556936 | 0.000146 | 0.250000 | 0.000000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,861.112 | 138.888 | 0.000 | 0.000 | 3.000 | 0.000 | 0.000 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,879.775176 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,908.647394 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,074.721058 | none |
| 107 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 434.826858 | b02136:lower |
| 108 | 492.924805 | 7.075195 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 109 | 375.262011 | 124.737989 | 0.000000 | 0.000000 | 0.000000 | 20.109085 | b02136:lower |
| 110 | 492.924805 | 7.075195 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 111 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 434.826858 | b02136:lower |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,074.721058 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,908.647394 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,879.775176 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g125_p0/nine_grid_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g125_p0/nine_grid_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
