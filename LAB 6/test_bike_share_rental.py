import pytest
from bike_share_rental import ride_cost, dock_status, can_unlock

#Example test cases:
def test_standard_ride():
    assert ride_cost("standard", 45, False, False) == 40

def test_dock_available():
    assert dock_status(5, 10) == "available"

#Write the rest of the test cases so that the code is 90- 100% covered.


# ---------------------------------------------------------------------------
# ride_cost
# ---------------------------------------------------------------------------

def test_ride_cost_unknown_bike_type():
    with pytest.raises(ValueError, match="unknown bike type"):
        ride_cost("tandem", 30, False, False)


def test_ride_cost_zero_minutes():
    with pytest.raises(ValueError, match="invalid duration"):
        ride_cost("standard", 0, False, False)


def test_ride_cost_negative_minutes():
    with pytest.raises(ValueError, match="invalid duration"):
        ride_cost("electric", -10, False, False)


def test_ride_cost_subscriber_first_block_free():
    # 30 min = 1 block, subscriber gets 1 block free -> 0 blocks -> free ride
    assert ride_cost("standard", 30, True, False) == 0


def test_ride_cost_subscriber_free_ignores_peak():
    # free ride returns early, so the peak surcharge is never added
    assert ride_cost("electric", 20, True, True) == 0


def test_ride_cost_subscriber_multiple_blocks():
    # 90 min = 3 blocks, minus 1 free = 2 blocks * 35
    assert ride_cost("electric", 90, True, False) == 70


def test_ride_cost_block_rounding_up():
    # 31 min rounds up to 2 blocks
    assert ride_cost("standard", 31, False, False) == 40


def test_ride_cost_peak_standard_surcharge():
    # 30 min = 1 block * 20 + 15 peak
    assert ride_cost("standard", 30, False, True) == 35


def test_ride_cost_peak_electric_surcharge():
    assert ride_cost("electric", 60, False, True) == 2 * 35 + 15


def test_ride_cost_peak_cargo_no_surcharge():
    # cargo bikes are exempt from the peak surcharge
    assert ride_cost("cargo", 30, False, True) == 50


def test_ride_cost_cargo_off_peak():
    assert ride_cost("cargo", 60, False, False) == 100


def test_ride_cost_exactly_180_minutes_no_long_ride_fee():
    # boundary: 180 is NOT > 180
    assert ride_cost("standard", 180, False, False) == 6 * 20


def test_ride_cost_long_ride_fee():
    # 181 min = 7 blocks * 20 + 100 long-ride fee
    assert ride_cost("standard", 181, False, False) == 7 * 20 + 100


def test_ride_cost_all_surcharges_combined():
    # 200 min = 7 blocks, subscriber -> 6 blocks * 35 + 15 peak + 100 long
    assert ride_cost("electric", 200, True, True) == 6 * 35 + 15 + 100


# ---------------------------------------------------------------------------
# dock_status
# ---------------------------------------------------------------------------

def test_dock_zero_capacity():
    with pytest.raises(ValueError, match="invalid capacity"):
        dock_status(0, 0)


def test_dock_negative_capacity():
    with pytest.raises(ValueError, match="invalid capacity"):
        dock_status(0, -5)


def test_dock_negative_bikes():
    with pytest.raises(ValueError, match="invalid bike count"):
        dock_status(-1, 10)


def test_dock_more_bikes_than_capacity():
    with pytest.raises(ValueError, match="invalid bike count"):
        dock_status(11, 10)


def test_dock_empty():
    assert dock_status(0, 10) == "empty"


def test_dock_full():
    assert dock_status(10, 10) == "full"


def test_dock_few_bikes():
    assert dock_status(2, 10) == "few bikes"


def test_dock_one_bike():
    assert dock_status(1, 10) == "few bikes"


def test_dock_few_slots():
    assert dock_status(8, 10) == "few slots"


def test_dock_one_slot_left():
    assert dock_status(9, 10) == "few slots"


def test_dock_available_boundary():
    # 3 bikes, 3 free slots -> neither "few" rule applies
    assert dock_status(3, 6) == "available"


# ---------------------------------------------------------------------------
# can_unlock
# ---------------------------------------------------------------------------

def test_unlock_blocked_by_active_ride():
    assert can_unlock(1000, True, 30) is False


def test_unlock_under_16():
    assert can_unlock(1000, False, 15) is False


def test_unlock_teen_enough_balance():
    assert can_unlock(100, False, 16) is True


def test_unlock_teen_low_balance():
    assert can_unlock(99, False, 17) is False


def test_unlock_adult_enough_balance():
    assert can_unlock(50, False, 18) is True


def test_unlock_adult_low_balance():
    assert can_unlock(49, False, 40) is False
