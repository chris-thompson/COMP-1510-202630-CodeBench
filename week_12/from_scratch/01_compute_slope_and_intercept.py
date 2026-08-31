"""
Step 1: fit a line to the data using nothing but lists and functions.

Before scikit-learn does linear regression for us, we do it ourselves. The
functions live in linear_regression.py, next door; this file is the driver
that calls them and shows the result.

The data is ten (years of experience, salary) pairs. We are looking for the
straight line that comes closest to all ten points at once.
"""

from linear_regression import load_data, compute_slope_and_intercept

DATA_FILE = "sample_data.csv"


def main():
    """
    Drive the program.
    """
    years_of_experience, salaries = load_data(DATA_FILE)
    print(f"Read {len(years_of_experience)} pairs from {DATA_FILE}.")
    print(f"Years of experience: {years_of_experience}")
    print(f"Salaries:            {salaries}\n")

    slope, intercept = compute_slope_and_intercept(years_of_experience,
                                                   salaries)
    print(f"slope     = {slope:.2f}")
    print(f"intercept = {intercept:.2f}\n")
    print("Our model, written out in full:")
    print(f"  salary = {slope:.2f} * years_of_experience + {intercept:.2f}")
    print(f"\nIn words: every extra year of experience is worth about "
          f"${slope:,.0f}, and someone with no experience at all would "
          f"start at about ${intercept:,.0f}.")


if __name__ == "__main__":
    main()
