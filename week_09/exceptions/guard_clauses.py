"""
A guard clause is a check at the very top of a function that rejects a bad
case immediately, so the rest of the function can assume everything is fine.

Compare each pair of functions below. Both members of a pair do the same
work. The guarded version is shorter, flatter, and easier to read, because
the unhappy paths are dealt with and dismissed before the real work starts.

Two rules to take away:

1. Validate arguments at the top of the function, and raise an exception if
   an argument breaks the contract the docstring promises.
2. Return or raise early. Every guard clause you write removes one level of
   indentation from the body.

Zen of Python 5: Flat is better than nested.
"""


def describe_score_nested(score: int) -> str:
    """
    Describe a percentage score as a letter grade, using nested ifs.

    Read this one and notice how far the real work is indented, and how far
    apart the if and its matching else have drifted.

    :param score: an int between 0 and 100 inclusive
    :precondition: score is an int
    :return: a str holding the letter grade, or a complaint about the score

    >>> describe_score_nested(85)
    'A'
    >>> describe_score_nested(0)
    'F'
    >>> describe_score_nested(101)
    'score must be between 0 and 100'
    """
    if type(score) is int:
        if score >= 0:
            if score <= 100:
                if score >= 80:
                    return 'A'
                elif score >= 65:
                    return 'B'
                elif score >= 50:
                    return 'C'
                else:
                    return 'F'
            else:
                return 'score must be between 0 and 100'
        else:
            return 'score must be between 0 and 100'
    else:
        return 'score must be an int'


def describe_score_guarded(score: int) -> str:
    """
    Describe a percentage score as a letter grade, using guard clauses.

    The first two statements are the guard clauses. Once they have run, the
    body knows score is an int between 0 and 100 and never has to ask again.

    :param score: an int between 0 and 100 inclusive
    :precondition: score is an int
    :return: a str holding the letter grade, or a complaint about the score

    >>> describe_score_guarded(85)
    'A'
    >>> describe_score_guarded(0)
    'F'
    >>> describe_score_guarded(101)
    'score must be between 0 and 100'
    """
    if type(score) is not int:
        return 'score must be an int'
    if score < 0 or score > 100:
        return 'score must be between 0 and 100'

    if score >= 80:
        return 'A'
    if score >= 65:
        return 'B'
    if score >= 50:
        return 'C'
    return 'F'


def average(numbers: list) -> float:
    """
    Calculate the arithmetic mean of a list of numbers.

    The guard clause raises instead of returning. Returning a fake answer
    such as -1 or None would force every caller to remember to check for it.
    Raising makes the failure impossible to ignore, and the :raises: line
    below is a promise this function must keep.

    :param numbers: a list of ints or floats
    :precondition: numbers is a list
    :precondition: every element of numbers is an int or a float
    :return: the mean of numbers as a float
    :raises ValueError: if numbers is empty

    >>> average([2, 4, 6])
    4.0
    >>> average([5])
    5.0
    >>> average([])
    Traceback (most recent call last):
    ValueError: cannot average an empty list
    """
    if len(numbers) == 0:
        raise ValueError('cannot average an empty list')

    return sum(numbers) / len(numbers)


def main():
    """
    Drive the program.
    """
    print('Both versions agree on every input, but one is far easier to read:')
    for score in [85, 70, 55, 0, 101]:
        nested = describe_score_nested(score)
        guarded = describe_score_guarded(score)
        print(f'  {score}: nested says "{nested}", guarded says "{guarded}"')

    print('\nA guard clause that raises cannot be ignored:')
    print(' ', average([2, 4, 6]))
    try:
        print(' ', average([]))
    except ValueError as error:
        print('  caught:', error)


if __name__ == '__main__':
    main()
