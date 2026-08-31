"""
Introducing Regex: backreferences.

A backreference is \\number, and it stands for whatever the group of that
number actually matched. It is not "the same pattern again"; it is "the same
TEXT again".

So (.)\\1{3} means: any character, then that exact character three more
times. Four of a kind.
"""

import re

SENTINEL = "quit"
FOUR_OF_A_KIND = re.compile(r"(.)\1{3}")
FIVE_OF_A_KIND = re.compile(r"^([2-9TJQKA])\1{4}$")


def find_four_of_a_kind(text: str) -> str | None:
    """
    Find the first run of one character repeated four times in some text.

    :param text: a string to search
    :precondition: text must be a string
    :return: the four repeated characters as a string, or None if there is
             no such run

    >>> find_four_of_a_kind('aaaa')
    'aaaa'
    >>> find_four_of_a_kind('I am so haaaaappy')
    'aaaa'
    >>> find_four_of_a_kind('abcabc')
    """
    match_object = FOUR_OF_A_KIND.search(text)
    if match_object:
        return match_object.group()
    return None


def is_five_of_a_kind(hand: str) -> bool:
    """
    Determine whether a five-card hand is five of a kind.

    The anchors ^ and $ force the whole string to match, so a longer hand
    that merely contains five of a kind is rejected.

    :param hand: a string of five card ranks, using T J Q K A for the
                 face cards
    :precondition: hand must be a string
    :return: True if hand is five of the same rank, otherwise False

    >>> is_five_of_a_kind('77777')
    True
    >>> is_five_of_a_kind('AAAAA')
    True
    >>> is_five_of_a_kind('7777K')
    False
    """
    return bool(FIVE_OF_A_KIND.search(hand))


def main():
    """
    Drive the program.
    """
    print(f"Type {SENTINEL} to stop.")
    user_input = input("Enter your text: ")
    while user_input != SENTINEL:
        run = find_four_of_a_kind(user_input)
        if run:
            print("  You entered four of a kind:", run)
        else:
            print("  No character appears four times in a row there.")
        print("  Read as a card hand, five of a kind:",
              is_five_of_a_kind(user_input))
        user_input = input("Enter your text: ")


if __name__ == "__main__":
    main()
