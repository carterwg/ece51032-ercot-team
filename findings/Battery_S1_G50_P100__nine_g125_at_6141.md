# 500 MW at bus 6141, S1 generator 50 MW and battery 100 MW / 400 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.943942 | 4,038.922296 | 17.454233 | 30.759838 | 0.566842 | 0.000192 | 0.099989 | 0.139984 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,313.300 | 195.629 | 230,208.668 | 230,208.668 | 7.000 | 3,004.764 | 3,457.529 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 199.978 | 199.978 | 0.000 | 399.955 | 497.181 | 497.181 |
| 2 | 199.978 | 199.978 | -0.000 | 399.955 | 680.198 | 680.198 |
| 3 | 199.978 | 199.978 | -0.000 | 399.955 | 624.391 | 624.391 |
| 4 | 199.978 | 199.978 | -0.000 | 399.955 | 699.922 | 699.922 |
| 5 | 199.978 | 199.978 | -0.000 | 399.955 | 639.670 | 639.670 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | 399.955153 | 0.000000 | 0.000000 | 99.988788 | 264.970037 | 8,004.987649 | b01921:upper |
| 30 | 599.932730 | 0.000000 | 99.988788 | 0.000000 | 267.423903 | 15,911.163802 | b02355:lower |
| 104 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | 399.955153 | 1,970.085844 | none |
| 105 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | 399.955153 | 998.958062 | b02136:lower |
| 106 | 498.712348 | 1.231593 | 0.000000 | 0.000000 | 399.955153 | 188.058673 | b02136:lower |
| 107 | 469.361575 | 30.582366 | 0.000000 | 0.000000 | 399.955153 | 96.932230 | b02136:lower |
| 108 | 356.270008 | 43.685145 | 0.000000 | 99.988788 | 299.966365 | 39.647743 | b02136:lower |
| 109 | 349.976829 | 49.978325 | 0.000000 | 99.988788 | 199.977577 | 20.109084 | b02136:lower |
| 110 | 356.270008 | 43.685145 | 0.000000 | 99.988788 | 99.988788 | 39.647743 | b02136:lower |
| 111 | 374.720675 | 25.234479 | 0.000000 | 99.988788 | -0.000000 | 96.932230 | b02136:lower |
| 112 | 498.712348 | 1.231593 | 0.000000 | 0.000000 | -0.000000 | 188.058673 | b02136:lower |
| 113 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 998.958062 | b02136:lower |
| 114 | 499.943942 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,970.085844 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g50_p100/nine_g125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g50_p100/nine_g125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
