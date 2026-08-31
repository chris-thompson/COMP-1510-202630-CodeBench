"""
Introducing Regex: choose between patterns with the pipe |

The pipe means "or". A regex holding a pipe matches the pattern on its left
or the pattern on its right. When both could match, the regex returns the
one that appears FIRST in the searched text, not the one written first in
the pattern.

Tina Fey wrote Mean Girls, one of the funniest movies ever.
"""

import re

SENTINEL = "quit"
HEROES_REGEX = re.compile(r"Batman|Tina Fey")


def find_hero(text: str) -> str | None:
    """
    Find the first of our two heroes named anywhere in some text.

    :param text: a string to search
    :precondition: text must be a string
    :return: the matched hero's name as a string, or None if neither appears

    >>> find_hero("My hero is Batman")
    'Batman'
    >>> find_hero("My hero is Tina Fey")
    'Tina Fey'
    >>> find_hero("Tina Fey and Batman")
    'Tina Fey'
    >>> find_hero("Superman")
    """
    match_object = HEROES_REGEX.search(text)
    if match_object:
        return match_object.group()
    return None


def main():
    """
    Drive the program.
    """
    print(f"Type {SENTINEL} to stop.")
    user_input = input("Enter your hero(es): ")
    while user_input != SENTINEL:
        hero = find_hero(user_input)
        if hero:
            # Only the first match, even when both heroes are named.
            print("The hero you entered is:", hero)
        else:
            print("Not acceptable.")
        user_input = input("Enter your hero(es): ")


if __name__ == "__main__":
    main()
