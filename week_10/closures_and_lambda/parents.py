"""
An example of inner (nested) functions.

Python lets us define a function inside another function. We call the inner
one a nested or inner function. We might do this to hide a helper from the
global scope, so no other function can reach it, or because we want to build
a closure. Closures come next, in closure.py.

Two questions to answer by experiment:

Q: What happens if we swap the order of the two inner function calls at the
   bottom of parent()?
Q: What happens if we try to call first_child() or second_child() from main(),
   outside the parent() function?
"""


def parent() -> None:
    """
    Call two inner functions, in the reverse of their defined order.

    Defining an inner function does not run it. The def statement only binds
    the name inside parent's local scope. Nothing prints until parent calls it.

    :postcondition: print one line from parent and one from each child

    >>> parent()
    Printing from the parent() function
    Printing from the inner second_child() function
    Printing from the inner first_child() function
    """
    print("Printing from the parent() function")

    def first_child() -> None:
        print("Printing from the inner first_child() function")

    def second_child() -> None:
        print("Printing from the inner second_child() function")

    second_child()
    first_child()


def main():
    """
    Drive the program. Demonstrate two inner functions.
    """
    parent()

    # Uncomment the next line. What does the interpreter say, and why?
    # first_child()


if __name__ == "__main__":
    main()
