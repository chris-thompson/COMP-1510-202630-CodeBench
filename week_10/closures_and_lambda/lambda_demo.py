"""
Demonstrate the lambda.

A lambda is a small anonymous function. It can accept any number of arguments,
but it contains exactly one expression, and it returns the value of that
expression without a return statement.

    lambda arguments: expression

A lambda is not a different kind of thing from a def. Both build a function
structure. The lambda simply has no name and no room for a body, so we reach
for it when a function is needed briefly, in one line, and naming it would add
noise rather than meaning.

Where lambdas earn their keep is as an argument to another function. We have
been doing this since Week 4, when we passed a key function to sorted.
"""

STUDENT_SCORES = [("Ursula", 88), ("Arthur", 71), ("Inid", 95), ("Oliver", 71)]


def double_with_def(number: int) -> int:
    """
    Double a number, written the usual way, with def.

    :param number: the number to double
    :precondition: number must be an integer
    :postcondition: calculate twice number without modifying any argument
    :return: twice number as an integer

    >>> double_with_def(5)
    10
    >>> double_with_def(0)
    0
    """
    return number * 2


def sort_by_score(records: list) -> list:
    """
    Sort name and score pairs into ascending order of score.

    sorted needs a function that, given one element of the list, returns the
    value to sort on. That function is needed once, it is one expression long,
    and a name for it would tell us nothing the code does not already say.
    This is exactly what a lambda is for.

    :param records: a list of (name, score) tuples
    :precondition: records must be a list of two-element tuples
    :precondition: the second element of each tuple must be a number
    :postcondition: build a new sorted list, leaving records unmodified
    :return: a new list of the tuples, ordered by score

    >>> sort_by_score([("Inid", 95), ("Arthur", 71)])
    [('Arthur', 71), ('Inid', 95)]
    >>> sort_by_score([("Arthur", 71), ("Oliver", 71)])
    [('Arthur', 71), ('Oliver', 71)]
    >>> sort_by_score([])
    []
    """
    return sorted(records, key=lambda record: record[1])


def sort_by_length(words: list) -> list:
    """
    Sort words into ascending order of length.

    There is no lambda here, on purpose. The function we need already exists
    and is called len, so writing key=lambda word: len(word) would be a longer
    way of saying key=len. Reach for a lambda when no function already does
    the job, not by reflex.

    :param words: a list of strings
    :precondition: words must be a list of strings
    :postcondition: build a new sorted list, leaving words unmodified
    :return: a new list of the words, ordered by length

    Note the tie below. "banana" and "cherry" are both six letters long, and
    sorted is stable, so they keep the order they arrived in.

    >>> sort_by_length(["banana", "fig", "cherry"])
    ['fig', 'banana', 'cherry']
    >>> sort_by_length(["fig"])
    ['fig']
    >>> sort_by_length([])
    []
    """
    return sorted(words, key=len)


def main():
    """
    Drive the program. Demonstrate lambdas, and when not to use one.
    """
    # A lambda builds a function structure, exactly as def does. Both of these
    # print something like <function ...>, and both can be called.
    double_with_lambda = lambda number: number * 2
    print(double_with_def)
    print(double_with_lambda)
    print(double_with_def(21), double_with_lambda(21))

    # Note, though, that PEP 8 asks us not to do what we did above. Run a
    # linter over this file, and it offers warning E731: "do not assign
    # a lambda expression, use a def". PyCharm underlines it too.
    #
    # We will follow this rule. If a function deserves a name, give it a def.
    # Naming a lambda gets us the drawbacks of both, including a useless
    # name in every traceback and debugger frame it appears in:
    print(double_with_lambda.__name__)

    print(sort_by_score(STUDENT_SCORES))
    print(sort_by_length(["banana", "fig", "cherry", "kiwi"]))

    # The original list is untouched. sorted always builds a new list.
    print(STUDENT_SCORES)


if __name__ == "__main__":
    main()
