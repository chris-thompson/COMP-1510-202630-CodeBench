"""
Command line arguments let us pass information to a program when we run it.

When we invoke a program like this:
    python3 sysdemo.py -1 0 1 Hello 3.14 True Difficult 1-player

Python collects everything after python3 into a list called sys.argv.
The first element, sys.argv[0], is always the script's own name, and
every element is a str. Run this file with different arguments from the
terminal (or a PyCharm run configuration) and watch the output change.
"""

import sys


def main(arguments: list):
    """
    Drive the program.

    :param arguments: a list of command line argument strs
    """
    print('This is the name of the script:', arguments[0])
    print('Number of arguments:', len(arguments))
    print('The arguments are:', arguments)


if __name__ == '__main__':
    main(sys.argv)
