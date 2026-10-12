from solution import is_anagram


def test_example():
    assert is_anagram("Dormitory", "dirty room") is True


def test_not_anagram():
    assert is_anagram("hello", "world") is False


def test_different_counts():
    assert is_anagram("aab", "abb") is False


def test_empty_strings():
    assert is_anagram("", "") is True
