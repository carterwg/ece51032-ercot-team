# 500 MW at bus 6141, S1 generator 150 MW and battery 0 MW / 0 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 350.764626 | 4,594.855837 | 12.195074 | 21.581346 | 0.405883 | 0.000814 | 0.210459 | 0.000000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 3,071,961.998 | 736.124 | 0.000 | 0.000 | 7.000 | 0.000 | 0.000 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 50 MW of S1 generation and 125 MW / 500 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,061.023 | 2,401,059.029 | 2,401,059.029 |

## week-3-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 350.764626 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,414.152303 | b02136:lower |
| 105 | 350.764626 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 443.024521 | b02136:lower |
| 106 | 245.535238 | 105.229388 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 49.321979 | 188.058673 | b02136:lower |
| 107 | 245.535238 | 105.229388 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 598.089736 | 96.932230 | b02136:lower |
| 108 | 245.535238 | 105.229388 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 943.059559 | 39.647743 | b02136:lower |
| 109 | 245.594932 | 105.169694 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,061.022803 | 20.109084 | b02136:lower |
| 110 | 245.535238 | 105.229388 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 943.059559 | 39.647743 | b02136:lower |
| 111 | 245.535238 | 105.229388 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 598.089736 | 96.932230 | b02136:lower |
| 112 | 245.957607 | 104.807018 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 51.447840 | 188.058673 | b02136:lower |
| 113 | 350.764626 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 443.024521 | b02136:lower |
| 114 | 350.764626 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,414.152303 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g150_p0/nine_g50_b125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g150_p0/nine_g50_b125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
