"""
Step 1 of 6: read the data and separate the features from the target.

Every machine learning program starts here. Before anything can be learned,
the data has to be in memory and split into the columns we know (the
features) and the column we want (the target).

Run each of the six numbered files in this folder in order. Each one repeats
the steps before it and adds exactly one more, so the output grows a little
at a time and nothing appears without having been explained first.
"""

from ml_pipeline import load_dataset, split_features_and_target

DATA_FILE = "sample_data.csv"


def main():
    """
    Drive the program.
    """
    data = load_dataset(DATA_FILE)
    print("The whole table, as pandas read it:")
    print(data)

    features, target = split_features_and_target(data)
    print("\nThe features. One row per person, one column per thing we know:")
    print(features)
    print("\nThe target. The salary we are trying to predict:")
    print(target)


if __name__ == "__main__":
    main()
