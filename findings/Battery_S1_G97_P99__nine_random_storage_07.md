# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 4,816.098031 | 17.363387 | 30.763287 | 0.566529 | 0.000771 | 0.194000 | 0.138600 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,276.570 | 723.430 | 179,302.782 | 179,302.782 | 9.000 | 1,990.548 | 1,974.589 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 1079, 2054, with 50 MW of S1 generation and 145 MW / 580 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 18 | 1,251.668 | 2,193,625.695 | 2,193,625.695 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 198.000 | 198.000 | 0.000 | 396.000 | 594.000 | 594.000 |
| 2 | 198.000 | 198.000 | 0.000 | 396.000 | 396.000 | 396.000 |
| 3 | 198.000 | 198.000 | -0.000 | 396.000 | 497.506 | 497.506 |
| 4 | 198.000 | 198.000 | 0.000 | 396.000 | 495.000 | 495.000 |
| 5 | 198.000 | 198.000 | 0.000 | 396.000 | 495.000 | 495.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 99.000000 | 744.226578 | 472.966344 | 14,734.265202 | b02579:lower |
| 1 | 599.000000 | 0.000000 | 99.000000 | 0.000000 | 198.000000 | 512.039730 | 172.346442 | 14,605.033593 | b02579:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 1,192.910109 | b02579:lower |
| 105 | 475.750000 | 24.250000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 392.146844 | b02579:lower |
| 106 | 403.000000 | 97.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 219.682794 | 136.148588 | b02579:lower |
| 107 | 399.574730 | 97.000000 | 0.000000 | 3.425270 | 392.574730 | 66.582577 | 786.585712 | -0.000000 | none |
| 108 | 304.000000 | 97.000000 | 0.000000 | 99.000000 | 293.574730 | 19.328866 | 1,046.011582 | 0.000000 | none |
| 109 | 304.000000 | 97.000000 | 0.000000 | 99.000000 | 194.574730 | 21.201683 | 1,185.085852 | -0.000000 | none |
| 110 | 304.000000 | 97.000000 | 0.000000 | 99.000000 | 95.574730 | 0.000000 | 1,026.682716 | -0.000000 | none |
| 111 | 307.425270 | 97.000000 | 0.000000 | 95.574730 | 0.000000 | 0.000000 | 627.853676 | -0.000000 | none |
| 112 | 407.069655 | 92.930345 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 221.884510 | 134.280650 | b02579:lower |
| 113 | 475.750000 | 24.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 392.146844 | b02579:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,192.910109 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_random_storage_07/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_random_storage_07/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
