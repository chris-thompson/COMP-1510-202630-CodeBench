"""
Functions are structures, and every structure has an address.

Because a function is a structure, we can store it in a variable, pass it to
another function as an argument, and return it from a function. We have been
doing the second of those since Week 4, when we passed a function to sorted
as its key argument.

This file shows the third. make_function builds a new function and returns it.
make_checker chooses between three functions and returns the one we asked for.
Neither returned function is called inside the factory. Look for the missing
parentheses on the return lines.

Compare this file with closure.py and lambda_demo.py.
"""

from typing import Callable


def make_function() -> Callable:
    """
    Build and return a function that adds its two arguments.

    :postcondition: build a new function that adds two numbers
    :return: a function that accepts two numbers and returns their sum

    >>> example = make_function()
    >>> example(3, 2)
    5
    >>> example(3, -3)
    0
    """

    def adder(first_argument, second_argument):
        return first_argument + second_argument

    return adder


def make_checker(instruction: str) -> Callable:
    """
    Select and return one of three functions that test a number.

    Each of the three is written as a lambda, because each is a single
    expression that we need only briefly. See lambda_demo.py.

    :param instruction: the name of the check we want, one of "even",
                        "positive", or "negative"
    :precondition: instruction must be "even", "positive", or "negative"
    :postcondition: select a function without modifying any argument
    :return: a function that accepts a number and returns True or False
    :raises ValueError: if instruction is not one of the three known names

    >>> is_even = make_checker("even")
    >>> is_even(4)
    True
    >>> is_negative = make_checker("negative")
    >>> is_negative(0)
    False
    >>> make_checker("prime")
    Traceback (most recent call last):
    ValueError: Unknown request
    """
    if instruction == "even":
        return lambda number: number % 2 == 0
    if instruction == "positive":
        return lambda number: number >= 0
    if instruction == "negative":
        return lambda number: number < 0
    raise ValueError("Unknown request")


def main():
    """
    Drive the program. Demonstrate functions that return functions.
    """
    is_even = make_checker("even")
    is_positive = make_checker("positive")
    is_negative = make_checker("negative")
    print(is_even(3))
    print(is_positive(3))
    print(is_negative(3))

    adder = make_function()
    print(adder(3, 2))
    print(adder(3, 3))
    print(adder(3, 1))

    # The name adder holds the address of a function structure.
    print(adder)


if __name__ == "__main__":
    main()
