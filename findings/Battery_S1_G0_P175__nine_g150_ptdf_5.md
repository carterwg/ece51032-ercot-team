# 500 MW at bus 6141, S1 generator 0 MW and battery 175 MW / 700 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.943901 | 4,356.141134 | 17.455476 | 30.759836 | 0.560789 | 0.000000 | 0.000000 | 0.244973 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,508.576 | 0.000 | 297,130.140 | 297,130.140 | 0.000 | 1,909.767 | 1,922.729 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 349.961 | 349.961 | -0.000 | 699.921 | 699.921 | 699.921 |
| 2 | 349.961 | 349.961 | -0.000 | 699.921 | 972.420 | 972.420 |
| 3 | 349.961 | 349.961 | 0.000 | 699.921 | 874.902 | 874.902 |
| 4 | 349.961 | 349.961 | -0.000 | 699.921 | 699.921 | 699.921 |
| 5 | 349.961 | 349.961 | 0.000 | 699.921 | 699.921 | 699.921 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 674.924267 | 0.000000 | 174.980365 | 0.000000 | 524.941096 | 15,328.703413 | none |
| 12 | 324.963536 | 0.000000 | 0.000000 | 174.980365 | 502.197606 | 7,762.760389 | b01854:lower |
| 104 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | 699.921462 | 1,652.867006 | none |
| 105 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | 699.921462 | 681.739224 | none |
| 106 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | 699.921462 | 0.000000 | none |
| 107 | 365.086387 | 0.000000 | 0.000000 | 134.857514 | 565.063948 | -0.000000 | none |
| 108 | 324.963536 | 0.000000 | 0.000000 | 174.980365 | 390.083582 | -0.000000 | none |
| 109 | 324.963536 | 0.000000 | 0.000000 | 174.980365 | 215.103217 | -0.000000 | none |
| 110 | 324.963536 | 0.000000 | 0.000000 | 174.980365 | 40.122851 | 0.000000 | none |
| 111 | 459.821050 | 0.000000 | 0.000000 | 40.122851 | 0.000000 | 0.000000 | none |
| 112 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 113 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 681.739224 | none |
| 114 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,652.867006 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p175/nine_g150_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p175/nine_g150_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
