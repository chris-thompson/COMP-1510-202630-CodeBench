"""
Demonstrate default parameter values, and the mutable default argument trap.

A parameter with a default value is optional when we invoke the function.
Parameters that have defaults must be listed after every parameter that does
not, so the interpreter can still match positional arguments correctly.

Run this file and compare add_pizza_sauce_dangerously with
add_pizza_sauce_safely. The two functions look almost identical.
Only one of them behaves the way we expect.
"""


def format_name(first: str, last: str, middle: str = "") -> str:
    """
    Build a full name from its parts.

    :param first: a given name
    :param last: a family name
    :param middle: a middle name, or an empty string if there is none
    :precondition: first must be a non-empty string
    :precondition: last must be a non-empty string
    :precondition: middle must be a string
    :postcondition: build the full name without modifying any argument
    :return: the full name as a string

    >>> format_name("Neil", "Harris", "Patrick")
    'Neil Patrick Harris'
    >>> format_name("Cher", "Bono")
    'Cher Bono'
    >>> format_name("Cher", "Bono", "")
    'Cher Bono'
    """
    if middle:
        return f"{first} {middle} {last}"
    return f"{first} {last}"


def add_pizza_sauce_dangerously(toppings: list = []) -> list:
    """
    Add sauce to a list of toppings, using a mutable default value.

    Do not write functions like this one. A default value is evaluated once
    when the def statement runs, not once per call. Every call that omits the
    argument therefore shares the very same list, and each call leaves its
    sauce behind for the next one.

    :param toppings: a list of topping names
    :precondition: toppings must be a list of strings
    :postcondition: append "sauce" to toppings
    :return: the toppings list, with "sauce" appended

    >>> add_pizza_sauce_dangerously(["cheese"])
    ['cheese', 'sauce']
    >>> add_pizza_sauce_dangerously()
    ['sauce']
    >>> add_pizza_sauce_dangerously()
    ['sauce', 'sauce']
    """
    toppings.append("sauce")
    return toppings


def add_pizza_sauce_safely(toppings: list | None = None) -> list:
    """
    Add sauce to a list of toppings, using None as the default value.

    This is the idiom to use. None is immutable, so there is nothing to carry
    over between calls. We test for None inside the function and build a fresh
    list whenever the caller omitted the argument.

    The annotation on toppings is a readability hint, not a promise the
    interpreter enforces. See week_07/function_annotations.py.

    :param toppings: a list of topping names, or None for a plain pizza
    :precondition: toppings must be a list of strings or None
    :postcondition: append "sauce" to a list without altering any default
    :return: a list of toppings, with "sauce" appended

    >>> add_pizza_sauce_safely(["cheese"])
    ['cheese', 'sauce']
    >>> add_pizza_sauce_safely()
    ['sauce']
    >>> add_pizza_sauce_safely()
    ['sauce']
    """
    if toppings is None:
        toppings = []
    toppings.append("sauce")
    return toppings


def main():
    """
    Drive the program. Demonstrate default values and the mutable default trap.
    """
    print(format_name("Neil", "Harris", "Patrick"))
    print(format_name("Cher", "Bono"))

    print("\nThree calls to the dangerous version, omitting the argument:")
    for _ in range(3):
        print(add_pizza_sauce_dangerously())

    print("\nThree calls to the safe version, omitting the argument:")
    for _ in range(3):
        print(add_pizza_sauce_safely())


if __name__ == "__main__":
    main()
