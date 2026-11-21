# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,200.225421 | 17.374753 | 30.763287 | 0.555827 | 0.000107 | 0.194000 | 0.138600 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,903.270 | 96.730 | 181,597.384 | 181,597.384 | 1.000 | 2,201.962 | 2,123.184 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 198.000 | 198.000 | 0.000 | 396.000 | 495.000 | 495.000 |
| 2 | 198.000 | 198.000 | 0.000 | 396.000 | 487.840 | 487.840 |
| 3 | 198.000 | 198.000 | 0.000 | 396.000 | 495.000 | 495.000 |
| 4 | 198.000 | 198.000 | 0.000 | 396.000 | 512.757 | 512.757 |
| 5 | 198.000 | 198.000 | -0.000 | 396.000 | 396.000 | 396.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 599.000000 | 0.000000 | 99.000000 | 0.000000 | 297.000000 | 16,560.599491 | none |
| 8 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 297.000000 | 11,689.898387 | none |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 2,808.782719 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 1,837.654937 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 1,003.728601 | none |
| 107 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 363.834401 | b02136:lower |
| 108 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 297.000000 | 60.580091 | b02136:lower |
| 109 | 304.269553 | 96.730447 | 0.000000 | 99.000000 | 198.000000 | 20.109084 | b02136:lower |
| 110 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 99.000000 | 60.580091 | b02136:lower |
| 111 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | -0.000000 | 462.834401 | b02136:lower |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,003.728601 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,837.654937 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 2,808.782719 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_grid_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_grid_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
