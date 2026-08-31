"""
Unit-test the square function with pytest.

pytest discovers any file named test_*.py and any function named test_*
inside it. A test is just a function that makes one assertion. When an
assertion fails, pytest shows developers the actual and expected values
for us, so a plain assertion is all we need.
"""

from week_04.square import square


def test_square_positive_integer():
    assert square(2) == 4


def test_square_negative_integer():
    assert square(-2) == 4


def test_square_zero():
    assert square(0) == 0


def test_square_positive_float():
    assert square(1.5) == 2.25


def test_square_negative_float():
    assert square(-1.5) == 2.25
