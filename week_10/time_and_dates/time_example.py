"""
The smallest possible way to time a block of code.

Python has a reputation for being slow. It is not a fast language, and when we
need speed, there are better tools. Python is quick to write, easy to read,
and in complete command of the data science and machine learning world.
The 3.11 through 3.14 releases have also been considerably faster than what
came before: https://docs.python.org/3/whatsnew/3.14.html

When you want to know how long something took, this is the whole technique.
Read the counter, do the work, read the counter again, subtract.

The same idea appears in three other files this week, each time wrapped in
something more convenient:

    iteration/profiling.py            the same thing, with commentary
    decorators/decorator_timer.py     the same thing, as a decorator
    decorators/memoization.py         the same thing, settling an argument

Once you find yourself pasting this snippet into a third function, stop and
use the decorator instead. That is what decorators are for.
"""

import time


def main():
    """
    Drive the program. Demonstrate the smallest useful timing snippet.
    """
    first_reading = time.perf_counter()

    # The code to be timed goes here. Anything at all. This one builds a list
    # of the first hundred thousand square numbers.
    squares = [value ** 2 for value in range(100000)]

    second_reading = time.perf_counter()

    print(f"Built {len(squares)} squares.")
    print(f"The code took {(second_reading - first_reading) * 1000:.2f}ms")


if __name__ == "__main__":
    main()
