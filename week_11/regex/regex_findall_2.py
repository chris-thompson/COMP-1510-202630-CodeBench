"""
Introducing Regex: search() finds one, findall() finds them all.

    search()   returns a Match object for the FIRST match, or None.
    findall()  returns a list. Never None: no matches gives an empty list.

findall() has one surprise worth memorising. What the list holds depends on
whether the pattern has groups:

    no parentheses   -> a list of strings, one per match
    one set          -> a list of strings, one per group-1 match
    two or more sets -> a list of TUPLES, one per match
"""

import re

MESSAGE = "Office: 604-555-1234 Cell: 604-555-5678"
PHONE_NUMBER_REGEX = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
GROUPED_PHONE_REGEX = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")


def find_all_phone_numbers(text: str) -> list:
    """
    Find every ten-digit phone number written with dashes in some text.

    :param text: a string to search
    :precondition: text must be a string
    :return: a list of the phone numbers as strings, in the order they appear

    >>> find_all_phone_numbers('Office: 604-555-1234 Cell: 604-555-5678')
    ['604-555-1234', '604-555-5678']
    >>> find_all_phone_numbers('Call 415-555-4242')
    ['415-555-4242']
    >>> find_all_phone_numbers('Moshi moshi')
    []
    """
    return PHONE_NUMBER_REGEX.findall(text)


def find_all_area_codes(text: str) -> list:
    """
    Find the area code of every phone number in some text.

    :param text: a string to search
    :precondition: text must be a string
    :return: a list of tuples, each holding the three parts of one number

    >>> find_all_area_codes('Office: 604-555-1234 Cell: 415-555-5678')
    [('604', '555', '1234'), ('415', '555', '5678')]
    >>> find_all_area_codes('Moshi moshi')
    []
    """
    return GROUPED_PHONE_REGEX.findall(text)


def main():
    """
    Drive the program.
    """
    print("Message:", MESSAGE)

    match_object = PHONE_NUMBER_REGEX.search(MESSAGE)
    if match_object:
        print("\nsearch() found only the first:", match_object.group())
    else:
        print("\nsearch() found nothing.")

    numbers = find_all_phone_numbers(MESSAGE)
    print(f"\nfindall() with no groups found {len(numbers)}:")
    print(" ", numbers)

    parts = find_all_area_codes(MESSAGE)
    print(f"\nfindall() WITH groups found {len(parts)}, as tuples:")
    print(" ", parts)

    # findall() never returns None. With no match it returns an empty list,
    # which is falsy, so an if-statement still reads the way you expect.
    print("\nNo match at all:", find_all_phone_numbers("Moshi moshi"))


if __name__ == "__main__":
    main()
