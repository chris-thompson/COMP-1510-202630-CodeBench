"""
A command-line tool built out of everything Week 12 introduced.

The four libraries below each do one job, and the point of this file is to
show how they fit together in a program of the kind we would actually
write. argparse reads the command line, so the district and the limit
arrive named, typed, and documented. logging reports what the program is
doing, at a level the user chooses with --verbose. python-dotenv supplies
the name of the data file from a .env file, so that setting lives outside
the source code. rich prints the finished report as a table.

Notice that no function does two of those jobs at once. Reading the data,
selecting the relays, and displaying the result are three separate
functions, which is what lets us test the selection without a terminal, a
file, or a command line anywhere in sight.

Two of these libraries are not part of the standard library. Install them
first:

    pip3 install rich python-dotenv

Copy .env.example to .env in this same folder to read a different data
file. The program still runs when .env is absent, because relays.json is
the default either way.

Run this from a terminal, not from the PyCharm Run button, because the Run
button does not let us pass arguments:

    python3 relay_scan.py harbour
    python3 relay_scan.py arcology --limit 2
    python3 relay_scan.py warren --verbose
    python3 relay_scan.py --help
"""

import argparse
import json
import logging
import os

from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

logger = logging.getLogger(__name__)


def parse_arguments() -> argparse.Namespace:
    """
    Parse and return the command-line arguments.

    The district is positional, so it is required and it is written
    without a leading dash. choices restricts it to the three districts
    this program knows about, and argparse rejects anything else before a
    line of our own code runs. --limit is optional and typed, so the text
    "3" arrives as the integer 3. --verbose is a flag: it is either
    present or absent, and it never carries a value of its own.

    :postcondition: the arguments in sys.argv are read and converted
    :postcondition: the program exits with a usage message when an
                    argument is missing, mistyped, or not a valid choice
    :return: an argparse.Namespace with the attributes district, limit,
             and verbose
    """
    parser = argparse.ArgumentParser(
        description="Scan relay stations in a city district."
    )

    parser.add_argument(
        "district",
        choices=("harbour", "arcology", "warren")
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=5
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true"
    )

    return parser.parse_args()


def configure_logging(verbose: bool) -> None:
    """
    Configure logging to write level-tagged records to the console.

    The verbose flag chooses between two levels. At DEBUG every record is
    written, including the running commentary the functions below log
    about their own progress. At INFO those DEBUG records go quiet
    without a single line of code changing.

    :param verbose: a boolean
    :precondition: verbose must be a boolean
    :postcondition: records at DEBUG level or above are written to the
                    console when verbose is True
    :postcondition: records at INFO level or above are written to the
                    console when verbose is False
    :return: None
    """
    level = logging.DEBUG if verbose else logging.INFO

    logging.basicConfig(
        level=level,
        format="%(levelname)s | %(message)s"
    )


def load_relays(filename: str) -> list:
    """
    Load and return relay data from a JSON file.

    json.load reads the whole file and turns its text into ordinary
    Python objects: the JSON array becomes a list, and each JSON object
    inside it becomes a dictionary. The with statement closes the file
    afterwards, even when reading it raises an exception.

    :param filename: a string
    :precondition: filename must name a readable UTF-8 encoded JSON file
    :precondition: the file must hold a JSON array of relay objects
    :postcondition: a DEBUG record is logged naming the file
    :return: a list of dictionaries, each with the keys "name",
             "district", "signal", and "status"
    """
    logger.debug("Loading relay data from %s", filename)

    with open(filename, "r", encoding="utf-8") as file_object:
        return json.load(file_object)


def scan_relays(relays: list, district: str, limit: int) -> list:
    """
    Return up to limit relays from the requested district.

    The loop stops as soon as it has collected enough relays rather than
    examining every relay and discarding the surplus afterwards. On a
    list of six that saves nothing; on a list of six million it is the
    difference between a fast program and a slow one.

    :param relays: a list of dictionaries
    :param district: a string
    :param limit: a non-negative integer
    :precondition: each dictionary in relays must have the key "district"
    :precondition: district must be a string
    :precondition: limit must be a non-negative integer
    :postcondition: relays is unchanged
    :postcondition: an INFO record is logged counting the matches
    :return: a list of the first limit dictionaries in relays whose
             "district" value equals district

    >>> first = {"name": "HARE-07", "district": "harbour", "signal": 94}
    >>> second = {"name": "HARE-23", "district": "arcology", "signal": 88}
    >>> scan_relays([first, second], "harbour", 5) == [first]
    True
    >>> scan_relays([first, second], "warren", 5)
    []
    >>> len(scan_relays([first, first, first], "harbour", 2))
    2
    """
    logger.debug("Scanning district: %s", district)

    matches = []

    for relay in relays:
        if relay["district"] == district:
            matches.append(relay)

        if len(matches) == limit:
            break

    logger.info("Found %s active relays", len(matches))

    return matches


def display_report(relays: list, district: str) -> None:
    """
    Display relay data as a rich table.

    Building the report and choosing what goes in it are two different
    jobs, so they are two different functions. This one is the only
    function in the file that writes to the screen.

    :param relays: a list of dictionaries
    :param district: a string
    :precondition: each dictionary in relays must have the keys "name",
                   "signal", and "status"
    :precondition: district must be a string
    :postcondition: relays is unchanged
    :postcondition: a table with one row for each dictionary in relays is
                    printed to the console
    :return: None
    """
    console = Console()

    table = Table(
        title=f"{district.upper()} RELAY SCAN"
    )

    table.add_column("Relay")
    table.add_column("Signal", justify="right")
    table.add_column("Status")

    for relay in relays:
        table.add_row(
            relay["name"],
            f'{relay["signal"]}%',
            relay["status"]
        )

    console.print(table)


def main():
    """
    Drive the program.

    Read the settings, read the command line, read the data, select the
    relays, and print the report, in that order. os.getenv takes a
    default as its second argument, so the program still runs when .env
    is missing or says nothing about RELAY_DATA_FILE.
    """
    load_dotenv()

    arguments = parse_arguments()
    configure_logging(arguments.verbose)

    data_file = os.getenv(
        "RELAY_DATA_FILE",
        "relays.json"
    )

    relays = load_relays(data_file)

    matches = scan_relays(
        relays,
        arguments.district,
        arguments.limit
    )

    logger.info("Scan complete")

    display_report(
        matches,
        arguments.district
    )


if __name__ == "__main__":
    main()
