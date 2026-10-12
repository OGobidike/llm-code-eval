from solution import flatten


def test_example():
    assert flatten([1, [2, (3, "ab")], [[4]]]) == [1, 2, 3, "ab", 4]


def test_already_flat():
    assert flatten([1, 2, 3]) == [1, 2, 3]


def test_empty_nested():
    assert flatten([[], [[]], ()]) == []


def test_deep():
    assert flatten([[[[[["x"]]]]]]) == ["x"]
