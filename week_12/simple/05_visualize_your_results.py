"""
First steps with ML!
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


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

    # Visualizing the training data
    plt.scatter(features_train, target_train, color='red')
    plt.plot(features_train, regressor.predict(features_train), color='blue')
    plt.title('Salary vs Experience (Training Data)')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.show()

    # Visualizing the test data
    plt.scatter(features_test, target_test, color='red')
    plt.plot(features_train, regressor.predict(features_train), color='blue')
    plt.title('Salary vs Experience (Test Data)')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.show()


if __name__ == '__main__':
    main()
