"""
Seeing is believing: the straight line and the wiggly curve, on one figure.

overfitting_demo.py reports the failure as two R-squared values. This file
draws it, which is more convincing and much harder to forget.

Watch the green curve. It passes through the black training points beautifully
and misses the red test points completely. That is the whole of overfitting in
one picture.

    pip3 install matplotlib
"""

import matplotlib.pyplot as plt

from polynomial_fit import (ABSURD_DEGREE, SENSIBLE_DEGREE, fit_polynomial,
                            load_dataset, smooth_x_values,
                            split_features_and_target, split_train_and_test)

DATA_FILE = "sample_data.csv"
SMOOTH_POINTS = 200
DEGREE_COLOURS = ((SENSIBLE_DEGREE, "blue"), (ABSURD_DEGREE, "green"))
Y_AXIS_LIMITS = (0, 14)


def main():
    """
    Drive the program.
    """
    data = load_dataset(DATA_FILE)
    features, target = split_features_and_target(data)
    features_train, features_test, target_train, target_test = (
        split_train_and_test(features, target))

    lowest = min(row[0] for row in features)
    highest = max(row[0] for row in features)
    smooth_x = smooth_x_values(lowest, highest, SMOOTH_POINTS)

    plt.scatter(features_train, target_train, color="black",
                label="Training data")
    plt.scatter(features_test, target_test, color="red",
                label="Unseen test data")
    for degree, colour in DEGREE_COLOURS:
        model = fit_polynomial(features_train, target_train, degree)
        plt.plot(smooth_x, model.predict(smooth_x), color=colour,
                 label=f"Degree {degree}")

    plt.title("A straight line learns; a wiggly curve memorizes")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.ylim(*Y_AXIS_LIMITS)
    plt.legend()
    print("Close the plot window to end the program.")
    plt.show()


if __name__ == "__main__":
    main()
