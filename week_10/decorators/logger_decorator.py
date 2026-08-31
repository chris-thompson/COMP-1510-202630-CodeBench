"""
Using a decorator for logging.

Logging is the classic reason to decorate. We want to know when a function ran
and what it was given, but we do not want to paste a print statement into the
top and bottom of every function we own. A decorator lets us add the behaviour
in one place and switch it on with a single line.

This file has two parts:

1. Part one is an ordinary logger. It works on functions that accept no
arguments, and on functions that accept any number of them, because the
wrapper takes *args and **kwargs and reports them.

2. Part two is a stretch. The register function is not a decorator. It is a
function that builds and returns a decorator so that we can write
@register(active=False) and configure the decoration at the point of use. It
is one more layer of indirection than the rest of this week. Read part one
until it is comfortable before you start on part two.
"""

from functools import wraps
from typing import Callable


def logger(function_to_be_logged: Callable) -> Callable:
    """
    Decorate a function so that its name and arguments are logged.

    :param function_to_be_logged: the function to decorate
    :precondition: function_to_be_logged must be a function
    :postcondition: build a wrapper that logs each call
    :return: the wrapper function
    """

    @wraps(function_to_be_logged)
    def wrapper(*args, **kwargs):
        print(f"Invoking {function_to_be_logged.__name__} "
              f"with args {args} and kwargs {kwargs}")
        result = function_to_be_logged(*args, **kwargs)
        print(f"Returning from {function_to_be_logged.__name__}")
        return result

    return wrapper


@logger
def target() -> None:
    """
    Print a message, taking no arguments at all.

    :postcondition: print the message to standard output
    """
    print("  In target function")


@logger
def print_a_pair(first: int, second: int) -> None:
    """
    Print two values on one line.

    :param first: the first value to print
    :param second: the second value to print
    :precondition: first must be an integer
    :precondition: second must be an integer
    :postcondition: print both values to standard output
    """
    print(f"  {first} {second}")


# --------------------------------------------------------------------------
# Part two, the stretch. A function that builds a decorator.
# --------------------------------------------------------------------------


def register(active: bool = True) -> Callable:
    """
    Build a decorator that runs the function only when active is True.

    Read the three layers from the outside in. register accepts the setting
    and returns wrap. wrap accepts the function and returns wrapper. wrapper
    is what finally runs in place of the original function.

    This extra layer is what lets us write @register(active=False). The
    parentheses mean we are calling register first, and decorating with
    whatever it hands back.

    :param active: True to run the decorated function, False to skip it
    :precondition: active must be a boolean
    :postcondition: build a decorator configured by active
    :return: a decorator function
    """

    def wrap(function_to_be_registered: Callable) -> Callable:
        @wraps(function_to_be_registered)
        def wrapper(*args, **kwargs):
            print(f"{function_to_be_registered.__name__} "
                  f"registration is {active}")
            if not active:
                print(f"  Did not invoke {function_to_be_registered.__name__}")
                return None
            result = function_to_be_registered(*args, **kwargs)
            print(f"  Invoked {function_to_be_registered.__name__}")
            return result

        return wrapper

    return wrap


@register()
def simple_function() -> None:
    """
    Print a message.

    :postcondition: print the message to standard output
    """
    print("  simple_function is printing")


@register(active=False)
def another_simple_function() -> None:
    """
    Print a message, if anyone ever lets it.

    :postcondition: print the message to standard output
    """
    print("  another_simple_function is printing")


def main():
    """
    Drive the program. Demonstrate a logging decorator and a decorator factory.
    """
    target()
    print_a_pair(4, 5)

    print("-" * 10)
    simple_function()
    print("-" * 10)
    another_simple_function()


if __name__ == "__main__":
    main()
