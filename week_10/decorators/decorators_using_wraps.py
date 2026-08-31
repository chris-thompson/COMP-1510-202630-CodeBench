"""
Keeping a decorated function's identity, with functools.wraps.

Run decorators.py first and look at what it prints for say_cake.__name__ and
say_cake.__doc__. The name is "wrapper" and the docstring is gone. That is not
a bug in the decorator, it is the truth: after decoration the name say_cake
holds the wrapper, and the wrapper has its own name and its own docstring.

That truth is inconvenient. Debuggers, tracebacks, the help() function, and
doctest all use __name__ and __doc__, so a decorated function becomes hard to
identify and impossible to document.

The functools module fixes this. Decorating the wrapper with @wraps copies the
original function's __name__, __doc__, __module__, and friends onto it. It is
one line, and there is no reason to leave it out.
"""

from functools import wraps
from typing import Callable


def noisy_without_wraps(function_to_be_logged: Callable) -> Callable:
    """
    Decorate a function so that it announces itself, losing its identity.

    :param function_to_be_logged: the function to decorate
    :precondition: function_to_be_logged must be a function
    :postcondition: build a wrapper that does not preserve the identity
    :return: the wrapper function
    """

    def inner(*args, **kwargs):
        print("Invoking", function_to_be_logged.__name__)
        result = function_to_be_logged(*args, **kwargs)
        print("Returning from", function_to_be_logged.__name__)
        return result

    return inner


def noisy_with_wraps(function_to_be_logged: Callable) -> Callable:
    """
    Decorate a function so that it announces itself, keeping its identity.

    The only difference from noisy_without_wraps is the @wraps line.

    :param function_to_be_logged: the function to decorate
    :precondition: function_to_be_logged must be a function
    :postcondition: build a wrapper that preserves the function's identity
    :return: the wrapper function
    """

    @wraps(function_to_be_logged)
    def inner(*args, **kwargs):
        print("Invoking", function_to_be_logged.__name__)
        result = function_to_be_logged(*args, **kwargs)
        print("Returning from", function_to_be_logged.__name__)
        return result

    return inner


@noisy_without_wraps
def greet_anonymously() -> None:
    """
    Print a message about De Morgan's laws.

    :postcondition: print the message to standard output
    """
    print("The negation of a disjunction is the conjunction of the negations.")


@noisy_with_wraps
def greet() -> None:
    """
    Print a message about De Morgan's laws.

    :postcondition: print the message to standard output
    """
    print("The negation of a disjunction is the conjunction of the negations.")


def main():
    """
    Drive the program. Contrast a decorator with and without functools.wraps.
    """
    greet_anonymously()
    print("Without @wraps")
    print("  Function name:", greet_anonymously.__name__)
    print("  Docstring:", greet_anonymously.__doc__)

    print()

    greet()
    print("With @wraps")
    print("  Function name:", greet.__name__)
    print("  Docstring:", greet.__doc__.strip().splitlines()[0])


if __name__ == "__main__":
    main()
