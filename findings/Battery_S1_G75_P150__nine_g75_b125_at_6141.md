# 500 MW at bus 6141, S1 generator 75 MW and battery 150 MW / 600 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.937844 | 4,911.600500 | 17.316400 | 30.759463 | 0.584061 | 0.000601 | 0.149981 | 0.209974 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,378,894.071 | 561.441 | 336,908.584 | 336,908.584 | 9.000 | 2,907.033 | 2,988.805 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 75 MW of S1 generation and 125 MW / 500 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,102.916 | 2,600,527.120 | 2,600,527.120 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 299.963 | 299.963 | -0.000 | 599.925 | 1,049.869 | 1,049.869 |
| 2 | 299.963 | 299.963 | 0.000 | 599.925 | 1,037.583 | 1,037.583 |
| 3 | 299.963 | 299.963 | 0.000 | 599.925 | 863.173 | 863.173 |
| 4 | 299.963 | 299.963 | -0.000 | 599.925 | 749.907 | 749.907 |
| 5 | 299.963 | 299.963 | 0.000 | 599.925 | 750.583 | 750.583 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 649.919197 | 0.000000 | 149.981353 | 0.000000 | 449.944059 | 599.367900 | 367.638555 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 3 | 349.956491 | 0.000000 | 0.000000 | 149.981353 | 449.944059 | 611.716587 | 122.546185 | 14,069.579627 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 499.937844 | 0.000000 | 0.000000 | 0.000000 | 599.925413 | 0.000000 | 0.000000 | 1,097.407640 | b02136:lower |
| 105 | 481.561487 | 18.376357 | 0.000000 | 0.000000 | 599.925413 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 424.947167 | 74.990677 | 0.000000 | 0.000000 | 599.925413 | 0.000000 | 158.965077 | 188.058673 | b02136:lower |
| 107 | 274.965814 | 74.990677 | 0.000000 | 149.981353 | 449.944059 | 0.000000 | 557.751480 | 96.932230 | b02136:lower |
| 108 | 274.965814 | 74.990677 | 0.000000 | 149.981353 | 299.962706 | 0.000000 | 902.721303 | 39.647743 | b02136:lower |
| 109 | 357.497381 | 74.990677 | 0.000000 | 67.449787 | 232.512920 | 0.000000 | 1,102.915664 | 20.109084 | b02136:lower |
| 110 | 316.195099 | 74.990677 | 0.000000 | 108.752069 | 123.760851 | 0.000000 | 943.950588 | 39.647743 | b02136:lower |
| 111 | 301.432792 | 74.744200 | 0.000000 | 123.760851 | 0.000000 | 36.418892 | 622.812360 | 96.932230 | b02136:lower |
| 112 | 424.947167 | 74.990677 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 158.965077 | 188.058673 | b02136:lower |
| 113 | 481.561487 | 18.376357 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 499.937844 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,097.407640 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g75_p150/nine_g75_b125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g75_p150/nine_g75_b125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
