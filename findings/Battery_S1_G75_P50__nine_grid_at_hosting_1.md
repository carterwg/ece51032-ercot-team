# 500 MW at bus 6141, S1 generator 75 MW and battery 50 MW / 200 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,149.340043 | 17.487576 | 30.763287 | 0.555629 | 0.000083 | 0.150000 | 0.070000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,925.264 | 74.736 | 79,982.510 | 79,982.510 | 1.000 | 1,627.542 | 1,726.268 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 100.000 | 100.000 | 0.000 | 200.000 | 250.000 | 250.000 |
| 2 | 100.000 | 100.000 | 0.000 | 200.000 | 200.000 | 200.000 |
| 3 | 100.000 | 100.000 | 0.000 | 200.000 | 233.755 | 233.755 |
| 4 | 100.000 | 100.000 | 0.000 | 200.000 | 200.000 | 200.000 |
| 5 | 100.000 | 100.000 | 0.000 | 200.000 | 200.000 | 200.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 550.000000 | 0.000000 | 50.000000 | 0.000000 | 150.000000 | 16,660.484869 | none |
| 10 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 150.000000 | 9,886.729621 | b02579:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 2,859.668097 | b02579:lower |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 1,888.540315 | b02579:lower |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 1,054.613979 | none |
| 107 | 466.660221 | 0.000000 | 0.000000 | 33.339779 | 166.660221 | 448.059557 | none |
| 108 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 116.660221 | 62.465469 | none |
| 109 | 375.264016 | 74.735984 | 0.000000 | 50.000000 | 66.660221 | 0.000000 | none |
| 110 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 16.660221 | 62.465469 | none |
| 111 | 483.339779 | 0.000000 | 0.000000 | 16.660221 | 0.000000 | 431.380000 | none |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,054.613979 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,888.540315 | b02579:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,859.668097 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g75_p50/nine_grid_at_hosting_1/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g75_p50/nine_grid_at_hosting_1/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
