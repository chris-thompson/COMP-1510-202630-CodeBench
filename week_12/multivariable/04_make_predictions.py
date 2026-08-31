"""
Step 4 of 5: predict the two hidden rows.

predict() is unchanged. It takes feature rows and returns one number for
each, whether a row is one number wide or three.
"""

from ml_pipeline import (load_dataset, split_features_and_target,
                         split_train_and_test, train_model, make_predictions)

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

    predicted = make_predictions(model, features_test)

    print("Predictions for the two rows the model never saw:\n")
    print(f"  {'features':>20}  {'predicted':>10}  {'actual':>10}  "
          f"{'gap':>10}")
    for row, guess, actual in zip(features_test, predicted, target_test):
        described = f"{row[0]}y {row[1]:.0f}yo lvl{row[2]:.0f}"
        print(f"  {described:>20}  {guess:>10.2f}  {actual:>10.2f}  "
              f"{actual - guess:>10.2f}")


if __name__ == "__main__":
    main()
