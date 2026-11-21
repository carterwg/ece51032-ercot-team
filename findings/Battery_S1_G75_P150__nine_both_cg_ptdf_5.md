# 500 MW at bus 6141, S1 generator 75 MW and battery 150 MW / 600 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.332246 | 30.763287 | 0.570970 | 0.000071 | 0.150000 | 0.210000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,880.235 | 119.765 | 284,459.029 | 284,459.029 | 6.000 | 2,285.734 | 2,650.732 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 300.000 | 300.000 | 0.000 | 600.000 | 600.000 | 600.000 |
| 2 | 300.000 | 300.000 | 0.000 | 600.000 | 812.660 | 812.660 |
| 3 | 300.000 | 300.000 | 0.000 | 600.000 | 900.000 | 900.000 |
| 4 | 300.000 | 300.000 | -0.000 | 600.000 | 797.497 | 797.497 |
| 5 | 300.000 | 300.000 | 0.000 | 600.000 | 717.800 | 717.800 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 650.000000 | 0.000000 | 150.000000 | 0.000000 | 580.496533 | 14,709.824912 | none |
| 13 | 350.000000 | 0.000000 | 0.000000 | 150.000000 | 281.668159 | 6,956.719711 | b01854:lower, b02579:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 1,009.008140 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 37.880358 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | -0.000000 | none |
| 107 | 331.250000 | 18.750000 | 0.000000 | 150.000000 | 450.000000 | -0.000000 | none |
| 108 | 323.985039 | 26.014961 | 0.000000 | 150.000000 | 300.000000 | -0.000000 | none |
| 109 | 331.250000 | 18.750000 | 0.000000 | 150.000000 | 150.000000 | -0.000000 | none |
| 110 | 331.250000 | 18.750000 | 0.000000 | 150.000000 | 0.000000 | 0.000000 | none |
| 111 | 481.250000 | 18.750000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 112 | 481.250000 | 18.750000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 37.880358 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g75_p150/nine_both_cg_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g75_p150/nine_both_cg_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
