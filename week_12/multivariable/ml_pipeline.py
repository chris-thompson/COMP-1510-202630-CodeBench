"""
The same six steps as simple/, with three features instead of one.

Read simple/ first. Then read this file and notice how little has changed.

The functions here are, with one addition, the same functions as the ones in
simple/ml_pipeline.py. That is the lesson, not an oversight. In simple/ the
model had one feature to work with, years of experience. Here it has three:
years of experience, age, and education level. The workflow does not care.
fit() still takes features and a target, predict() still takes features, and
score() still returns an R-squared.

What changes is only the shape of the data going in. A feature row was
[3.2]; now it is [3.2, 28, 3]. The model learns one coefficient per feature
rather than a single slope, and the straight line becomes a flat plane
through a space we can no longer draw. Everything else is untouched.

The addition is evaluate_model, which reports three different measures of
error rather than one, because with several features it becomes worth asking
in what way a model is wrong, not just how much.

    pip3 install pandas scikit-learn
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (mean_absolute_error, mean_squared_error,
                             r2_score)
from sklearn.model_selection import train_test_split

TEST_SIZE = 0.2
RANDOM_STATE = 0


def load_dataset(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    :param path: the name of a readable CSV file with a header row
    :precondition: path must name a readable CSV file with a header row
    :postcondition: the file named by path is not modified
    :return: a pandas DataFrame with one column per CSV column

    >>> data = load_dataset("sample_data.csv")
    >>> list(data.columns)
    ['YearsExperience', 'Age', 'EducationLevel', 'Salary']
    >>> len(data)
    10
    """
    return pd.read_csv(path)


def split_features_and_target(data: pd.DataFrame) -> tuple:
    """
    Split a DataFrame into its feature columns and its target column.

    The code is identical to the single-feature version. iloc[:, :-1] means
    every column but the last, whether that is one column or a hundred.

    :param data: a pandas DataFrame of at least two columns
    :precondition: data must be a DataFrame whose last column is the target
    :postcondition: data is unchanged
    :return: a tuple of the feature array and the target array

    >>> table = pd.DataFrame({"a": [1.0, 2.0], "b": [3.0, 4.0],
    ...                       "y": [5.0, 6.0]})
    >>> features, target = split_features_and_target(table)
    >>> features.tolist()
    [[1.0, 3.0], [2.0, 4.0]]
    >>> target.tolist()
    [5.0, 6.0]
    """
    return data.iloc[:, :-1].values, data.iloc[:, -1].values


def split_train_and_test(features, target, test_size: float = TEST_SIZE,
                         random_state: int = RANDOM_STATE) -> tuple:
    """
    Hold part of the data back so the model can be tested on data it never saw.

    :param features: an array of feature rows
    :param target: an array of target values, one per feature row
    :param test_size: the proportion of the data to hold back, between 0
                      and 1 exclusive
    :param random_state: an integer seed for the shuffle
    :precondition: features and target must have the same number of rows
    :precondition: test_size must be between 0 and 1 exclusive
    :precondition: random_state must be an integer
    :return: a tuple of four arrays: the training features, the test
             features, the training targets, and the test targets

    >>> features = [[1, 9], [2, 8], [3, 7], [4, 6], [5, 5]]
    >>> target = [2, 4, 6, 8, 10]
    >>> parts = split_train_and_test(features, target, test_size=0.4)
    >>> len(parts)
    4
    >>> len(parts[0]), len(parts[1])
    (3, 2)
    """
    return train_test_split(features, target, test_size=test_size,
                            random_state=random_state)


def train_model(features_train, target_train) -> LinearRegression:
    """
    Fit a linear regression to the training data.

    With three features the model learns three coefficients rather than one
    slope, so coef_ is an array of three numbers. The call is unchanged.

    :param features_train: an array of training feature rows
    :param target_train: an array of training target values
    :precondition: features_train and target_train must have the same
                   number of rows
    :precondition: features_train must contain at least two distinct rows
    :return: a fitted LinearRegression

    >>> model = train_model([[1, 0], [2, 0], [3, 1]], [2, 4, 6])
    >>> len(model.coef_)
    2
    >>> model = train_model([[1, 9], [2, 8], [3, 7]], [2, 4, 6])
    >>> round(float(model.predict([[4, 6]])[0]), 2)
    8.0
    """
    model = LinearRegression()
    model.fit(features_train, target_train)
    return model


def make_predictions(model: LinearRegression, features):
    """
    Predict a target value for every row of features.

    :param model: a fitted LinearRegression
    :param features: an array of feature rows with the same number of
                     columns the model was trained on
    :precondition: model must already have been fitted
    :precondition: features must have the same number of columns as the
                   training features
    :return: an array of one predicted target value per feature row

    >>> model = train_model([[1, 9], [2, 8], [3, 7]], [2, 4, 6])
    >>> len(make_predictions(model, [[4, 6], [5, 5]]))
    2
    >>> [round(float(value)) for value in make_predictions(model, [[4, 6]])]
    [8]
    """
    return model.predict(features)


def evaluate_model(target_true, target_predicted) -> dict:
    """
    Measure how wrong a model's predictions were, three different ways.

    R-squared says how much of the variation the model accounted for, and
    is the easiest of the three to compare between models. The mean
    absolute error is the average size of a miss, in the units of the
    target, so it is the one to quote to somebody who wants an answer in
    dollars. The mean squared error squares each miss before averaging,
    which makes it much less forgiving of a single very bad prediction.

    :param target_true: an array of the true target values
    :param target_predicted: an array of predicted values, one per true
                             value
    :precondition: target_true and target_predicted must be the same length
    :precondition: target_true must contain at least two distinct values
    :return: a dictionary with the keys "r2", "mae", and "mse"

    >>> scores = evaluate_model([1.0, 2.0, 3.0], [1.0, 2.0, 3.0])
    >>> scores["r2"], scores["mae"], scores["mse"]
    (1.0, 0.0, 0.0)
    >>> scores = evaluate_model([1.0, 2.0, 3.0], [2.0, 2.0, 4.0])
    >>> round(scores["mae"], 2), round(scores["mse"], 2)
    (0.67, 0.67)
    """
    return {
        "r2": r2_score(target_true, target_predicted),
        "mae": mean_absolute_error(target_true, target_predicted),
        "mse": mean_squared_error(target_true, target_predicted),
    }
