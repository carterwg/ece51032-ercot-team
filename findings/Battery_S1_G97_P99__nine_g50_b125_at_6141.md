# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.944569 | 4,610.832069 | 17.349524 | 30.759877 | 0.578425 | 0.000750 | 0.193978 | 0.138585 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,835.966 | 678.462 | 246,952.705 | 246,952.705 | 7.000 | 3,015.732 | 2,950.912 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 50 MW of S1 generation and 125 MW / 500 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,027.722 | 2,304,915.936 | 2,304,915.936 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 197.978 | 197.978 | 0.000 | 395.956 | 593.934 | 593.934 |
| 2 | 197.978 | 197.978 | 0.000 | 395.956 | 695.984 | 695.984 |
| 3 | 197.978 | 197.978 | 0.000 | 395.956 | 720.066 | 720.066 |
| 4 | 197.978 | 197.978 | 0.000 | 395.956 | 692.923 | 692.923 |
| 5 | 197.978 | 197.978 | 0.000 | 395.956 | 468.984 | 468.984 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 598.933594 | 0.000000 | 98.989025 | 0.000000 | 296.967074 | 655.155206 | 342.573958 | 14,700.221125 | b01921:upper, b02355:lower |
| 3 | 400.955545 | 0.000000 | 0.000000 | 98.989025 | 296.967074 | 456.765278 | 4.774924 | 14,356.535779 | b01921:upper, b02355:lower |
| 104 | 499.944569 | 0.000000 | 0.000000 | 0.000000 | 395.956099 | 0.000000 | 0.000000 | 1,398.176071 | b02136:lower |
| 105 | 499.944569 | 0.000000 | 0.000000 | 0.000000 | 395.956099 | 0.000000 | 0.000000 | 427.048289 | b02136:lower |
| 106 | 402.955323 | 96.989246 | 0.000000 | 0.000000 | 395.956099 | 0.000000 | 86.858724 | 188.058673 | b02136:lower |
| 107 | 303.966298 | 96.989246 | 0.000000 | 98.989025 | 296.967074 | 0.000000 | 536.637456 | 96.932230 | b02136:lower |
| 108 | 303.966298 | 96.989246 | 0.000000 | 98.989025 | 197.978050 | 0.000000 | 881.607279 | 39.647743 | b02136:lower |
| 109 | 332.418100 | 96.989246 | 0.000000 | 70.537223 | 127.440827 | 0.000000 | 1,027.721875 | 20.109084 | b02136:lower |
| 110 | 335.889575 | 96.989246 | 0.000000 | 67.065748 | 60.375079 | 0.000000 | 913.530555 | 39.647743 | b02136:lower |
| 111 | 343.042492 | 96.526998 | 0.000000 | 60.375079 | 0.000000 | 0.000000 | 577.672888 | 96.932230 | b02136:lower |
| 112 | 402.955323 | 96.989246 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 86.858724 | 188.058673 | b02136:lower |
| 113 | 499.944569 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 427.048289 | b02136:lower |
| 114 | 499.944569 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,398.176071 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g50_b125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g50_b125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
