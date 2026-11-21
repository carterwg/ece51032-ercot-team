# 500 MW at bus 6141, S1 generator 97 MW and battery 99 MW / 396 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.315213 | 30.763287 | 0.614644 | 0.000830 | 0.194000 | 0.138600 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,923.227 | 1,076.773 | 242,383.105 | 242,383.105 | 106.732 | 3,313.912 | 3,661.959 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 198.000 | 198.000 | 0.000 | 396.000 | 536.754 | 536.754 |
| 2 | 198.000 | 198.000 | 0.000 | 396.000 | 745.306 | 745.306 |
| 3 | 198.000 | 198.000 | -0.000 | 396.000 | 713.872 | 713.872 |
| 4 | 198.000 | 198.000 | 0.000 | 396.000 | 649.807 | 649.807 |
| 5 | 198.000 | 198.000 | 0.000 | 396.000 | 497.173 | 497.173 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 599.000000 | 0.000000 | 99.000000 | 0.000000 | 297.000000 | 14,623.623467 | b01921:upper, b02355:lower |
| 11 | 401.000000 | 0.000000 | 0.000000 | 99.000000 | 297.000000 | 7,445.175489 | b01921:upper, b02090:lower, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 396.000000 | 1,009.008140 | b02136:lower |
| 105 | 486.248366 | 13.751634 | 0.000000 | 0.000000 | 396.000000 | 306.816946 | b02136:lower |
| 106 | 449.679414 | 50.320586 | 0.000000 | 0.000000 | 396.000000 | 188.058673 | b02136:lower |
| 107 | 421.619070 | 78.380930 | 0.000000 | 0.000000 | 396.000000 | 96.932230 | b02136:lower |
| 108 | 310.041805 | 90.958195 | 0.000000 | 99.000000 | 297.000000 | 39.647743 | b02136:lower |
| 109 | 304.025310 | 96.974690 | 0.000000 | 99.000000 | 198.000000 | 20.109084 | b02136:lower |
| 110 | 310.041805 | 90.958195 | 0.000000 | 99.000000 | 99.000000 | 39.647743 | b02136:lower |
| 111 | 327.681274 | 73.318726 | 0.000000 | 99.000000 | 0.000000 | 96.932230 | b02136:lower |
| 112 | 449.679414 | 50.320586 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 486.248366 | 13.751634 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g200_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g97_p99/nine_g200_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
