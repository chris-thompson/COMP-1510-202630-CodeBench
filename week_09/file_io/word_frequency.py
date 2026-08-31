"""
Count the words in a real book and report the ten most common.

This example puts the whole term together: a with-block and a file object
from this week, a dictionary and a comprehension from Week 6, sorted with a
key function from Week 4, and string methods from Week 3.

The text is Lewis Carroll's Alice's Adventures in Wonderland, downloaded
from Project Gutenberg. Try it on any other plain-text file you like.
"""

import string


def clean_word(word: str) -> str:
    """
    Strip surrounding punctuation from a word and convert it to lower case.

    Punctuation is only removed from the two ends, so an apostrophe inside a
    word survives and "don't" stays one word.

    :param word: a str containing one whitespace-delimited word
    :precondition: word is a str
    :return: the cleaned word as a lower case str

    >>> clean_word('Alice')
    'alice'
    >>> clean_word('"Curiouser!"')
    'curiouser'
    >>> clean_word("don't")
    "don't"
    >>> clean_word('---')
    ''
    """
    return word.strip(string.punctuation).lower()


def count_words(text: str) -> dict:
    """
    Count how many times each word appears in a passage of text.

    Words that clean down to nothing, such as a lone dash, are discarded.

    :param text: a str containing any amount of text
    :precondition: text is a str
    :return: a dict mapping each word to its count as an int

    >>> count_words('the cat the hat')
    {'the': 2, 'cat': 1, 'hat': 1}
    >>> count_words('Down, down, DOWN!')
    {'down': 3}
    >>> count_words('')
    {}
    """
    counts = {}
    for word in text.split():
        cleaned = clean_word(word)
        if cleaned:
            counts[cleaned] = counts.get(cleaned, 0) + 1
    return counts


def most_common(counts: dict, how_many: int) -> list:
    """
    Find the most frequent words in a dict of word counts.

    The key argument tells sorted to rank each word by its count instead of
    alphabetically. We pass the dict's own get method as that key function,
    the same way we passed functions to sorted back in Week 4.

    :param counts: a dict mapping words to int counts
    :param how_many: an int number of words to return
    :precondition: counts is a dict mapping str to int
    :precondition: how_many is an int that is zero or greater
    :return: a list of (word, count) tuples, most frequent first

    >>> most_common({'the': 2, 'cat': 1, 'hat': 1}, 2)
    [('the', 2), ('cat', 1)]
    >>> most_common({'the': 2, 'cat': 1}, 0)
    []
    >>> most_common({}, 5)
    []
    """
    ranked = sorted(counts, key=counts.get, reverse=True)
    return [(word, counts[word]) for word in ranked[:how_many]]


def read_book(filename: str) -> str:
    """
    Read an entire plain-text file into one str.

    The encoding 'utf-8-sig' is plain UTF-8, except that it also removes the
    invisible marker some editors put at the very start of a file. Without
    it, the first word of the book would carry a hidden character.

    :param filename: a str naming a text file
    :precondition: filename names an existing readable text file
    :return: the whole contents of the file as a str
    :raises FileNotFoundError: if no file called filename exists
    """
    with open(filename, encoding='utf-8-sig') as file_object:
        return file_object.read()


def main():
    """
    Drive the program.
    """
    filename = 'alice.txt'
    try:
        text = read_book(filename)
    except FileNotFoundError:
        print(f'Could not find {filename}. Run this from the file_io folder.')
        return

    counts = count_words(text)
    print(f'{filename} contains {len(text)} characters')
    print(f'and {len(counts)} different words.\n')
    print('The ten most common words are:')
    for word, count in most_common(counts, 10):
        print(f'  {count} {word}')


if __name__ == '__main__':
    main()
