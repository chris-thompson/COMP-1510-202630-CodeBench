"""
Move around inside an open file with tell and seek.

Python keeps a file cursor for every open file. It is just an integer: how
far we are from the beginning. Two methods work with it.

    file_object.tell()      ask where the cursor is
    file_object.seek(n)     move the cursor to position n

seek counts from the beginning of the file. It is absolute, not relative:
seek(54) means "go to position 54", never "move forward 54".

seek also takes an optional SECOND argument called whence, which says where
to count from. The io module names the three choices:

    io.SEEK_SET  is 0   count from the beginning (the default)
    io.SEEK_CUR  is 1   count from where the cursor is now
    io.SEEK_END  is 2   count from the end

Here is the trap. Because those constants are plain integers, writing

    file_object.seek(io.SEEK_END)      # WRONG

is really seek(2), which moves the cursor to position 2 near the START of
the file. Python does not complain, and the mistake is easy to miss. What
you meant was

    file_object.seek(0, io.SEEK_END)   # correct: zero characters from the end

One more rule: in text mode Python only allows seek(0, io.SEEK_END). Any
other combination of offset and whence raises io.UnsupportedOperation. To
return to the beginning, just call seek(0).
"""

import io

QUOTE = ("If you can't handle me at my worst, "
         "you probably have healthy boundaries -- Anonymous")


def make_file(filename: str) -> None:
    """
    Create a file holding the quote, replacing it if it already exists.

    :param filename: a str naming the file to create
    :precondition: filename is a str
    :postcondition: filename is created or overwritten with QUOTE
    """
    with open(filename, 'w') as file_object:
        file_object.write(QUOTE)


def read_file(filename: str) -> None:
    """
    Read one file several times over, moving the cursor between reads.

    :param filename: a str naming the file to read
    :precondition: filename names an existing readable text file
    :postcondition: the demonstration is printed
    :raises FileNotFoundError: if no file called filename exists
    """
    with open(filename) as file_object:
        print('cursor starts at', file_object.tell())
        print('whole file:', file_object.read())
        print('after read the cursor is at', file_object.tell())

        # seek(0) returns to the beginning. This is the everyday case.
        file_object.seek(0)

        # Jump straight to an interesting word. seek counts from the start.
        offset = QUOTE.index('healthy')
        file_object.seek(offset)
        print(f'\nfrom position {offset}:', file_object.read(18))

        # tell lets us memorize a spot and come back to it later.
        remember = file_object.tell()
        file_object.seek(0)
        print('back at the beginning:', file_object.read(2))
        file_object.seek(remember)
        print(f'returned to position {remember}:', file_object.read(10))

        # The only whence trick text mode allows: zero from the end.
        end = file_object.seek(0, io.SEEK_END)
        print(f'\nthe end of the file is at position {end}')

        # And the classic bug, so you can see what it really does.
        wrong = file_object.seek(io.SEEK_END)
        print(f'seek(io.SEEK_END) put the cursor at {wrong}, not {end}!')


def main():
    """
    Drive the program.
    """
    filename = 'seek_demo.txt'
    make_file(filename)
    read_file(filename)


if __name__ == '__main__':
    main()
