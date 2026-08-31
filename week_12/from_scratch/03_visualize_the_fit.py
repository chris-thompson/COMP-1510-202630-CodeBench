"""
Step 3: see the fit, with matplotlib.

Numbers are hard to argue with and easy to misread. A picture of ten points
and one line tells us in a second what the slope and intercept only imply.

matplotlib draws a figure a piece at a time: scatter() puts the points down,
plot() draws the line, the label functions name the axes, and show() opens
the window. Nothing appears on screen until show() is called.

matplotlib is not part of the standard library. Install it first:

    pip3 install matplotlib
"""

import matplotlib.pyplot as plt

from linear_regression import (load_data, compute_slope_and_intercept,
                               fitted_line)

DATA_FILE = "sample_data.csv"


def main():
    """
    Drive the program.
    """
    years_of_experience, salaries = load_data(DATA_FILE)
    slope, intercept = compute_slope_and_intercept(years_of_experience,
                                                   salaries)
    print(f"slope = {slope:.2f}, intercept = {intercept:.2f}")
    print("Close the plot window to end the program.")

    predicted_salaries = fitted_line(years_of_experience, slope, intercept)

    plt.scatter(years_of_experience, salaries, color="red",
                label="Actual salary")
    plt.plot(years_of_experience, predicted_salaries, color="blue",
             label="Our line")
    plt.title("Salary versus experience, fitted from scratch")
    plt.xlabel("Years of experience")
    plt.ylabel("Salary")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
