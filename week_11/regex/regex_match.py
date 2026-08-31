"""
Introducing Regex: match() when all we want is yes or no.

search() looks for the pattern ANYWHERE in the string. match() insists the
pattern start at the very beginning. When we are validating a whole value
rather than hunting through a message, match() is usually what we mean.

Both return a Match object or None, and a Match object is truthy while None
is falsy, so either one drops straight into an if-statement. bool() turns
the answer into a plain True or False.
"""

import re

ROBOT_NAME_REGEX = re.compile(r"[A-Za-z0-9]{1,10}3000$")


def is_robot_name(the_name: str) -> bool:
    """
    Determine whether a name is a valid robot name.

    A robot name may contain only letters and numbers, must be no more than
    ten characters long, and must end with the four characters 3000.

    :param the_name: a robot's name in string form
    :precondition: the_name must be a string
    :return: True if the_name is valid, otherwise False

    >>> is_robot_name('Andre3000')
    True
    >>> is_robot_name('3000Andre')
    False
    >>> is_robot_name('30003000')
    True
    >>> is_robot_name('Andre300000')
    False
    >>> is_robot_name('@13#$!~')
    False
    """
    return bool(ROBOT_NAME_REGEX.match(the_name))


def main():
    """
    Drive the program.
    """
    for candidate in ['Andre3000', '3000Andre', '30003000', '@13#$!~']:
        print(f'{candidate!r} is a robot name: {is_robot_name(candidate)}')

    # The difference between match() and search(), on one string. The
    # pattern is there, but not at the start, so match() says no.
    print("\nsearch() looks anywhere:  ",
          bool(re.compile(r"3000").search('Andre3000')))
    print("match() insists on the start:",
          bool(re.compile(r"3000").match('Andre3000')))


if __name__ == '__main__':
    main()
