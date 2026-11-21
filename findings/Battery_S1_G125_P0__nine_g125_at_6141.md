# 500 MW at bus 6141, S1 generator 125 MW and battery 0 MW / 0 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 400.559270 | 4,005.592700 | 13.975811 | 24.645040 | 0.454587 | 0.000380 | 0.200280 | 0.000000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 3,508,514.715 | 384.490 | 0.000 | 0.000 | 5.000 | 0.000 | 0.000 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 400.559270 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,003.415440 | none |
| 105 | 400.559270 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,032.287658 | b02136:lower |
| 106 | 400.559270 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 198.361322 | b02136:lower |
| 107 | 346.712759 | 53.846511 | 0.000000 | 0.000000 | 0.000000 | 96.932230 | b02136:lower |
| 108 | 312.215777 | 88.343493 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 109 | 300.449497 | 100.109773 | 0.000000 | 0.000000 | 0.000000 | 20.109085 | b02136:lower |
| 110 | 312.215777 | 88.343493 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 111 | 346.712759 | 53.846511 | 0.000000 | 0.000000 | 0.000000 | 96.932230 | b02136:lower |
| 112 | 400.559270 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 198.361322 | b02136:lower |
| 113 | 400.559270 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,032.287658 | b02136:lower |
| 114 | 400.559270 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,003.415440 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g125_p0/nine_g125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g125_p0/nine_g125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
