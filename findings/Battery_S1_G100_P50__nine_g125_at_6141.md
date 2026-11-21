# 500 MW at bus 6141, S1 generator 100 MW and battery 50 MW / 200 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.943942 | 4,038.922296 | 17.423448 | 30.759838 | 0.567437 | 0.000385 | 0.199978 | 0.069992 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,117.230 | 391.699 | 127,635.255 | 127,635.255 | 7.000 | 3,104.490 | 3,089.534 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 99.989 | 99.989 | -0.000 | 199.978 | 335.254 | 335.254 |
| 2 | 99.989 | 99.989 | -0.000 | 199.978 | 382.503 | 382.503 |
| 3 | 99.989 | 99.989 | -0.000 | 199.978 | 324.424 | 324.424 |
| 4 | 99.989 | 99.989 | -0.000 | 199.978 | 349.961 | 349.961 |
| 5 | 99.989 | 99.989 | -0.000 | 199.978 | 349.961 | 349.961 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 549.938336 | 0.000000 | 49.994394 | 0.000000 | 149.983182 | 15,633.706777 | b02355:lower |
| 2 | 449.949547 | 0.000000 | 0.000000 | 49.994394 | 149.983182 | 15,733.695565 | b02355:lower |
| 104 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | 199.977577 | 1,970.085844 | none |
| 105 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | 199.977577 | 998.958062 | b02136:lower |
| 106 | 497.605810 | 2.338132 | 0.000000 | 0.000000 | 199.977577 | 188.058673 | b02136:lower |
| 107 | 441.884511 | 58.059431 | 0.000000 | 0.000000 | 199.977577 | 96.932230 | b02136:lower |
| 108 | 361.938622 | 88.010925 | 0.000000 | 49.994394 | 149.983182 | 39.647743 | b02136:lower |
| 109 | 349.991266 | 99.958281 | 0.000000 | 49.994394 | 99.988788 | 20.109084 | b02136:lower |
| 110 | 361.938622 | 88.010925 | 0.000000 | 49.994394 | 49.994394 | 39.647743 | b02136:lower |
| 111 | 396.966494 | 52.983053 | 0.000000 | 49.994394 | -0.000000 | 96.932230 | b02136:lower |
| 112 | 497.605810 | 2.338132 | 0.000000 | 0.000000 | -0.000000 | 188.058673 | b02136:lower |
| 113 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 998.958062 | b02136:lower |
| 114 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,970.085844 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g100_p50/nine_g125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g100_p50/nine_g125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
