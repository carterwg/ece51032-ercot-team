# 500 MW at bus 6141, S1 generator 145 MW and battery 10 MW / 40 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 384.852389 | 4,598.154507 | 13.377169 | 23.678649 | 0.445317 | 0.000863 | 0.223214 | 0.010776 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 3,370,526.185 | 780.742 | 19,658.239 | 19,658.239 | 7.000 | 2,553.997 | 2,553.997 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 50 MW of S1 generation and 125 MW / 500 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-3-submission-1 | 9 | 1,053.326 | 2,342,057.386 | 2,342,057.386 |

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 15.394 | 15.394 | -0.000 | 30.788 | 46.182 | 46.182 |
| 2 | 15.394 | 15.394 | -0.000 | 30.788 | 61.576 | 61.576 |
| 3 | 15.394 | 15.394 | -0.000 | 30.788 | 61.576 | 61.576 |
| 4 | 15.394 | 15.394 | -0.000 | 30.788 | 46.182 | 46.182 |
| 5 | 15.394 | 15.394 | -0.000 | 30.788 | 38.485 | 38.485 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 392.549437 | 0.000000 | 7.697048 | 0.000000 | 23.091143 | 702.217020 | 285.666233 | 14,700.221125 | b01921:upper, b02355:lower |
| 3 | 377.155341 | 0.000000 | 0.000000 | 7.697048 | 23.091143 | 464.714148 | 117.036170 | 14,382.233739 | b01921:upper, b02355:lower |
| 104 | 384.852389 | 0.000000 | 0.000000 | 0.000000 | 30.788191 | 0.000000 | 0.000000 | 1,410.853633 | b02136:lower |
| 105 | 384.852389 | 0.000000 | 0.000000 | 0.000000 | 30.788191 | 0.000000 | 0.000000 | 439.725851 | b02136:lower |
| 106 | 273.245196 | 111.607193 | 0.000000 | 0.000000 | 30.788191 | 0.000000 | 49.321754 | 188.058673 | b02136:lower |
| 107 | 265.548148 | 111.607193 | 0.000000 | 7.697048 | 23.091143 | 0.000000 | 590.392463 | 96.932230 | b02136:lower |
| 108 | 265.548148 | 111.607193 | 0.000000 | 7.697048 | 15.394096 | 0.000000 | 935.362286 | 39.647743 | b02136:lower |
| 109 | 265.548148 | 111.607193 | 0.000000 | 7.697048 | 7.697048 | 0.000000 | 1,053.025080 | 20.109084 | b02136:lower |
| 110 | 273.245196 | 111.607193 | 0.000000 | 0.000000 | 7.697048 | 0.000000 | 943.059333 | 39.647743 | b02136:lower |
| 111 | 266.056405 | 111.098936 | 0.000000 | 7.697048 | -0.000000 | 0.000000 | 592.819449 | 96.932230 | b02136:lower |
| 112 | 273.245196 | 111.607193 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 49.321754 | 188.058673 | b02136:lower |
| 113 | 384.852389 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 439.725851 | b02136:lower |
| 114 | 384.852389 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | 0.000000 | 0.000000 | 1,410.853633 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g145_p10/nine_g50_b125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g145_p10/nine_g50_b125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
