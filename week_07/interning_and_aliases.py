"""
Python preloads ("interns") small integers and reuses them everywhere.

Interning is just caching: the interpreter keeps one shared structure for
each integer in a small range, and every variable assigned one of those
values is bound to the same structure. Variables that store the same
values is bound to the same structure. Variables that store the same
address are called aliases. We can observe all of this with the id()
function and the identity operator is.
"""


def is_interned(value: int) -> bool:
    """
    Determine whether value is one of the interpreter's interned integers.

    Building a brand-new int from a string forces the interpreter to
    look the value up: inside the interned range it hands back the one
    shared structure, and outside the range it constructs a new structure.

    :param value: an int
    :return: True if value is interned (cached), otherwise False

    >>> is_interned(0)
    True
    >>> is_interned(256)
    True
    >>> is_interned(257)
    False
    >>> is_interned(-5)
    True
    >>> is_interned(-6)
    False
    """
    freshly_built = int(str(value))
    return freshly_built is value


def main():
    """
    Drive the program.
    """
    small = 5
    print('id(small):', id(small))
    print('id(5):    ', id(5), ' <- the same address: 5 is interned')

    big = int('5000')
    print('id(big):           ', id(big))
    print("id(int('5000')):   ", id(int('5000')), ' <- a new object each time')

    interned_values = [value for value in range(-10, 300)
                       if is_interned(value)]
    print('Interned range on this interpreter:',
          min(interned_values), 'to', max(interned_values))


if __name__ == '__main__':
    main()
