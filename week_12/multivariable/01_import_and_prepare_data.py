"""
Step 1 of 5: read a table with three feature columns instead of one.

simple/ predicted salary from years of experience alone. This folder adds
age and education level, so each row of features is now three numbers wide.

Everything else about the workflow is about to stay exactly the same. Watch
for how little the code changes as the five steps go by.
"""

from ml_pipeline import load_dataset, split_features_and_target

DATA_FILE = "sample_data.csv"


def main():
    """
    Drive the program.
    """
    data = load_dataset(DATA_FILE)
    print("The whole table. Four columns now, not two:")
    print(data)

    features, target = split_features_and_target(data)
    print("\nThe features. Three columns: experience, age, education:")
    print(features)
    print("\nThe target is still one column, the salary:")
    print(target)


if __name__ == "__main__":
    main()
