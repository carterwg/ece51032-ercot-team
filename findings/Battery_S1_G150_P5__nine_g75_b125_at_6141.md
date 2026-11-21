# 500 MW at bus 6141, S1 generator 150 MW and battery 5 MW / 20 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.923047 | 4,900.490501 | 17.368647 | 30.758553 | 0.583681 | 0.001196 | 0.299954 | 0.006999 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,213.768 | 1,112.126 | 13,173.848 | 13,173.848 | 9.000 | 2,640.759 | 2,640.759 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 75 MW of S1 generation and 125 MW / 500 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,100.142 | 2,463,334.676 | 2,463,334.676 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 9.998 | 9.998 | -0.000 | 19.997 | 39.994 | 39.994 |
| 2 | 9.998 | 9.998 | -0.000 | 19.997 | 44.713 | 44.713 |
| 3 | 9.998 | 9.998 | -0.000 | 19.997 | 34.995 | 34.995 |
| 4 | 9.998 | 9.998 | -0.000 | 19.997 | 24.996 | 24.996 |
| 5 | 9.998 | 9.998 | -0.000 | 19.997 | 24.996 | 24.996 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 504.922278 | 0.000000 | 4.999230 | 0.000000 | 14.997691 | 733.427909 | 345.606442 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 3 | 494.923817 | 0.000000 | 0.000000 | 4.999230 | 14.997691 | 488.951939 | 133.653661 | 14,069.579627 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 499.923047 | 0.000000 | 0.000000 | 0.000000 | 19.996922 | 0.000000 | 0.000000 | 1,108.517639 | b02136:lower |
| 105 | 468.554892 | 31.368156 | 0.000000 | 0.000000 | 19.996922 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 349.946133 | 149.976914 | 0.000000 | 0.000000 | 19.996922 | 0.000000 | 74.533120 | 188.058673 | b02136:lower |
| 107 | 344.946903 | 149.976914 | 0.000000 | 4.999230 | 14.997691 | 0.000000 | 618.301647 | 96.932230 | b02136:lower |
| 108 | 344.946903 | 149.976914 | 0.000000 | 4.999230 | 9.998461 | 0.000000 | 963.271470 | 39.647743 | b02136:lower |
| 109 | 344.946903 | 149.976914 | 0.000000 | 4.999230 | 4.999230 | 0.000000 | 1,080.934264 | 20.109084 | b02136:lower |
| 110 | 349.946133 | 149.976914 | 0.000000 | 0.000000 | 4.999230 | 0.000000 | 968.270700 | 39.647743 | b02136:lower |
| 111 | 345.395223 | 149.528594 | 0.000000 | 4.999230 | -0.000000 | 0.000000 | 620.723133 | 96.932230 | b02136:lower |
| 112 | 349.946133 | 149.976914 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 74.533120 | 188.058673 | b02136:lower |
| 113 | 468.554892 | 31.368156 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 499.923047 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 1,108.517639 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g150_p5/nine_g75_b125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g150_p5/nine_g75_b125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
