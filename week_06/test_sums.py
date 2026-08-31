"""
Unit-test running_sum with pytest.

We always try to identify the disjoint equivalence partitions: an empty
list, a single item, and lists of negative, zero, positive, and mixed
values. running_sum modifies its list in place, so each test builds a list,
runs the function, and then asserts on the same list. Each test makes
exactly one assertion using a plain assert.
"""

import week_06.sums as sums


def test_running_sum_empty():
    values = []
    sums.running_sum(values)
    assert values == []


def test_running_sum_one_item():
    values = [5]
    sums.running_sum(values)
    assert values == [5]


def test_running_sum_two_items():
    values = [2, 5]
    sums.running_sum(values)
    assert values == [2, 7]


def test_running_sum_multi_negative():
    values = [-1, -5, -3, -4]
    sums.running_sum(values)
    assert values == [-1, -6, -9, -13]


def test_running_sum_multi_zeros():
    values = [0, 0, 0, 0]
    sums.running_sum(values)
    assert values == [0, 0, 0, 0]


def test_running_sum_multi_positive():
    values = [4, 2, 3, 6]
    sums.running_sum(values)
    assert values == [4, 6, 9, 15]


def test_running_sum_multi_mix():
    values = [4, 0, 2, -5, 0]
    sums.running_sum(values)
    assert values == [4, 4, 6, 1, 1]
