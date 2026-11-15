# ece51032-ercot-team

Private repository for the ECE51032 project.

- `analysis/`: team bus-screening and hosting-capacity results.
- `ercot-connection-game/`: complete course repository, imported as a Git subtree.
  See its [README](ercot-connection-game/README.md) and
  [tutorial](ercot-connection-game/docs/student_tutorial/tutorial.pdf).

Run course commands from `ercot-connection-game/` so that data paths resolve:

```bash
cd ercot-connection-game
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[tutorial,test]" pandas
ercot-game-check-csv --file examples/eight_team_round/submissions/team-01.csv
```

The course files were imported from
[MhaoMou/ercot-connection-game](https://github.com/MhaoMou/ercot-connection-game)
at commit `b3b04c8a751d029506a49125b5c32fe93404d7dc` on November 15, 2026.
The source-code and course-material licenses remain in the imported directory.
All course files are tracked directly in this repository; cloning the team
repository also retrieves them.

To import future course updates, run from the team repository root on your
working branch, then review and test the changes:

```bash
git subtree pull --prefix=ercot-connection-game https://github.com/MhaoMou/ercot-connection-game.git main --squash
```
