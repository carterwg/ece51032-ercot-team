from itertools import product

import pytest

from team_strategy.experiments.battery_s1_optimization import (
    FIELDS, ROOT, adversarial_fields, colocalized_award, hosting_profile, prior_fields, read,
    storage_envelope, validation_fields,
)


def test_adversarial_grid_shares_one_field_with_the_existing_set():
    config = read(ROOT / FIELDS)
    adverse = adversarial_fields(config)
    equipment = {
        (round(500 * field['rival_plan']['generation_schedule']['1']),
         field['rival_plan']['storage_power_schedule']['1'])
        for field in adverse
    }
    assert equipment == set(product((50, 75, 100, 125), (125, 150, 175, 200)))
    assert len(adverse) == 16
    assert len(prior_fields(config)) == 21
    assert len(validation_fields(config)) == 36


def test_colocated_screen_respects_daily_exact_cycle():
    pytest.importorskip('highspy')
    # A single hour has ample support from storage. With constant grid limits,
    # a full day cannot be covered by discharging that same stored energy.
    envelope = storage_envelope([4000.] * 24)
    assert colocalized_award((100, 0), (100, 0), envelope) == 500
    assert colocalized_award((0, 200), (0, 200), envelope) == pytest.approx(399.96, abs=.0001)


def test_colocated_screen_reproduces_the_existing_reduced_award():
    pytest.importorskip('highspy')
    config = read(ROOT / FIELDS)
    envelope = storage_envelope(hosting_profile(config))
    assert colocalized_award((75, 150), (75, 125), envelope) == pytest.approx(499.937843788, abs=1e-6)
