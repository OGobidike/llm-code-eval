import pytest

from solution import binary_search

NUMS = [1, 3, 5, 7, 9, 11]


@pytest.mark.parametrize("target, index", [(1, 0), (7, 3), (11, 5)])
def test_found(target, index):
    assert binary_search(NUMS, target) == index


@pytest.mark.parametrize("target", [0, 4, 12])
def test_missing(target):
    assert binary_search(NUMS, target) == -1


def test_empty():
    assert binary_search([], 3) == -1
