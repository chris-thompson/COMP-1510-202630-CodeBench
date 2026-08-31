"""
How do we access values defined in __init__.py? We must
import them from the package. Check this out!
"""
import time

from week_07 import CONSTANT_VALUE
from week_07 import import_time


def main():
    """
    Drive the program.
    """
    print('CONSTANT_VALUE:', CONSTANT_VALUE)
    time.sleep(1)
    print('The package was imported at:', import_time)
    print('The time is now:            ', time.time())


if __name__ == '__main__':
    main()
