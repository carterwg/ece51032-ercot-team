# 500 MW at bus 6141, S1 generator 100 MW and battery 25 MW / 100 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,149.340043 | 17.472335 | 30.763287 | 0.555842 | 0.000110 | 0.200000 | 0.035000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,900.264 | 99.736 | 40,663.562 | 40,663.562 | 1.000 | 1,627.542 | 1,726.268 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 50.000 | 50.000 | 0.000 | 100.000 | 125.000 | 125.000 |
| 2 | 50.000 | 50.000 | 0.000 | 100.000 | 100.000 | 100.000 |
| 3 | 50.000 | 50.000 | 0.000 | 100.000 | 125.000 | 125.000 |
| 4 | 50.000 | 50.000 | 0.000 | 100.000 | 100.000 | 100.000 |
| 5 | 50.000 | 50.000 | 0.000 | 100.000 | 100.000 | 100.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 525.000000 | 0.000000 | 25.000000 | 0.000000 | 75.000000 | 16,685.484869 | none |
| 10 | 475.000000 | 0.000000 | 0.000000 | 25.000000 | 75.000000 | 9,861.729621 | b02579:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 100.000000 | 2,859.668097 | b02579:lower |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 100.000000 | 1,888.540315 | b02579:lower |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 100.000000 | 1,054.613979 | none |
| 107 | 483.339779 | 0.000000 | 0.000000 | 16.660221 | 83.339779 | 431.380000 | none |
| 108 | 475.000000 | 0.000000 | 0.000000 | 25.000000 | 58.339779 | 37.465469 | none |
| 109 | 375.264016 | 99.735984 | 0.000000 | 25.000000 | 33.339779 | -0.000000 | none |
| 110 | 475.000000 | 0.000000 | 0.000000 | 25.000000 | 8.339779 | 37.465469 | none |
| 111 | 491.660221 | 0.000000 | 0.000000 | 8.339779 | 0.000000 | 423.059557 | none |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,054.613979 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,888.540315 | b02579:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,859.668097 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g100_p25/nine_grid_at_hosting_1/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g100_p25/nine_grid_at_hosting_1/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
