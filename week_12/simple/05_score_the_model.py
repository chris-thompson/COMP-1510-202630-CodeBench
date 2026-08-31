"""
Step 5 of 6: score the model, on data it learned from and on data it did not.

score() returns the R-squared value: 1.0 is a perfect fit, 0.0 is no better
than always guessing the average, and a negative number is worse than
guessing the average.

The two scores below are the reason step 2 mattered. The training score is
the model marking its own homework. The test score is the one that means
something, because those two rows were hidden while it learned.
"""

from ml_pipeline import (load_dataset, split_features_and_target,
                         split_train_and_test, train_model, score_model)

DATA_FILE = "sample_data.csv"


def main():
    """
    Drive the program.
    """
    data = load_dataset(DATA_FILE)
    features, target = split_features_and_target(data)
    features_train, features_test, target_train, target_test = (
        split_train_and_test(features, target))
    model = train_model(features_train, target_train)

    training_score = score_model(model, features_train, target_train)
    test_score = score_model(model, features_test, target_test)

    print(f"R-squared on the training data: {training_score:.2f}")
    print(f"R-squared on the unseen test data: {test_score:.2f}")
    print("\nThese two are close together, which is what we want to see.")
    print("When the training score is far higher than the test score, the")
    print("model has memorized rather than learned. That has a name, and")
    print("the overfitting/ folder is where we watch it happen.")


if __name__ == "__main__":
    main()
