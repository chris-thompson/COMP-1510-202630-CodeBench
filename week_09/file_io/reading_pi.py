"""
Read a large file. Is it any different from reading a small one?

pi_million_digits.txt holds the first million digits of pi, one chunk per
line. Reading it uses exactly the same code as reading pi_digits.txt: open
it, read the lines, join them together. Big files are not a special case.

Two things to look at:

1. rstrip removes the newline at the end of every line. What happens if we
   leave it out? Try it and explain the answer to yourself.
2. lines is a list of str, and pi_string is a single str. Watch the types.
"""


def read_digits(filename: str) -> str:
    """
    Read a file of digits and join every line into one long str.

    :param filename: a str naming a text file of digits
    :precondition: filename names an existing readable text file
    :postcondition: the type of each intermediate value is printed
    :return: the file contents as a single str with no newlines
    :raises FileNotFoundError: if no file called filename exists
    """
    with open(filename) as file_object:
        lines = file_object.readlines()

    print('readlines gave us a', type(lines), 'of', len(lines), 'lines')

    pi_string = ''
    for line in lines:
        pi_string += line.rstrip()  # What happens if we omit this? Why?

    print('joined together we have a', type(pi_string))
    return pi_string


def main():
    """
    Drive the program.
    """
    pi_string = read_digits('pi_million_digits.txt')

    print(f'\nthe string is {len(pi_string)} characters long')
    print('it starts:', pi_string[:52])
    print('it ends:  ', pi_string[-20:])

    # A million digits was promised. Is that what we got?
    digits = [character for character in pi_string if character.isdigit()]
    print(f'\nbut only {len(digits)} of those characters are digits')
    print('So where did the other characters come from? Open the file and')
    print('look at the start of any line, then read what rstrip promises to')
    print('remove. rstrip only strips the RIGHT-hand end of a string.')


if __name__ == '__main__':
    main()
