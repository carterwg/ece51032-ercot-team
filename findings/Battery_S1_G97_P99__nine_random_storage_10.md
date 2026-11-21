# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.366294 | 30.763287 | 0.563977 | 0.000416 | 0.194000 | 0.138600 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,526.147 | 473.853 | 199,210.478 | 199,210.478 | 7.000 | 2,188.003 | 2,202.962 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, 5395, 6342, 5451, 6004, with 145 MW of S1 generation and 110 MW / 440 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 45 | 990.000 | 1,873,247.276 | 1,873,247.276 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 198.000 | 198.000 | 0.000 | 396.000 | 486.788 | 486.788 |
| 2 | 198.000 | 198.000 | 0.000 | 396.000 | 594.000 | 594.000 |
| 3 | 198.000 | 198.000 | 0.000 | 396.000 | 545.596 | 545.596 |
| 4 | 198.000 | 198.000 | 0.000 | 396.000 | 547.824 | 547.824 |
| 5 | 198.000 | 198.000 | 0.000 | 396.000 | 495.000 | 495.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 599.000000 | 0.000000 | 99.000000 | 0.000000 | 297.000000 | 695.643467 | 264.000000 | 14,191.980000 | none |
| 11 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 297.000000 | 0.000000 | 656.301652 | 8,101.477141 | b01854:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 1,009.008140 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 37.880358 | none |
| 106 | 428.790265 | 71.209735 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 141.730668 | 0.000000 | none |
| 107 | 427.250000 | 72.750000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 514.940178 | 0.000000 | none |
| 108 | 328.250000 | 72.750000 | 0.000000 | 99.000000 | 297.000000 | 0.000000 | 948.694488 | 0.000000 | none |
| 109 | 328.250000 | 72.750000 | 0.000000 | 99.000000 | 198.000000 | 0.000000 | 990.000000 | -0.000000 | none |
| 110 | 328.250000 | 72.750000 | 0.000000 | 99.000000 | 99.000000 | 0.000000 | 948.694488 | 0.000000 | none |
| 111 | 328.250000 | 72.750000 | 0.000000 | 99.000000 | 0.000000 | 0.000000 | 415.940178 | -0.000000 | none |
| 112 | 461.106257 | 38.893743 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 37.880358 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_random_storage_10/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_random_storage_10/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
