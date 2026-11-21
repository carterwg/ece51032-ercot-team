# 500 MW at bus 6141, S1 generator 0 MW and battery 200 MW / 800 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 4,105.634342 | 17.416906 | 30.763287 | 0.566381 | 0.000000 | 0.000000 | 0.280000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,380,000.000 | 0.000 | 393,060.581 | 393,060.581 | 0.000 | 3,234.134 | 3,548.279 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 400.000 | 400.000 | -0.000 | 800.000 | 805.230 | 805.230 |
| 2 | 400.000 | 400.000 | 0.000 | 800.000 | 1,022.005 | 1,022.005 |
| 3 | 400.000 | 400.000 | 0.000 | 800.000 | 1,190.989 | 1,190.989 |
| 4 | 400.000 | 400.000 | 0.000 | 800.000 | 1,271.559 | 1,271.559 |
| 5 | 400.000 | 400.000 | 0.000 | 800.000 | 833.519 | 833.519 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 463.119873 | 8,038.286815 | b01921:upper |
| 22 | 700.000000 | 0.000000 | 200.000000 | 0.000000 | 200.000000 | 14,374.840619 | b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 800.000000 | 1,903.373798 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 800.000000 | 932.246016 | b02136:lower |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 800.000000 | 188.058673 | b02136:lower |
| 107 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 800.000000 | 96.932230 | b02136:lower |
| 108 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 600.000000 | 39.647743 | b02136:lower |
| 109 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 400.000000 | 20.109084 | b02136:lower |
| 110 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 200.000000 | 39.647743 | b02136:lower |
| 111 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 0.000000 | 96.932230 | b02136:lower |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 932.246016 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,903.373798 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p200/nine_g125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p200/nine_g125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
