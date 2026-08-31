"""
range structures, iterators, and dict views all look like sequences, but
they behave very differently. This file shows how.
"""


def main():
    """
    Drive the program.
    """
    # A range is reusable: it computes its values fresh every time it's
    # walked, so the same range structure can be iterated more than once.
    countdown = range(3, 0, -1)
    print('First pass over the range:', list(countdown))
    print('Second pass over the same range:', list(countdown))

    # An iterator is single-use: once exhausted, it stays exhausted.
    countdown_iterator = iter([3, 2, 1])
    print('First pass over the iterator:', list(countdown_iterator))
    print('Second pass over the same iterator:', list(countdown_iterator))

    # A dict view is live: it doesn't copy the dict, so it reflects later
    # changes to the dict it came from.
    inventory = {'apples': 4, 'pears': 2}
    keys_view = inventory.keys()
    print('View before adding a key:', list(keys_view))
    inventory['plums'] = 7
    print('Same view after adding a key:', list(keys_view))

    print('type(range(3)):', type(range(3)))
    print('type(iter([1, 2, 3])):', type(iter([1, 2, 3])))
    print('type({}.keys()):', type({}.keys()))


if __name__ == '__main__':
    main()
