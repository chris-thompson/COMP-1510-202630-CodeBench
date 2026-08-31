def find_two_smallest(some_list):
    """
    Return a tuple that contains the sorted indices of the two smallest values
    in some_list.

    :param some_list: a list of numbers
    :precondition: some_list contains at least two elements
    :postcondition: some_list is unchanged
    :return: a tuple of the indices of the two smallest values, in
        ascending order

    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    """

    # Suggested approach
    # Find the index of the minimum item in L
    # Remove that item from the list
    # Find the index of the new minimum item in the list
    # Put the smallest item back in the list
    # If necessary, adjust the second index
    # Return the two indices
