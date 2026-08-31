"""
Memoization is where recursion and decorators pay off together. I love it.

The Fibonacci numbers have an obvious recursive definition, and writing it out
gives fibonacci_recursive below. It is correct, it is three lines long, and it
is catastrophically slow.

The reason is that it solves the same subproblems over and over. Computing
fibonacci_recursive(5) computes fibonacci_recursive(3) twice, and each of
those computes fibonacci_recursive(1) again, and so on. The number of calls
roughly doubles for every step, so the 33rd term takes about eleven million
calls, and the 500th term might not finish before the sun burns out.

Memoization fixes it. We keep a dictionary of answers we have already worked
out. Before doing any work we look in the dictionary, and we only compute a
term we have never seen. Each term is then computed exactly once, so the cost
grows linearly with the term rather than doubling, and the 500th term arrives
instantly.

This file imports the timer decorator from decorator_timer.py rather than
copying it. That is what modules are for. See week_07/module_information.py.
"""

from decorator_timer import timer

FAIR_COMPARISON_TERM = 33
SHOWING_OFF_TERM = 500


def fibonacci_recursive(nth_term: int) -> int:
    """
    Calculate a Fibonacci number by naive recursion.

    :param nth_term: which Fibonacci number to calculate
    :precondition: nth_term must be an integer greater than or equal to zero
    :precondition: nth_term must be small, because the cost doubles each step
    :postcondition: calculate the term without modifying any argument
    :return: the nth Fibonacci number as an integer

    >>> fibonacci_recursive(0)
    0
    >>> fibonacci_recursive(1)
    1
    >>> fibonacci_recursive(10)
    55
    """
    if nth_term == 0:
        return 0
    if nth_term == 1:
        return 1
    return (fibonacci_recursive(nth_term - 1)
            + fibonacci_recursive(nth_term - 2))


def fibonacci_memoized(nth_term: int, memory: dict) -> int:
    """
    Calculate a Fibonacci number by recursion, remembering every answer.

    The dictionary is passed in rather than created here, so that the same
    memory can be reused across calls and so that we can look at it afterwards.

    :param nth_term: which Fibonacci number to calculate
    :param memory: a dictionary of terms already calculated
    :precondition: nth_term must be an integer greater than or equal to zero
    :precondition: memory must be a dict mapping terms to Fibonacci numbers
    :postcondition: add every term calculated along the way to memory
    :return: the nth Fibonacci number as an integer

    >>> fibonacci_memoized(0, {})
    0
    >>> fibonacci_memoized(10, {})
    55
    >>> answers = {}
    >>> fibonacci_memoized(10, answers)
    55
    >>> answers[7]
    13
    """
    if nth_term in memory:
        return memory[nth_term]
    if nth_term == 0:
        memory[nth_term] = 0
    elif nth_term == 1:
        memory[nth_term] = 1
    else:
        memory[nth_term] = (fibonacci_memoized(nth_term - 1, memory)
                            + fibonacci_memoized(nth_term - 2, memory))
    return memory[nth_term]


@timer
def time_the_recursive_version(nth_term: int) -> int:
    """
    Calculate a Fibonacci number by naive recursion, and time it.

    :param nth_term: which Fibonacci number to calculate
    :precondition: nth_term must be an integer greater than or equal to zero
    :precondition: nth_term must be small enough to finish today
    :postcondition: print the elapsed time to standard output
    :return: the nth Fibonacci number as an integer
    """
    return fibonacci_recursive(nth_term)


@timer
def time_the_memoized_version(nth_term: int, memory: dict) -> int:
    """
    Calculate a Fibonacci number with memoization, and report how long it took.

    :param nth_term: which Fibonacci number to calculate
    :param memory: a dictionary of terms already calculated
    :precondition: nth_term must be an integer greater than or equal to zero
    :precondition: memory must be a dict mapping terms to Fibonacci numbers
    :postcondition: print the elapsed time to standard output
    :return: the nth Fibonacci number as an integer
    """
    return fibonacci_memoized(nth_term, memory)


def main():
    """
    Drive the program. Contrast naive recursion with memoized recursion.
    """
    print(f"Term {FAIR_COMPARISON_TERM}, the same answer computed two ways:")
    print(time_the_recursive_version(FAIR_COMPARISON_TERM))
    print(time_the_memoized_version(FAIR_COMPARISON_TERM, {}))

    print(f"\nTerm {SHOWING_OFF_TERM}, which only one of the two can reach:")
    print(time_the_memoized_version(SHOWING_OFF_TERM, {}))

    # Do not raise FAIR_COMPARISON_TERM much above 35 unless you have somewhere
    # to be. Every step you add roughly doubles the wait.


if __name__ == "__main__":
    main()
