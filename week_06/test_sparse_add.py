"""
Unit-test sparse_add with pytest.

A sparse vector stores only its non-zero entries as a dictionary. These
tests follow the usual rhythm: assemble the two input vectors, state the
expected result, run the function, and assert. Each test makes one
assertion with a plain assert; dictionary equality ignores key order, so
the expected dictionary may list its keys in any order.
"""

from week_06.sparse_add import sparse_add


def test_sparse_add_same_single_index():
    vector_one = {1: 1, "length": 400}
    vector_two = {"length": 400, 1: 1}
    assert sparse_add(vector_one, vector_two) == {1: 2, "length": 400}


def test_sparse_add_different_single_index():
    vector_one = {1: 1, "length": 400}
    vector_two = {2: 1, "length": 400}
    assert sparse_add(vector_one, vector_two) == {1: 1, 2: 1, "length": 400}


def test_sparse_add_overlapping_indices():
    vector_one = {1: 1, 3: 2, 5: 1, "length": 400}
    vector_two = {3: 2, 4: 2, 5: 2, "length": 400}
    expected = {1: 1, 3: 4, 4: 2, 5: 3, "length": 400}
    assert sparse_add(vector_one, vector_two) == expected
