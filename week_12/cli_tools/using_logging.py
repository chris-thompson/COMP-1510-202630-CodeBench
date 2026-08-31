"""
The logging module is the professional replacement for debug print() calls.

A print() call has no level, no timestamp, and no off switch. When we are
finished debugging we go hunting through the file deleting the calls one by
one, and when the bug comes back we write them all again.

Every logging record instead carries a level, a timestamp, and the name of
whatever produced it. We choose a level once, when the program starts, and
every call below that level goes quiet without a single line of code
changing. The five levels, from least to most serious, are DEBUG, INFO,
WARNING, ERROR, and CRITICAL.

Records go to the console by default. Give basicConfig a filename instead
and the same records go to a file, which is what a program that runs
unattended needs: something to read afterwards to find out what happened.

Records go to standard error, while print() goes to standard output. They
are two different streams, so the prints below use flush=True to keep the
two in step with each other on the screen.

Run this file and then open using_logging.log to see the difference.
"""

import logging

LOG_FILE = "using_logging.log"

LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}


def configure_logging(level_name: str = "INFO",
                      log_file: str | None = None) -> None:
    """
    Configure logging to write level-tagged records to the console or a file.

    Levels arrive as strings, because that is how a user types them on the
    command line or writes them in a .env file. The LEVELS dictionary turns
    that string into the constant the logging module wants.

    force=True lets us call this function more than once in one program.
    Without it, only the first call would have any effect.

    :param level_name: a key of LEVELS
    :param log_file: the name of a file to write records to, or None to
                     write to the console
    :precondition: level_name must be a key of LEVELS
    :precondition: log_file must be a string or None
    :postcondition: records at or above level_name are written to log_file,
                    or to the console when log_file is None
    :postcondition: records below level_name are discarded
    :return: None
    """
    logging.basicConfig(
        level=LEVELS[level_name],
        format="%(asctime)s %(levelname)s: %(message)s",
        filename=log_file,
        force=True,
    )


def divide(numerator: float, denominator: float) -> float | None:
    """
    Divide a numerator by a denominator, logging the attempt and the result.

    The logging calls use %s placeholders rather than an f-string. The
    logging module only builds the finished message if the record is
    actually going to be written, so a DEBUG call in a program running at
    INFO level costs almost nothing.

    :param numerator: a real number
    :param denominator: a real number
    :precondition: numerator must be a real number
    :precondition: denominator must be a real number
    :postcondition: an INFO record is logged describing the attempt
    :postcondition: an ERROR record is logged when denominator is zero
    :return: the quotient, or None when denominator is zero

    >>> configure_logging("CRITICAL")
    >>> divide(10, 2)
    5.0
    >>> divide(-9, 3)
    -3.0
    >>> divide(10, 0) is None
    True
    """
    logging.info("Dividing %s by %s", numerator, denominator)
    if denominator == 0:
        logging.error("Cannot divide %s by zero", numerator)
        return None
    return numerator / denominator


def main():
    """
    Drive the program.
    """
    print("First, at DEBUG level, writing to the console:", flush=True)
    configure_logging("DEBUG")
    logging.debug("Starting up. Only DEBUG level or lower shows this.")
    print("10 / 2 =", divide(10, 2), flush=True)
    print("10 / 0 =", divide(10, 0), flush=True)
    logging.warning("This is a warning, not an error.")

    print("\nNow at WARNING level. The INFO records go quiet:", flush=True)
    configure_logging("WARNING")
    print("10 / 2 =", divide(10, 2), flush=True)
    print("10 / 0 =", divide(10, 0), flush=True)

    configure_logging("INFO", LOG_FILE)
    logging.info("This record went to a file, not to the console.")
    divide(7, 0)
    print(f"\nThe last few records went to {LOG_FILE}.", flush=True)
    print("Open it and read it.", flush=True)


if __name__ == "__main__":
    main()
