# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.341826 | 30.763287 | 0.588233 | 0.000629 | 0.194000 | 0.138600 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,339.085 | 660.915 | 298,586.880 | 298,586.880 | 9.000 | 3,271.036 | 3,369.762 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 50 MW of S1 generation and 200 MW / 800 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,800.000 | 4,612,515.346 | 4,612,515.346 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 198.000 | 198.000 | 0.000 | 396.000 | 891.000 | 891.000 |
| 2 | 198.000 | 198.000 | 143.355 | 396.000 | 945.645 | 945.645 |
| 3 | 198.000 | 198.000 | 198.000 | 396.000 | 838.918 | 838.918 |
| 4 | 198.000 | 198.000 | 0.000 | 396.000 | 608.914 | 608.914 |
| 5 | 198.000 | 198.000 | -0.000 | 396.000 | 693.000 | 693.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 599.000000 | 0.000000 | 99.000000 | 0.000000 | 297.000000 | 794.311199 | 600.000000 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 2 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 297.000000 | 992.311199 | 600.000000 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |
| 105 | 452.309234 | 47.690766 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 427.250000 | 72.750000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 573.854651 | 188.058673 | b02136:lower |
| 107 | 320.466307 | 80.533693 | 0.000000 | 99.000000 | 297.000000 | 0.000000 | 979.728802 | 96.932230 | b02136:lower |
| 108 | 304.000000 | 97.000000 | 0.000000 | 99.000000 | 198.000000 | 0.000000 | 1,231.842231 | 39.647743 | b02136:lower |
| 109 | 357.017915 | 97.000000 | 0.000000 | 45.982085 | 152.017915 | 0.000000 | 1,402.522940 | 20.109084 | b02136:lower |
| 110 | 374.232085 | 72.750000 | 0.000000 | 53.017915 | 99.000000 | 173.854651 | 1,588.428967 | 39.647743 | b02136:lower |
| 111 | 328.250000 | 72.750000 | 0.000000 | 99.000000 | -0.000000 | 173.854651 | 1,197.477060 | 96.932230 | b02136:lower |
| 112 | 427.250000 | 72.750000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 573.854651 | 188.058673 | b02136:lower |
| 113 | 452.309234 | 47.690766 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 49.281810 | 0.000000 | 959.726330 | b02090:lower, b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g50_b200_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g50_b200_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
