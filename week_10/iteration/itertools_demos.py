"""
The itertools module, part one: the four functions from the slides.

Developers iterate constantly, so Python ships a module of ready-made
iterators. Each function here returns an iterator, not a list. Nothing is
computed until something asks for the next value, which is what lets count()
and cycle() describe infinite sequences without needing infinite memory.

Two of these never end. count() counts forever and cycle() repeats forever.
Never pass either one to list(), and never write a bare for-loop over one
without a way out. In this file we take a fixed number of values with next().

Part two, in itertools_demos_more.py, covers four more that are not on the
slides.
"""

import itertools

NAMES = ["Arthur", "Eryn", "Inid", "Oliver", "Ursula", "Yorgan"]
PRIMARY_COLOURS = ["cyan", "magenta", "yellow"]
SPICES = ["ginger", "allspice", "cumin", "mint"]


def take(iterator, how_many: int) -> list:
    """
    Collect a fixed number of values from an iterator into a list.

    This is how we take a safe bite out of an endless iterator.

    :param iterator: the iterator to take values from
    :param how_many: the number of values to take
    :precondition: iterator must be able to supply how_many more values
    :precondition: how_many must be an integer greater than or equal to zero
    :postcondition: advance iterator by how_many values
    :return: a list of the values taken

    >>> take(itertools.count(0), 4)
    [0, 1, 2, 3]
    >>> take(itertools.count(10, 5), 3)
    [10, 15, 20]
    >>> take(itertools.count(0), 0)
    []
    """
    values = []
    for _ in range(how_many):
        values.append(next(iterator))
    return values


def number_the_names(names: list) -> list:
    """
    Pair each name with its position in the list, starting the count at one.

    itertools.count is the endless counter that supplies the numbers. The
    for-loop stops when the names run out, which is what keeps the endless
    counter safe here.

    :param names: a list of names
    :precondition: names must be a list of strings
    :postcondition: build a new list, leaving names unmodified
    :return: a list of (number, name) tuples

    >>> number_the_names(["Arthur", "Eryn"])
    [(1, 'Arthur'), (2, 'Eryn')]
    >>> number_the_names(["Inid"])
    [(1, 'Inid')]
    >>> number_the_names([])
    []
    """
    counter = itertools.count(1)
    pairs = []
    for name in names:
        pairs.append((next(counter), name))
    return pairs


def main():
    """
    Drive the program. Demonstrate four itertools functions.
    """
    # count(start, step) streams evenly spaced values, forever.
    print(number_the_names(NAMES))
    print(take(itertools.count(0, 2), 10))

    # The steps do not have to be whole numbers.
    print(take(itertools.count(start=0.5, step=0.75), 5))

    # cycle(iterable) streams the members of an iterable over and over.
    print(take(itertools.cycle([True, False]), 8))

    # permutations(iterable) streams every possible ordering of the members.
    permutations = list(itertools.permutations(PRIMARY_COLOURS))
    print(f"There are {len(permutations)} permutations:")
    for permutation in permutations:
        print(f"\t{permutation}")

    # combinations(iterable, r) streams every group of r members, ignoring
    # order. Order is what separates the two: there are six orderings of
    # three colours above, and six pairs from four spices below.
    size = 2
    combinations = list(itertools.combinations(SPICES, size))
    print(f"There are {len(combinations)} combinations of size {size}:")
    for combination in combinations:
        print(f"\t{combination}")


if __name__ == "__main__":
    main()
