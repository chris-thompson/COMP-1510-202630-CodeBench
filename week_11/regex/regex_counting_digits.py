"""
Introducing Regex: anchoring with the caret ^ and the dollar sign $

The caret says "the match must start at the beginning of the text". The
dollar sign says "the match must end at the end of the text". Used together
they force the ENTIRE string to match, which is what validation almost
always wants.

^(\\d{1,3})(,\\d{3})*$ describes a number written with thousands separators:
one to three digits, then any number of groups of a comma and three more
digits. 1,000,000 passes. 1,00,000 does not.
"""

import re

SENTINEL = "quit"
GROUPED_DIGITS = re.compile(r"^(\d{1,3})(,\d{3})*$")


def is_grouped_number(text: str) -> bool:
    """
    Determine whether a string is a number written with comma separators.

    :param text: a string that may or may not be a grouped number
    :precondition: text must be a string
    :return: True if text is a correctly grouped number, otherwise False

    >>> is_grouped_number('1,000,000')
    True
    >>> is_grouped_number('42')
    True
    >>> is_grouped_number('1,00,000')
    False
    >>> is_grouped_number('the number is 1,000')
    False
    """
    return bool(GROUPED_DIGITS.search(text))


def main():
    """
    Drive the program.
    """
    print(f"Type {SENTINEL} to stop. Try 1,000,000 and then 1,00,000.")
    user_input = input("Enter a number with comma separators: ")
    while user_input != SENTINEL:
        if is_grouped_number(user_input):
            print("  Valid:", user_input)
        else:
            print("  Invalid. The anchors demand the WHOLE string match.")
        user_input = input("Enter a number with comma separators: ")


if __name__ == "__main__":
    main()
