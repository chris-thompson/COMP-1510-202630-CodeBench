"""
What the for-loop has been doing for us all term.

An iterable is any structure that can hand out its members one at a time. An
iterator is the device that actually does the handing out. They are not the
same thing.

Passing an iterable to iter() builds a fresh iterator. Passing that iterator
to next() returns the following member of the iterable, every time, until there
are none left, at which point next() raises StopIteration.

A for-loop does this and hides all of it:

    1. calls iter() on the iterable to get an iterator
    2. calls next() on the iterator, again and again
    3. stops quietly when StopIteration arrives

An iterator is used up once it is exhausted. It cannot be rewound or reused.
The iterable can build you a new one, but the old one is finished.

We rarely use iter() and next() by hand. Knowing they are there is knowledge
that lets us understand a traceback, understand a generator in Week 11, and
know why looping over the same iterator twice quietly does nothing the second
time.
"""

FRUITS = ("apple", "banana", "cherry")


def main():
    """
    Drive the program. Demonstrate iter() and next() directly.
    """
    fruity_iterator = iter(FRUITS)
    print(next(fruity_iterator))
    print(next(fruity_iterator))
    print(next(fruity_iterator))

    # The tuple has three members and we have taken all three. Asking for a
    # fourth is not a mistake in our code, it is how the iterator says "done".
    try:
        print(next(fruity_iterator))
    except StopIteration:
        print("StopIteration: this iterator is exhausted.")

    # The tuple is untouched. It will build us a brand new iterator whenever
    # we ask, which is why a for-loop over FRUITS still works perfectly.
    for fruit in FRUITS:
        print(fruit)

    # An iterable and its iterator are different types.
    print(type(FRUITS))
    print(type(iter(FRUITS)))

    # A range is an iterable, not an iterator. It builds a new iterator each
    # time it is asked, which is why we can loop over the same range twice.
    print(type(range(0, 1)))
    print(type(iter(range(0, 1))))


if __name__ == "__main__":
    main()
