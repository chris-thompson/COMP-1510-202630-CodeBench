"""
Introducing Regex: greedy and non-greedy matching

Regular expressions are hungry. When several lengths of text could match,
a regex takes the biggest bite it can. (Ha){3,5} will happily swallow five
Ha's even though three would have satisfied it.

Following the closing curly brace with a question mark makes the regex
non-greedy: (Ha){3,5}? takes the smallest bite that still works. Uncomment
the second pattern below and compare the two on the same input.
"""

import re

SENTINEL = "quit"
GREEDY_REGEX = re.compile(r"(Ha){3,5}")
NON_GREEDY_REGEX = re.compile(r"(Ha){3,5}?")


def measure_laugh(text: str, non_greedy: bool = False) -> str | None:
    """
    Find a run of between three and five Ha's in some text.

    :param text: a string to search
    :param non_greedy: True to take the shortest run, False for the longest
    :precondition: text must be a string
    :precondition: non_greedy must be a boolean
    :return: the matched laugh as a string, or None if there is no match

    >>> measure_laugh("HaHaHaHaHa")
    'HaHaHaHaHa'
    >>> measure_laugh("HaHaHaHaHa", non_greedy=True)
    'HaHaHa'
    >>> measure_laugh("HaHa")
    """
    if non_greedy:
        match_object = NON_GREEDY_REGEX.search(text)
    else:
        match_object = GREEDY_REGEX.search(text)
    if match_object:
        return match_object.group()
    return None


def main():
    """
    Drive the program.
    """
    print(f"Type {SENTINEL} to stop. Try HaHaHaHaHa.")
    user_input = input("How funny is the joke? ")
    while user_input != SENTINEL:
        greedy = measure_laugh(user_input)
        non_greedy = measure_laugh(user_input, non_greedy=True)
        if greedy:
            print("  Greedy (Ha){3,5} takes the most it can:  ", greedy)
            print("  Non-greedy (Ha){3,5}? takes the least:   ", non_greedy)
        else:
            print("  Not funny. That is fewer than three Ha's.")
        user_input = input("How funny is the joke? ")


if __name__ == "__main__":
    main()
