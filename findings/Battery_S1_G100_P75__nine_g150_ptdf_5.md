# 500 MW at bus 6141, S1 generator 100 MW and battery 75 MW / 300 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.943901 | 4,356.141134 | 17.394287 | 30.759836 | 0.561582 | 0.000404 | 0.199978 | 0.104988 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,096.791 | 411.785 | 129,455.611 | 129,455.611 | 6.000 | 1,893.811 | 1,726.268 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 149.983 | 149.983 | -0.000 | 299.966 | 374.958 | 374.958 |
| 2 | 149.983 | 149.983 | -0.000 | 299.966 | 374.958 | 374.958 |
| 3 | 149.983 | 149.983 | -0.000 | 299.966 | 374.958 | 374.958 |
| 4 | 149.983 | 149.983 | -0.000 | 299.966 | 299.966 | 299.966 |
| 5 | 149.983 | 149.983 | -0.000 | 299.966 | 299.966 | 299.966 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 424.952316 | 0.000000 | 0.000000 | 74.991585 | 74.991585 | 15,441.473918 | none |
| 1 | 574.935487 | 0.000000 | 74.991585 | 0.000000 | 149.983170 | 15,428.692193 | none |
| 104 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | 299.966341 | 1,652.867006 | none |
| 105 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | 299.966341 | 681.739224 | none |
| 106 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | 299.966341 | 0.000000 | none |
| 107 | 365.086387 | 74.991585 | 0.000000 | 59.865929 | 240.100412 | 0.000000 | none |
| 108 | 331.547163 | 93.405153 | 0.000000 | 74.991585 | 165.108827 | 0.000000 | none |
| 109 | 324.963536 | 99.988780 | 0.000000 | 74.991585 | 90.117242 | -0.000000 | none |
| 110 | 331.547163 | 93.405153 | 0.000000 | 74.991585 | 15.125656 | 0.000000 | none |
| 111 | 459.821050 | 24.997195 | 0.000000 | 15.125656 | -0.000000 | 0.000000 | none |
| 112 | 474.946706 | 24.997195 | 0.000000 | 0.000000 | -0.000000 | -0.000000 | none |
| 113 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 681.739224 | none |
| 114 | 499.943901 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,652.867006 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g100_p75/nine_g150_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g100_p75/nine_g150_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
