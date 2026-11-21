# 500 MW at bus 6141, S1 generator 75 MW and battery 150 MW / 600 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 4,138.963838 | 17.334730 | 30.763287 | 0.568256 | 0.000301 | 0.150000 | 0.210000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,665.453 | 334.547 | 315,507.126 | 315,507.126 | 7.000 | 2,770.411 | 2,738.496 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 55 MW of S1 generation and 70 MW / 280 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 509.455 | 1,104,850.159 | 1,104,850.159 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 300.000 | 300.000 | 0.000 | 600.000 | 655.414 | 655.414 |
| 2 | 300.000 | 300.000 | 0.000 | 600.000 | 1,119.077 | 1,119.077 |
| 3 | 300.000 | 300.000 | -0.000 | 600.000 | 828.282 | 828.282 |
| 4 | 300.000 | 300.000 | 0.000 | 600.000 | 815.310 | 815.310 |
| 5 | 300.000 | 300.000 | 0.000 | 600.000 | 761.512 | 761.512 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 650.000000 | 0.000000 | 150.000000 | 0.000000 | 450.000000 | 226.424417 | 242.738229 | 15,449.973441 | b01921:upper, b02355:lower |
| 11 | 350.000000 | 0.000000 | 0.000000 | 150.000000 | 394.586033 | 0.000000 | 312.260606 | 8,669.472257 | b01921:upper |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 0.000000 | 1,870.044302 | none |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 0.000000 | 898.916520 | b02136:lower |
| 106 | 480.579827 | 19.420173 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 107 | 298.280663 | 51.719337 | 0.000000 | 150.000000 | 450.000000 | 0.000000 | 194.083207 | 96.932230 | b02136:lower |
| 108 | 293.610092 | 56.389908 | 0.000000 | 150.000000 | 300.000000 | 0.000000 | 509.454937 | 39.647743 | b02136:lower |
| 109 | 275.042937 | 74.957063 | 0.000000 | 150.000000 | 150.000000 | 0.000000 | 509.454937 | 20.109084 | b02136:lower |
| 110 | 293.610092 | 56.389908 | 0.000000 | 150.000000 | 0.000000 | 0.000000 | 509.454937 | 39.647743 | b02136:lower |
| 111 | 443.750000 | 56.250000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 315.371730 | 96.932230 | b02136:lower |
| 112 | 480.579827 | 19.420173 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 898.916520 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,870.044302 | none |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g75_p150/nine_random_storage_01/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g75_p150/nine_random_storage_01/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
