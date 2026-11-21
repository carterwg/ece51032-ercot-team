# Intermediate runs and validation history

| Run | Recorded status | Meaning | Evidence |
| --- | --- | --- | --- |
| part1-stage1 | selection saved | candidate selection, no dispatch | [raw record](<../runs/part1-stage1>) |
| part1-initial-seven | complete | component evidence reused in final Part 1; no extra independent replication | [raw record](<../runs/part1-initial-seven>) |
| part1-extended-backgrounds | complete | component evidence reused in final Part 1; no extra independent replication | [raw record](<../runs/part1-extended-backgrounds>) |
| part1-failed-gurobi | failed | RuntimeError: independent solution checks failed: 0.00039463199294687, 2.0463630789890885e-12, 0.0 | [raw record](<../runs/part1-failed-gurobi>) |
| part2-cli-primary | selection saved | generated and validated CSV only; no scored game run | [raw record](<../runs/part2-cli-primary>) |
| part2-cli-benchmark | selection saved | generated and validated CSV only; no scored game run | [raw record](<../runs/part2-cli-benchmark>) |
| part2-scheduled-cli-s1 | selection saved | generated and validated CSV only; no scored game run | [raw record](<../runs/part2-scheduled-cli-s1>) |
| part2-scheduled-cli-s2 | selection saved | generated and validated CSV only; no scored game run | [raw record](<../runs/part2-scheduled-cli-s2>) |

Scores, value, energy, and generator hours are **not applicable** to candidate selection/CSV-only checks or physical grouping components. Failed solver attempts do not receive fabricated zero scores. The initial seven-background report and two-background extension feed the final nine-background Part 1 record; they are not counted twice. The recorded Gurobi failure is preserved, while the completed final analysis uses its documented accepted solver.

## Personal notes

<!-- USER_NOTES -->
