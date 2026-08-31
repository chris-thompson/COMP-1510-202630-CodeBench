"""
The pprint module lets us "pretty-print" things.

Check out how it prints the dictionary created from this
dictionary comprehension!
"""

import pprint


def make_board(width, height):
    """
    Create a board.
    :param width: The width of the board
    :param height: The height of the board
    :precondition: width is a positive non-zero integer
    :precondition: height is a positive non-zero integer
    :return: the board as a dictionary whose keys are (row, column)
             tuples and whose values are location description strings

    >>> make_board(1, 1)
    {(0, 0): 'This room is empty'}
    >>> make_board(2, 1)
    {(0, 0): 'This room is empty', (0, 1): 'This room is empty'}
    """
    return {(row, column): "This room is empty"
            for row in range(height)
            for column in range(width)}


def main():
    """
    Drive the program.
    """
    board = make_board(5, 5)
    print(board)
    print("And now the pretty print version:")
    pprint.pprint(board)


if __name__ == "__main__":
    main()
