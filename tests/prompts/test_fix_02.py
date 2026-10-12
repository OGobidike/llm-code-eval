from solution import add_tag


def test_calls_are_independent():
    assert add_tag("a") == ["a"]
    assert add_tag("b") == ["b"]


def test_existing_list_is_used():
    tags = ["x"]
    assert add_tag("y", tags) == ["x", "y"]
