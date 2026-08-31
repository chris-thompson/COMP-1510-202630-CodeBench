"""
Working with tuples.

A tuple behaves like a list but is immutable: once created, its elements
cannot be changed. Tuples shine when the position of each element has a
fixed meaning, like (latitude, longitude).
"""


def describe_location(coordinates):
    """
    Build a sentence describing a (latitude, longitude) pair.

    :param coordinates: a tuple of (latitude, longitude) as floats
    :precondition: coordinates contains exactly two elements
    :postcondition: coordinates is unchanged
    :return: a string naming the latitude and longitude

    >>> describe_location((45.4236, 75.7009))
    'Latitude 45.4236 north, longitude 75.7009 west'
    >>> describe_location((0.0, 0.0))
    'Latitude 0.0 north, longitude 0.0 west'
    """
    return f'Latitude {coordinates[0]} north, longitude {coordinates[1]} west'


def main():
    """
    Drive the program.
    """
    parliament_hill = (45.4236, 75.7009)
    print('Coordinates:', parliament_hill)
    print('Tuple length:', len(parliament_hill))
    print('Latitude:', parliament_hill[0])
    print(describe_location(parliament_hill))

    # Parentheses are optional: Python packs comma-separated values
    # into a tuple
    screen_size = 1920, 1080
    print('Screen size:', screen_size)

    # A one-element tuple needs a trailing comma
    lonely = (42,)
    print('One element:', lonely, len(lonely))

    # Tuples are immutable. Uncomment the next line to see the TypeError:
    # parliament_hill[1] = 50.0


if __name__ == '__main__':
    main()
