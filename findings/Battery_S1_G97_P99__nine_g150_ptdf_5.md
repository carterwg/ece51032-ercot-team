# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 4,386.191468 | 17.368931 | 30.763287 | 0.561364 | 0.000392 | 0.194000 | 0.138600 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,600.022 | 399.978 | 169,274.381 | 169,274.381 | 6.000 | 1,893.811 | 1,726.268 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 198.000 | 198.000 | -0.000 | 396.000 | 495.000 | 495.000 |
| 2 | 198.000 | 198.000 | 0.000 | 396.000 | 478.693 | 478.693 |
| 3 | 198.000 | 198.000 | -0.000 | 396.000 | 495.000 | 495.000 |
| 4 | 198.000 | 198.000 | 0.000 | 396.000 | 396.000 | 396.000 |
| 5 | 198.000 | 198.000 | 0.000 | 396.000 | 396.000 | 396.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 99.000000 | 15,435.431999 | none |
| 1 | 599.000000 | 0.000000 | 99.000000 | 0.000000 | 198.000000 | 15,374.633444 | none |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 1,622.816672 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 651.688890 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | -0.000000 | none |
| 107 | 368.324310 | 72.750000 | 0.000000 | 58.925690 | 337.074310 | 0.000000 | none |
| 108 | 310.135953 | 90.864047 | 0.000000 | 99.000000 | 238.074310 | 0.000000 | none |
| 109 | 304.000000 | 97.000000 | 0.000000 | 99.000000 | 139.074310 | -0.000000 | none |
| 110 | 310.135953 | 90.864047 | 0.000000 | 99.000000 | 40.074310 | 0.000000 | none |
| 111 | 435.675690 | 24.250000 | 0.000000 | 40.074310 | 0.000000 | -0.000000 | none |
| 112 | 475.750000 | 24.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 651.688890 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,622.816672 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g150_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g150_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
