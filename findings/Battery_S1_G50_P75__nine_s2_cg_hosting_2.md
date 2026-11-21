# 500 MW at bus 6141, S1 generator 50 MW and battery 75 MW / 300 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,149.340043 | 17.502989 | 30.763287 | 0.555243 | 0.000055 | 0.100000 | 0.105000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,950.264 | 49.736 | 109,500.000 | 109,500.000 | 1.000 | 1,544.770 | 1,559.726 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 150.000 | 150.000 | 0.000 | 300.000 | 300.000 | 300.000 |
| 2 | 150.000 | 150.000 | 0.000 | 300.000 | 300.000 | 300.000 |
| 3 | 150.000 | 150.000 | 0.000 | 300.000 | 300.000 | 300.000 |
| 4 | 150.000 | 150.000 | 0.000 | 300.000 | 300.000 | 300.000 |
| 5 | 150.000 | 150.000 | 0.000 | 300.000 | 300.000 | 300.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 575.000000 | 0.000000 | 75.000000 | 0.000000 | 225.000000 | 16,635.484869 | none |
| 12 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 206.797089 | 8,869.581114 | b02579:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 2,859.668097 | b02579:lower |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 1,888.540315 | b02579:lower |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 300.000000 | 1,054.613979 | none |
| 107 | 441.660221 | 0.000000 | 0.000000 | 58.339779 | 241.660221 | 473.059557 | none |
| 108 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 166.660221 | 87.465469 | none |
| 109 | 375.264016 | 49.735984 | 0.000000 | 75.000000 | 91.660221 | 0.000000 | none |
| 110 | 425.000000 | 0.000000 | 0.000000 | 75.000000 | 16.660221 | 87.465469 | none |
| 111 | 483.339779 | 0.000000 | 0.000000 | 16.660221 | 0.000000 | 431.380000 | none |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,054.613979 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,888.540315 | b02579:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,859.668097 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g50_p75/nine_s2_cg_hosting_2/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g50_p75/nine_s2_cg_hosting_2/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
