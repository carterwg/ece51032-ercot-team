# 500 MW at bus 6141, S1 generator 150 MW and battery 0 MW / 0 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 494.131325 | 4,941.313246 | 17.173221 | 30.402208 | 0.578004 | 0.001221 | 0.296479 | 0.000000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,327,448.209 | 1,142.195 | 0.000 | 0.000 | 9.000 | 0.000 | 0.000 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 50 MW of S1 generation and 175 MW / 700 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,556.514 | 3,806,977.223 | 3,806,977.223 |

## week-3-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 494.131325 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,067.694894 | b02136:lower |
| 105 | 441.568866 | 52.562459 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 345.891927 | 148.239397 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 332.460308 | 188.058673 | b02136:lower |
| 107 | 345.891927 | 148.239397 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 881.228065 | 96.932230 | b02136:lower |
| 108 | 345.891927 | 148.239397 | 0.000000 | 0.000000 | 0.000000 | 157.369821 | 1,383.567709 | 39.647743 | b02136:lower |
| 109 | 346.497299 | 147.634026 | 0.000000 | 0.000000 | 0.000000 | 18.642770 | 1,364.924939 | 20.109084 | b02136:lower |
| 110 | 345.891927 | 148.239397 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,226.197888 | 39.647743 | b02136:lower |
| 111 | 345.891927 | 148.239397 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 881.228065 | 96.932230 | b02136:lower |
| 112 | 345.891927 | 148.239397 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 332.460308 | 188.058673 | b02136:lower |
| 113 | 441.568866 | 52.562459 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 494.131325 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,067.694894 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g150_p0/nine_g50_b175_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g150_p0/nine_g50_b175_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
