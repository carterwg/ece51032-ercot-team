# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.925738 | 4,901.500501 | 17.343191 | 30.758718 | 0.584058 | 0.000775 | 0.193971 | 0.138579 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,627.213 | 722.248 | 243,001.784 | 243,001.784 | 9.000 | 2,741.485 | 2,755.447 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 75 MW of S1 generation and 125 MW / 500 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,100.394 | 2,522,600.057 | 2,522,600.057 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 197.971 | 197.971 | 0.000 | 395.941 | 666.756 | 666.756 |
| 2 | 197.971 | 197.971 | 0.000 | 395.941 | 828.679 | 828.679 |
| 3 | 197.971 | 197.971 | 0.000 | 395.941 | 671.169 | 671.169 |
| 4 | 197.971 | 197.971 | 0.000 | 395.941 | 494.926 | 494.926 |
| 5 | 197.971 | 197.971 | 0.000 | 395.941 | 582.522 | 582.522 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 598.911034 | 0.000000 | 98.985296 | 0.000000 | 296.955888 | 659.623299 | 366.797897 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 3 | 400.940442 | 0.000000 | 0.000000 | 98.985296 | 296.955888 | 570.540309 | 122.265966 | 14,069.579627 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 499.925738 | 0.000000 | 0.000000 | 0.000000 | 395.941184 | 0.000000 | 0.000000 | 1,107.507639 | b02136:lower |
| 105 | 478.096015 | 21.829723 | 0.000000 | 0.000000 | 395.941184 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 402.940144 | 96.985593 | 0.000000 | 0.000000 | 395.941184 | 0.000000 | 128.383345 | 188.058673 | b02136:lower |
| 107 | 303.954848 | 96.985593 | 0.000000 | 98.985296 | 296.955888 | 0.000000 | 578.165806 | 96.932230 | b02136:lower |
| 108 | 303.954848 | 96.985593 | 0.000000 | 98.985296 | 197.970592 | 0.000000 | 923.135629 | 39.647743 | b02136:lower |
| 109 | 303.954848 | 96.985593 | 0.000000 | 98.985296 | 98.985296 | 0.000000 | 1,040.798423 | 20.109084 | b02136:lower |
| 110 | 303.954848 | 96.985593 | 0.000000 | 98.985296 | 0.000000 | 0.000000 | 923.135629 | 39.647743 | b02136:lower |
| 111 | 403.250290 | 96.675447 | 0.000000 | 0.000000 | 0.000000 | 6.117379 | 685.689967 | 96.932230 | b02136:lower |
| 112 | 402.940144 | 96.985593 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 128.383345 | 188.058673 | b02136:lower |
| 113 | 478.096015 | 21.829723 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 499.925738 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,107.507639 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g75_b125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g75_b125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
