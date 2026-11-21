# 500 MW at bus 6141, S1 generator 200 MW and battery 0 MW / 0 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,204.225006 | 17.305623 | 30.763287 | 0.557319 | 0.000345 | 0.400000 | 0.000000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,636.135 | 363.865 | 0.000 | 0.000 | 3.000 | 0.000 | 0.000 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,804.783134 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,833.655352 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 999.729016 | none |
| 107 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 359.834816 | b02136:lower |
| 108 | 417.932763 | 82.067237 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 109 | 300.269969 | 199.730031 | 0.000000 | 0.000000 | 0.000000 | 20.109085 | b02136:lower |
| 110 | 417.932763 | 82.067237 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 111 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 359.834816 | b02136:lower |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 999.729016 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,833.655352 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,804.783134 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g200_p0/nine_grid_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g200_p0/nine_grid_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
