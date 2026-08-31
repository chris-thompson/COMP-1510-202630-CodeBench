"""
Working with the Boolean operators and, or, and not.

An expression that uses and is only True when both operands are True.
An expression that uses or is True when at least one operand is True.
The not operator flips True to False and False to True.

Python also short-circuits: if the left operand of and or or already
decides the answer, the right operand is never evaluated.
"""

MINIMUM_SALARY = 30000.0
MINIMUM_YEARS = 2


def qualifies_for_loan(salary, years_on_job):
    """
    Determine whether an applicant qualifies for the standard loan.

    An applicant must meet the minimum salary and the minimum years of
    employment.

    :param salary: the applicant's annual salary as a float
    :param years_on_job: the applicant's whole years of employment as an int
    :precondition: salary is a non-negative number
    :precondition: years_on_job is a non-negative integer
    :return: True if the applicant qualifies, else False

    >>> qualifies_for_loan(50000.0, 3)
    True
    >>> qualifies_for_loan(50000.0, 1)
    False
    >>> qualifies_for_loan(30000.0, 2)
    True
    """
    return salary >= MINIMUM_SALARY and years_on_job >= MINIMUM_YEARS


def qualifies_for_flexible_loan(salary, years_on_job):
    """
    Determine whether an applicant qualifies for the flexible loan.

    An applicant must meet the minimum salary or the minimum years of
    employment.

    :param salary: the applicant's annual salary as a float
    :param years_on_job: the applicant's whole years of employment as an int
    :precondition: salary is a non-negative number
    :precondition: years_on_job is a non-negative integer
    :return: True if the applicant qualifies, else False

    >>> qualifies_for_flexible_loan(50000.0, 0)
    True
    >>> qualifies_for_flexible_loan(0.0, 2)
    True
    >>> qualifies_for_flexible_loan(0.0, 0)
    False
    """
    return salary >= MINIMUM_SALARY or years_on_job >= MINIMUM_YEARS


def is_positive(number):
    """
    Report whether number is greater than zero.

    The printed message proves the check actually ran, which lets us
    watch short-circuiting happen in main().

    :param number: an int or a float
    :postcondition: a message naming number is printed
    :return: True if number is greater than zero, else False

    >>> is_positive(7)
    Checking 7
    True
    >>> is_positive(-2)
    Checking -2
    False
    >>> is_positive(0)
    Checking 0
    False
    """
    print('Checking', number)
    return number > 0


def main():
    """
    Drive the program.
    """
    print('Both operands are evaluated when the left one is True:')
    print(is_positive(5) and is_positive(10))

    print('\nShort-circuiting: the left operand is False, so and stops early:')
    print(is_positive(-5) and is_positive(10))

    print('\nor short-circuits too: the left is True, so or stops early:')
    print(is_positive(5) or is_positive(10))

    print('\nnot flips a Boolean value:')
    print(not qualifies_for_loan(50000.0, 3))


if __name__ == '__main__':
    main()
