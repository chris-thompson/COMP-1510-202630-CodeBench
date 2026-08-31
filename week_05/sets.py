"""
Working with sets.
"""


def main():
    """
    Drive the program.
    """
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket)  # Duplicates have been removed!
    print(len(basket))

    for item in basket:
        print(item)

    print('apple' in basket)

    basket.remove('apple')
    basket.discard('apricot')  # WOW!
    print(basket)

    basket.add('apricot')
    print(basket)

    basket = {'apple', 'orange', 'banana'}
    basket.update(['apricot', 'mango', 'grapefruit'])
    print(basket)

    basket.clear()
    print(basket)

    some_fruit = {'apple', 'orange', 'banana'}
    other_fruit = {'grapefruit', 'lime', 'banana'}
    print('Union:', some_fruit.union(other_fruit))
    print('Intersection:', some_fruit.intersection(other_fruit))
    print('Difference:', some_fruit.difference(other_fruit))
    print('Symmetric Difference:',
          some_fruit.symmetric_difference(other_fruit))
    print('Subset:', {'apple'}.issubset(some_fruit))
    print('Superset:', some_fruit.issuperset({'apple', 'banana'}))

    # Set elements must be immutable (hashable): a tuple works, a list does not
    set_of_size_one = {(1, 2, 3)}
    print(set_of_size_one)

    # A frozenset is an immutable set, so it can even live inside another set
    weekend = frozenset(['Saturday', 'Sunday'])
    print(weekend)
    print('Saturday' in weekend)
    print({frozenset(['a', 'b']), frozenset(['c'])})


if __name__ == '__main__':
    main()
