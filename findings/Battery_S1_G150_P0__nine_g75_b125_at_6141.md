# 500 MW at bus 6141, S1 generator 150 MW and battery 0 MW / 0 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.901525 | 4,896.450502 | 17.374953 | 30.757228 | 0.583601 | 0.001195 | 0.299941 | 0.000000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,026.732 | 1,110.628 | 0.000 | 0.000 | 9.000 | 0.000 | 0.000 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 75 MW of S1 generation and 125 MW / 500 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,099.137 | 2,562,406.688 | 2,562,406.688 |

## week-3-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 499.901525 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,112.557638 | b02136:lower |
| 105 | 469.259618 | 30.641907 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 349.931068 | 149.970458 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 71.102349 | 188.058673 | b02136:lower |
| 107 | 349.931068 | 149.970458 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 619.870106 | 96.932230 | b02136:lower |
| 108 | 349.931068 | 149.970458 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 964.839929 | 39.647743 | b02136:lower |
| 109 | 350.379706 | 149.521820 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,084.924209 | 20.109084 | b02136:lower |
| 110 | 349.931068 | 149.970458 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 964.839929 | 39.647743 | b02136:lower |
| 111 | 349.931068 | 149.970458 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 619.870106 | 96.932230 | b02136:lower |
| 112 | 349.931068 | 149.970458 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 71.102349 | 188.058673 | b02136:lower |
| 113 | 469.259618 | 30.641907 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 499.901525 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,112.557638 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g150_p0/nine_g75_b125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g150_p0/nine_g75_b125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
