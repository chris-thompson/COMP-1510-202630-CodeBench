"""
Demonstrate the conditional expression, also called the ternary operator.

X if C else Y evaluates the condition C first. If C is True, the whole
expression is X. Otherwise, the whole expression is Y.
"""


def describe_age(age):
    """
    Describe an age as minor or adult.

    :param age: an int greater than or equal to zero
    :precondition: age is an int greater than or equal to zero
    :return: the string 'minor' if age is less than 21, otherwise 'adult'

    >>> describe_age(12)
    'minor'
    >>> describe_age(21)
    'adult'
    >>> describe_age(0)
    'minor'
    """
    return 'minor' if age < 21 else 'adult'


def main():
    """
    Drive the program.
    """
    for age in [12, 20, 21, 68]:
        print(f'At age {age} you are considered: {describe_age(age)}')


if __name__ == "__main__":
    main()
