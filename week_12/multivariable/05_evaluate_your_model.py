"""
Step 5 of 5: measure the error three ways, and compare with simple/.

R-squared is the headline number. The mean absolute error is the average
size of a miss, in dollars, which is the figure to quote to somebody who
wants to know what the model is worth. The mean squared error squares each
miss first, so one badly wrong prediction weighs far more heavily.

Run simple/05_score_the_model.py beside this one. Three features score a
little better than one on this data. A little, not a lot, and on ten rows
that difference is well within the range of luck. More columns are not
automatically a better model; they are only more to learn from.
"""

from ml_pipeline import (load_dataset, split_features_and_target,
                         split_train_and_test, train_model, make_predictions,
                         evaluate_model)

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

    scores = evaluate_model(target_test, predicted)
    print("Scored against the two rows the model never saw:\n")
    print(f"  R-squared           : {scores['r2']:>12.2f}")
    print(f"  Mean absolute error : {scores['mae']:>12.2f}")
    print(f"  Mean squared error  : {scores['mse']:>12.2f}")
    print(f"\nOn average this model is about ${scores['mae']:,.0f} out.")


if __name__ == "__main__":
    main()
