"""
argparse turns sys.argv into named, typed, self-documenting arguments.

In Week 7 we passed arguments to a program with sys.argv, which hands us a
list of strings and nothing else. There are no names, so we count positions
by hand. There are no types, so "3" arrives as text and we convert it
ourselves. There is no help, so the only way to learn what a program accepts
is to read its source code.

argparse fixes all three problems. We describe each argument once, and
argparse reads it, converts it, checks it, and writes the --help screen for
us. Every professional command-line tool works this way.

Run this from a terminal, not from the PyCharm Run button, because the Run
button does not let us pass arguments:

    python3 using_argparse.py --name Ada
    python3 using_argparse.py --name Ada --repeat 3 --shout
    python3 using_argparse.py --name Ada --repeat 2 --output csv
    python3 using_argparse.py --help
"""

import argparse

OUTPUT_CHOICES = ("plain", "csv")


def build_parser() -> argparse.ArgumentParser:
    """
    Build the argument parser for this program.

    Each add_argument call describes one option, and the keyword arguments
    do the real work. default supplies a value when the option is absent.
    type converts the text argparse read into the type we want. choices
    restricts the value to a fixed set and rejects anything else. The
    action "store_true" makes a flag, which is either present or absent
    and never carries a value of its own.

    :postcondition: create a parser that accepts --name, --repeat,
                    --output, and --shout
    :return: an argparse.ArgumentParser

    >>> parser = build_parser()
    >>> arguments = parser.parse_args(["--name", "Ada"])
    >>> arguments.name, arguments.repeat, arguments.output, arguments.shout
    ('Ada', 1, 'plain', False)
    >>> parser.parse_args(["--repeat", "3"]).repeat
    3
    >>> parser.parse_args(["--output", "csv", "--shout"]).shout
    True
    """
    parser = argparse.ArgumentParser(description="Greet someone.")
    parser.add_argument("--name", default="World",
                        help="who to greet")
    parser.add_argument("--repeat", type=int, default=1,
                        help="how many greetings to produce")
    parser.add_argument("--output", choices=OUTPUT_CHOICES,
                        default="plain",
                        help="how to format the greetings")
    parser.add_argument("--shout", action="store_true",
                        help="greet in capital letters")
    return parser


def greet(name: str, shout: bool) -> str:
    """
    Build a greeting for a name.

    :param name: a string
    :param shout: a boolean
    :precondition: name must be a string
    :precondition: shout must be a boolean
    :return: "Hello, {name}!", in capital letters if shout is True

    >>> greet("Ada", False)
    'Hello, Ada!'
    >>> greet("Ada", True)
    'HELLO, ADA!'
    >>> greet("", False)
    'Hello, !'
    """
    message = f"Hello, {name}!"
    return message.upper() if shout else message


def format_output(greetings: list, output: str) -> str:
    """
    Format a list of greetings in one of the supported output styles.

    This is where the choices we gave argparse earn their keep. Because
    argparse has already rejected every value except "plain" and "csv",
    this function only ever sees a value it knows how to handle.

    A greeting contains a comma of its own, so each csv row wraps its
    greeting in double quotes. A comma inside a field would otherwise look
    like the end of that field.

    :param greetings: a list of strings
    :param output: one of the strings in OUTPUT_CHOICES
    :precondition: greetings must be a list of strings
    :precondition: output must be one of the strings in OUTPUT_CHOICES
    :postcondition: greetings is unchanged
    :return: the greetings as one string, one greeting per line, with a
             "number,greeting" header row when output is "csv"

    >>> format_output(["Hello, Ada!"], "plain")
    'Hello, Ada!'
    >>> format_output(["Hi!", "Hi!"], "plain")
    'Hi!\\nHi!'
    >>> format_output(["Hello, Ada!"], "csv")
    'number,greeting\\n1,"Hello, Ada!"'
    """
    if output == "csv":
        rows = [f'{number},"{greeting}"'
                for number, greeting in enumerate(greetings, start=1)]
        return "\n".join(["number,greeting"] + rows)
    return "\n".join(greetings)


def main():
    """
    Drive the program.
    """
    arguments = build_parser().parse_args()
    greetings = [greet(arguments.name, arguments.shout)
                 for _ in range(arguments.repeat)]
    print(format_output(greetings, arguments.output))


if __name__ == "__main__":
    main()
