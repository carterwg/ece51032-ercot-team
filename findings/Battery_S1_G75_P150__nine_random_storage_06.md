# 500 MW at bus 6141, S1 generator 75 MW and battery 150 MW / 600 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.316885 | 30.763287 | 0.586273 | 0.000129 | 0.150000 | 0.210000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,804.663 | 195.337 | 420,310.144 | 420,310.144 | 9.000 | 3,422.616 | 3,551.263 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 165 MW of S1 generation and 185 MW / 740 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,665.000 | 4,262,488.280 | 4,262,488.280 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 300.000 | 300.000 | 0.000 | 600.000 | 1,309.713 | 1,309.713 |
| 2 | 300.000 | 300.000 | 144.145 | 600.000 | 1,267.498 | 1,267.498 |
| 3 | 300.000 | 300.000 | 150.000 | 600.000 | 1,350.000 | 1,350.000 |
| 4 | 300.000 | 300.000 | 0.000 | 600.000 | 730.763 | 730.763 |
| 5 | 300.000 | 300.000 | 0.000 | 600.000 | 1,031.499 | 1,031.499 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 650.000000 | 0.000000 | 150.000000 | 0.000000 | 450.000000 | 698.311199 | 555.000000 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 2 | 350.000000 | 0.000000 | 0.000000 | 150.000000 | 450.000000 | 813.311199 | 370.000000 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |
| 105 | 487.070356 | 12.929644 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 331.250000 | 18.750000 | 0.000000 | 150.000000 | 450.000000 | 0.000000 | 444.104651 | 188.058673 | b02136:lower |
| 107 | 331.250000 | 18.750000 | 0.000000 | 150.000000 | 300.000000 | 0.000000 | 992.872408 | 96.932230 | b02136:lower |
| 108 | 331.250000 | 18.750000 | 0.000000 | 150.000000 | 150.000000 | 0.000000 | 1,337.842231 | 39.647743 | b02136:lower |
| 109 | 593.750000 | 56.250000 | 150.000000 | 0.000000 | 300.000000 | 276.652743 | 1,252.157769 | 20.109084 | b02136:lower |
| 110 | 331.250000 | 18.750000 | 0.000000 | 150.000000 | 150.000000 | 74.104651 | 1,411.946882 | 39.647743 | b02136:lower |
| 111 | 331.250000 | 18.750000 | 0.000000 | 150.000000 | 0.000000 | 117.127592 | 1,110.000000 | 96.932230 | b02136:lower |
| 112 | 480.521942 | 19.478058 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 578.961044 | 188.058673 | b02136:lower |
| 113 | 487.070356 | 12.929644 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 3.199406 | 0.000000 | 1,005.808734 | b02090:lower, b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g75_p150/nine_random_storage_06/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g75_p150/nine_random_storage_06/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
