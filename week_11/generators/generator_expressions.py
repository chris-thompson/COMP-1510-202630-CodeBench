"""
A generator expression is a comprehension that has not run yet.

In Week 6 we learned the list comprehension. Square brackets build the whole
list, right now, in memory:

    squares = [number * number for number in range(1000000)]

Change the square brackets to parentheses, and almost nothing about the
syntax changes, but everything about the behaviour does:

    squares = (number * number for number in range(1000000))

That is a generator expression. No squaring has happened. Nothing is in
memory but the recipe and the place it stopped. Each value is computed when
it is asked for, and then it is gone.

Use a list comprehension when you need the values more than once, or need to
index them, or need to know how many there are. Use a generator expression
when you are going to walk the values exactly once, especially if there are
a great many of them.
"""

import sys

TEMPERATURES = [18, 21, 25, 30, 14, 27, 22]
WORDS = ["mango", "fig", "clementine", "kiwi", "pomegranate"]


def total_of_squares(bound: int) -> int:
    """
    Add up the squares of every number from zero up to the bound inclusive.

    The generator expression is passed straight to sum() without brackets of
    its own. When a generator expression is the only argument to a function,
    the function's own round brackets are enough.

    :param bound: an integer greater than or equal to zero
    :precondition: bound must be an integer greater than or equal to zero
    :return: the sum of the squares from 0 to bound inclusive

    >>> total_of_squares(3)
    14
    >>> total_of_squares(1)
    1
    >>> total_of_squares(0)
    0
    """
    return sum(number * number for number in range(bound + 1))


def longest_word_length(words: list) -> int:
    """
    Find the length of the longest word in a list of words.

    :param words: a list of strings
    :precondition: words must be a list of at least one string
    :postcondition: words is unchanged
    :return: the length of the longest string in words

    >>> longest_word_length(["fig", "clementine"])
    10
    >>> longest_word_length(["kiwi"])
    4
    >>> longest_word_length(["a", "bb", "cc"])
    2
    """
    return max(len(word) for word in words)


def warm_days(temperatures: list, threshold: int) -> list:
    """
    Count off the days that were warmer than a threshold.

    The generator expression here feeds a for-loop, one value at a time, so
    the intermediate list of warm days is never built at all.

    :param temperatures: a list of daily temperatures in degrees Celsius
    :param threshold: a temperature in degrees Celsius
    :precondition: temperatures must be a list of real numbers
    :precondition: threshold must be a real number
    :postcondition: temperatures is unchanged
    :return: a list of the temperatures greater than threshold, in order

    >>> warm_days([18, 25, 14, 30], 20)
    [25, 30]
    >>> warm_days([18, 14], 20)
    []
    >>> warm_days([20], 20)
    []
    """
    warm = []
    for temperature in (reading for reading in temperatures
                        if reading > threshold):
        warm.append(temperature)
    return warm


def main():
    """
    Drive the program.
    """
    # Same values, same order, two very different structures.
    as_a_list = [number * number for number in range(10)]
    as_a_generator = (number * number for number in range(10))
    print("List comprehension: ", as_a_list)
    print("Generator expression:", as_a_generator)
    print("Walk it to see the values:", list(as_a_generator))

    # A generator expression is used up once, exactly like a generator
    # function. The list can be walked over and over.
    print("\nWalking the list again:     ", as_a_list)
    print("Walking the generator again:", list(as_a_generator))

    # The reason we care. A million squares in a list costs megabytes; the
    # same million squares as a generator expression cost a couple of
    # hundred bytes, because only one of them exists at a time.
    million_in_a_list = [number * number for number in range(1000000)]
    million_lazily = (number * number for number in range(1000000))
    print(f"\nA million squares in a list:      "
          f"{sys.getsizeof(million_in_a_list):>9,} bytes")
    print(f"A million squares as a generator: "
          f"{sys.getsizeof(million_lazily):>9,} bytes")

    print("\nSum of the squares up to 10:", total_of_squares(10))
    print("Longest word in", WORDS, "is", longest_word_length(WORDS),
          "letters")
    print("Days warmer than 20 degrees:", warm_days(TEMPERATURES, 20))


if __name__ == "__main__":
    main()
