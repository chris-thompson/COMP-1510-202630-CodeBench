"""
map() applies a function to every value in an iterable, one at a time.
"""


def celsius_list_to_fahrenheit(temperatures: list) -> list:
    """
    Convert a list of Celsius temperatures to Fahrenheit.

    :param temperatures: a list of real numbers in degrees Celsius
    :precondition: temperatures is a list of real numbers
    :postcondition: temperatures is unchanged
    :return: a list of the Fahrenheit equivalent of each temperature, in
             the same order

    >>> celsius_list_to_fahrenheit([0, 100])
    [32.0, 212.0]
    >>> celsius_list_to_fahrenheit([-40])
    [-40.0]
    >>> celsius_list_to_fahrenheit([])
    []
    """
    return list(map(lambda celsius: celsius * 9 / 5 + 32, temperatures))


def main():
    """
    Drive the program.
    """
    temperatures = [0, 20, 37, 100]
    print('Celsius:', temperatures)
    print('Fahrenheit:', celsius_list_to_fahrenheit(temperatures))

    # map() can take more than one iterable: it walks them in lockstep
    # and passes one value from each to the function.
    prices = [4.00, 2.50, 6.75]
    quantities = [2, 5, 1]
    totals = list(map(lambda price, quantity: price * quantity,
                      prices, quantities))
    print('Line totals:', totals)


if __name__ == '__main__':
    main()
