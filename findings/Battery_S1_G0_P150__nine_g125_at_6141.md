# 500 MW at bus 6141, S1 generator 0 MW and battery 150 MW / 600 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.943942 | 4,038.922296 | 17.485011 | 30.759838 | 0.566252 | 0.000000 | 0.000000 | 0.209976 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,508.929 | 0.000 | 305,232.351 | 305,232.351 | 0.000 | 3,087.537 | 4,030.953 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 299.966 | 299.966 | -0.000 | 599.933 | 691.075 | 691.075 |
| 2 | 299.966 | 299.966 | -0.000 | 599.933 | 867.618 | 867.618 |
| 3 | 299.966 | 299.966 | 0.000 | 599.933 | 857.231 | 857.231 |
| 4 | 299.966 | 299.966 | -0.000 | 599.933 | 909.589 | 909.589 |
| 5 | 299.966 | 299.966 | -0.000 | 599.933 | 966.270 | 966.270 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | 349.960759 | 0.000000 | 0.000000 | 149.983182 | 364.958825 | 8,054.982043 | b01921:upper |
| 22 | 649.927124 | 0.000000 | 149.983182 | 0.000000 | 214.925548 | 14,491.569482 | b01921:upper, b02355:lower |
| 104 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | 599.932730 | 1,970.085844 | none |
| 105 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | 599.932730 | 998.958062 | b02136:lower |
| 106 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | 599.932730 | 188.058673 | b02136:lower |
| 107 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | 599.932730 | 96.932230 | b02136:lower |
| 108 | 349.960759 | 0.000000 | 0.000000 | 149.983182 | 449.949547 | 39.647743 | b02136:lower |
| 109 | 349.960759 | 0.000000 | 0.000000 | 149.983182 | 299.966365 | 20.109084 | b02136:lower |
| 110 | 349.960759 | 0.000000 | 0.000000 | 149.983182 | 149.983182 | 39.647743 | b02136:lower |
| 111 | 349.960759 | 0.000000 | 0.000000 | 149.983182 | -0.000000 | 96.932230 | b02136:lower |
| 112 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 188.058673 | b02136:lower |
| 113 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 998.958062 | b02136:lower |
| 114 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,970.085844 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p150/nine_g125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p150/nine_g125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
