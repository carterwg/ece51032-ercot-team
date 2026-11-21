# 500 MW at bus 6141, S1 generator 200 MW and battery 0 MW / 0 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000000 | 4,835.814984 | 17.861703 | 30.763287 | 0.000000 | 0.001585 | 0.400000 | 0.000000 |
| week-2-submission-2 | 500.000000 | 5,000.000000 | 14.708347 | 30.763287 | 0.000000 | 2.554941 | 1.000000 | 0.000000 |
| week-3-submission-1 | 500.000000 | 4,835.814984 | 17.279620 | 30.763287 | 0.582083 | 0.001585 | 0.400000 | 0.000000 |
| week-3-submission-2 | 500.000000 | 5,000.000000 | 13.029019 | 30.763287 | 1.679328 | 2.554941 | 1.000000 | 0.000000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,378,534.561 | 1,465.439 | 0.000 | 0.000 | 9.000 | 0.000 | 0.000 |
| week-2-submission-2 | 1,479,067.593 | 2,900,932.407 | 0.000 | 0.000 | 8,760.000 | 0.000 | 0.000 |
| week-3-submission-1 | 4,378,534.561 | 1,465.439 | 0.000 | 0.000 | 9.000 | 0.000 | 0.000 |
| week-3-submission-2 | 1,479,067.593 | 2,900,932.407 | 0.000 | 0.000 | 8,760.000 | 0.000 | 0.000 |

Four-round score **$62.878688B**. S2 uses a new 500 MW site with 500 MW generation at bus 6141 after carrying all teams’ actual S1 net withdrawals.

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 50 MW of S1 generation and 150 MW / 600 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-2-submission-1 | 9 | 1,300.744 | 3,144,106.581 | 3,144,106.581 |
| week-2-submission-2 | 0 | 0.000 | 0.000 | 0.000 |
| week-3-submission-1 | 9 | 1,300.744 | 3,144,106.581 | 3,144,106.581 |
| week-3-submission-2 | 0 | 0.000 | 0.000 | 0.000 |

## week-2-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,173.193156 | b02136:lower |
| 105 | 466.933513 | 33.066487 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 186.338137 | 188.058673 | b02136:lower |
| 107 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 735.105894 | 96.932230 | b02136:lower |
| 108 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 76.141613 | 1,156.217329 | 39.647743 | b02136:lower |
| 109 | 300.694457 | 199.305543 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,199.938487 | 20.109084 | b02136:lower |
| 110 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,080.075716 | 39.647743 | b02136:lower |
| 111 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 735.105894 | 96.932230 | b02136:lower |
| 112 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 186.338137 | 188.058673 | b02136:lower |
| 113 | 466.933513 | 33.066487 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,173.193156 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-2-submission-2 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 40.615066 | 459.384934 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 767.042497 | b01921:upper, b02090:lower, b02136:lower |
| 105 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 107 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 96.932229 | b02136:lower |
| 108 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 109 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 20.109084 | b02136:lower |
| 110 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 111 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 96.932229 | b02136:lower |
| 112 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 40.615066 | 459.384934 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 767.042497 | b01921:upper, b02090:lower, b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-3-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,173.193156 | b02136:lower |
| 105 | 466.933513 | 33.066487 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 186.338137 | 188.058673 | b02136:lower |
| 107 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 735.105894 | 96.932230 | b02136:lower |
| 108 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 76.141613 | 1,156.217329 | 39.647743 | b02136:lower |
| 109 | 300.694457 | 199.305543 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,199.938487 | 20.109084 | b02136:lower |
| 110 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,080.075716 | 39.647743 | b02136:lower |
| 111 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 735.105894 | 96.932230 | b02136:lower |
| 112 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 186.338137 | 188.058673 | b02136:lower |
| 113 | 466.933513 | 33.066487 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,173.193156 | b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-3-submission-2 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 40.615066 | 459.384934 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 767.042497 | b01921:upper, b02090:lower, b02136:lower |
| 105 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 107 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 96.932229 | b02136:lower |
| 108 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 109 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 20.109084 | b02136:lower |
| 110 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 111 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 96.932229 | b02136:lower |
| 112 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 40.615066 | 459.384934 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 767.042497 | b01921:upper, b02090:lower, b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/campaign/g200_p0/nine_g50_b150_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/campaign/g200_p0/nine_g50_b150_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
