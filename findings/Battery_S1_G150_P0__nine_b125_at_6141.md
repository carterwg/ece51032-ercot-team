# 500 MW at bus 6141, S1 generator 150 MW and battery 0 MW / 0 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.943942 | 4,038.922296 | 17.393853 | 30.759838 | 0.566962 | 0.000458 | 0.299966 | 0.000000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,990.307 | 518.621 | 0.000 | 0.000 | 7.000 | 0.000 | 0.000 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 0 MW of S1 generation and 125 MW / 500 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 884.745 | 1,955,989.980 | 1,955,989.980 |

## week-3-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,970.085844 | none |
| 105 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 998.958062 | b02136:lower |
| 106 | 476.916994 | 23.026947 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 107 | 462.448146 | 37.495796 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 534.298909 | 96.932230 | b02136:lower |
| 108 | 387.456555 | 112.487387 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 804.277140 | 39.647743 | b02136:lower |
| 109 | 350.261209 | 149.682733 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 884.744589 | 20.109084 | b02136:lower |
| 110 | 439.529813 | 60.414128 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 856.350399 | 39.647743 | b02136:lower |
| 111 | 387.456555 | 112.487387 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 459.307318 | 96.932230 | b02136:lower |
| 112 | 476.916994 | 23.026947 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 998.958062 | b02136:lower |
| 114 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,970.085844 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g150_p0/nine_b125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g150_p0/nine_b125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
