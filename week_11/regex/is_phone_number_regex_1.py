"""
Introducing Regex: the same job, in one line.

Everything the twenty-line function in is_phone_number.py does by hand, the
pattern \\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d does by description. We say what the
text should look like, and the re module works out how to check it.

Note the r before the pattern. The escape character in Python is the
backslash, and regular expressions are full of backslashes, so we hand the
compile function a raw string: a string prefaced with r, in which the
backslash is just a backslash.
"""

import re

SENTINEL = "quit"
PHONE_NUMBER_REGEX = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")


def find_phone_number(text: str) -> str | None:
    """
    Find a ten-digit phone number written with dashes anywhere in some text.

    Unlike is_phone_number.py, this searches: the number may be buried in
    the middle of a longer message.

    :param text: a string to search
    :precondition: text must be a string
    :return: the matched phone number as a string, or None if there is none

    >>> find_phone_number('415-555-4242')
    '415-555-4242'
    >>> find_phone_number('Call me at 604-555-1234 tonight')
    '604-555-1234'
    >>> find_phone_number('Moshi moshi')
    """
    match_object = PHONE_NUMBER_REGEX.search(text)
    if match_object:
        return match_object.group()
    return None


def main():
    """
    Drive the program.
    """
    print(f"Type {SENTINEL} to stop.")
    user_input = input("Enter a 10-digit phone number with dashes: ")
    while user_input != SENTINEL:
        number = find_phone_number(user_input)
        if number:
            print("The phone number you entered is:", number)
        else:
            print("That is not a phone number.")
        user_input = input("Enter a 10-digit phone number with dashes: ")


if __name__ == "__main__":
    main()
