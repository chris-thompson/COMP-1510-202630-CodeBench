"""
First steps with ML!
"""

import pandas as pd


def main():
    """
    Drive the program.
    """
    data = pd.read_csv('sample_data.csv')
    print(data)
    features = data.iloc[:, :-1].values
    target = data.iloc[:, -1].values
    print(features)
    print(target)


if __name__ == '__main__':
    main()
