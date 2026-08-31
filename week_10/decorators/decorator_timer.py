"""
A practical decorator: timing a function.

This is the decorator that finally justifies the whole idea. We want to know
how long a function takes, we do not want to edit the function to find out,
and we want the same answer for every function we ask about. One decorator
does all three.

time.perf_counter is the right clock for this. It returns a number of seconds
from an arbitrary starting point, chosen for precision rather than for telling
us the date. Subtracting two readings gives an elapsed time. Do not use
time.time for measuring durations, because the wall clock can be adjusted
underneath you while your code runs.

memoization.py imports the timer from this file and uses it to make a real
argument about algorithms.
"""

import time
from functools import wraps
from typing import Callable


def timer(function_to_be_timed: Callable) -> Callable:
    """
    Decorate a function so that its runtime is printed after every call.

    :param function_to_be_timed: the function to time
    :precondition: function_to_be_timed must be a function
    :postcondition: build a wrapper that times and reports each call
    :return: the wrapper function
    """

    @wraps(function_to_be_timed)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = function_to_be_timed(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {function_to_be_timed.__name__!r} "
              f"in {run_time:.4f} secs")
        return value

    return wrapper_timer


@timer
def waste_some_time(number_of_times: int) -> None:
    """
    Do a great deal of arithmetic for no reason whatsoever.

    :param number_of_times: how much work to do
    :precondition: number_of_times must be a positive integer
    :postcondition: waste an amount of time that grows with number_of_times

    There is no doctest here. The decorator prints a different elapsed time on
    every run and on every machine, so there is no output to expect.
    """
    for _ in range(number_of_times):
        sum([value ** 2 for value in range(number_of_times)])


def main():
    """
    Drive the program. Demonstrate a timing decorator.
    """
    # The work grows with the square of the argument, so tripling the input
    # costs roughly nine times as much. Watch the two numbers.
    waste_some_time(1000)
    waste_some_time(3000)


if __name__ == "__main__":
    main()
