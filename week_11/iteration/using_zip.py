"""
zip() walks several iterables side by side, one value from each at a time.

zip() is lazy. It is an iterator, not a list: it does not zip everything up
the moment we call it. Each time it is asked for a value it builds ONE tuple
holding the next value from each iterable, and it stops the moment the
shortest one runs out.
"""

import itertools


def pair_names_and_scores(names: list, scores: list) -> list:
    """
    Pair each name with the score at the same position.

    :param names: a list of strings
    :param scores: a list of ints
    :precondition: names is a list of strings
    :precondition: scores is a list of ints
    :postcondition: names is unchanged
    :postcondition: scores is unchanged
    :return: a list of (name, score) tuples, one per position common to
             both lists

    >>> pair_names_and_scores(['Amy', 'Bo'], [91, 78])
    [('Amy', 91), ('Bo', 78)]
    >>> pair_names_and_scores(['Amy', 'Bo'], [91])
    [('Amy', 91)]
    >>> pair_names_and_scores([], [])
    []
    """
    return list(zip(names, scores))


def main():
    """
    Drive the program.
    """
    names = ['Amy', 'Bo', 'Genevieve']
    scores = [91, 78, 85]

    print('Paired up:', pair_names_and_scores(names, scores))

    # zip() is also how you build a dict from two parallel lists.
    score_by_name = dict(zip(names, scores))
    print('As a dict:', score_by_name)

    # zip() stops at the shortest iterable -- it does not pad or raise.
    short_scores = [91]
    print('Mismatched lengths:', pair_names_and_scores(names, short_scores))

    # zip(*pairs) undoes a zip: it turns rows back into columns.
    pairs = list(zip(names, scores))
    unzipped_names, unzipped_scores = zip(*pairs)
    print('Unzipped names:', unzipped_names)
    print('Unzipped scores:', unzipped_scores)

    # itertools.count() from Week 10 counts upward forever. On its own that
    # is useless, because nothing stops it. Paired with zip() it becomes a
    # numbering machine: zip() stops when the names do, so the endless
    # counter is safe here.
    numbered = list(zip(itertools.count(1), names))
    print('Numbered with itertools.count:', numbered)


if __name__ == '__main__':
    main()
