"""
Step 2 of 5: hold two rows back for testing, exactly as before.

The split does not care how many feature columns there are. It shuffles the
rows and cuts them into a training set and a test set, keeping each row's
features and its target together.
"""

from ml_pipeline import (load_dataset, split_features_and_target,
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

    print(f"{len(features)} rows in total, split 80/20 after shuffling.\n")
    print(f"Training features ({len(features_train)} rows):")
    print(features_train)
    print("\nTraining targets:")
    print(target_train)
    print(f"\nTest features ({len(features_test)} rows), hidden until "
          f"scoring time:")
    print(features_test)
    print("\nTest targets:")
    print(target_test)


if __name__ == "__main__":
    main()
