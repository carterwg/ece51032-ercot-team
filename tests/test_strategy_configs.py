"""Named full-network configurations share the same legality contract."""

import json

import pytest

from team_strategy.context import load_context
from team_strategy.contracts import RoundKey
from team_strategy.strategies import build_strategy
from team_strategy.validation import validate_plan

from conftest import RELEASE, ROOT


@pytest.mark.parametrize(
    "config_file", sorted((ROOT / "configs/strategies").glob("*.json")),
    ids=lambda path: path.stem,
)
def test_named_configuration_on_active_network(config_file):
    config = json.loads(config_file.read_text())
    context = load_context(release_file=RELEASE, round=RoundKey(2, 1), team_id="team-test")
    strategy = build_strategy(config["strategy"], config["params"])
    plan = strategy.propose(context)
    assert plan == strategy.propose(context)
    assert validate_plan(plan, context).valid
    if config_file.stem == "carter_rank1_cg":
        assert len(plan.sites) == 1
        site = plan.sites[0]
        assert site.bus_id == "6141"
        assert site.connection_mw == site.generator_mw == context.connection_budget_mw
        assert site.storage_power_mw == site.storage_energy_mwh == 0
