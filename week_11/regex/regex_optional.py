"""
Introducing Regex: match zero or one with the question mark ?

The question mark marks the group before it as optional: the pattern matches
whether that group is present or absent, but never more than once. It is the
right tool for a part of a pattern that is genuinely allowed to be missing,
such as the area code of a phone number.
"""

import re

SENTINEL = "quit"
BATMAN_REGEX = re.compile(r"Bat(wo)?man")
PHONE_NUMBER_REGEX = re.compile(r"(\d\d\d-)?(\d\d\d)-(\d\d\d\d)")


def find_bat_hero(text: str) -> str | None:
    """
    Find the first Bat-clan name with an optional "wo" in the middle.

    :param text: a string to search
    :precondition: text must be a string
    :return: the matched name as a string, or None if there is no match

    >>> find_bat_hero("Batman")
    'Batman'
    >>> find_bat_hero("Batwoman")
    'Batwoman'
    >>> find_bat_hero("Batwowoman")
    """
    match_object = BATMAN_REGEX.search(text)
    if match_object:
        return match_object.group()
    return None


def find_phone_number(text: str) -> str | None:
    """
    Find a phone number whose three-digit area code is optional.

    :param text: a string to search
    :precondition: text must be a string
    :return: the matched phone number as a string, or None if there is none

    >>> find_phone_number("604-555-1234")
    '604-555-1234'
    >>> find_phone_number("555-1234")
    '555-1234'
    >>> find_phone_number("Moshi moshi")
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
    user_input = input("Who is your favourite superhero? ")
    while user_input != SENTINEL:
        hero = find_bat_hero(user_input)
        if hero:
            print("You selected:", hero)
        else:
            print("Wrong answer.")

        user_input = input("Enter a phone number, with or without an area"
                           " code: ")
        if user_input == SENTINEL:
            break
        number = find_phone_number(user_input)
        if number:
            print("Your number is:", number)
        else:
            print("That is not a valid number.")

        user_input = input("Who is your favourite superhero? ")


if __name__ == "__main__":
    main()
