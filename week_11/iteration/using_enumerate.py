"""
enumerate() replaces the old range(len(...)) habit for numbered loops.
"""


def number_the_old_way(items: list) -> list:
    """
    Pair every item with its position, counting from 0.

    :param items: a list
    :precondition: items is a list
    :postcondition: items is unchanged
    :return: a list of (index, item) tuples

    >>> number_the_old_way(['a', 'b', 'c'])
    [(0, 'a'), (1, 'b'), (2, 'c')]
    >>> number_the_old_way([])
    []
    """
    numbered = []
    for index in range(len(items)):
        numbered.append((index, items[index]))
    return numbered


def number_the_new_way(items: list, start: int = 0) -> list:
    """
    Pair every item with its position, using enumerate().

    :param items: a list
    :param start: an int to count from
    :precondition: items is a list
    :precondition: start is an int
    :postcondition: items is unchanged
    :postcondition: start is unchanged
    :return: a list of (index, item) tuples, indexed from start

    >>> number_the_new_way(['a', 'b', 'c'])
    [(0, 'a'), (1, 'b'), (2, 'c')]
    >>> number_the_new_way(['a', 'b', 'c'], start=1)
    [(1, 'a'), (2, 'b'), (3, 'c')]
    >>> number_the_new_way([])
    []
    """
    return list(enumerate(items, start=start))


def main():
    """
    Drive the program.
    """
    runners = ['Priya', 'Marcus', 'Sofia']

    print('The old way:')
    for index, runner in number_the_old_way(runners):
        print(f'  {index}: {runner}')

    print('The new way (same result, no indexing):')
    for place, runner in number_the_new_way(runners, start=1):
        print(f'  {place}. {runner}')


if __name__ == '__main__':
    main()
