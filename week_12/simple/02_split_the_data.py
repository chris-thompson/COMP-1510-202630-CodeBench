"""
First steps with ML!
"""

import pandas as pd
from sklearn.model_selection import train_test_split


def main():
    """
    Drive the program.
    """
    data = pd.read_csv('sample_data.csv')
    print(data)
    features = data.iloc[:, :-1].values
    target = data.iloc[:, 1].values
    print(features)
    print(target)
    features_train, features_test, target_train, target_test = (
        train_test_split(features, target, test_size=0.2, random_state=0))
    print(features_train)
    print(features_test)
    print(target_train)
    print(target_test)


if __name__ == '__main__':
    main()
