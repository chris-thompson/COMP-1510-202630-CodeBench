"""
The itertools module, part two: four more that are not on the slides.

Read itertools_demos.py first. Nothing here will appear on a quiz, but all
four are worth knowing, and dropwhile is a good excuse to use a lambda.

Each function below returns an iterator. Printing an iterator shows you its
address, not its contents:

    >>> itertools.chain([1, 2], [3])            # doctest: +SKIP
    <itertools.chain object at 0x104d58f70>

That is not a broken iterator, it is an iterator that has not been asked for
anything yet. Wrap it in list() to see the values, exactly as we do below.
"""

import itertools

VALUES = [1, 3, 5, 7, 9, 3, 1]


def main():
    """
    Drive the program. Demonstrate chain, repeat, dropwhile, and islice.
    """
    # chain(*iterables) streams several iterables one after another, as though
    # they were a single sequence. Nothing is copied.
    chained = list(itertools.chain([1, 2, 3], [2, 3, 4]))
    print(chained)

    # repeat(value, times) streams the same value a given number of times.
    repeated = list(itertools.repeat("hello", 5))
    print(repeated)

    # dropwhile(predicate, iterable) throws away members from the front for as
    # long as the predicate is True, then streams everything that is left.
    # Note the trailing 3 and 1 survive: dropwhile stops testing at the first
    # False and never looks again. That surprises people.
    dropped = list(itertools.dropwhile(lambda value: value < 5, VALUES))
    print(dropped)

    # islice(iterable, start, stop) slices an iterable the way [start:stop]
    # slices a list, but without needing the whole thing in memory first.
    sliced = list(itertools.islice(VALUES, 3, 6))
    print(sliced)


if __name__ == "__main__":
    main()
