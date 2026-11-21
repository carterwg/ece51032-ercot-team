# 500 MW at bus 6141, S1 generator 200 MW and battery 0 MW / 0 MWh

| Round | Our admitted MW | All teams admitted MW | Net score $B | IT value $B | Grid cost $B | Generator fuel $B | Generator capital $B | Battery capital $B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 500.000000 | 5,000.000000 | 17.862774 | 30.763287 | 0.000000 | 0.000513 | 0.400000 | 0.000000 |
| week-2-submission-2 | 500.000000 | 5,000.000000 | 17.133425 | 30.763287 | 0.000000 | 0.129862 | 1.000000 | 0.000000 |
| week-3-submission-1 | 500.000000 | 5,000.000000 | 17.298882 | 30.763287 | 0.563892 | 0.000513 | 0.400000 | 0.000000 |
| week-3-submission-2 | 500.000000 | 5,000.000000 | 16.137882 | 30.763287 | 0.995543 | 0.129862 | 1.000000 | 0.000000 |

| Round | Grid purchased MWh/yr | Generator MWh/yr | Battery charged MWh/yr | Battery discharged MWh/yr | Gen on h/yr | Discharge h/yr | Charge h/yr |
| --- | --- | --- | --- | --- | --- | --- | --- |
| week-2-submission-1 | 4,379,350.000 | 650.000 | 0.000 | 0.000 | 7.000 | 0.000 | 0.000 |
| week-2-submission-2 | 4,153,240.462 | 226,759.538 | 0.000 | 0.000 | 1,866.918 | 0.000 | 0.000 |
| week-3-submission-1 | 4,379,350.000 | 650.000 | 0.000 | 0.000 | 7.000 | 0.000 | 0.000 |
| week-3-submission-2 | 4,153,240.462 | 226,759.538 | 0.000 | 0.000 | 1,866.918 | 0.000 | 0.000 |

Four-round score **$68.432964B**. S2 uses a new 500 MW site with 500 MW generation at bus 6141 after carrying all teams’ actual S1 net withdrawals.

Battery discharge is shifted energy. Annual grid purchases include charging. The hours use representative-day weights.

Each of the nine rivals requests 500 MW split equally across 1079, 2054, with 160 MW of S1 generation and 145 MW / 580 MWh of S1 storage. The recorded S1 battery cycles were checked site by site.

| Round | Rival battery sites checked | Rival storage admitted MW | Rival batteries charged MWh/yr | Rival batteries discharged MWh/yr |
| --- | --- | --- | --- | --- |
| week-2-submission-1 | 18 | 1,305.000 | 2,270,931.888 | 2,270,931.888 |
| week-2-submission-2 | 0 | 0.000 | 0.000 | 0.000 |
| week-3-submission-1 | 18 | 1,305.000 | 2,270,931.888 | 2,270,931.888 |
| week-3-submission-2 | 0 | 0.000 | 0.000 | 0.000 |

## week-2-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02579:lower |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 385.012132 | b02579:lower |
| 106 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 148.005031 | 112.679659 | b02579:lower |
| 107 | 350.000000 | 150.000000 | 0.000000 | 0.000000 | 0.000000 | 16.559822 | 942.500000 | -0.000000 | none |
| 108 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 72.500000 | 1,140.694488 | -0.000000 | none |
| 109 | 350.000000 | 150.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,305.000000 | -0.000000 | none |
| 110 | 350.000000 | 150.000000 | 0.000000 | 0.000000 | 0.000000 | 217.500000 | 825.694488 | 0.000000 | none |
| 111 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 131.559822 | 797.500000 | -0.000000 | none |
| 112 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 498.725637 | 112.679659 | b02579:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 385.012132 | b02579:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-2-submission-2 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 560.821604 | b02579:lower |
| 105 | 0.202213 | 499.797787 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 384.809919 | b02579:lower |
| 106 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 112.679659 | b02579:lower |
| 107 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 108 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 109 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 110 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 111 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 112 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 112.679659 | b02579:lower |
| 113 | 0.202213 | 499.797787 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 384.809919 | b02579:lower |
| 114 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 560.821604 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-3-submission-1 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02579:lower |
| 105 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 385.012132 | b02579:lower |
| 106 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 148.005031 | 112.679659 | b02579:lower |
| 107 | 350.000000 | 150.000000 | 0.000000 | 0.000000 | 0.000000 | 16.559822 | 942.500000 | -0.000000 | none |
| 108 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 72.500000 | 1,140.694488 | -0.000000 | none |
| 109 | 350.000000 | 150.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,305.000000 | -0.000000 | none |
| 110 | 350.000000 | 150.000000 | 0.000000 | 0.000000 | 0.000000 | 217.500000 | 825.694488 | 0.000000 | none |
| 111 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 131.559822 | 797.500000 | -0.000000 | none |
| 112 | 450.000000 | 50.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 498.725637 | 112.679659 | b02579:lower |
| 113 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 385.012132 | b02579:lower |
| 114 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 1,009.008140 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

## week-3-submission-2 dispatch

| Hour | Grid MW | Our generator MW | Charge MW | Discharge MW | End SOC MWh | Rival charge MW | Rival discharge MW | All-team spare native generation MW | Binding lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 560.821604 | b02579:lower |
| 105 | 0.202213 | 499.797787 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 384.809919 | b02579:lower |
| 106 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 112.679659 | b02579:lower |
| 107 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 108 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 109 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 110 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 111 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | -0.000000 | none |
| 112 | 0.000000 | 500.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 112.679659 | b02579:lower |
| 113 | 0.202213 | 499.797787 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 384.809919 | b02579:lower |
| 114 | 375.000000 | 125.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 560.821604 | b02579:lower |

The hourly table shows dispatched power and lines at their limits. Storage feasibility depends on charge and discharge across the day.

[Full result](<../runs/battery-s1-500mw/campaign/g200_p0/nine_random_storage_08/attempt-01/result.json>) · [Solver audit](<../runs/battery-s1-500mw/campaign/g200_p0/nine_random_storage_08/attempt-01/execution.json>)

## Personal notes

<!-- USER_NOTES -->
