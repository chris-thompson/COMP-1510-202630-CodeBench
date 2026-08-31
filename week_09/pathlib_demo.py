"""
pathlib represents file system paths as objects instead of plain strings.
The / operator joins path segments, and a Path works the same way on
Windows, macOS, and Linux.
"""

import pathlib
import tempfile


def build_data_path(directory: str, filename: str) -> pathlib.Path:
    """
    Join a directory and a filename into one Path.

    :param directory: a str naming a directory
    :param filename: a str naming a file
    :precondition: directory is a str
    :precondition: filename is a str
    :postcondition: directory is unchanged
    :postcondition: filename is unchanged
    :return: a Path combining directory and filename

    >>> build_data_path('data', 'students.txt').as_posix()
    'data/students.txt'
    """
    return pathlib.Path(directory) / filename


def describe_path(path: str) -> str:
    """
    Report whether a path exists, and whether it is a file or a directory.

    :param path: a str naming a path
    :precondition: path is a str
    :postcondition: path is unchanged
    :return: a str describing what, if anything, exists at path

    >>> describe_path('/definitely/does/not/exist.txt')
    '/definitely/does/not/exist.txt does not exist'
    """
    path = pathlib.Path(path)
    if not path.exists():
        return f'{path} does not exist'
    if path.is_dir():
        return f'{path} is a directory'
    return f'{path} is a file'


def write_and_read(path: str, text: str) -> str:
    """
    Write text to a file, then read it back, using pathlib's shortcuts.

    :param path: a str naming the file to write
    :param text: a str to write to the file
    :precondition: path is a str
    :precondition: text is a str
    :postcondition: path is unchanged
    :postcondition: text is unchanged
    :postcondition: a file at path is created or overwritten with text
    :return: the text read back from path

    >>> scratch = pathlib.Path(tempfile.mkdtemp()) / 'greeting.txt'
    >>> write_and_read(scratch, 'Hello, pathlib!')
    'Hello, pathlib!'
    """
    path = pathlib.Path(path)
    path.write_text(text)
    return path.read_text()


def list_text_files(directory: str) -> list:
    """
    List the names of every .txt file directly inside a directory.

    :param directory: a str naming a directory
    :precondition: directory is a str naming an existing directory
    :postcondition: directory is unchanged
    :return: a sorted list of file names ending in .txt

    >>> scratch = tempfile.mkdtemp()
    >>> _ = (pathlib.Path(scratch) / 'a.txt').write_text('hi')
    >>> _ = (pathlib.Path(scratch) / 'b.txt').write_text('there')
    >>> _ = (pathlib.Path(scratch) / 'notes.md').write_text('skip me')
    >>> list_text_files(scratch)
    ['a.txt', 'b.txt']
    """
    return sorted([path.name for path in pathlib.Path(directory).iterdir()
                   if path.suffix == '.txt'])


def main():
    """
    Drive the program.
    """
    data_path = build_data_path('data', 'students.txt')
    print(f'Built path: {data_path}')
    print(describe_path(str(data_path)))
    print(describe_path('file_io'))
    print('file_io/*.txt:', list_text_files('file_io'))


if __name__ == '__main__':
    main()
