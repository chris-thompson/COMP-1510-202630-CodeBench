"""
First steps with ML!
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


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
    regressor = LinearRegression()
    regressor.fit(features_train, target_train)
    print(regressor)
    print(regressor.__doc__)
    predicted_values = regressor.predict(features_test)
    print(predicted_values)
    print(target_test)


if __name__ == '__main__':
    main()
