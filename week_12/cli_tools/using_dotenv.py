"""
python-dotenv keeps secrets and per-machine settings out of our source code.

An API key written into a .py file is a key we have published. The moment
that file is pushed to GitHub, anyone who can read the repository can read
the key, and deleting it later does not help, because git remembers.

The convention is a file called .env, holding one key=value pair per line,
which git is told to ignore. load_dotenv() reads that file into the
environment, and os.environ reads it back out again. The code never contains
the secret; it only contains the name of the secret.

The .env file is deliberately absent from this repository. Copy .env.example
to .env in this same folder, edit it if you like, and run this file. The
defaults work either way, because a program should still start when an
optional setting is missing.

python-dotenv is not part of the standard library. Install it first:

    pip3 install python-dotenv
"""

import os

from dotenv import load_dotenv

DEFAULT_NAME = "World"
DEFAULT_VOLUME = "quiet"


def read_settings(environment: dict) -> dict:
    """
    Read the greeting settings out of an environment.

    The environment is a parameter rather than something this function
    reaches out and grabs, which is what makes it testable: the doctests
    below hand it an ordinary dictionary.

    :param environment: a dictionary of environment variables
    :precondition: environment must be a dictionary with string values
    :postcondition: environment is unchanged
    :return: a dictionary with the keys "name" and "volume", taken from
             GREETING_NAME and GREETING_VOLUME, falling back to
             DEFAULT_NAME and DEFAULT_VOLUME when they are absent

    >>> read_settings({"GREETING_NAME": "Ada", "GREETING_VOLUME": "loud"})
    {'name': 'Ada', 'volume': 'loud'}
    >>> read_settings({"GREETING_NAME": "Ada"})
    {'name': 'Ada', 'volume': 'quiet'}
    >>> read_settings({})
    {'name': 'World', 'volume': 'quiet'}
    """
    return {
        "name": environment.get("GREETING_NAME", DEFAULT_NAME),
        "volume": environment.get("GREETING_VOLUME", DEFAULT_VOLUME),
    }


def load_greeting_settings() -> dict:
    """
    Load the greeting settings from a .env file in the current directory.

    :postcondition: the variables in a .env file in the current directory
                    are loaded into the environment
    :return: a dictionary with the keys "name" and "volume"
    """
    load_dotenv()
    return read_settings(os.environ)


def build_greeting(settings: dict) -> str:
    """
    Build a greeting from a settings dictionary.

    :param settings: a dictionary with the keys "name" and "volume"
    :precondition: settings must have the keys "name" and "volume"
    :postcondition: settings is unchanged
    :return: "Hello, {name}!", in capital letters when volume is "loud"

    >>> build_greeting({"name": "Ada", "volume": "quiet"})
    'Hello, Ada!'
    >>> build_greeting({"name": "Ada", "volume": "loud"})
    'HELLO, ADA!'
    """
    message = f"Hello, {settings['name']}!"
    return message.upper() if settings["volume"] == "loud" else message


def main():
    """
    Drive the program.
    """
    settings = load_greeting_settings()
    print(f"Settings read from the environment: {settings}")
    print(build_greeting(settings))


if __name__ == "__main__":
    main()
