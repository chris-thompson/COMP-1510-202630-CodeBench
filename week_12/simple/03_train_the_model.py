"""
Step 3 of 6: fit the model to the training data.

This is the whole of the learning, and it is one line: model.fit().

What comes out is the same pair of numbers we computed by hand in
from_scratch/, a slope and an intercept. scikit-learn calls them coef_ and
intercept_, and the trailing underscore is its convention for "this was
learned from data, it was not given to us".
"""

from ml_pipeline import (load_dataset, split_features_and_target,
                         split_train_and_test, train_model)

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

    print("The model, fitted:")
    print(f"  {model}")
    print("\nWhat it learned from the training data:")
    print(f"  slope     (coef_)      = {model.coef_[0]:.2f}")
    print(f"  intercept (intercept_) = {model.intercept_:.2f}")
    print("\nThat is the same kind of answer from_scratch/ worked out by "
          "hand,\nfrom eight rows here rather than all ten.")


if __name__ == "__main__":
    main()
