"""
Removing elements from a list you are looping over is a classic trap.

The for-loop's hidden position moves forward while remove() shifts the
remaining elements left - so some elements slide into positions the
loop has already passed and are never visited.
"""


def remove_negatives_broken(numbers):
    """
    Remove the negative numbers from numbers. Or try to! This is broken.

    The for-loop walks numbers while remove() shrinks it. When two
    negative numbers sit side by side, the second one slides into a
    position the loop has already visited and survives.

    :param numbers: a list of numbers
    :postcondition: some, but not necessarily all, negative numbers are
        removed from numbers

    >>> values = [-5, 1, -3, 2]
    >>> remove_negatives_broken(values)
    >>> values
    [1, 2]
    >>> values = [-1, -2, 3]
    >>> remove_negatives_broken(values)
    >>> values
    [-2, 3]
    """
    for number in numbers:
        if number < 0:
            numbers.remove(number)


def remove_negatives(numbers):
    """
    Remove every negative number from numbers.

    Looping over a sliced copy lets us shrink the original safely: the
    copy never changes, so no element is skipped.

    :param numbers: a list of numbers
    :postcondition: every negative number is removed from numbers

    >>> values = [-1, -2, 3]
    >>> remove_negatives(values)
    >>> values
    [3]
    >>> values = [1, 2]
    >>> remove_negatives(values)
    >>> values
    [1, 2]
    """
    for number in numbers[:]:
        if number < 0:
            numbers.remove(number)


def remove_every(values, target):
    """
    Remove every occurrence of target from values.

    :param values: a list
    :param target: the value to remove
    :postcondition: every occurrence of target is removed from values

    >>> party = ['Sith Lord', 'Jedi', 'Sith Lord']
    >>> remove_every(party, 'Sith Lord')
    >>> party
    ['Jedi']
    >>> numbers = [1, 2, 3]
    >>> remove_every(numbers, 4)
    >>> numbers
    [1, 2, 3]
    """
    while target in values:
        values.remove(target)


def main():
    """
    Drive the program.
    """
    values = [-1, -2, 3]
    remove_negatives_broken(values)
    print('The broken version left one behind:', values)

    values = [-1, -2, 3]
    remove_negatives(values)
    print('The fixed version got them all:', values)

    party = ['Sith Lord', 'Jedi', 'Sith Lord']
    remove_every(party, 'Sith Lord')
    print('Later, alligators:', party)


if __name__ == '__main__':
    main()
