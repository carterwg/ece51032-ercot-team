# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.338556 | 30.763287 | 0.591632 | 0.000499 | 0.194000 | 0.138600 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,443.252 | 556.748 | 220,924.988 | 220,924.988 | 9.000 | 2,555.000 | 3,019.721 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 145 MW of S1 generation and 80 MW / 320 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 720.000 | 1,499,688.322 | 1,499,688.322 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 198.000 | 198.000 | 0.000 | 396.000 | 595.837 | 595.837 |
| 2 | 198.000 | 198.000 | 0.000 | 396.000 | 687.715 | 687.715 |
| 3 | 198.000 | 198.000 | 0.000 | 396.000 | 646.353 | 646.353 |
| 4 | 198.000 | 198.000 | -0.000 | 396.000 | 495.554 | 495.554 |
| 5 | 198.000 | 198.000 | 0.000 | 396.000 | 497.173 | 497.173 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 599.000000 | 0.000000 | 99.000000 | 0.000000 | 297.000000 | 434.311199 | 240.000000 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 3 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 297.000000 | 400.000000 | 50.210451 | 14,069.579627 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |
| 105 | 481.393118 | 18.606882 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 431.912874 | 68.087126 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 107 | 329.622408 | 72.750000 | 0.000000 | 97.627592 | 298.372408 | 0.000000 | 383.744817 | 96.932230 | b02136:lower |
| 108 | 317.796759 | 83.203241 | 0.000000 | 99.000000 | 199.372408 | 0.000000 | 576.255183 | 39.647743 | b02136:lower |
| 109 | 319.601293 | 81.398707 | 0.000000 | 99.000000 | 100.372408 | 0.000000 | 720.000000 | 20.109084 | b02136:lower |
| 110 | 327.742014 | 73.257986 | 0.000000 | 99.000000 | 1.372408 | 0.000000 | 720.000000 | 39.647743 | b02136:lower |
| 111 | 425.877592 | 72.750000 | 0.000000 | 1.372408 | 0.000000 | 0.000000 | 480.000000 | 96.932230 | b02136:lower |
| 112 | 431.912874 | 68.087126 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 481.393118 | 18.606882 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_random_storage_04/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_random_storage_04/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
