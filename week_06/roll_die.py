"""
Demonstrate how to use a random number generator.
"""

import random


def roll_die(rolls, sides):
    """
    Roll a die with the specified number of sides the specified number
    of times.

    :param rolls: a positive non-zero int
    :param sides: a positive non-zero int
    :precondition: rolls must be a positive non-zero int
    :precondition: sides must be a positive non-zero int
    :return: the sum of the rolls as a random int between rolls and
             sides * rolls inclusive
    """
    return random.randint(rolls, sides * rolls)
