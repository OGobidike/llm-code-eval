from solution import average


def test_normal():
    assert average([2, 4, 6]) == 4


def test_empty_returns_none():
    assert average([]) is None


def test_single():
    assert average([5]) == 5
