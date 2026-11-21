# 500 MW at bus 6141, S1 generator 0 MW and battery 200 MW / 800 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,204.225006 | 17.429102 | 30.763287 | 0.554185 | 0.000000 | 0.000000 | 0.280000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,380,000.000 | 0.000 | 339,173.747 | 339,173.747 | 0.000 | 2,123.181 | 2,306.679 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 400.000 | 400.000 | -0.000 | 800.000 | 1,106.980 | 1,106.980 |
| 2 | 400.000 | 400.000 | 0.000 | 800.000 | 958.272 | 958.272 |
| 3 | 400.000 | 400.000 | 0.000 | 800.000 | 800.000 | 800.000 |
| 4 | 400.000 | 400.000 | 0.000 | 800.000 | 858.060 | 858.060 |
| 5 | 400.000 | 400.000 | -0.000 | 800.000 | 800.000 | 800.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 700.000000 | 0.000000 | 200.000000 | 0.000000 | 635.780756 | 16,318.398461 | none |
| 8 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 600.000000 | 11,786.898802 | none |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 800.000000 | 2,804.783134 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 800.000000 | 1,833.655352 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 800.000000 | 999.729016 | none |
| 107 | 317.933455 | 0.000000 | 0.000000 | 182.066545 | 617.933455 | 541.901362 | b02136:lower |
| 108 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 417.933455 | 157.580506 | b02136:lower |
| 109 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 217.933455 | 20.379053 | b02136:lower |
| 110 | 300.000000 | 0.000000 | 0.000000 | 200.000000 | 17.933455 | 157.580506 | b02136:lower |
| 111 | 482.066545 | 0.000000 | 0.000000 | 17.933455 | -0.000000 | 377.768271 | b02136:lower |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 999.729016 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,833.655352 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 2,804.783134 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p200/nine_grid_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p200/nine_grid_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
