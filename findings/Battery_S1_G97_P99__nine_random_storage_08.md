# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.367219 | 30.763287 | 0.563168 | 0.000300 | 0.194000 | 0.138600 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,636.250 | 363.750 | 188,292.151 | 188,292.151 | 7.000 | 2,104.233 | 2,204.959 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 1079, 2054, with 160 MW of S1 generation and 145 MW / 580 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 18 | 1,305.000 | 2,257,739.588 | 2,257,739.588 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 198.000 | 198.000 | 0.000 | 396.000 | 594.000 | 594.000 |
| 2 | 198.000 | 198.000 | 0.000 | 396.000 | 468.893 | 468.893 |
| 3 | 198.000 | 198.000 | 0.000 | 396.000 | 417.081 | 417.081 |
| 4 | 198.000 | 198.000 | 0.000 | 396.000 | 580.715 | 580.715 |
| 5 | 198.000 | 198.000 | 0.000 | 396.000 | 495.000 | 495.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 99.000000 | 418.931019 | 261.445417 | 14,664.137865 | b02579:lower |
| 1 | 599.000000 | 0.000000 | 99.000000 | 0.000000 | 198.000000 | 1,127.589497 | 0.000000 | 13,633.235415 | b02579:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02579:lower |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 385.012132 | b02579:lower |
| 106 | 475.750000 | 24.250000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 512.656599 | 100.860621 | b02579:lower |
| 107 | 427.250000 | 72.750000 | 0.000000 | 0.000000 | 396.000000 | 81.809822 | 725.000000 | 0.000000 | none |
| 108 | 328.250000 | 72.750000 | 0.000000 | 99.000000 | 297.000000 | 283.555512 | 870.000000 | 0.000000 | none |
| 109 | 328.250000 | 72.750000 | 0.000000 | 99.000000 | 198.000000 | 146.354059 | 870.000000 | 0.000000 | none |
| 110 | 328.250000 | 72.750000 | 0.000000 | 99.000000 | 99.000000 | 0.000000 | 1,305.000000 | 0.000000 | none |
| 111 | 376.750000 | 24.250000 | 0.000000 | 99.000000 | 0.000000 | 61.372616 | 1,014.062794 | 0.000000 | none |
| 112 | 475.750000 | 24.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 496.372616 | 100.860621 | b02579:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 385.012132 | b02579:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_random_storage_08/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_random_storage_08/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
