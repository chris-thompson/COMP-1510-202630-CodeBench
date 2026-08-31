"""
Step 2 of 6: hold some of the data back for testing.

This is the step it is tempting to skip. If we train on all ten rows and
then score the model on those same ten rows, we have learned nothing except
that the model can recite what it was shown.

So we hide two rows before training begins. The model never sees them, and
at the end they are the only honest test of whether it learned anything.
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
    print(f"Training features ({len(features_train)} rows) "
          f"-- the model will see these:")
    print(features_train)
    print("\nTraining targets, the answers that go with them:")
    print(target_train)
    print(f"\nTest features ({len(features_test)} rows) "
          f"-- hidden until scoring time:")
    print(features_test)
    print("\nTest targets, the answers we will check against:")
    print(target_test)


if __name__ == "__main__":
    main()
