# 500 MW at bus 6141, S1 generator 75 MW and battery 150 MW / 600 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 4,427.614621 | 17.342170 | 30.763287 | 0.560814 | 0.000303 | 0.150000 | 0.210000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,690.736 | 309.264 | 246,871.193 | 246,871.193 | 6.000 | 1,893.811 | 1,906.773 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 300.000 | 300.000 | -0.000 | 600.000 | 750.000 | 750.000 |
| 2 | 300.000 | 300.000 | 0.000 | 600.000 | 628.978 | 628.978 |
| 3 | 300.000 | 300.000 | -0.000 | 600.000 | 750.000 | 750.000 |
| 4 | 300.000 | 300.000 | 0.000 | 600.000 | 600.000 | 600.000 |
| 5 | 300.000 | 300.000 | -0.000 | 600.000 | 600.000 | 600.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 350.000000 | 0.000000 | 0.000000 | 150.000000 | 150.000000 | 15,445.008846 | none |
| 1 | 650.000000 | 0.000000 | 150.000000 | 0.000000 | 300.000000 | 15,282.210291 | none |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 1,581.393519 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 610.265737 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | none |
| 107 | 372.669948 | 56.250000 | 0.000000 | 71.080052 | 528.919948 | 0.000000 | none |
| 108 | 279.743217 | 70.256783 | 0.000000 | 150.000000 | 378.919948 | 0.000000 | none |
| 109 | 275.000000 | 75.000000 | 0.000000 | 150.000000 | 228.919948 | -0.000000 | none |
| 110 | 279.743217 | 70.256783 | 0.000000 | 150.000000 | 78.919948 | 0.000000 | none |
| 111 | 402.330052 | 18.750000 | 0.000000 | 78.919948 | -0.000000 | 0.000000 | none |
| 112 | 481.250000 | 18.750000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 610.265737 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,581.393519 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g75_p150/nine_g150_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g75_p150/nine_g150_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
