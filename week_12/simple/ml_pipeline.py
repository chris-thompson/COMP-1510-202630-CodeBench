"""
The six steps of a supervised machine learning workflow, as six functions.

from_scratch/ showed that a linear regression is arithmetic we can do
ourselves. This folder does the same job with scikit-learn, and the point is
how little code is left once a library does the work.

The workflow is always the same six steps, whatever the model:

    1. load the data
    2. separate the features from the target
    3. hold some data back for testing
    4. fit the model to the training data
    5. predict the values of the test data
    6. score those predictions against the truth

Two words used throughout. The features are what we know: the columns we
feed in. The target is what we want: the column we are trying to work out.
Here the feature is years of experience and the target is salary.

Step 3 is the one that is easy to skip and never should be. A model that is
scored on the same data it learned from is marking its own homework.

scikit-learn and pandas are not part of the standard library:

    pip3 install pandas scikit-learn
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

TEST_SIZE = 0.2
RANDOM_STATE = 0


def load_dataset(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    A DataFrame is a table: named, typed columns and numbered rows, rather
    like a spreadsheet Python can index. read_csv reads the header row for
    us and works out the type of each column.

    :param path: the name of a readable CSV file with a header row, in the
                 current working directory or named by a path
    :precondition: path must name a readable CSV file with a header row
    :postcondition: the file named by path is not modified
    :return: a pandas DataFrame with one column per CSV column

    >>> data = load_dataset("sample_data.csv")
    >>> list(data.columns)
    ['YearsExperience', 'Salary']
    >>> len(data)
    10
    """
    return pd.read_csv(path)


def split_features_and_target(data: pd.DataFrame) -> tuple:
    """
    Split a DataFrame into its feature columns and its target column.

    The convention followed here is that the target is the last column and
    everything before it is a feature. iloc selects by position: [:, :-1]
    means every row, every column but the last, and [:, -1] means every
    row, the last column only. The .values at the end hands back a plain
    array of numbers, which is what scikit-learn wants.

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

    Any model can recite the data it was trained on. The only honest
    question is how it does on data it has never seen, so we hide some
    before training begins and keep it hidden until scoring time.

    train_test_split shuffles before it cuts, so the test set is not simply
    the bottom of the file. Shuffling uses random numbers, and random_state
    fixes the seed, which is why this program gives the same answer every
    time it runs. That is a deliberate choice for teaching, and for any
    result someone else has to be able to reproduce.

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

    >>> features = [[1], [2], [3], [4], [5]]
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

    fit() is where the learning happens. It works out the same slope and
    intercept that from_scratch/linear_regression.py computed by hand, and
    stores them on the model as coef_ and intercept_.

    :param features_train: an array of training feature rows
    :param target_train: an array of training target values
    :precondition: features_train and target_train must have the same
                   number of rows
    :precondition: features_train must contain at least two distinct rows
    :return: a fitted LinearRegression

    >>> model = train_model([[1], [2], [3]], [2, 4, 6])
    >>> round(float(model.coef_[0]), 2)
    2.0
    >>> model = train_model([[0], [1], [2]], [1, 3, 5])
    >>> round(float(model.intercept_), 2)
    1.0
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

    >>> model = train_model([[1], [2], [3]], [2, 4, 6])
    >>> [round(float(value), 2) for value in make_predictions(model, [[4]])]
    [8.0]
    >>> len(make_predictions(model, [[4], [5]]))
    2
    """
    return model.predict(features)


def score_model(model: LinearRegression, features, target) -> float:
    """
    Score a fitted model against known answers, as an R-squared value.

    R-squared answers one question: how much of the variation in the target
    did the model account for? 1.0 is a perfect fit. 0.0 is no better than
    always guessing the average. A negative value is worse than guessing
    the average, which a model is quite capable of being.

    :param model: a fitted LinearRegression
    :param features: an array of feature rows
    :param target: an array of the true target values for those rows
    :precondition: model must already have been fitted
    :precondition: features and target must have the same number of rows
    :return: the R-squared value of the model's predictions

    >>> model = train_model([[1], [2], [3]], [2, 4, 6])
    >>> score_model(model, [[1], [2], [3]], [2, 4, 6])
    1.0
    >>> round(score_model(model, [[1], [2], [3]], [6, 4, 2]), 1)
    -3.0
    """
    return model.score(features, target)
