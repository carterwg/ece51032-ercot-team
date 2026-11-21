# 500 MW at bus 6141, S1 generator 0 MW and battery 35 MW / 140 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 3,059.352163 | 17.659318 | 30.763287 | 0.554970 | 0.000000 | 0.000000 | 0.049000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,380,000.000 | 0.000 | 66,248.479 | 66,248.479 | 0.000 | 1,892.814 | 1,892.814 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 70.000 | 70.000 | 0.000 | 140.000 | 245.000 | 245.000 |
| 2 | 70.000 | 70.000 | 0.000 | 140.000 | 140.000 | 140.000 |
| 3 | 70.000 | 70.000 | 0.000 | 140.000 | 175.000 | 175.000 |
| 4 | 70.000 | 70.000 | 0.000 | 140.000 | 175.000 | 175.000 |
| 5 | 70.000 | 70.000 | 0.000 | 140.000 | 175.000 | 175.000 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 465.000000 | 0.000000 | 0.000000 | 35.000000 | 35.000000 | 16,698.271304 | none |
| 1 | 535.000000 | 0.000000 | 35.000000 | 0.000000 | 70.000000 | 16,765.472749 | none |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 140.000000 | 2,949.655977 | b02579:lower |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 140.000000 | 1,978.528195 | none |
| 106 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 140.000000 | 1,144.601859 | none |
| 107 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 140.000000 | 504.707659 | none |
| 108 | 465.000000 | 0.000000 | 0.000000 | 35.000000 | 105.000000 | 137.453349 | none |
| 109 | 465.000000 | 0.000000 | 0.000000 | 35.000000 | 70.000000 | 0.251896 | none |
| 110 | 465.000000 | 0.000000 | 0.000000 | 35.000000 | 35.000000 | 137.453349 | none |
| 111 | 465.000000 | 0.000000 | 0.000000 | 35.000000 | 0.000000 | 539.707659 | none |
| 112 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,144.601859 | none |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,978.528195 | none |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 2,949.655977 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g0_p35/nine_grid_at_hosting_1/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g0_p35/nine_grid_at_hosting_1/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
