# 500 MW at bus 6141, S1 generator 0 MW and battery 175 MW / 700 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 4,072.305347 | 17.451833 | 30.763287 | 0.566454 | 0.000000 | 0.000000 | 0.245000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,380,000.000 | 0.000 | 335,035.006 | 335,035.006 | 0.000 | 3,415.636 | 3,535.315 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 350.000 | 350.000 | 0.000 | 700.000 | 705.333 | 705.333 |
| 2 | 350.000 | 350.000 | 0.000 | 700.000 | 865.018 | 865.018 |
| 3 | 350.000 | 350.000 | 0.000 | 700.000 | 984.449 | 984.449 |
| 4 | 350.000 | 350.000 | -0.000 | 700.000 | 1,097.974 | 1,097.974 |
| 5 | 350.000 | 350.000 | -0.000 | 700.000 | 892.502 | 892.502 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | 325.000000 | 0.000000 | 0.000000 | 175.000000 | 393.241438 | 8,046.615810 | b01921:upper |
| 22 | 675.000000 | 0.000000 | 175.000000 | 0.000000 | 206.559315 | 14,433.169614 | b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 700.000000 | 1,936.702793 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 700.000000 | 965.575011 | b02136:lower |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 700.000000 | 188.058673 | b02136:lower |
| 107 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 700.000000 | 96.932230 | b02136:lower |
| 108 | 325.000000 | 0.000000 | 0.000000 | 175.000000 | 525.000000 | 39.647743 | b02136:lower |
| 109 | 325.000000 | 0.000000 | 0.000000 | 175.000000 | 350.000000 | 20.109084 | b02136:lower |
| 110 | 325.000000 | 0.000000 | 0.000000 | 175.000000 | 175.000000 | 39.647743 | b02136:lower |
| 111 | 325.000000 | 0.000000 | 0.000000 | 175.000000 | -0.000000 | 96.932230 | b02136:lower |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 188.058673 | b02136:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 965.575011 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,936.702793 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p175/nine_g125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p175/nine_g125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
