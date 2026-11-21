# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.342901 | 30.763287 | 0.587471 | 0.000316 | 0.194000 | 0.138600 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,606.097 | 393.903 | 241,934.958 | 241,934.958 | 9.000 | 2,821.263 | 3,189.258 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 170 MW of S1 generation and 120 MW / 480 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,080.000 | 2,399,545.628 | 2,399,545.628 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 198.000 | 198.000 | 0.000 | 396.000 | 709.649 | 709.649 |
| 2 | 198.000 | 198.000 | -0.000 | 396.000 | 727.047 | 727.047 |
| 3 | 198.000 | 198.000 | -0.000 | 396.000 | 739.413 | 739.413 |
| 4 | 198.000 | 198.000 | 0.000 | 396.000 | 495.000 | 495.000 |
| 5 | 198.000 | 198.000 | -0.000 | 396.000 | 402.088 | 402.088 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 599.000000 | 0.000000 | 99.000000 | 0.000000 | 297.000000 | 554.311199 | 360.000000 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 3 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 273.436938 | 589.789549 | 240.000000 | 14,069.579627 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |
| 105 | 483.966288 | 16.033712 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 441.328733 | 58.671267 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 107 | 376.750000 | 24.250000 | 0.000000 | 99.000000 | 297.000000 | 0.000000 | 1,027.122408 | 96.932230 | b02136:lower |
| 108 | 359.335774 | 41.664226 | 0.000000 | 99.000000 | 198.000000 | 0.000000 | 1,080.000000 | 39.647743 | b02136:lower |
| 109 | 328.250000 | 72.750000 | 0.000000 | 99.000000 | 99.000000 | 0.000000 | 676.255025 | 20.109084 | b02136:lower |
| 110 | 359.335774 | 41.664226 | 0.000000 | 99.000000 | -0.000000 | 0.000000 | 1,080.000000 | 39.647743 | b02136:lower |
| 111 | 435.835135 | 64.164865 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 456.622566 | 96.932230 | b02136:lower |
| 112 | 441.328733 | 58.671267 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 483.966288 | 16.033712 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_random_storage_05/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_random_storage_05/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
