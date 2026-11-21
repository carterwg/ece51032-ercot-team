# 500 MW at bus 6141, S1 generator 75 MW and battery 150 MW / 600 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.316721 | 30.763287 | 0.586153 | 0.000413 | 0.150000 | 0.210000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,379,540.802 | 459.198 | 415,467.544 | 415,467.544 | 9.000 | 3,090.532 | 3,089.529 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 85 MW of S1 generation and 155 MW / 620 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,395.000 | 3,290,138.817 | 3,290,138.817 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 300.000 | 300.000 | -0.000 | 600.000 | 1,162.134 | 1,162.134 |
| 2 | 300.000 | 300.000 | 47.628 | 600.000 | 1,414.221 | 1,414.221 |
| 3 | 300.000 | 300.000 | 300.000 | 600.000 | 1,186.670 | 1,186.670 |
| 4 | 300.000 | 300.000 | 0.000 | 600.000 | 798.529 | 798.529 |
| 5 | 300.000 | 300.000 | -0.000 | 600.000 | 815.868 | 815.868 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 650.000000 | 0.000000 | 150.000000 | 0.000000 | 450.000000 | 608.311199 | 465.000000 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 2 | 350.000000 | 0.000000 | 0.000000 | 150.000000 | 450.000000 | 753.311199 | 310.000000 | 14,429.312268 | b01919:lower, b01921:upper, b02355:lower |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |
| 105 | 475.987805 | 24.012195 | 0.000000 | 0.000000 | 600.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 421.772940 | 56.250000 | 0.000000 | 21.977060 | 578.022940 | 0.000000 | 332.127592 | 188.058673 | b02136:lower |
| 107 | 293.750000 | 56.250000 | 0.000000 | 150.000000 | 428.022940 | 22.127592 | 775.000000 | 96.932230 | b02136:lower |
| 108 | 276.326464 | 73.673536 | 0.000000 | 150.000000 | 278.022940 | 27.301376 | 930.000000 | 39.647743 | b02136:lower |
| 109 | 318.244975 | 56.250000 | 0.000000 | 125.505025 | 152.517915 | 0.000000 | 1,240.000000 | 20.109084 | b02136:lower |
| 110 | 435.907769 | 56.250000 | 0.000000 | 7.842231 | 144.675684 | 0.000000 | 1,240.000000 | 39.647743 | b02136:lower |
| 111 | 299.074316 | 56.250000 | 0.000000 | 144.675684 | -0.000000 | 155.000000 | 913.196724 | 96.932230 | b02136:lower |
| 112 | 443.750000 | 56.250000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 354.104651 | 188.058673 | b02136:lower |
| 113 | 475.987805 | 24.012195 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g75_p150/nine_random_storage_03/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g75_p150/nine_random_storage_03/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
