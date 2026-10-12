from solution import csv_line


def test_mixed_values():
    assert csv_line([1, "a", 2.5]) == "1,a,2.5"


def test_single():
    assert csv_line(["x"]) == "x"


def test_empty():
    assert csv_line([]) == ""


def test_tuple_input():
    assert csv_line((1, 2)) == "1,2"
