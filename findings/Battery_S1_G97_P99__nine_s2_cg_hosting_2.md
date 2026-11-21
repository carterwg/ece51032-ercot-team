# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,220.332498 | 17.375398 | 30.763287 | 0.555183 | 0.000107 | 0.194000 | 0.138600 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,903.272 | 96.728 | 144,639.000 | 144,639.000 | 1.000 | 1,545.770 | 1,560.726 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 198.000 | 198.000 | -0.000 | 396.000 | 396.000 | 396.000 |
| 2 | 198.000 | 198.000 | -0.000 | 396.000 | 396.000 | 396.000 |
| 3 | 198.000 | 198.000 | 0.000 | 396.000 | 396.000 | 396.000 |
| 4 | 198.000 | 198.000 | 0.000 | 396.000 | 396.000 | 396.000 |
| 5 | 198.000 | 198.000 | -0.000 | 396.000 | 495.000 | 495.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 599.000000 | 0.000000 | 99.000000 | 0.000000 | 297.000000 | 16,540.492414 | none |
| 12 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 233.635651 | 8,822.588659 | b02579:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 2,788.675642 | b02579:lower |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 1,817.547860 | b02579:lower |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 983.621524 | none |
| 107 | 412.347324 | 0.000000 | 0.000000 | 87.652676 | 308.347324 | 431.380000 | none |
| 108 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 209.347324 | 40.473014 | none |
| 109 | 304.271561 | 96.728439 | 0.000000 | 99.000000 | 110.347324 | -0.000000 | none |
| 110 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 11.347324 | 40.473014 | none |
| 111 | 488.652676 | 0.000000 | 0.000000 | 11.347324 | -0.000000 | 355.074648 | none |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 983.621524 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,817.547860 | b02579:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 2,788.675642 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_s2_cg_hosting_2/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_s2_cg_hosting_2/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
