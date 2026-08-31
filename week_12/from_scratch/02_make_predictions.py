"""
Step 2: use the fitted line to predict salaries.

Step 1 gave us a slope and an intercept. Two numbers are now standing in
for ten data points, and we can ask the line about any number of years we
like, including years nobody in the data actually had.

Compare the predicted salaries with the real ones. The gaps are called the
residuals, and least squares is precisely the rule that made the total of
their squares as small as it could be.
"""

from linear_regression import load_data, compute_slope_and_intercept, predict

DATA_FILE = "sample_data.csv"
NEW_YEARS = (4.5, 8.0, 15.0)


def main():
    """
    Drive the program.
    """
    years_of_experience, salaries = load_data(DATA_FILE)
    slope, intercept = compute_slope_and_intercept(years_of_experience,
                                                   salaries)
    print(f"slope = {slope:.2f}, intercept = {intercept:.2f}\n")

    print("Years in the data, predicted against actual:")
    print(f"  {'years':>6}  {'predicted':>10}  {'actual':>10}  {'gap':>10}")
    for years, actual in zip(years_of_experience, salaries):
        predicted = predict(years, slope, intercept)
        print(f"  {years:>6}  {predicted:>10.2f}  {actual:>10.2f}  "
              f"{actual - predicted:>10.2f}")

    print("\nYears nobody in the data had. The line answers anyway:")
    for years in NEW_YEARS:
        print(f"  {years:>6}  {predict(years, slope, intercept):>10.2f}")
    print("\nThe last one is a warning. Fifteen years is far outside the "
          "range\nwe fitted, so that number is a guess dressed up as "
          "arithmetic.")


if __name__ == "__main__":
    main()
