# 500 MW at bus 6141, S1 generator 50 MW and battery 50 MW / 200 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,124.342848 | 17.537905 | 30.763287 | 0.555328 | 0.000055 | 0.100000 | 0.070000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,950.261 | 49.739 | 74,598.812 | 74,598.812 | 1.000 | 1,794.082 | 1,727.266 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 100.000 | 100.000 | 0.000 | 200.000 | 219.086 | 219.086 |
| 2 | 100.000 | 100.000 | 0.000 | 200.000 | 200.000 | 200.000 |
| 3 | 100.000 | 100.000 | 0.000 | 200.000 | 200.000 | 200.000 |
| 4 | 100.000 | 100.000 | 0.000 | 200.000 | 200.000 | 200.000 |
| 5 | 100.000 | 100.000 | 0.000 | 200.000 | 200.000 | 200.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 550.000000 | 0.000000 | 50.000000 | 0.000000 | 150.000000 | 16,685.482064 | none |
| 12 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 106.580032 | 8,869.578309 | b02579:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 2,884.665292 | b02579:lower |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 1,913.537510 | b02579:lower |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 1,079.611174 | none |
| 107 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 150.000000 | 489.716974 | none |
| 108 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 100.000000 | 87.462664 | none |
| 109 | 400.261211 | 49.738789 | 0.000000 | 50.000000 | 50.000000 | 0.000000 | none |
| 110 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 0.000000 | 87.462664 | none |
| 111 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 439.716974 | none |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,079.611174 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,913.537510 | b02579:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,884.665292 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g50_p50/nine_s2_cg_hosting_2/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g50_p50/nine_s2_cg_hosting_2/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
