"""
A generator is a function that pauses instead of finishing.

An ordinary function runs from top to bottom and then it is gone. A
generator function contains the yield keyword, and that one keyword changes
everything: calling it runs none of the body. It hands back a generator
which is an iterator. The body runs a little at a time, pausing at
each yield and remembering exactly where it stopped.

The pausing is the whole idea. A generator that yields a million values
never holds a million values in memory. It holds one, plus the place it
stopped. So efficient!

A note on the return type written below. A generator function does not
return the numbers; it returns the generator that produces them. We write
that as Iterator[int], which reads as "an iterator whose values are
integers". The square brackets say what the iterator hands out, in the same
way that list[str] would say a list of strings.
"""

from typing import Iterator


def gen_numbers() -> Iterator[int]:
    """
    Generate the numbers 1, 2, and 3, one at a time.

    :postcondition: create a generator that yields 1, then 2, then 3
    :return: a generator of the integers 1, 2, and 3

    >>> list(gen_numbers())
    [1, 2, 3]
    >>> next(gen_numbers())
    1
    >>> sum(gen_numbers())
    6
    """
    yield 1
    yield 2
    yield 3


def gen_numbers_out_loud() -> Iterator[int]:
    """
    Generate the numbers 1, 2, and 3, announcing every pause and restart.

    The printing is here so we can watch when the body actually runs. Notice
    in the output that "Start" does not appear until the first value is
    asked for, and "End" does not appear until the generator is exhausted.

    :postcondition: create a generator that yields 1, then 2, then 3
    :return: a generator of the integers 1, 2, and 3

    >>> list(gen_numbers_out_loud())
    Start
    Continue
    Final
    End
    [1, 2, 3]
    """
    print("Start")
    yield 1
    print("Continue")
    yield 2
    print("Final")
    yield 3
    print("End")


def evens_up_to(limit: int) -> Iterator[int]:
    """
    Generate every even number from zero up to the limit inclusive.

    :param limit: an integer greater than or equal to zero
    :precondition: limit must be an integer greater than or equal to zero
    :postcondition: create a generator that yields the even numbers in order
    :return: a generator of the even numbers from 0 to limit inclusive

    >>> list(evens_up_to(6))
    [0, 2, 4, 6]
    >>> list(evens_up_to(5))
    [0, 2, 4]
    >>> list(evens_up_to(0))
    [0]
    """
    value = 0
    while value <= limit:
        yield value
        value += 2


def main():
    """
    Drive the program.
    """
    print("A generator works in a for-loop, like any other iterable:")
    for value in gen_numbers():
        print(" ", value)

    print("\nOr we can pull the values out by hand with next():")
    a_number_generator = gen_numbers()
    print(" ", next(a_number_generator))
    print(" ", next(a_number_generator))
    print(" ", next(a_number_generator))

    # A generator is used up once. There is no fourth value to hand out, so
    # next() raises StopIteration. This is the exception a for-loop catches
    # for us, quietly, every single time we write one.
    try:
        print(" ", next(a_number_generator))
    except StopIteration:
        print("  StopIteration: that generator is exhausted for good.")

    # Calling the function again builds a brand new generator, back at 1.
    print("\nA fresh call starts over:", next(gen_numbers()))

    print("\nThe body runs only when a value is asked for:")
    for value in gen_numbers_out_loud():
        print("  got", value)

    print("\nEven numbers up to 6:", list(evens_up_to(6)))
    print("Even numbers up to 5:", list(evens_up_to(5)))

    # The same generator, walked twice. The second walk finds nothing,
    # because the first walk consumed it. This is the mistake to remember.
    evens = evens_up_to(4)
    print("\nFirst walk over one generator: ", list(evens))
    print("Second walk over the same one:", list(evens))


if __name__ == "__main__":
    main()
