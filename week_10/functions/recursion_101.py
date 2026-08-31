"""
Demonstrate simple recursion.

A recursive function is a function that calls itself. On its own that is just
an infinite loop, so every recursive function needs two parts:

1. a base case, the version of the problem we can answer immediately, and
2. a recursive step, which reduces the problem to a smaller problem of the
   same shape and calls the function again.

Every recursive call in this file makes the problem strictly smaller, so every
call eventually reaches the base case. A recursive function that never reaches
its base case raises RecursionError instead of running forever.
"""


def repeat_message(times: int) -> None:
    """
    Print a message a given number of times, using recursion instead of a loop.

    :param times: the number of times to print the message
    :precondition: times must be an integer greater than or equal to zero
    :postcondition: print the message that many times

    >>> repeat_message(2)
    This is my life now.
    This is my life now.
    >>> repeat_message(0)
    """
    if times > 0:
        print("This is my life now.")
        repeat_message(times - 1)


def factorial(value: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    This is the canonical example. The factorial of 0 is 1, and the factorial
    of any larger value is that value multiplied by the factorial below it.

    :param value: the number whose factorial we want
    :precondition: value must be an integer greater than or equal to zero
    :postcondition: calculate the factorial without modifying any argument
    :return: the factorial as an integer

    >>> factorial(5)
    120
    >>> factorial(1)
    1
    >>> factorial(0)
    1
    """
    if value == 0:
        return 1
    return value * factorial(value - 1)


def print_numbers(bound: int) -> None:
    """
    Print every integer from a bound down to zero.

    :param bound: the number to count down from
    :precondition: bound must be an integer greater than or equal to zero
    :postcondition: print the countdown to standard output

    >>> print_numbers(3)
    3
    2
    1
    0
    >>> print_numbers(0)
    0
    """
    if bound == 0:
        print(0)
    else:
        print(bound)
        print_numbers(bound - 1)


def print_triangle(base: int) -> None:
    """
    Print a right triangle of asterisks with a given base.

    Notice that the recursive call comes after the loop. The work a recursive
    function does before its recursive call, and the work it does after, are
    both useful. Here the loop draws one row and the recursive call draws the
    rest of the triangle.

    :param base: the width of the widest row
    :precondition: base must be an integer greater than or equal to zero
    :postcondition: print the triangle to standard output

    >>> print_triangle(3)
    ***
    **
    *
    >>> print_triangle(1)
    *
    >>> print_triangle(0)
    """
    if base == 0:
        return
    for _ in range(base):
        print("*", end="")
    print()
    print_triangle(base - 1)


def main():
    """
    Drive the program. Demonstrate four simple recursive functions.
    """
    repeat_message(3)
    print(f"factorial(5) is {factorial(5)}")
    print_numbers(5)
    print_triangle(5)


if __name__ == "__main__":
    main()
