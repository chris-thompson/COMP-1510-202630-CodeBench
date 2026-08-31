"""
Introducing Regex: a real job, done with a pattern.

Everything else in this folder is a demonstration. This one is a tool. It
walks a folder tree and reports every file whose name matches a pattern we
describe, which is the sort of thing we would otherwise do by hand.

It also shows regex working alongside pathlib from Week 9. The pattern
describes the NAME; pathlib does the walking.
"""

import pathlib
import re

HERE = pathlib.Path(__file__).parent  # So useful!


def matching_file_names(pattern: str, names: list) -> list:
    """
    Keep the file names that match a regular expression from the beginning.

    :param pattern: a regular expression in string form
    :param names: a list of file names as strings
    :precondition: pattern must be a valid regular expression
    :precondition: names must be a list of strings
    :postcondition: names is unchanged
    :return: a sorted list of the names that match pattern

    >>> matching_file_names(r'regex_', ['regex_plus.py', 'find_files.py'])
    ['regex_plus.py']
    >>> matching_file_names(r'.*\\.py$', ['notes.txt', 'a.py'])
    ['a.py']
    >>> matching_file_names(r'nothing', ['a.py', 'b.py'])
    []
    """
    compiled = re.compile(pattern)
    return sorted(name for name in names if compiled.match(name))


def find_files(pattern: str, base: pathlib.Path) -> list:
    """
    Find every file at or below a folder whose name matches a pattern.

    :param pattern: a regular expression in string form
    :param base: a Path to an existing folder
    :precondition: pattern must be a valid regular expression
    :precondition: base must be a Path to a folder that exists
    :postcondition: the file tree below base is traversed
    :return: a sorted list of the matching Paths
    """
    compiled = re.compile(pattern)
    return sorted(path for path in base.rglob("*")
                  if path.is_file() and compiled.match(path.name))


def main():
    """
    Drive the program.
    """
    # Every demonstration file in this folder, found by its name.
    print(f"Files in {HERE.name}/ whose names start with regex_:")
    for path in find_files(r"regex_.*\.py$", HERE):
        print("  ", path.name)

    # A different pattern, the same function. This is the payoff: the
    # behaviour is described by the pattern, not written into the code.
    print(f"\nFiles in {HERE.name}/ about phone numbers:")
    for path in find_files(r".*phone_number.*\.py$", HERE):
        print("  ", path.name)


if __name__ == "__main__":
    main()
