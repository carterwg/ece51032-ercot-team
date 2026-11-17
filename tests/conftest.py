from pathlib import Path

import pytest

from team_strategy.context import load_context
from team_strategy.contracts import RoundKey

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "ercot-connection-game"
RELEASE = ROOT / "configs/rounds/finalized_release_500mw.json"
DEMO = COURSE / "data/teaching/ieee14_demo_representative"
DEMO_RULES = COURSE / "data/teaching/dispatch_scoring_rules_ieee14_demo_representative_v1.json"


@pytest.fixture
def context():
    return load_context(
        release_file=RELEASE, round=RoundKey(2, 1), team_id="team-test",
        scenario_dir=DEMO, rules_file=DEMO_RULES,
    )


@pytest.fixture
def carried_scenario(tmp_path):
    from ercot_game.base_load import materialize_base_load_artifact

    output = tmp_path / "carried"
    materialize_base_load_artifact(DEMO, {}, output, validate=False)
    return output
