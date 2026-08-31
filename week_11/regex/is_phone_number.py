"""
Introducing Regex: the problem regular expressions were invented to solve.

Before we meet the re module, this is what validating a phone number looks
like by hand. Read it and ask yourself two questions. Is it correct? How
long did it take you to decide?

The answer to the second question is the reason regular expressions exist.
"""


def is_phone_number(text: str) -> bool:
    """
    Determine whether a string is a phone number of the form NNN-NNN-NNNN.

    This function is correct, I think. Is it? It is hard to tell. Yuck. It
    is so ugly. Compare it with is_phone_number_regex_1.py, which does the
    same job in one line.

    :param text: a string that may or may not be a phone number
    :precondition: text must be a string
    :return: True if text is a phone number, otherwise False

    >>> is_phone_number('415-555-4242')
    True
    >>> is_phone_number('Moshi moshi')
    False
    >>> is_phone_number('415-555-424')
    False
    >>> is_phone_number('415 555 4242')
    False
    """
    if len(text) != 12:
        return False  # not phone number-sized
    for index in range(0, 3):
        if not text[index].isdecimal():
            return False  # not an area code
    if text[3] != '-':
        return False  # does not have first hyphen
    for index in range(4, 7):
        if not text[index].isdecimal():
            return False  # does not have first 3 digits
    if text[7] != '-':
        return False  # does not have the second hyphen
    for index in range(8, 12):
        if not text[index].isdecimal():
            return False  # does not have last 4 digits
    return True  # "text" is a phone number!


def main():
    """
    Drive the program.
    """
    for candidate in ['415-555-4242', 'Moshi moshi', '415 555 4242']:
        print(f'{candidate!r} is a phone number: {is_phone_number(candidate)}')


if __name__ == "__main__":
    main()
