"""
Profiling is what we call timing a piece of code to find out how long it takes.

The quick way is to read a clock before and after. The time module gives us
two clocks, and the difference between them matters:

    time.time()          seconds since the beginning of the Epoch. This is the
                         wall clock. It can be adjusted while your program
                         runs, by the operating system or by a time server,
                         which makes it the wrong tool for measuring a
                         duration.

    time.perf_counter()  a performance counter with the highest resolution the
                         machine offers, counting from an arbitrary point.
                         The number itself means nothing. The difference
                         between two readings is exactly what we want.
                         time.perf_counter_ns() gives the same in nanoseconds.

Use perf_counter for durations. time.time is for telling us what day it is.

Once you have measured something, you usually want to measure the next thing
too, which is why decorators/decorator_timer.py wraps all of this up into a
decorator you can apply to any function at all.

A note on the arithmetic below. Python integers have no upper limit, but
converting one to a string is a different matter: since Python 3.11, there
has been a 4300-digit ceiling on that conversion, because the conversion
cost grows faster than the number does. The upper bound here stays under the
ceiling on purpose.
"""

import time

UPPER_BOUND = 1000


def multiply_everything_below(upper_bound: int) -> int:
    """
    Multiply together every integer from one up to, but not including, a bound.

    :param upper_bound: the exclusive upper bound of the multiplication
    :precondition: upper_bound must be an integer greater than or equal to one
    :postcondition: calculate the product without modifying any argument
    :return: the product as an integer

    >>> multiply_everything_below(5)
    24
    >>> multiply_everything_below(2)
    1
    >>> multiply_everything_below(1)
    1
    """
    product = 1
    for value in range(1, upper_bound):
        product = product * value
    return product


def main():
    """
    Drive the program. Demonstrate timing a calculation with perf_counter.
    """
    start_time = time.perf_counter()
    product = multiply_everything_below(UPPER_BOUND)
    end_time = time.perf_counter()

    print(f"Took {end_time - start_time:f} seconds to calculate.")

    # Converting the product to a string to measure it is itself real work.
    # Time that separately and compare.
    start_time = time.perf_counter()
    digits = len(str(product))
    end_time = time.perf_counter()

    print(f"The result is {digits} digits long.")
    print(f"Took {end_time - start_time:f} seconds just to count the digits.")


if __name__ == "__main__":
    main()
