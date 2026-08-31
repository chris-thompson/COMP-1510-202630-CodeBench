"""
Introducing Regex: the pipe inside a group

Putting the pipe inside parentheses lets the alternatives share everything
around them. Bat(mobile|copter|bat|submarine) is a much shorter way of
writing Batmobile|Batcopter|Batbat|Batsubmarine, and there is only one place
to fix when the prefix changes.
"""

import re

SENTINEL = "quit"
GADGET_REGEX = re.compile(r"Bat(mobile|copter|bat|submarine)")


def find_gadget(text: str) -> str | None:
    """
    Find the first Bat-gadget named anywhere in some text.

    :param text: a string to search
    :precondition: text must be a string
    :return: the matched gadget as a string, or None if there is no match

    >>> find_gadget("The Batmobile is parked outside")
    'Batmobile'
    >>> find_gadget("Batsubmarine")
    'Batsubmarine'
    >>> find_gadget("Batplane")
    """
    match_object = GADGET_REGEX.search(text)
    if match_object:
        return match_object.group()
    return None


def main():
    """
    Drive the program.
    """
    print(f"Type {SENTINEL} to stop.")
    user_input = input("Enter your favourite bat gadget: ")
    while user_input != SENTINEL:
        gadget = find_gadget(user_input)
        if gadget:
            print("The gadget you entered is:", gadget)
        else:
            print("Not acceptable.")
        user_input = input("Enter your favourite bat gadget: ")


if __name__ == "__main__":
    main()
