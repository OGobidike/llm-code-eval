import pytest

from solution import letter_grade


@pytest.mark.parametrize(
    "score, grade",
    [(100, "A"), (90, "A"), (89.9, "B"), (80, "B"), (79, "C"), (70, "C"),
     (69, "D"), (60, "D"), (59.5, "F"), (0, "F"), (-5, "F")],
)
def test_same_behavior(score, grade):
    assert letter_grade(score) == grade
