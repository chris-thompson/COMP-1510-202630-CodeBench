"""
Step 6 of 6: draw the result.

Two plots, and they should be read as a pair. The first shows the line
against the data it was fitted to. The second shows the same line, drawn
across the same range, against the two points it had never seen.

The line does not move between the plots. Only the points do. That is the
whole idea of a train/test split in one picture.

    pip3 install matplotlib
"""

import matplotlib.pyplot as plt

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

    line_of_best_fit = make_predictions(model, features)
    print("Close each plot window to see the next one.")

    plt.scatter(features_train, target_train, color="red",
                label="Training data")
    plt.plot(features, line_of_best_fit, color="blue", label="The model")
    plt.title("Salary versus experience: the data the model learned from")
    plt.xlabel("Years of experience")
    plt.ylabel("Salary")
    plt.legend()
    plt.show()

    plt.scatter(features_test, target_test, color="green",
                label="Unseen test data")
    plt.plot(features, line_of_best_fit, color="blue", label="The model")
    plt.title("The same line, against the two rows it never saw")
    plt.xlabel("Years of experience")
    plt.ylabel("Salary")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
