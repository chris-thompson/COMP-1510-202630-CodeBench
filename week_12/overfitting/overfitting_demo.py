"""
Watch a model memorize instead of learn, in two numbers per model.

sample_data.csv is deliberately small and deliberately noisy: ten points
that trend upwards, with enough scatter that a curve free to bend can reach
almost every one of them.

Two models are fitted to the same seven training points. Read the two scores
each one reports as a pair, because neither means much on its own:

    a high training score alone      proves nothing
    a high training score and a
    low test score together          is overfitting, caught in the act

Run overfitting_plot.py afterwards to see the same result as a picture.
"""

from polynomial_fit import (ABSURD_DEGREE, SENSIBLE_DEGREE, fit_polynomial,
                            load_dataset, split_features_and_target,
                            split_train_and_test)

DATA_FILE = "sample_data.csv"


def main():
    """
    Drive the program.
    """
    data = load_dataset(DATA_FILE)
    features, target = split_features_and_target(data)
    features_train, features_test, target_train, target_test = (
        split_train_and_test(features, target))

    print(f"{len(features_train)} points to learn from, "
          f"{len(features_test)} held back.\n")

    for degree in (SENSIBLE_DEGREE, ABSURD_DEGREE):
        model = fit_polynomial(features_train, target_train, degree)
        training_score = model.score(features_train, target_train)
        test_score = model.score(features_test, target_test)
        shape = "a straight line" if degree == 1 else "a wiggly curve"
        print(f"Degree {degree}, {shape}:")
        print(f"  R-squared on the training data:    {training_score:>8.2f}")
        print(f"  R-squared on the unseen test data: {test_score:>8.2f}\n")

    print("The straight line scores about the same on both, which is what")
    print("learning looks like. The curve scores a perfect 1.00 on the data")
    print("it memorized and worse than useless on the data it did not: a")
    print("negative R-squared is worse than having guessed the average.")


if __name__ == "__main__":
    main()
