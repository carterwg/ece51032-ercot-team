# 500 MW at bus 6141, S1 generator 100 MW and battery 95 MW / 380 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 499.152164 | 4,999.152164 | 17.285250 | 30.711123 | 0.613771 | 0.000863 | 0.199661 | 0.132774 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-3-submission-1 | 4,371,448.928 | 1,124.031 | 236,915.307 | 236,915.307 | 106.732 | 3,313.912 | 3,661.959 |

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

## week-3-submission-1 dispatch

| Day | Start SOC MWh | End SOC MWh | Minimum SOC MWh | Maximum SOC MWh | Charged MWh | Discharged MWh |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 189.678 | 189.678 | 0.000 | 379.356 | 527.662 | 527.662 |
| 2 | 189.678 | 189.678 | 0.000 | 379.356 | 731.898 | 731.898 |
| 3 | 189.678 | 189.678 | 0.000 | 379.356 | 688.058 | 688.058 |
| 4 | 189.678 | 189.678 | 0.000 | 379.356 | 637.402 | 637.402 |
| 5 | 189.678 | 189.678 | 0.000 | 379.356 | 477.215 | 477.215 |

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 11 | 404.313253 | 0.000000 | 0.000000 | 94.838911 | 284.516734 | 7,441.862236 | b01921:upper, b02090:lower, b02355:lower |
| 23 | 593.991075 | 0.000000 | 94.838911 | 0.000000 | 189.677822 | 14,226.378101 | b01921:upper, b02355:lower |
| 104 | 499.152164 | 0.000000 | 0.000000 | 0.000000 | 379.355645 | 1,009.855976 | b02136:lower |
| 105 | 485.064899 | 14.087266 | 0.000000 | 0.000000 | 379.355645 | 306.816946 | b02136:lower |
| 106 | 447.484946 | 51.667218 | 0.000000 | 0.000000 | 379.355645 | 188.058673 | b02136:lower |
| 107 | 418.648834 | 80.503330 | 0.000000 | 0.000000 | 379.355645 | 96.932230 | b02136:lower |
| 108 | 310.666288 | 93.646965 | 0.000000 | 94.838911 | 284.516734 | 39.647743 | b02136:lower |
| 109 | 304.483459 | 99.829794 | 0.000000 | 94.838911 | 189.677822 | 20.109084 | b02136:lower |
| 110 | 310.666288 | 93.646965 | 0.000000 | 94.838911 | 94.838911 | 39.647743 | b02136:lower |
| 111 | 328.793425 | 75.519828 | 0.000000 | 94.838911 | 0.000000 | 96.932230 | b02136:lower |
| 112 | 447.484946 | 51.667218 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 485.064899 | 14.087266 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 499.152164 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.855976 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/sweep/g100_p95/nine_g200_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/sweep/g100_p95/nine_g200_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
