"""
Fitting curves of any degree, to watch a model memorize instead of learn.

A degree 1 model is the straight line from simple/. Raise the degree and the
model is allowed to bend: degree 2 can make one bend, degree 3 two bends, and
by degree 6 it can wander wherever it likes.

More freedom sounds like an improvement. It is a trap. Given enough freedom a
model will thread its way through every training point exactly, noise and all,
and score a perfect 1.0 on the data it learned from. It has not found the
pattern. It has memorized the answers, and it falls apart the moment it is
shown a point it has not seen before.

That failure has a name: overfitting. It is the single most important idea in
this hour, and the reason the train/test split in simple/ was not optional.

PolynomialFeatures adds the extra columns a bend needs, LinearRegression fits
them, and make_pipeline chains the two into one model that still answers to
fit, predict, and score.

    pip3 install pandas scikit-learn matplotlib
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

TEST_SIZE = 0.3
RANDOM_STATE = 1
SENSIBLE_DEGREE = 1
ABSURD_DEGREE = 6


def load_dataset(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    :param path: the name of a readable CSV file with a header row
    :precondition: path must name a readable CSV file with a header row
    :postcondition: the file named by path is not modified
    :return: a pandas DataFrame with one column per CSV column

    >>> data = load_dataset("sample_data.csv")
    >>> list(data.columns)
    ['x', 'y']
    >>> len(data)
    10
    """
    return pd.read_csv(path)


def split_features_and_target(data: pd.DataFrame) -> tuple:
    """
    Split a DataFrame into its feature columns and its target column.

    :param data: a pandas DataFrame of at least two columns
    :precondition: data must be a DataFrame whose last column is the target
    :postcondition: data is unchanged
    :return: a tuple of the feature array and the target array

    >>> table = pd.DataFrame({"x": [1.0, 2.0], "y": [3.0, 4.0]})
    >>> features, target = split_features_and_target(table)
    >>> features.tolist()
    [[1.0], [2.0]]
    >>> target.tolist()
    [3.0, 4.0]
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

    >>> parts = split_train_and_test([[1], [2], [3], [4]], [1, 2, 3, 4],
    ...                              test_size=0.5)
    >>> len(parts[0]), len(parts[1])
    (2, 2)
    """
    return train_test_split(features, target, test_size=test_size,
                            random_state=random_state)


def fit_polynomial(features_train, target_train, degree: int):
    """
    Fit a polynomial curve of the given degree to the training data.

    Degree 1 is a straight line and cannot bend at all. Every degree above
    that buys the curve another bend to spend on getting closer to the
    training points.

    :param features_train: an array of single-column training feature rows
    :param target_train: an array of training target values
    :param degree: an integer of 1 or greater
    :precondition: features_train and target_train must have the same
                   number of rows
    :precondition: degree must be an integer of 1 or greater
    :return: a fitted model that answers to predict and score

    >>> model = fit_polynomial([[0], [1], [2]], [0.0, 1.0, 4.0], 2)
    >>> round(float(model.predict([[3]])[0]), 2)
    9.0
    >>> model = fit_polynomial([[0], [1], [2]], [0.0, 2.0, 4.0], 1)
    >>> round(model.score([[0], [1], [2]], [0.0, 2.0, 4.0]), 2)
    1.0
    """
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(features_train, target_train)
    return model


def smooth_x_values(lowest: float, highest: float, count: int) -> list:
    """
    Build evenly spaced feature rows spanning a range, for drawing a curve.

    A curve drawn through only the ten data points would look like ten
    straight segments. Asking the model for its answer at two hundred
    evenly spaced points instead makes the curve look like a curve.

    :param lowest: a real number
    :param highest: a real number greater than lowest
    :param count: an integer of 2 or greater
    :precondition: highest must be greater than lowest
    :precondition: count must be an integer of 2 or greater
    :postcondition: the first row is lowest and the last row is highest
    :return: a list of count single-value lists, evenly spaced from lowest
             to highest inclusive

    >>> smooth_x_values(0.0, 1.0, 3)
    [[0.0], [0.5], [1.0]]
    >>> smooth_x_values(0.0, 3.0, 2)
    [[0.0], [3.0]]
    """
    step = (highest - lowest) / (count - 1)
    return [[lowest + step * index] for index in range(count)]
