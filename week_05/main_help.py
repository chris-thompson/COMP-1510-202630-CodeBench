"""
This module guesses whether something is a dinosaur or not.
"""


def is_dinosaur(name):
    """
    Return True if the named creature is recognized as a dinosaur,
    and False otherwise.

    :param name: the name of a creature as a string
    :return: True if name is a recognized dinosaur, else False

    >>> is_dinosaur('Tyrannosaurus')
    True
    >>> is_dinosaur('Pterodactyl')
    False
    """
    return name in ['Tyrannosaurus', 'Triceratops']


if __name__ == '__main__':
    # Drive the program. Scroll up to see all the output when this finishes.
    help(__name__)
