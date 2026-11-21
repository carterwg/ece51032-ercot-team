# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.358028 | 30.763287 | 0.572563 | 0.000096 | 0.194000 | 0.138600 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,840.885 | 159.115 | 195,091.147 | 195,091.147 | 6.000 | 2,201.964 | 2,553.000 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 198.000 | 198.000 | 0.000 | 396.000 | 396.000 | 396.000 |
| 2 | 198.000 | 198.000 | -0.000 | 396.000 | 594.000 | 594.000 |
| 3 | 198.000 | 198.000 | 0.000 | 396.000 | 594.000 | 594.000 |
| 4 | 198.000 | 198.000 | -0.000 | 396.000 | 542.497 | 542.497 |
| 5 | 198.000 | 198.000 | 0.000 | 396.000 | 495.000 | 495.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 599.000000 | 0.000000 | 99.000000 | 0.000000 | 376.496533 | 14,760.824912 | none |
| 11 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 297.000000 | 7,445.175489 | b01854:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 1,009.008140 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 37.880358 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | none |
| 107 | 376.750000 | 24.250000 | 0.000000 | 99.000000 | 297.000000 | 0.000000 | none |
| 108 | 363.134538 | 37.865462 | 0.000000 | 99.000000 | 198.000000 | 0.000000 | none |
| 109 | 376.750000 | 24.250000 | 0.000000 | 99.000000 | 99.000000 | -0.000000 | none |
| 110 | 376.750000 | 24.250000 | 0.000000 | 99.000000 | 0.000000 | 0.000000 | none |
| 111 | 475.750000 | 24.250000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 112 | 475.750000 | 24.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 37.880358 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_both_cg_ptdf_5/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_both_cg_ptdf_5/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
