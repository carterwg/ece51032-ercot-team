# 500 MW at bus 6141, S1 generator 0 MW and battery 125 MW / 500 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,149.340043 | 17.534130 | 30.763287 | 0.554157 | 0.000000 | 0.000000 | 0.175000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,380,000.000 | 0.000 | 201,859.268 | 201,859.268 | 0.000 | 1,910.767 | 1,841.953 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 250.000 | 250.000 | -0.000 | 500.000 | 552.095 | 552.095 |
| 2 | 250.000 | 250.000 | 0.000 | 500.000 | 527.524 | 527.524 |
| 3 | 250.000 | 250.000 | 0.000 | 500.000 | 500.000 | 500.000 |
| 4 | 250.000 | 250.000 | 0.000 | 500.000 | 625.000 | 625.000 |
| 5 | 250.000 | 250.000 | -0.000 | 500.000 | 534.001 | 534.001 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 625.000000 | 0.000000 | 125.000000 | 0.000000 | 375.000000 | 16,448.283424 | none |
| 12 | 375.000000 | 0.000000 | 0.000000 | 125.000000 | 306.797089 | 8,919.581114 | b02579:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 500.000000 | 2,859.668097 | b02579:lower |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 500.000000 | 1,888.540315 | b02579:lower |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 500.000000 | 1,054.613979 | none |
| 107 | 412.779779 | 0.000000 | 0.000000 | 87.220221 | 412.779779 | 501.940000 | none |
| 108 | 375.000000 | 0.000000 | 0.000000 | 125.000000 | 287.779779 | 137.465469 | none |
| 109 | 375.000000 | 0.000000 | 0.000000 | 125.000000 | 162.779779 | 0.264016 | none |
| 110 | 375.000000 | 0.000000 | 0.000000 | 125.000000 | 37.779779 | 137.465469 | none |
| 111 | 462.220221 | 0.000000 | 0.000000 | 37.779779 | -0.000000 | 452.499557 | none |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,054.613979 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 1,888.540315 | b02579:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 2,859.668097 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p125/nine_s2_cg_hosting_2/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p125/nine_s2_cg_hosting_2/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
