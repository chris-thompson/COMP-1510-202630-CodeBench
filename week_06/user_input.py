"""
Demonstrate a function that depends on the built-in input function.

Run this function and it pauses, waiting for a human to type. How can
we unit test that? test_user_input.py shows how the monkeypatch fixture
replaces input with a predictable fake.
"""


def ask_for_value_and_convert_to_upper():
    """
    Ask the user for a value and return it stripped and converted to uppercase.

    :postcondition: prompts the user for input on standard output
    :return: the user's input as a string, stripped of surrounding
             whitespace and converted to uppercase
    """
    return input("Enter your name please").strip().upper()
