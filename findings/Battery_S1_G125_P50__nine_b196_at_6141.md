# 500 MW at bus 6141, S1 generator 125 MW and battery 50 MW / 200 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 4,510.990027 | 17.365826 | 30.763287 | 0.576497 | 0.000964 | 0.250000 | 0.070000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,127.159 | 872.841 | 105,853.446 | 105,853.446 | 7.000 | 2,355.545 | 2,256.814 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 0 MW of S1 generation and 196 MW / 784 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,572.308 | 3,661,962.505 | 3,661,962.505 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 100.000 | 100.000 | 0.000 | 200.000 | 263.555 | 263.555 |
| 2 | 100.000 | 100.000 | 0.000 | 200.000 | 260.843 | 260.843 |
| 3 | 100.000 | 100.000 | 0.000 | 200.000 | 400.000 | 400.000 |
| 4 | 100.000 | 100.000 | 0.000 | 200.000 | 250.000 | 250.000 |
| 5 | 100.000 | 100.000 | 0.000 | 200.000 | 220.784 | 220.784 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 550.000000 | 0.000000 | 50.000000 | 0.000000 | 150.000000 | 1,048.205394 | 494.416265 | 14,607.844311 | b01921:upper, b02355:lower |
| 9 | 450.000000 | 0.000000 | 0.000000 | 50.000000 | 150.000000 | 0.000000 | 285.846993 | 9,644.852975 | b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 0.000000 | 0.000000 | 1,498.018113 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 200.000000 | 0.000000 | 0.000000 | 526.890331 | b02136:lower |
| 106 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 200.000000 | 0.000000 | 370.094678 | 188.058673 | b02136:lower |
| 107 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 200.000000 | 20.692880 | 939.555316 | 96.932230 | b02136:lower |
| 108 | 325.000000 | 125.000000 | 0.000000 | 50.000000 | 150.000000 | 0.000000 | 1,213.832258 | 39.647743 | b02136:lower |
| 109 | 325.000000 | 125.000000 | 0.000000 | 50.000000 | 100.000000 | 0.000000 | 1,331.495053 | 20.109084 | b02136:lower |
| 110 | 327.158566 | 122.841434 | 0.000000 | 50.000000 | 50.000000 | 0.000000 | 1,215.990824 | 39.647743 | b02136:lower |
| 111 | 345.692880 | 125.000000 | 0.000000 | 29.307120 | 20.692880 | 0.000000 | 889.555316 | 96.932230 | b02136:lower |
| 112 | 354.307120 | 125.000000 | 0.000000 | 20.692880 | 0.000000 | 0.000000 | 349.401798 | 188.058673 | b02136:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 526.890331 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,498.018113 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g125_p50/nine_b196_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g125_p50/nine_b196_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
