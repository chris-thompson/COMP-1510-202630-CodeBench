"""
A module for demonstrating exceptions.

Use common or existing exceptions when possible, i.e.:

IndexError
KeyError
ValueError
TypeError
etc.

Examine the following functions. They all do the same thing, more or less.
But as we travel down the list, the quality of the function changes.

What change(s) do you observe from convert to another_convert to
yet_another_convert to informative_convert? Run the program and compare the
answers each one gives for the same input.

One thing to expect when you run it: informative_convert writes its message
to sys.stderr instead of the usual sys.stdout. Those are two separate
streams, so your terminal may print the error lines out of order with the
rest of the output. That is normal, and it is why error messages belong on
stderr: a user can send the two streams to different places.
"""

import sys


def a_terrible_non_pythonic_convert_dont_do_this(value) -> int:
    """
    Convert to an integer. This code is not Pythonic. Yuck.

    It checks the type of everything before it dares to do any work, which
    is the Look Before You Leap style. Note the order of the two guards: we
    have to know value is an int BEFORE we compare it to 0, or comparing a
    str to an int raises a TypeError we never meant to cause.
    """
    if type(value) is not int:
        raise TypeError("That's not an integer")
    if value < 0:
        raise ValueError('No negative numbers!')
    return value


def convert(value) -> int:
    """
    Convert to an integer. Meh. That -1 stuff tells me a C dev wrote this.
    """
    try:
        the_int = int(value)
    except ValueError:
        the_int = -1
    return the_int


def another_convert(value) -> int:
    """
    Convert to an integer. Safer. But note the use of pass. Absolutely not.
    """
    the_int = -1
    try:
        the_int = int(value)
    except (ValueError, TypeError):
        pass
    return the_int


def yet_another_convert(value) -> int:
    """
    Convert to an integer. Better yet. Clarity. Parsimony. But that -1 though.
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return -1


def informative_convert(value) -> int | None:
    """
    Convert to an integer. Prints a very helpful error message! Probably best.
    """
    try:
        return int(value)
    except (ValueError, TypeError) as error:
        print(f'Conversion error: {error}. Returning None.', file=sys.stderr)
        return None


def main():
    """
    Drive the program.
    """
    for value in ['42', 'forty-two']:
        print(f'\nconverting the string "{value}"')
        print('  convert:             ', convert(value))
        print('  another_convert:     ', another_convert(value))
        print('  yet_another_convert: ', yet_another_convert(value))
        print('  informative_convert: ', informative_convert(value))

    print('\nconverting None')
    print('  convert handles only ValueError, so None still crashes it:')
    try:
        convert(None)
    except TypeError as error:
        print('    TypeError:', error)
    print('  the others also handle TypeError, so they survive:')
    print('    another_convert:     ', another_convert(None))
    print('    yet_another_convert: ', yet_another_convert(None))
    print('    informative_convert: ', informative_convert(None))

    print('\nThe LBYL version refuses the work instead of attempting it:')
    try:
        a_terrible_non_pythonic_convert_dont_do_this('42')
    except TypeError as error:
        print('    TypeError:', error)

    print('\nOnly informative_convert tells us what actually went wrong.')


if __name__ == '__main__':
    main()
