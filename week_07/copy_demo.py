"""
Copying containers: aliases, shallow copies, and deep copies.

An assignment statement never copies a datum -- it copies an address.
A shallow copy (copy.copy or a whole-list slice [:]) makes a new outer
container but shares the inner addresses. A deep copy (copy.deepcopy)
makes a new container and new copies of everything inside it.
"""

import copy


def summarize_sharing(original: list, duplicate: list) -> str:
    """
    Describe how much memory two lists of rows share.

    :param original: a list of lists
    :param duplicate: a list of lists
    :return: 'aliases' if both names are bound to the same structure,
             'shares rows' if duplicate is a different list containing
             at least one of original's row objects, and 'independent'
             if the two lists share nothing

    >>> rows = [[1, 2], [3, 4]]
    >>> summarize_sharing(rows, rows)
    'aliases'
    >>> summarize_sharing(rows, rows[:])
    'shares rows'
    >>> summarize_sharing([], [])
    'independent'
    """
    if original is duplicate:
        return 'aliases'
    for row in duplicate:
        for candidate in original:
            if row is candidate:
                return 'shares rows'
    return 'independent'


def main():
    """
    Drive the program.
    """
    even = list(range(0, 10, 2))
    odd = list(range(1, 9, 2))
    numbers = [even, odd]

    alias = numbers
    shallow = copy.copy(numbers)  # the same as numbers[:]
    deep = copy.deepcopy(numbers)

    print('alias:  ', summarize_sharing(numbers, alias))
    print('shallow:', summarize_sharing(numbers, shallow))
    print('deep:   ', summarize_sharing(numbers, deep))

    numbers[0].append(10)
    print('After numbers[0].append(10):')
    print('the shallow copy sees the change:', shallow[0])
    print('the deep copy does not:         ', deep[0])


if __name__ == '__main__':
    main()
