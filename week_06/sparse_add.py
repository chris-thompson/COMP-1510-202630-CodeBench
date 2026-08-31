"""
Add two sparse vectors represented as dictionaries.

A sparse vector stores only its non-zero entries. Each vector is a
dictionary that maps an integer index to its value, plus a special
"length" key that records the full length of the vector.
"""


def sparse_add(vector_one, vector_two):
    """
    Add two sparse vectors and return their sum as a new sparse vector.

    :param vector_one: a dict mapping int indices to int values, plus a
                       "length" key
    :param vector_two: a dict mapping int indices to int values, plus a
                       "length" key
    :precondition: both vectors share the same "length" value
    :precondition: every key is either the string "length" or a
                   non-negative int index
    :postcondition: vector_one and vector_two are unchanged
    :return: a new dict whose index values are the sums of the two
             inputs' values

    >>> sparse_add({1: 1, 'length': 400}, {1: 1, 'length': 400})
    {'length': 400, 1: 2}
    >>> sparse_add({1: 1, 'length': 400}, {2: 1, 'length': 400})
    {'length': 400, 1: 1, 2: 1}
    """
    result = {"length": vector_one["length"]}
    for index in vector_one:
        if index != "length":
            result[index] = vector_one[index]
    for index in vector_two:
        if index != "length":
            result[index] = result.get(index, 0) + vector_two[index]
    return result


def main():
    """Drive the program."""
    print(sparse_add({1: 1, "length": 400}, {2: 1, "length": 400}))


if __name__ == "__main__":
    main()
