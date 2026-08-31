"""
Your first decorators.

A decorator is a function that accepts a function and returns a new function
that wraps it. The wrapper runs some code, calls the original function, and
maybe runs some more code. The original function is never edited.

The pie syntax @my_decorator above a def is a shortcut. This:

    @my_decorator
    def say_cake():
        ...

means exactly this:

    def say_cake():
        ...
    say_cake = my_decorator(say_cake)

After either one, the name say_cake holds the address of the wrapper, not the
address of the function we wrote. That is the whole trick.

Notice that every wrapper below accepts *args and **kwargs and passes them
straight through. Without that, a decorator only works on functions that take
no arguments. See week_10/functions/args_and_kwargs.py.
"""

from typing import Callable

CAKE = "Cake! Gâteau! 케이크! 蛋糕! bánh ngọt! Торт! केक! کیک 🎂"


def my_decorator(function_to_be_wrapped: Callable) -> Callable:
    """
    Decorate a function so that it prints a message before and after it runs.

    :param function_to_be_wrapped: the function to decorate
    :precondition: function_to_be_wrapped must be a function
    :postcondition: build a wrapper around function_to_be_wrapped
    :return: the wrapper function
    """

    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        function_to_be_wrapped(*args, **kwargs)
        print("Something is happening after the function is called.")

    return wrapper


def do_twice(function_to_be_called_twice: Callable) -> Callable:
    """
    Decorate a function so that it runs twice each time it is called.

    :param function_to_be_called_twice: the function to decorate
    :precondition: function_to_be_called_twice must be a function
    :postcondition: build a wrapper around function_to_be_called_twice
    :return: the wrapper function
    """

    def wrapper_do_twice(*args, **kwargs):
        function_to_be_called_twice(*args, **kwargs)
        function_to_be_called_twice(*args, **kwargs)

    return wrapper_do_twice


def decorate_and_return(function_to_be_decorated: Callable) -> Callable:
    """
    Decorate a function that returns a value, preserving that value.

    Look closely at the return statement inside the wrapper. A wrapper that
    calls the original function but does not return its result will hand back
    None instead, and the caller's value disappears.

    :param function_to_be_decorated: the function to decorate
    :precondition: function_to_be_decorated must be a function
    :postcondition: build a wrapper around function_to_be_decorated
    :return: the wrapper function
    """

    def wrapper_returns(*args, **kwargs):
        print("Something is happening before the function is called.")
        return function_to_be_decorated(*args, **kwargs)

    return wrapper_returns


@my_decorator
def say_cake() -> None:
    """
    Print the word cake in several languages.

    :postcondition: print the cake message to standard output
    """
    print(CAKE)


@do_twice
def greet_with_cake(name: str) -> None:
    """
    Print a cake greeting for someone.

    :param name: the name of the person to greet
    :precondition: name must be a string
    :postcondition: print the greeting to standard output
    """
    print(f"Cake for {name}!")


@decorate_and_return
def return_greeting(name: str) -> str:
    """
    Build and return a greeting.

    :param name: the name of the person to greet
    :precondition: name must be a string
    :postcondition: build the greeting without modifying any argument
    :return: the greeting as a string
    """
    return f"Hi {name}"


def main():
    """
    Drive the program. Demonstrate three decorators written by hand.
    """
    say_cake()

    # The decoration cost us something. say_cake no longer knows its own name
    # or its own docstring, because the name say_cake now refers to the
    # wrapper. decorators_using_wraps.py shows how to get them back.
    print("Function name:", say_cake.__name__)
    print("Docstring:", say_cake.__doc__)
    print("Module:", say_cake.__module__)

    greet_with_cake("everyone")

    hi_justin = return_greeting("Justin")
    print(hi_justin)


if __name__ == "__main__":
    main()
