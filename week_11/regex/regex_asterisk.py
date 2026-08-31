"""
Introducing Regex: match zero or more with the asterisk *

The asterisk applies to the group immediately before it and means "any
number of times, including no times at all". Bat(wo)*man therefore matches
Batman, Batwoman, Batwowoman, and so on forever.
"""

import re

SENTINEL = "quit"
BATMAN_REGEX = re.compile(r"Bat(wo)*man")


def find_bat_hero(text: str) -> str | None:
    """
    Find the first member of the Bat-clan named anywhere in some text.

    :param text: a string to search
    :precondition: text must be a string
    :return: the matched name as a string, or None if there is no match

    >>> find_bat_hero("Batman")
    'Batman'
    >>> find_bat_hero("I choose Batwowowoman today")
    'Batwowowoman'
    >>> find_bat_hero("Superman")
    """
    match_object = BATMAN_REGEX.search(text)
    if match_object:
        return match_object.group()
    return None


def main():
    """
    Drive the program.
    """
    print(f"Type {SENTINEL} to stop.")
    user_input = input("Who is your favourite superhero? ")
    while user_input != SENTINEL:
        hero = find_bat_hero(user_input)
        if hero:
            print("You selected:", hero)
        else:
            print("Wrong answer.")
        user_input = input("Who is your favourite superhero? ")


if __name__ == "__main__":
    main()
