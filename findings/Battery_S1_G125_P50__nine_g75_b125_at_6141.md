# 500 MW at bus 6141, S1 generator 125 MW and battery 50 MW / 200 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.925738 | 4,901.500501 | 17.355892 | 30.758718 | 0.583732 | 0.000998 | 0.249963 | 0.069990 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,420.720 | 928.741 | 126,189.578 | 126,189.578 | 9.000 | 2,641.759 | 2,740.485 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 75 MW of S1 generation and 125 MW / 500 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,100.394 | 2,468,509.852 | 2,468,509.852 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 99.985 | 99.985 | -0.000 | 199.970 | 399.941 | 399.941 |
| 2 | 99.985 | 99.985 | -0.000 | 199.970 | 422.807 | 422.807 |
| 3 | 99.985 | 99.985 | -0.000 | 199.970 | 312.212 | 312.212 |
| 4 | 99.985 | 99.985 | -0.000 | 199.970 | 249.963 | 249.963 |
| 5 | 99.985 | 99.985 | 0.000 | 199.970 | 249.963 | 249.963 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 549.918311 | 0.000000 | 49.992574 | 0.000000 | 149.977721 | 708.616021 | 366.797897 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 3 | 449.933164 | 0.000000 | 0.000000 | 49.992574 | 149.977721 | 489.063863 | 89.782241 | 14,069.579627 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 499.925738 | 0.000000 | 0.000000 | 0.000000 | 199.970295 | 0.000000 | 0.000000 | 1,107.507639 | b02136:lower |
| 105 | 472.797626 | 27.128111 | 0.000000 | 0.000000 | 199.970295 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 374.944303 | 124.981434 | 0.000000 | 0.000000 | 199.970295 | 0.000000 | 100.387504 | 188.058673 | b02136:lower |
| 107 | 324.951729 | 124.981434 | 0.000000 | 49.992574 | 149.977721 | 0.000000 | 599.162687 | 96.932230 | b02136:lower |
| 108 | 324.951729 | 124.981434 | 0.000000 | 49.992574 | 99.985148 | 0.000000 | 944.132510 | 39.647743 | b02136:lower |
| 109 | 363.550116 | 124.981434 | 0.000000 | 11.394187 | 88.590961 | 0.000000 | 1,100.393691 | 20.109084 | b02136:lower |
| 110 | 326.600260 | 124.981434 | 0.000000 | 48.344043 | 40.246918 | 0.000000 | 945.781041 | 39.647743 | b02136:lower |
| 111 | 335.082808 | 124.596012 | 0.000000 | 40.246918 | 0.000000 | 0.000000 | 611.329828 | 96.932230 | b02136:lower |
| 112 | 374.944303 | 124.981434 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 100.387504 | 188.058673 | b02136:lower |
| 113 | 472.797626 | 27.128111 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 499.925738 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,107.507639 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g125_p50/nine_g75_b125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g125_p50/nine_g75_b125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
