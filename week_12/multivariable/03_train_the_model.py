"""
Step 3 of 5: fit the model. The call is identical to the one in simple/.

One line of code learns from three columns as readily as from one. What
changes is what comes out: coef_ now holds three numbers, one for each
feature, saying how much that feature moves the prediction.

With one feature the model was a straight line. With three it is a flat
plane through a space we cannot draw, which is why step 5 reports numbers
rather than a picture.
"""

from ml_pipeline import (load_dataset, split_features_and_target,
                         split_train_and_test, train_model)

DATA_FILE = "sample_data.csv"
FEATURE_NAMES = ("years of experience", "age", "education level")


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
    print(f"  {model}\n")
    print("One coefficient per feature, in the order the columns appear:")
    for name, coefficient in zip(FEATURE_NAMES, model.coef_):
        print(f"  {name:>20}: {coefficient:>12.2f}")
    print(f"  {'intercept':>20}: {model.intercept_:>12.2f}")


if __name__ == "__main__":
    main()
