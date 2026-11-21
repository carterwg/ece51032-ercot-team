# 500 MW at bus 6141, S1 generator 125 MW and battery 50 MW / 200 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.901525 | 4,946.414282 | 17.353883 | 30.757228 | 0.584835 | 0.001036 | 0.249951 | 0.069986 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,168.568 | 968.792 | 144,435.489 | 144,435.489 | 9.000 | 3,105.490 | 3,186.263 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 50 MW of S1 generation and 175 MW / 700 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,556.279 | 3,739,667.025 | 3,739,667.025 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 99.980 | 99.980 | -0.000 | 199.961 | 394.032 | 394.032 |
| 2 | 99.980 | 99.980 | 0.000 | 199.961 | 499.902 | 499.902 |
| 3 | 99.980 | 99.980 | 99.980 | 199.961 | 399.921 | 399.921 |
| 4 | 99.980 | 99.980 | 0.000 | 199.961 | 288.257 | 288.257 |
| 5 | 99.980 | 99.980 | 0.000 | 199.961 | 299.941 | 299.941 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 549.891678 | 0.000000 | 49.990153 | 0.000000 | 149.970458 | 815.666586 | 518.759822 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 3 | 449.911373 | 0.000000 | 0.000000 | 49.990153 | 116.597717 | 758.542704 | 404.177285 | 14,069.579627 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 499.901525 | 0.000000 | 0.000000 | 0.000000 | 199.960610 | 0.000000 | 0.000000 | 1,062.593858 | b02136:lower |
| 105 | 452.653812 | 47.247714 | 0.000000 | 0.000000 | 199.960610 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 359.873748 | 124.975381 | 0.000000 | 15.052396 | 184.908214 | 0.000000 | 345.839881 | 188.058673 | b02136:lower |
| 107 | 324.935991 | 124.975381 | 0.000000 | 49.990153 | 134.918062 | 0.000000 | 859.669881 | 96.932230 | b02136:lower |
| 108 | 324.935991 | 124.975381 | 0.000000 | 49.990153 | 84.927909 | 0.000000 | 1,204.639704 | 39.647743 | b02136:lower |
| 109 | 373.448958 | 124.975381 | 0.000000 | 1.477186 | 83.450723 | 0.000000 | 1,370.815465 | 20.109084 | b02136:lower |
| 110 | 341.465573 | 124.975381 | 0.000000 | 33.460571 | 49.990153 | 0.000000 | 1,221.169286 | 39.647743 | b02136:lower |
| 111 | 325.467262 | 124.444110 | 0.000000 | 49.990153 | 0.000000 | 15.052396 | 877.143762 | 96.932230 | b02136:lower |
| 112 | 374.926144 | 124.975381 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 360.892277 | 188.058673 | b02136:lower |
| 113 | 452.653812 | 47.247714 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 499.901525 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,062.593858 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g125_p50/nine_g50_b175_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g125_p50/nine_g50_b175_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
