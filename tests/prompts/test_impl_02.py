from solution import merge_intervals


def test_overlapping():
    assert merge_intervals([[1, 3], [2, 6], [8, 10]]) == [[1, 6], [8, 10]]


def test_touching_merge():
    assert merge_intervals([[1, 3], [3, 5]]) == [[1, 5]]


def test_unsorted_input():
    assert merge_intervals([[8, 10], [1, 3], [2, 4]]) == [[1, 4], [8, 10]]


def test_contained_interval():
    assert merge_intervals([[1, 10], [2, 3]]) == [[1, 10]]


def test_empty():
    assert merge_intervals([]) == []


def test_input_not_modified():
    data = [[5, 6], [1, 2]]
    merge_intervals(data)
    assert data == [[5, 6], [1, 2]]
