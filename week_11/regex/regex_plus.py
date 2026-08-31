"""
Introducing Regex: match one or more with the plus +

The plus is the asterisk's stricter sibling. The asterisk allows the group
to be absent; the plus insists it appear at least once. Bat(wo)+man matches
Batwoman and Batwowoman, but it does not match Batman.
"""

import re

SENTINEL = "quit"
BATWOMAN_REGEX = re.compile(r"Bat(wo)+man")


def find_bat_hero(text: str) -> str | None:
    """
    Find the first Bat-clan name that contains at least one "wo".

    :param text: a string to search
    :precondition: text must be a string
    :return: the matched name as a string, or None if there is no match

    >>> find_bat_hero("Batwoman")
    'Batwoman'
    >>> find_bat_hero("Batwowowoman")
    'Batwowowoman'
    >>> find_bat_hero("Batman")
    """
    match_object = BATWOMAN_REGEX.search(text)
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
            print("Wrong answer. Remember the plus demands at least one wo.")
        user_input = input("Who is your favourite superhero? ")


if __name__ == "__main__":
    main()
