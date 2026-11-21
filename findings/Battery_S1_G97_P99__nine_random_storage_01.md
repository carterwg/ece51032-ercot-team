# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 4,100.301656 | 17.362462 | 30.763287 | 0.567853 | 0.000373 | 0.194000 | 0.138600 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,591.745 | 408.255 | 216,308.256 | 216,308.256 | 7.000 | 2,505.140 | 2,700.603 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 55 MW of S1 generation and 70 MW / 280 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 504.042 | 1,115,655.582 | 1,115,655.582 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 198.000 | 198.000 | -0.000 | 396.000 | 398.698 | 398.698 |
| 2 | 198.000 | 198.000 | 0.000 | 396.000 | 725.232 | 725.232 |
| 3 | 198.000 | 198.000 | 0.000 | 396.000 | 557.121 | 557.121 |
| 4 | 198.000 | 198.000 | 0.000 | 396.000 | 653.304 | 653.304 |
| 5 | 198.000 | 198.000 | 0.000 | 396.000 | 622.194 | 622.194 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 599.000000 | 0.000000 | 99.000000 | 0.000000 | 297.000000 | 280.023462 | 206.675092 | 15,449.973441 | b01921:upper, b02355:lower |
| 11 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 297.000000 | 0.000000 | 344.649885 | 8,689.523718 | b01921:upper |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 1,908.706484 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 937.578702 | b02136:lower |
| 106 | 483.393792 | 16.606208 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 188.058674 | b02136:lower |
| 107 | 343.250321 | 57.749679 | 0.000000 | 99.000000 | 297.000000 | 0.000000 | 240.643054 | 96.932232 | b02136:lower |
| 108 | 327.202004 | 73.797996 | 0.000000 | 99.000000 | 198.000000 | 0.000000 | 504.042232 | 39.647743 | b02136:lower |
| 109 | 304.052871 | 96.947129 | 0.000000 | 99.000000 | 99.000000 | 0.000000 | 504.042232 | 20.109084 | b02136:lower |
| 110 | 327.202005 | 73.797995 | 0.000000 | 99.000000 | 0.000000 | 0.000000 | 504.042232 | 39.647743 | b02136:lower |
| 111 | 427.250000 | 72.750000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 263.399177 | 96.932230 | b02136:lower |
| 112 | 483.393792 | 16.606208 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 937.578702 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,908.706484 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_random_storage_01/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_random_storage_01/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
