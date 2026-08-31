"""
Introducing Regex: what the wildcard does to findall().

The same sentence, two patterns that differ by two characters, two utterly
different results.

    .at    one character, then "at". findall() returns every three-letter
           match it can find, left to right.
    .*at   any amount of anything, then "at". Because .* is greedy it
           swallows the whole sentence up to the LAST "at", so findall()
           returns a single enormous match.

The lesson: .* is almost never what you want in the middle of a pattern.
"""

import re

SENTENCE = ("The fat cat and rat in the hat sat on the flat mat"
            " with pat to chat")
AT_WORDS_REGEX = re.compile(r".at")
GREEDY_AT_REGEX = re.compile(r".*at")


def find_at_words(text: str) -> list:
    """
    Find every three-character run that ends in "at".

    :param text: a string to search
    :precondition: text must be a string
    :return: a list of the matched strings, in the order they appear

    >>> find_at_words('the fat cat')
    ['fat', 'cat']
    >>> find_at_words('flat')
    ['lat']
    >>> find_at_words('nothing here')
    []
    """
    return AT_WORDS_REGEX.findall(text)


def main():
    """
    Drive the program.
    """
    print("Sentence:", SENTENCE)

    print("\n.at   finds every three-letter match:")
    print(" ", find_at_words(SENTENCE))

    print("\n.*at  is greedy, so it finds exactly one:")
    print(" ", GREEDY_AT_REGEX.findall(SENTENCE))

    # Notice 'lat' and 'hat' in the first list. The dot does not know what a
    # word is; it matches the character before "at" whatever that is, even
    # the l inside "flat".


if __name__ == "__main__":
    main()
