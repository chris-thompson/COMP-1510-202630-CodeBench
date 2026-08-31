"""
Unit-test a function that reads user input, using pytest.

The function calls the built-in input function, which would normally pause
and wait for a human to type. We use the built-in monkeypatch fixture to
replace builtins.input with a function that returns a fixed string, so the
test runs to completion without any human interaction.
"""

from week_06 import user_input


def test_ask_for_value_and_convert_to_upper(monkeypatch):
    def fake_input(prompt=""):
        return "2qt4wrdz"

    monkeypatch.setattr("builtins.input", fake_input)
    assert user_input.ask_for_value_and_convert_to_upper() == "2QT4WRDZ"
