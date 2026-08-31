"""
subprocess runs another program from inside a Python program.

Everything we have written so far has done its own work. Sometimes the work
is already done by a program that exists, and the right move is to run that
program rather than reimplement it.

subprocess.run() starts a program, waits for it to finish, and hands back a
result carrying the exit code and, if we ask, whatever the program printed.
An exit code of 0 means success, by a convention older than Python.

The program we run here is Python itself. Naming a command such as "ls"
would work on macOS and fail on Windows, whereas sys.executable is the exact
Python interpreter running this file, wherever it happens to live. Reaching
for a portable name rather than a familiar one is worth the small effort.
"""

import subprocess
import sys


def run_and_capture(command: list) -> dict:
    """
    Run a program, wait for it to finish, and collect what it produced.

    capture_output keeps the program's output from spilling onto our own
    screen and hands it to us instead. text turns the bytes into a string,
    which is almost always what we want.

    :param command: a list whose first item is a program and whose
                    remaining items are its arguments
    :precondition: command must be a non-empty list of strings naming a
                   program that exists and the arguments to give it
    :postcondition: command is unchanged
    :return: a dictionary with the keys "returncode", "stdout", and
             "stderr"

    >>> result = run_and_capture([sys.executable, "-c", "print('hi')"])
    >>> result["returncode"]
    0
    >>> result["stdout"].strip()
    'hi'
    >>> failed = run_and_capture([sys.executable, "-c", "raise SystemExit(3)"])
    >>> failed["returncode"]
    3
    """
    completed = subprocess.run(command, capture_output=True, text=True)
    return {
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


def succeeded(result: dict) -> bool:
    """
    Report whether a finished program reported success.

    :param result: a dictionary with the key "returncode"
    :precondition: result must have the key "returncode"
    :postcondition: result is unchanged
    :return: True if the return code is 0, otherwise False

    >>> succeeded({"returncode": 0})
    True
    >>> succeeded({"returncode": 1})
    False
    """
    return result["returncode"] == 0


def main():
    """
    Drive the program.
    """
    print("Asking Python which version it is, by running Python:\n")
    version = run_and_capture([sys.executable, "--version"])
    print(f"  it printed  : {version['stdout'].strip()}")
    print(f"  exit code   : {version['returncode']}")
    print(f"  succeeded?  : {succeeded(version)}\n")

    print("Now running a program that deliberately fails:\n")
    failure = run_and_capture([sys.executable, "-c", "raise SystemExit(3)"])
    print(f"  exit code   : {failure['returncode']}")
    print(f"  succeeded?  : {succeeded(failure)}")
    print("\nAn exit code of 0 means success. Anything else is the program")
    print("telling us, in the only word it has left, that something is wrong.")


if __name__ == "__main__":
    main()
