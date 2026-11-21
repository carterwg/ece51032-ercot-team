# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.343770 | 30.763287 | 0.586550 | 0.000367 | 0.194000 | 0.138600 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,549.829 | 450.171 | 292,609.752 | 292,609.752 | 9.000 | 3,271.033 | 3,187.263 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 100 MW of S1 generation and 175 MW / 700 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,575.000 | 3,861,476.251 | 3,861,476.251 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 198.000 | 198.000 | 0.000 | 396.000 | 841.510 | 841.510 |
| 2 | 198.000 | 198.000 | 22.166 | 396.000 | 849.536 | 849.536 |
| 3 | 198.000 | 198.000 | 198.000 | 396.000 | 854.442 | 854.442 |
| 4 | 198.000 | 198.000 | 0.000 | 396.000 | 675.099 | 675.099 |
| 5 | 198.000 | 198.000 | 0.000 | 396.000 | 693.000 | 693.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 599.000000 | 0.000000 | 99.000000 | 0.000000 | 297.000000 | 719.311199 | 525.000000 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 1 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 198.000000 | 756.814540 | 350.000000 | 14,552.010372 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |
| 105 | 473.834655 | 26.165345 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 427.250000 | 72.750000 | 0.000000 | 0.000000 | 396.000000 | 0.000000 | 236.354651 | 188.058673 | b02136:lower |
| 107 | 376.750000 | 24.250000 | 0.000000 | 99.000000 | 297.000000 | 0.000000 | 1,184.622408 | 96.932230 | b02136:lower |
| 108 | 340.744204 | 60.255796 | 0.000000 | 99.000000 | 198.000000 | 0.000000 | 1,159.512037 | 39.647743 | b02136:lower |
| 109 | 427.250000 | 72.750000 | 0.000000 | 0.000000 | 198.000000 | 0.000000 | 1,247.755025 | 20.109084 | b02136:lower |
| 110 | 376.750000 | 24.250000 | 0.000000 | 99.000000 | 99.000000 | 0.000000 | 1,529.592231 | 39.647743 | b02136:lower |
| 111 | 328.250000 | 72.750000 | 0.000000 | 99.000000 | 0.000000 | 81.041239 | 767.163647 | 96.932230 | b02136:lower |
| 112 | 427.250000 | 72.750000 | 0.000000 | 0.000000 | 0.000000 | 19.686588 | 256.041239 | 188.058673 | b02136:lower |
| 113 | 475.750000 | 24.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 19.686588 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 3.199407 | 0.000000 | 1,005.808733 | b02090:lower, b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g100_b175_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g100_b175_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
