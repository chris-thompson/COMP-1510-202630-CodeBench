"""
Unit-test function_can_throw with pytest, including the exception it raises.

Everything we already know still applies: pytest discovers any file named
test_*.py and any function named test_* inside it, and each test makes
exactly one check.

The new idea is in the last three tests. function_can_throw promises, in its
docstring, to raise a ValueError when it is given something that is not a
positive integer. A promise in a docstring is part of the function's
contract, so we have to prove the function keeps it. We cannot use a plain
assert for this, because the exception would end the test before the assert
ever ran. Instead we import pytest and use pytest.raises as a context
manager:

    with pytest.raises(SomeException):
        do_something()

The block passes if the code inside it raises that exception, and fails if
it raises nothing or raises something else. That single 'with' is the whole
check, so it counts as this test's one assertion.
"""

import pytest

from week_09.exceptions import exceptions_102


def test_factorial_of_zero_is_one():
    assert exceptions_102.function_can_throw(0) == 1


def test_factorial_of_one_is_one():
    assert exceptions_102.function_can_throw(1) == 1


def test_factorial_of_small_positive_integer():
    assert exceptions_102.function_can_throw(5) == 120


def test_factorial_of_larger_positive_integer():
    assert exceptions_102.function_can_throw(10) == 3628800


def test_negative_integer_raises_value_error():
    with pytest.raises(ValueError):
        exceptions_102.function_can_throw(-1)


def test_string_raises_value_error():
    with pytest.raises(ValueError):
        exceptions_102.function_can_throw('a')


def test_float_raises_value_error():
    with pytest.raises(ValueError):
        exceptions_102.function_can_throw(3.5)
