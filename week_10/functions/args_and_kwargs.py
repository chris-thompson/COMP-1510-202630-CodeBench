"""
Demonstrate variable length parameter lists: *args and **kwargs.

Sometimes we cannot predict how many arguments a function will receive.
A single asterisk tells the interpreter to pack the leftover positional
arguments into a tuple. A double asterisk tells it to pack the leftover
keyword arguments into a dictionary.

The names args and kwargs are only a convention. The asterisks do the work,
so *toppings and **user_info are just as valid and maybe even easier to read.
"""


def make_pizza(*toppings: str) -> str:
    """
    Describe a pizza built from an arbitrary number of toppings.

    Python packs every positional argument into a tuple called toppings.
    A tuple is created even when the caller passes one argument or none.

    :param toppings: zero or more topping names
    :precondition: every topping must be a string
    :postcondition: build a description without modifying any argument
    :return: a description of the pizza as a string

    >>> make_pizza()
    'A plain pizza'
    >>> make_pizza("green peppers")
    'A pizza with green peppers'
    >>> make_pizza("ham", "pineapple", "garlic")
    'A pizza with ham, pineapple, garlic'
    """
    if not toppings:
        return "A plain pizza"
    return f"A pizza with {', '.join(toppings)}"


def make_sized_pizza(size: str, *toppings: str) -> str:
    """
    Describe a sized pizza built from any number of toppings.

    When a function mixes ordinary parameters with a variable length parameter
    list, the starred parameter must come last. Python matches the positional
    arguments first, then sweeps everything left over into the tuple.

    :param size: the size of the pizza
    :param toppings: zero or more topping names
    :precondition: size must be a non-empty string
    :precondition: every topping must be a string
    :postcondition: build a description without modifying any argument
    :return: a description of the pizza as a string

    >>> make_sized_pizza("small")
    'A small plain pizza'
    >>> make_sized_pizza("large", "basil")
    'A large pizza with basil'
    >>> make_sized_pizza("medium", "ham", "pineapple")
    'A medium pizza with ham, pineapple'
    """
    if not toppings:
        return f"A {size} plain pizza"
    return f"A {size} pizza with {', '.join(toppings)}"


def build_profile(first: str, last: str, **user_info: str) -> dict:
    """
    Build a dictionary holding everything we know about a user.

    Python packs every leftover keyword argument into a dictionary called
    user_info. Inside the function we treat it as an ordinary dictionary.

    :param first: a given name
    :param last: a family name
    :param user_info: zero or more extra name-value pairs about the user
    :precondition: first must be a non-empty string
    :precondition: last must be a non-empty string
    :postcondition: build a new dictionary without modifying any argument
    :return: a dictionary of everything known about the user

    >>> build_profile("albert", "einstein")
    {'first_name': 'albert', 'last_name': 'einstein'}
    >>> build_profile("albert", "einstein", field="physics")
    {'first_name': 'albert', 'last_name': 'einstein', 'field': 'physics'}
    >>> build_profile("ada", "lovelace", born="1815")["born"]
    '1815'
    """
    profile = {"first_name": first, "last_name": last}
    for key in user_info:
        profile[key] = user_info[key]
    return profile


def main():
    """
    Drive the program. Demonstrate *args and **kwargs.
    """
    print(make_pizza())
    print(make_pizza("green peppers"))
    print(make_pizza("ham", "pineapple", "garlic"))

    print(make_sized_pizza("small"))
    print(make_sized_pizza("large", "ham", "pineapple", "garlic"))

    print(build_profile("albert", "einstein",
                        location="princeton",
                        field="physics"))


if __name__ == "__main__":
    main()
