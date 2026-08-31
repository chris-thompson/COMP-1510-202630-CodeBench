"""
Step 4 of 6: predict the salaries of the two rows the model never saw.

predict() takes feature rows and hands back one predicted target for each.
We give it the test features, which have been hidden since step 2, and then
put the predictions beside the true answers to see how close they came.
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
    print(f"  {'years':>6}  {'predicted':>10}  {'actual':>10}  {'gap':>10}")
    for years, guess, actual in zip(features_test, predicted, target_test):
        print(f"  {years[0]:>6}  {guess:>10.2f}  {actual:>10.2f}  "
              f"{actual - guess:>10.2f}")
    print("\nClose is not a number. Step 5 turns 'close' into one.")


if __name__ == "__main__":
    main()
