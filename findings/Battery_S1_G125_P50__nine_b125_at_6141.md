# 500 MW at bus 6141, S1 generator 125 MW and battery 50 MW / 200 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 4,072.305347 | 17.375081 | 30.763287 | 0.567745 | 0.000461 | 0.250000 | 0.070000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,481.024 | 518.976 | 104,915.827 | 104,915.827 | 7.000 | 2,302.688 | 2,470.227 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 0 MW of S1 generation and 125 MW / 500 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 893.076 | 1,958,025.780 | 1,958,025.780 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 100.000 | 100.000 | 0.000 | 200.000 | 250.000 | 250.000 |
| 2 | 100.000 | 100.000 | 0.000 | 200.000 | 320.197 | 320.197 |
| 3 | 100.000 | 100.000 | 0.000 | 200.000 | 287.249 | 287.249 |
| 4 | 100.000 | 100.000 | 0.000 | 200.000 | 286.653 | 286.653 |
| 5 | 100.000 | 100.000 | 0.000 | 200.000 | 250.000 | 250.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 550.000000 | 0.000000 | 50.000000 | 0.000000 | 150.000000 | 585.403680 | 297.692112 | 15,312.606552 | b01921:upper, b02355:lower |
| 9 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 150.000000 | 0.000000 | 103.159118 | 9,900.849780 | b01921:upper |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 0.000000 | 0.000000 | 1,936.702793 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 0.000000 | 0.000000 | 965.575011 | b02136:lower |
| 106 | 449.508347 | 50.491653 | 0.000000 | 0.000000 | 200.000000 | 0.000000 | 5.918345 | 188.058673 | b02136:lower |
| 107 | 406.250000 | 93.750000 | 0.000000 | 0.000000 | 200.000000 | 0.000000 | 511.427755 | 96.932230 | b02136:lower |
| 108 | 356.250000 | 93.750000 | 0.000000 | 50.000000 | 150.000000 | 0.000000 | 806.397578 | 39.647743 | b02136:lower |
| 109 | 325.265964 | 124.734036 | 0.000000 | 50.000000 | 100.000000 | 0.000000 | 893.076337 | 20.109084 | b02136:lower |
| 110 | 356.250000 | 93.750000 | 0.000000 | 50.000000 | 50.000000 | 0.000000 | 806.397578 | 39.647743 | b02136:lower |
| 111 | 418.750000 | 31.250000 | 0.000000 | 50.000000 | 0.000000 | 0.000000 | 523.927755 | 96.932230 | b02136:lower |
| 112 | 468.750000 | 31.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 25.159998 | 188.058673 | b02136:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 965.575011 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,936.702793 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g125_p50/nine_b125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g125_p50/nine_b125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
