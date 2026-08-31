"""
Introducing Regex: grouping with parentheses.

Parentheses carve a pattern into numbered groups, and the Match object hands
each one back on request. Group 0 is the whole match; group 1 is the first
pair of parentheses; group 2 the second, and so on.

Watch the s. group() returns one string. groups() returns a tuple of all of
the numbered groups, and leaves out group 0.
"""

import re

PHONE_NUMBER_REGEX = re.compile(r"(\d{3})-(\d{3})-(\d{4})")


def split_phone_number(text: str) -> tuple | None:
    """
    Split a phone number into its area code, exchange, and subscriber number.

    :param text: a string to search
    :precondition: text must be a string
    :return: a tuple of the three parts as strings, or None if there is no
             phone number in text

    >>> split_phone_number('415-555-4242')
    ('415', '555', '4242')
    >>> split_phone_number('Call 604-555-1234 tonight')
    ('604', '555', '1234')
    >>> split_phone_number('Moshi moshi')
    """
    match_object = PHONE_NUMBER_REGEX.search(text)
    if match_object:
        return match_object.groups()
    return None


def main():
    """
    Drive the program.
    """
    user_input = input("Enter a 10-digit phone number with dashes: ")
    match_object = PHONE_NUMBER_REGEX.search(user_input)
    if match_object:
        print("The whole match, group():   ", match_object.group())
        print("The same thing, group(0):   ", match_object.group(0))
        print("Every group, groups():      ", match_object.groups())
        print("The area code, group(1):    ", match_object.group(1))
        print("The exchange, group(2):     ", match_object.group(2))
        print("The subscriber, group(3):   ", match_object.group(3))
    else:
        print("That is not a phone number.")


if __name__ == "__main__":
    main()
