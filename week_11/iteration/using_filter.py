"""
filter() keeps the values that pass a predicate, and throws the rest away.
"""


def keep_long_names(names: list) -> list:
    """
    Find every name longer than four characters.

    :param names: a list of strings
    :precondition: names is a list of strings
    :postcondition: names is unchanged
    :return: a list of the names in names with more than four characters,
             in their original order

    >>> keep_long_names(['Amy', 'Yusuf', 'Bo', 'Genevieve'])
    ['Yusuf', 'Genevieve']
    >>> keep_long_names(['Amy', 'Bo'])
    []
    >>> keep_long_names([])
    []
    """
    return list(filter(lambda name: len(name) > 4, names))


def main():
    """
    Drive the program.
    """
    names = ['Amy', 'Yusuf', 'Bo', 'Genevieve', 'Tariq']
    print('All names:', names)
    print('Names longer than four characters:', keep_long_names(names))

    # filter() also accepts None instead of a function: it keeps every
    # value that is truthy, which is a quick way to drop empty strings.
    answers = ['yes', '', 'no', '', 'maybe']
    print('Non-empty answers:', list(filter(None, answers)))


if __name__ == '__main__':
    main()
