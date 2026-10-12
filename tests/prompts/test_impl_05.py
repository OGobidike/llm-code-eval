import pytest

from solution import parse_duration


@pytest.mark.parametrize(
    "text, seconds",
    [("1h30m", 5400), ("45s", 45), ("2h5s", 7205), ("1h1m1s", 3661), ("0s", 0)],
)
def test_valid(text, seconds):
    assert parse_duration(text) == seconds


@pytest.mark.parametrize("text", ["", "abc", "5", "1m1h", "1h1h", "-5s", "1.5h"])
def test_invalid_raises(text):
    with pytest.raises(ValueError):
        parse_duration(text)
