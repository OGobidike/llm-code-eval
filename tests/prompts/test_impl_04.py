from solution import longest_unique_substring


def test_classic():
    assert longest_unique_substring("abcabcbb") == 3


def test_all_same():
    assert longest_unique_substring("bbbbb") == 1


def test_repeat_inside_window():
    assert longest_unique_substring("pwwkew") == 3


def test_jump_back():
    assert longest_unique_substring("abba") == 2


def test_empty():
    assert longest_unique_substring("") == 0


def test_long_input_is_fast():
    s = "ab" * 50_000 + "c"
    assert longest_unique_substring(s) == 3
