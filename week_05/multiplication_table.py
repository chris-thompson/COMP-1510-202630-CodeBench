"""
Cool things we can do with list and range functions.
"""


def print_table(size):
    """
    Print the multiplication table for the numbers 1 through size inclusive.

    :param size: the largest number in the table as an int
    :precondition: size is a positive integer
    :postcondition: a size-by-size multiplication table is printed
    """
    numbers = list(range(1, size + 1))

    for number in numbers:
        print('\t' + str(number), end='')
    print()

    for number in numbers:
        print(number, end='')
        for other_number in numbers:
            print('\t' + str(number * other_number), end='')
        print()


def main():
    """
    Drive the program.
    """
    print_table(5)


if __name__ == "__main__":
    main()
