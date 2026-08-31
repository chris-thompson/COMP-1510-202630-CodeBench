"""
Linear regression from first principles, with nothing but lists and functions.

Before we let a library do this for us, we should do it ourselves once. A
linear regression draws the single straight line that comes closest to a
cloud of points. The line has the same two numbers every straight line has:

    y = slope * x + intercept

"Closest" has to mean something exact. We use least squares, which chooses
the line that makes the total of the squared vertical distances between the
points and the line as small as it can be. Squaring matters twice over: it
makes every distance positive, so misses above and below cannot cancel each
other out, and it punishes one large miss far more than several small ones.

The arithmetic works out to two quantities:

    covariance   how much x and y move together
    variance     how much x moves on its own

and the slope is simply one divided by the other. Once we have the slope,
the line is pinned down by the fact that it must pass through the point
(mean of x, mean of y).

This module holds the functions. The numbered files beside it use them, one
step at a time. Nothing here is imported from outside the standard library.
"""

HEADER_ROWS = 1


def parse_rows(lines: list) -> tuple:
    """
    Parse two-column CSV text into a list of x values and a list of y values.

    Separating the parsing from the file reading is what makes this
    function testable: the doctests below hand it a list of strings, so no
    file has to exist for us to know it works.

    :param lines: a list of strings, the first of which is a header row and
                  each of the rest of which is "x_value,y_value"
    :precondition: lines must be a list of strings in that format
    :postcondition: lines is unchanged
    :return: a tuple of two lists of floats, the x values and the y values,
             in the order they appeared

    >>> parse_rows(["Years,Salary", "1.1,39343.00", "2.0,43525.00"])
    ([1.1, 2.0], [39343.0, 43525.0])
    >>> parse_rows(["Years,Salary", "3.0,60150.00"])
    ([3.0], [60150.0])
    >>> parse_rows(["Years,Salary"])
    ([], [])
    """
    x_values = []
    y_values = []
    for line in lines[HEADER_ROWS:]:
        x_text, y_text = line.strip().split(",")
        x_values.append(float(x_text))
        y_values.append(float(y_text))
    return x_values, y_values


def load_data(path: str) -> tuple:
    """
    Load two columns of numbers from a CSV file with a header row.

    :param path: the name of a readable CSV file whose first row is a
                 header and whose remaining rows are "x_value,y_value"
    :precondition: path must name a readable CSV file in that format
    :postcondition: the file named by path is not modified
    :return: a tuple of two lists of floats, the x values and the y values,
             in file order

    >>> x_values, y_values = load_data("sample_data.csv")
    >>> len(x_values), len(y_values)
    (10, 10)
    >>> x_values[0], y_values[0]
    (1.1, 39343.0)
    """
    with open(path) as data_file:
        return parse_rows(data_file.readlines())


def compute_slope_and_intercept(x_values: list, y_values: list) -> tuple:
    """
    Fit the least-squares line y = slope * x + intercept to some points.

    :param x_values: a list of real numbers
    :param y_values: a list of real numbers of the same length as x_values
    :precondition: x_values must be a non-empty list of real numbers
    :precondition: y_values must be a list of real numbers of the same
                   length as x_values
    :precondition: the values in x_values must not all be equal
    :postcondition: x_values is unchanged
    :postcondition: y_values is unchanged
    :return: a tuple of two floats, the slope and the intercept of the
             best-fit line

    >>> compute_slope_and_intercept([1, 2, 3], [2, 4, 6])
    (2.0, 0.0)
    >>> compute_slope_and_intercept([0, 1, 2], [1, 3, 5])
    (2.0, 1.0)
    >>> compute_slope_and_intercept([1, 2], [5, 5])
    (0.0, 5.0)
    """
    number_of_points = len(x_values)
    mean_x = sum(x_values) / number_of_points
    mean_y = sum(y_values) / number_of_points

    covariance = sum((x - mean_x) * (y - mean_y)
                     for x, y in zip(x_values, y_values))
    variance = sum((x - mean_x) ** 2 for x in x_values)

    slope = covariance / variance
    return slope, mean_y - slope * mean_x


def predict(x_value: float, slope: float, intercept: float) -> float:
    """
    Predict a y value for one x value, using a line we have already fitted.

    This is the whole point of fitting a line. Once we have the two
    numbers, we can ask about x values that were never in the data.

    :param x_value: a real number
    :param slope: a real number
    :param intercept: a real number
    :precondition: x_value must be a real number
    :precondition: slope must be a real number
    :precondition: intercept must be a real number
    :return: slope * x_value + intercept

    >>> predict(5.0, 2.0, 1.0)
    11.0
    >>> predict(0.0, 2.0, 1.0)
    1.0
    >>> predict(-1.0, 2.0, 1.0)
    -1.0
    """
    return slope * x_value + intercept


def fitted_line(x_values: list, slope: float, intercept: float) -> list:
    """
    Predict a y value for every x value in a list.

    :param x_values: a list of real numbers
    :param slope: a real number
    :param intercept: a real number
    :precondition: x_values must be a list of real numbers
    :precondition: slope must be a real number
    :precondition: intercept must be a real number
    :postcondition: x_values is unchanged
    :return: a list of the predicted y value for each x value, in order

    >>> fitted_line([1.0, 2.0, 3.0], 2.0, 0.0)
    [2.0, 4.0, 6.0]
    >>> fitted_line([], 2.0, 0.0)
    []
    """
    return [predict(x_value, slope, intercept) for x_value in x_values]
