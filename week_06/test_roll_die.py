"""
Unit-test roll_die with pytest.

roll_die uses random.randint, so most tests can only assert that the result
falls inside the expected range. The final test shows how to make the
randomness predictable with the built-in monkeypatch fixture: we replace
random.randint with a function that always returns the same value. The test
then becomes deterministic, so it checks our logic instead of the random
module's output.
"""

from week_06 import roll_die


def test_roll_one_sided_die_once():
    assert roll_die.roll_die(1, 1) == 1


def test_roll_six_sided_die_once():
    assert 1 <= roll_die.roll_die(1, 6) <= 6


def test_roll_six_sided_die_twice():
    assert 2 <= roll_die.roll_die(2, 6) <= 12


def test_roll_ten_sided_die_ten_times():
    assert 10 <= roll_die.roll_die(10, 10) <= 100


def test_roll_die_with_predictable_randint(monkeypatch):
    def fake_randint(low, high):
        return 5

    monkeypatch.setattr("random.randint", fake_randint)
    assert roll_die.roll_die(3, 3) == 5
