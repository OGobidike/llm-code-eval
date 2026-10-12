from solution import remove_low_stock


def test_removes_low_items():
    stock = {"apples": 2, "pears": 10, "plums": 0}
    assert remove_low_stock(stock, 3) == {"pears": 10}


def test_returns_same_dict():
    stock = {"a": 1, "b": 5}
    assert remove_low_stock(stock, 2) is stock


def test_nothing_to_remove():
    assert remove_low_stock({"a": 5}, 1) == {"a": 5}
