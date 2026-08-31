"""
Comparing and rounding floating-point numbers.

Most decimal fractions cannot be represented exactly in binary, so two
floats that "should" be equal often differ by a tiny amount. We call
this representation error. Never compare floats with ==; compare the
difference to a tolerance instead, or let math.isclose do it for us.
"""

import math

TOLERANCE = 0.0001


def is_close_enough(first, second):
    """
    Determine whether two floats are within TOLERANCE of each other.

    :param first: a float
    :param second: a float
    :return: True if first and second differ by less than TOLERANCE,
        else False

    >>> is_close_enough(0.1 + 0.2, 0.3)
    True
    >>> is_close_enough(1.0, 1.1)
    False
    >>> is_close_enough(-0.5, -0.5)
    True
    """
    return abs(first - second) < TOLERANCE


def main():
    """
    Drive the program.
    """
    print('Representation error in action:')
    print(0.1 + 0.2)
    print(0.1 + 0.2 == 0.3)

    print('\nCompare the difference to a tolerance instead:')
    print(is_close_enough(0.1 + 0.2, 0.3))

    print('\nThe math module does this for us:')
    print(math.isclose(0.1 + 0.2, 0.3))
    print(math.isclose(1000.0, 1001.0, rel_tol=0.01))
    print(math.isclose(0.0000001, 0.0, abs_tol=0.001))

    print('\nRounding floats with the built-in round function:')
    print(round(3.14159, 2))
    print(round(9.75))
    print(round(2.675, 2))  # Representation error strikes: not 2.68!
    print(round(0.5))  # Python rounds ties to the nearest even number
    print(round(2.5))


if __name__ == '__main__':
    main()
