# 500 MW at bus 6141, S1 generator 75 MW and battery 150 MW / 600 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,229.222420 | 17.347846 | 30.763287 | 0.555358 | 0.000082 | 0.150000 | 0.210000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,925.273 | 74.727 | 257,195.566 | 257,195.566 | 1.000 | 2,102.236 | 2,389.452 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 300.000 | 300.000 | 0.000 | 600.000 | 750.000 | 750.000 |
| 2 | 300.000 | 300.000 | 0.000 | 600.000 | 674.917 | 674.917 |
| 3 | 300.000 | 300.000 | 0.000 | 600.000 | 750.000 | 750.000 |
| 4 | 300.000 | 300.000 | 0.000 | 600.000 | 658.763 | 658.763 |
| 5 | 300.000 | 300.000 | 0.000 | 600.000 | 600.000 | 600.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 650.000000 | 0.000000 | 150.000000 | 0.000000 | 600.000000 | 16,343.401047 | none |
| 8 | 350.000000 | 0.000000 | 0.000000 | 150.000000 | 450.000000 | 11,711.901388 | none |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 2,779.785720 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 1,808.657938 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 974.731602 | none |
| 107 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 334.837402 | b02136:lower |
| 108 | 350.000000 | 0.000000 | 0.000000 | 150.000000 | 450.000000 | 82.583092 | b02136:lower |
| 109 | 275.272555 | 74.727445 | 0.000000 | 150.000000 | 300.000000 | 20.109084 | b02136:lower |
| 110 | 350.000000 | 0.000000 | 0.000000 | 150.000000 | 150.000000 | 82.583092 | b02136:lower |
| 111 | 350.000000 | 0.000000 | 0.000000 | 150.000000 | 0.000000 | 484.837402 | b02136:lower |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 974.731602 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,808.657938 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,779.785720 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g75_p150/nine_grid_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g75_p150/nine_grid_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
