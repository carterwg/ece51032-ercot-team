# 500 MW at bus 6141, S1 generator 200 MW and battery 0 MW / 0 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000000 | 5,000.000000 | 17.862135 | 30.763287 | 0.000000 | 0.001152 | 0.400000 | 0.000000 |
| week-2-submission-2 | 500.000000 | 5,000.000000 | 14.541985 | 30.763287 | 0.000000 | 2.721302 | 1.000000 | 0.000000 |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.271596 | 30.763287 | 0.590540 | 0.001152 | 0.400000 | 0.000000 |
| week-3-submission-2 | 500.000000 | 5,000.000000 | 12.982844 | 30.763287 | 1.559141 | 2.721302 | 1.000000 | 0.000000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,378,759.451 | 1,240.549 | 0.000 | 0.000 | 9.000 | 0.000 | 0.000 |
| week-2-submission-2 | 1,341,538.912 | 3,038,461.088 | 0.000 | 0.000 | 8,760.000 | 0.000 | 0.000 |
| week-3-submission-1 | 4,378,759.451 | 1,240.549 | 0.000 | 0.000 | 9.000 | 0.000 | 0.000 |
| week-3-submission-2 | 1,341,538.912 | 3,038,461.088 | 0.000 | 0.000 | 8,760.000 | 0.000 | 0.000 |

Four-round score **$62.658560B**. S2 uses a new 500 MW site with 500 MW generation at bus 6141 after carrying all teams’ actual S1 net withdrawals.

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 6141, with 100 MW of S1 generation and 125 MW / 500 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-2-submission-1 | 9 | 1,125.000 | 2,550,876.501 | 2,550,876.501 |
| week-2-submission-2 | 0 | 0.000 | 0.000 | 0.000 |
| week-3-submission-1 | 9 | 1,125.000 | 2,550,876.501 | 2,550,876.501 |
| week-3-submission-2 | 0 | 0.000 | 0.000 | 0.000 |

## week-2-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |
| 105 | 451.102439 | 48.897561 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 321.071882 | 178.928118 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 107 | 350.000000 | 150.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 707.872408 | 96.932230 | b02136:lower |
| 108 | 344.448376 | 155.551624 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,022.308301 | 39.647743 | b02136:lower |
| 109 | 341.726359 | 158.273641 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,125.000000 | 20.109084 | b02136:lower |
| 110 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 777.842231 | 39.647743 | b02136:lower |
| 111 | 350.000000 | 150.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 707.872408 | 96.932230 | b02136:lower |
| 112 | 350.000000 | 150.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 159.104651 | 188.058673 | b02136:lower |
| 113 | 451.102439 | 48.897561 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |

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
| 114 | 24.196564 | 475.803436 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 767.042497 | b01921:upper, b02090:lower, b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-3-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |
| 105 | 451.102439 | 48.897561 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 106 | 321.071882 | 178.928118 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 188.058673 | b02136:lower |
| 107 | 350.000000 | 150.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 707.872408 | 96.932230 | b02136:lower |
| 108 | 344.448376 | 155.551624 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,022.308301 | 39.647743 | b02136:lower |
| 109 | 341.726359 | 158.273641 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,125.000000 | 20.109084 | b02136:lower |
| 110 | 300.000000 | 200.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 777.842231 | 39.647743 | b02136:lower |
| 111 | 350.000000 | 150.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 707.872408 | 96.932230 | b02136:lower |
| 112 | 350.000000 | 150.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 159.104651 | 188.058673 | b02136:lower |
| 113 | 451.102439 | 48.897561 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 306.816946 | b02136:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02136:lower |

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
| 114 | 24.196564 | 475.803436 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 767.042497 | b01921:upper, b02090:lower, b02136:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/campaign/g200_p0/nine_g100_b125_at_6141/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/campaign/g200_p0/nine_g100_b125_at_6141/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
