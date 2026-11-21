# 500 MW at bus 6141, S1 generator 200 MW and battery 0 MW / 0 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000000 | 5,000.000000 | 17.862908 | 30.763287 | 0.000000 | 0.000380 | 0.400000 | 0.000000 |
| week-2-submission-2 | 500.000000 | 5,000.000000 | 14.538766 | 30.763287 | 0.000000 | 2.724521 | 1.000000 | 0.000000 |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.276571 | 30.763287 | 0.586337 | 0.000380 | 0.400000 | 0.000000 |
| week-3-submission-2 | 500.000000 | 5,000.000000 | 12.967171 | 30.763287 | 1.571595 | 2.724521 | 1.000000 | 0.000000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,379,446.526 | 553.474 | 0.000 | 0.000 | 9.000 | 0.000 | 0.000 |
| week-2-submission-2 | 1,340,695.515 | 3,039,304.485 | 0.000 | 0.000 | 8,760.000 | 0.000 | 0.000 |
| week-3-submission-1 | 4,379,446.526 | 553.474 | 0.000 | 0.000 | 9.000 | 0.000 | 0.000 |
| week-3-submission-2 | 1,340,695.515 | 3,039,304.485 | 0.000 | 0.000 | 8,760.000 | 0.000 | 0.000 |

Four-round score **$62.645416B**. S2 uses a new 500 MW site with 500 MW generation at bus 6141 after carrying all teams’ actual S1 net withdrawals.

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 165 MW of S1 generation and 185 MW / 740 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-2-submission-1 | 9 | 1,665.000 | 4,186,003.631 | 4,186,003.631 |
| week-2-submission-2 | 0 | 0.000 | 0.000 | 0.000 |
| week-3-submission-1 | 9 | 1,665.000 | 4,186,003.631 | 4,186,003.631 |
| week-3-submission-2 | 0 | 0.000 | 0.000 | 0.000 |

## week-2-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |
| 105 | 468.078743 | 31.921257 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 562.854651 | 188.058673 | b02136:lower |
| 107 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,111.622408 | 96.932230 | b02136:lower |
| 108 | 350.000000 | 150.000000 | 0.000000 | 0.000000 | 0.000000 | 413.961045 | 1,028.053276 | 39.647743 | b02136:lower |
| 109 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,574.255025 | 20.109084 | b02136:lower |
| 110 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,456.592231 | 39.647743 | b02136:lower |
| 111 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,111.622408 | 96.932230 | b02136:lower |
| 112 | 410.368711 | 89.631289 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 228.961045 | 188.058673 | b02136:lower |
| 113 | 468.078743 | 31.921257 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 3.199407 | 0.000000 | 1,005.808733 | b02090:lower, b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-2-submission-2 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 24.196564 | 475.803436 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 767.042497 | b01921:upper, b02090:lower, b02136:lower |
| 105 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 107 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 96.932229 | b02136:lower |
| 108 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 109 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 20.109084 | b02136:lower |
| 110 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 111 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 96.932229 | b02136:lower |
| 112 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 23.876624 | 476.123376 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 767.042497 | b01921:upper, b02090:lower, b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-3-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |
| 105 | 468.078743 | 31.921257 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 562.854651 | 188.058673 | b02136:lower |
| 107 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,111.622408 | 96.932230 | b02136:lower |
| 108 | 350.000000 | 150.000000 | 0.000000 | 0.000000 | 0.000000 | 413.961045 | 1,028.053276 | 39.647743 | b02136:lower |
| 109 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,574.255025 | 20.109084 | b02136:lower |
| 110 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,456.592231 | 39.647743 | b02136:lower |
| 111 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,111.622408 | 96.932230 | b02136:lower |
| 112 | 410.368711 | 89.631289 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 228.961045 | 188.058673 | b02136:lower |
| 113 | 468.078743 | 31.921257 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 3.199407 | 0.000000 | 1,005.808733 | b02090:lower, b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-3-submission-2 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 24.196564 | 475.803436 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 767.042497 | b01921:upper, b02090:lower, b02136:lower |
| 105 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 107 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 96.932229 | b02136:lower |
| 108 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 109 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 20.109084 | b02136:lower |
| 110 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 39.647743 | b02136:lower |
| 111 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 96.932229 | b02136:lower |
| 112 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 113 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 23.876624 | 476.123376 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 767.042497 | b01921:upper, b02090:lower, b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/campaign/g200_p0/nine_random_storage_06/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/campaign/g200_p0/nine_random_storage_06/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
