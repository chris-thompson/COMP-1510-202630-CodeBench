"""
Introducing Regex: the wildcard . and the three ways to repeat it.

The dot matches any single character except a newline. Combine it with a
quantifier and it becomes "some amount of anything":

    .+   one or more of anything, greedy    -- takes as much as it can
    .*   zero or more of anything, greedy   -- takes as much as it can
    .*?  zero or more of anything, LAZY     -- takes as little as it can

The three patterns below differ by one character each, and all three are run
against the same text so the difference is visible rather than theoretical.
"""

import re

RECORD = "First Name: Seven Last Name: of Nine"
DOT_PLUS_REGEX = re.compile(r"First Name: (.+) Last Name: (.+)")
DOT_STAR_REGEX = re.compile(r"First Name: (.*) Last Name: (.*)")
NON_GREEDY_REGEX = re.compile(r"<(.*?)>")
GREEDY_REGEX = re.compile(r"<(.*)>")


def split_name(text: str) -> tuple | None:
    """
    Pull the first and last name out of a "First Name: ... Last Name: ..."
    record.

    The dot-plus requires at least one character in each name. The dot-star
    version in this file's DOT_STAR_REGEX would accept an empty one.

    :param text: a string to search
    :precondition: text must be a string
    :return: a tuple of the first and last name as strings, or None if text
             is not in that format

    >>> split_name('First Name: Seven Last Name: of Nine')
    ('Seven', 'of Nine')
    >>> split_name('First Name: Kathryn Last Name: Janeway')
    ('Kathryn', 'Janeway')
    >>> split_name('Moshi moshi')
    """
    match_object = DOT_PLUS_REGEX.search(text)
    if match_object:
        return match_object.groups()
    return None


def first_tag(text: str) -> str | None:
    """
    Find the first angle-bracketed tag in some text, without over-reaching.

    This is the classic reason to want a lazy quantifier. The greedy .* runs
    all the way to the LAST closing bracket in the text; the lazy .*? stops
    at the first one.

    :param text: a string to search
    :precondition: text must be a string
    :return: the contents of the first tag as a string, or None if there is
             no tag

    >>> first_tag('<b>bold</b>')
    'b'
    >>> first_tag('<title>Star Trek</title>')
    'title'
    >>> first_tag('no tags here')
    """
    match_object = NON_GREEDY_REGEX.search(text)
    if match_object:
        return match_object.group(1)
    return None


def main():
    """
    Drive the program.
    """
    print("Text:", RECORD)
    print("  .+  gives:", DOT_PLUS_REGEX.search(RECORD).groups())
    print("  .*  gives:", DOT_STAR_REGEX.search(RECORD).groups())

    # With a name missing, the difference between .+ and .* finally shows.
    incomplete = "First Name:  Last Name: Nine"
    print("\nText:", repr(incomplete))
    print("  .+  gives:", DOT_PLUS_REGEX.search(incomplete))
    print("  .*  gives:", DOT_STAR_REGEX.search(incomplete).groups())

    # Greedy versus lazy, on text with more than one closing bracket.
    markup = "<b>bold</b> and <i>italic</i>"
    print("\nText:", markup)
    print("  Greedy <(.*)>  grabs:", GREEDY_REGEX.search(markup).group(1))
    print("  Lazy   <(.*?)> grabs:", NON_GREEDY_REGEX.search(markup).group(1))
    print("  Every tag, lazily:   ", NON_GREEDY_REGEX.findall(markup))


if __name__ == "__main__":
    main()
