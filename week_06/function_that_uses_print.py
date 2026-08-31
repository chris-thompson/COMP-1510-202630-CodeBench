"""
Demonstrate a function whose only job is to print.

A function like this returns nothing we can assert on, so an ordinary
unit test cannot check it. test_function_that_uses_print.py shows how
the capsys fixture captures what the function printed.
"""


def my_printer(value):
    """
    Print the specified value.

    :param value: any value that can be printed
    :postcondition: prints value to standard output
    """
    print(value)
