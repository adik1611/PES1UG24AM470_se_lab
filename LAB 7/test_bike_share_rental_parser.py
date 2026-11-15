from hypothesis import given, strategies as st
from bike_share_rental_parser import parse_ride_duration, format_station_code, parse_ride_log

@given(st.text() | st.none())
def test_parse_ride_duration_no_crash(s):
    try:
        result = parse_ride_duration(s)
    except Exception as e:
        assert False, f"parse_ride_duration crashed on {s!r}: {type(e).__name__}: {e}"
    # A valid duration is a non-negative number of minutes; anything else must be None
    assert result is None or (isinstance(result, int) and result >= 0)

@given(st.text() | st.none())
def test_format_station_code_no_crash(s):
    try:
        result = format_station_code(s)
    except Exception as e:
        assert False, f"format_station_code crashed on {s!r}: {type(e).__name__}: {e}"
    # A valid code looks like 'A-12'; anything else must be None
    assert result is None or (isinstance(result, str) and result[1] == '-')

@given(st.text() | st.none())
def test_parse_ride_log_no_crash(s):
    try:
        result = parse_ride_log(s)
    except Exception as e:
        assert False, f"parse_ride_log crashed on {s!r}: {type(e).__name__}: {e}"
    # A valid log line becomes (str, int, bool); anything else must be None
    assert result is None or (
        isinstance(result, tuple)
        and len(result) == 3
        and isinstance(result[0], str)
        and isinstance(result[1], int)
        and isinstance(result[2], bool)
    )
