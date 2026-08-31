"""
Demonstrate append mode, and the difference between 'a' and 'w'.

Opening a file with 'w' throws away whatever was in it. Opening the same
file with 'a' keeps the old contents and adds to the end. Run this program
two or three times in a row and watch the file grow: that is append mode.

To start over, delete append_demo.txt and run it again.
"""


def add_a_line(filename: str, message: str) -> None:
    """
    Add one line to the end of a file, creating the file if it is missing.

    Mode 'a' is append mode. It never deletes anything, and the file cursor
    starts at the end of the file rather than the beginning.

    :param filename: a str naming the file to append to
    :param message: a str to add as a new line
    :precondition: filename is a str
    :precondition: message is a str
    :postcondition: message and a newline are added to the end of filename
    """
    with open(filename, 'a') as file_object:
        # write does not add a newline for us, so we add one ourselves
        file_object.write(message + '\n')


def show_file(filename: str) -> None:
    """
    Print the entire contents of a file, and how many lines it holds.

    :param filename: a str naming the file to read
    :precondition: filename names an existing readable text file
    :postcondition: the contents of filename are printed
    :raises FileNotFoundError: if no file called filename exists
    """
    with open(filename) as file_object:
        contents = file_object.read()

    print(f'{filename} now holds {len(contents.splitlines())} line(s):')
    print(contents, end='')


def main():
    """
    Drive the program.
    """
    filename = 'append_demo.txt'
    add_a_line(filename, 'Hello from append mode.')
    show_file(filename)


if __name__ == '__main__':
    main()
