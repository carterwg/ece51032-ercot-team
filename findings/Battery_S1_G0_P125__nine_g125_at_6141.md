# 500 MW at bus 6141, S1 generator 0 MW and battery 125 MW / 500 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 400.559270 | 4,005.592700 | 14.037778 | 24.645040 | 0.453084 | 0.000000 | 0.000000 | 0.140196 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 3,508,899.205 | 0.000 | 238,864.558 | 238,864.558 | 0.000 | 3,373.751 | 3,367.773 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 200.280 | 200.280 | -0.000 | 400.559 | 621.579 | 621.579 |
| 2 | 200.280 | 200.280 | -0.000 | 400.559 | 739.185 | 739.185 |
| 3 | 200.280 | 200.280 | -0.000 | 400.559 | 649.016 | 649.016 |
| 4 | 200.280 | 200.280 | -0.000 | 400.559 | 600.839 | 600.839 |
| 5 | 200.280 | 200.280 | -0.000 | 400.559 | 637.372 | 637.372 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 500.699088 | 0.000000 | 100.139818 | 0.000000 | 300.419453 | 15,616.890949 | b02355:lower |
| 2 | 300.419453 | 0.000000 | 0.000000 | 100.139818 | 300.419453 | 15,817.170584 | b02355:lower |
| 104 | 400.559270 | 0.000000 | 0.000000 | 0.000000 | 400.559270 | 2,003.415440 | none |
| 105 | 400.559270 | 0.000000 | 0.000000 | 0.000000 | 400.559270 | 1,032.287658 | b02136:lower |
| 106 | 400.559270 | 0.000000 | 0.000000 | 0.000000 | 400.559270 | 198.361322 | b02136:lower |
| 107 | 400.559270 | 0.000000 | 0.000000 | 0.000000 | 400.559270 | 96.932230 | b02136:lower |
| 108 | 300.419453 | 0.000000 | 0.000000 | 100.139818 | 300.419453 | 39.647743 | b02136:lower |
| 109 | 300.419453 | 0.000000 | 0.000000 | 100.139818 | 200.279635 | 20.109085 | b02136:lower |
| 110 | 300.419453 | 0.000000 | 0.000000 | 100.139818 | 100.139818 | 39.647743 | b02136:lower |
| 111 | 300.419453 | 0.000000 | 0.000000 | 100.139818 | -0.000000 | 96.932230 | b02136:lower |
| 112 | 400.559270 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 198.361322 | b02136:lower |
| 113 | 400.559270 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,032.287658 | b02136:lower |
| 114 | 400.559270 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 2,003.415440 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p125/nine_g125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p125/nine_g125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
