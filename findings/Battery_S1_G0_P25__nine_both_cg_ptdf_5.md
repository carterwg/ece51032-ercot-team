# 500 MW at bus 6141, S1 generator 0 MW and battery 25 MW / 100 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.653152 | 30.763287 | 0.575135 | 0.000000 | 0.000000 | 0.035000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,380,000.000 | 0.000 | 43,106.918 | 43,106.918 | 0.000 | 1,724.277 | 1,973.592 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 50.000 | 50.000 | 0.000 | 100.000 | 100.000 | 100.000 |
| 2 | 50.000 | 50.000 | 0.000 | 100.000 | 100.000 | 100.000 |
| 3 | 50.000 | 50.000 | 0.000 | 100.000 | 150.000 | 150.000 |
| 4 | 50.000 | 50.000 | 0.000 | 100.000 | 125.000 | 125.000 |
| 5 | 50.000 | 50.000 | 0.000 | 100.000 | 125.000 | 125.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 525.000000 | 0.000000 | 25.000000 | 0.000000 | 80.496533 | 14,834.824912 | none |
| 11 | 475.000000 | 0.000000 | 0.000000 | 25.000000 | 75.000000 | 7,371.175489 | b01854:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 100.000000 | 1,009.008140 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 100.000000 | 37.880358 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 100.000000 | 0.000000 | none |
| 107 | 475.000000 | 0.000000 | 0.000000 | 25.000000 | 75.000000 | 0.000000 | none |
| 108 | 475.000000 | 0.000000 | 0.000000 | 25.000000 | 50.000000 | 0.000000 | none |
| 109 | 475.000000 | 0.000000 | 0.000000 | 25.000000 | 25.000000 | -0.000000 | none |
| 110 | 475.000000 | 0.000000 | 0.000000 | 25.000000 | 0.000000 | 0.000000 | none |
| 111 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 37.880358 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p25/nine_both_cg_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p25/nine_both_cg_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
