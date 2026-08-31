"""
Demonstrate closures.

A closure is an inner function that captures a variable from the function that
built it, and keeps its access to that variable even after the outer function
has returned. The captured variable becomes a fixed, private part of the new
function.

generate_power is a factory. Each call to it hands back a brand new function
with a different base baked in. Compare this file with parents.py, where the
inner functions capture nothing, and with functions_are_structures.py, where
the returned function is chosen rather than built.
"""

from typing import Callable


def generate_power(number: int) -> Callable:
    """
    Build and return a function that raises a fixed base to a given power.

    The inner function nth_power closes over the parameter number. Every
    function generate_power returns remembers its own value of number.

    :param number: the base of the exponent for the returned function
    :precondition: number must be an integer
    :postcondition: build a new function that closes over number
    :return: a function that accepts a power and returns number to that power

    >>> powers_of_two = generate_power(2)
    >>> powers_of_two(7)
    128
    >>> powers_of_three = generate_power(3)
    >>> powers_of_three(5)
    243
    >>> powers_of_two(0)
    1
    """

    # Define the inner function ...
    def nth_power(power):
        # ... which closes over number, making the base a fixed part of the
        # new function.
        return number ** power

    # ... and return it. Note there are no parentheses here. We are returning
    # the function itself, not the result of calling it.
    return nth_power


def main():
    """
    Drive the program. Demonstrate how to build and use closures.
    """
    powers_of_ten = generate_power(10)
    print(powers_of_ten(1))
    print(powers_of_ten(3))
    print(powers_of_ten(6))

    powers_of_four = generate_power(4)
    print(powers_of_four(1))
    print(powers_of_four(2))
    print(powers_of_four(3))
    print(powers_of_four(4))

    # A power does not have to be a whole number. This is the cube root of 4.
    print(powers_of_four(1 / 3))

    # powers_of_ten and powers_of_four are two different closures, each with
    # its own captured base.
    print(powers_of_ten)
    print(powers_of_four)


if __name__ == "__main__":
    main()
