"""
The Ackermann function is a famous recursive mathematical algorithm.

It computes nothing useful. What it does is build a recursive call stack that
grows and shrinks, sometimes for a very long time, which makes it a standard
way to test how well a system handles deep recursion.

Be careful with the arguments. ackermann(3, 3) returns 61 after a few thousand
calls, but the work grows so fast that ackermann(4, 2) has 19,729 digits and
ackermann(4, 3) will exhaust the call stack and raise RecursionError. Raise the
arguments one step at a time, and know that Python will stop you before your
computer does.

Compare this file with recursion_101.py, where every example is small enough
to trace by hand.
"""


def ackermann(first: int, second: int) -> int:
    """
    Calculate the Ackermann value of two non-negative integers.

    :param first: the first argument to the Ackermann function
    :param second: the second argument to the Ackermann function
    :precondition: first must be an integer greater than or equal to zero
    :precondition: second must be an integer greater than or equal to zero
    :precondition: first and second must be small enough to finish
    :postcondition: calculate the Ackermann value, modifying nothing
    :return: the Ackermann value as an integer

    >>> ackermann(0, 0)
    1
    >>> ackermann(1, 2)
    4
    >>> ackermann(3, 3)
    61
    """
    if first == 0:
        return second + 1
    if second == 0:
        return ackermann(first - 1, 1)
    return ackermann(first - 1, ackermann(first, second - 1))


def main():
    """
    Drive the program. Demonstrate a famously expensive recursive function.
    """
    for second in range(4):
        print(f"ackermann(2, {second}) is {ackermann(2, second)}")
    print(f"ackermann(3, 3) is {ackermann(3, 3)}")


if __name__ == "__main__":
    main()
