"""
Can you fix this?
"""


def average(values):
    """
    Return the average of the numbers in values.  Some items in values are
    None, and they are not counted toward the average.

    :param values: a list that contains numbers and/or None
    :precondition: values contains at least one element
    :postcondition: values is unchanged
    :return: the average of the non-None numbers as a float, or None if
        values contains no numbers

    >>> average([20, 30])
    25.0
    >>> average([None, 20, 30])
    25.0
    >>> result = average([None, None, None])
    >>> result is None
    True
    """
