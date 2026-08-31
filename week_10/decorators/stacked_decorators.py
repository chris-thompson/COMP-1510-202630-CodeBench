"""
Stacking decorators.

We can put more than one decorator on a function. When we do, order matters,
and the order is not the one most people guess.

    @make_bold
    @make_italic
    def challenge():
        ...

Python applies the decorator nearest the def first, then works upward. So the
line above means:

    challenge = make_bold(make_italic(challenge))

make_italic wraps the original function, and make_bold wraps that. The bold
tags therefore end up on the outside, because make_bold was applied last.

Swap the two decorator lines and run the file again. The output changes to
<i><b>...</b></i>. Nothing else in the file needs to change.
"""

from functools import wraps
from typing import Callable


def make_bold(function_to_be_emboldened: Callable) -> Callable:
    """
    Decorate a function so HTML bold tags surround its return value.

    :param function_to_be_emboldened: a function that returns a string
    :precondition: function_to_be_emboldened must be a function
    :precondition: function_to_be_emboldened must return a string
    :postcondition: build a wrapper that adds bold tags
    :return: the wrapper function
    """

    @wraps(function_to_be_emboldened)
    def emboldened(*args, **kwargs):
        return "<b>" + function_to_be_emboldened(*args, **kwargs) + "</b>"

    return emboldened


def make_italic(function_to_be_italicized: Callable) -> Callable:
    """
    Decorate a function so HTML italic tags surround its return value.

    :param function_to_be_italicized: a function that returns a string
    :precondition: function_to_be_italicized must be a function
    :precondition: function_to_be_italicized must return a string
    :postcondition: build a wrapper that adds italic tags
    :return: the wrapper function
    """

    @wraps(function_to_be_italicized)
    def italicized(*args, **kwargs):
        return "<i>" + function_to_be_italicized(*args, **kwargs) + "</i>"

    return italicized


@make_bold
@make_italic
def challenge() -> str:
    """
    Return a line of dialogue.

    :postcondition: build the line without modifying anything
    :return: the line as a string
    """
    return ("There are no stupid questions, but there are some absolutely "
            "unhinged variable names")


@make_italic
@make_bold
def challenge_the_other_way() -> str:
    """
    Return the same line, decorated in the opposite order.

    :postcondition: build the line without modifying anything
    :return: the line as a string
    """
    return ("There are no stupid questions, but there are some absolutely "
            "unhinged variable names")


def main():
    """
    Drive the program. Demonstrate that stacking order matters.
    """
    print("@make_bold over @make_italic:", challenge())
    print("@make_italic over @make_bold:", challenge_the_other_way())


if __name__ == "__main__":
    main()
