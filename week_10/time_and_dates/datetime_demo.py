"""
The datetime module: dates and times as values, not as strings.

A date is not a string. "2026-11-09" is a string that happens to look like a
date. If we try to add seven days to it or ask which of two came
first or find out what weekday it lands on, the string is useless. Storing
dates as strings and picking them apart with slicing is one of the most common
beginner mistakes, and it fails the instant someone types a date in a
different format. It is unnecessary tedium. Don't do it.

The datetime module gives us real types instead:

    date          a calendar day, with no time attached
    time          a time of day, with no date attached
    datetime      both together
    timedelta     a duration, i.e., the difference between two of the above

The rule of thumb is to parse input into a real datetime as early as you can,
do all the arithmetic and comparison on those structures, and format back into
a string only at the moment you print it.

Note that time.perf_counter (see profiling.py) and datetime answer different
questions. perf_counter measures how long your code took. datetime tells you
what day it is. Do not use either one for the other's job.
"""

import datetime

TERM_START = datetime.date(2026, 9, 8)
TERM_WEEKS = 14


def days_between(first: datetime.date, second: datetime.date) -> int:
    """
    Calculate the number of days from one date to another.

    Subtracting two dates gives a timedelta, and a timedelta knows how many
    days it holds. There is no calendar arithmetic for us to get wrong, and
    leap years are already handled.

    :param first: the earlier date
    :param second: the later date
    :precondition: first must be a datetime.date
    :precondition: second must be a datetime.date
    :postcondition: calculate the difference without modifying any argument
    :return: the number of days from first to second, negative if
             second is earlier

    >>> days_between(datetime.date(2026, 9, 8), datetime.date(2026, 9, 15))
    7
    >>> days_between(datetime.date(2026, 9, 8), datetime.date(2026, 9, 8))
    0
    >>> days_between(datetime.date(2026, 3, 1), datetime.date(2026, 2, 1))
    -28
    """
    return (second - first).days


def add_weeks(start: datetime.date, weeks: int) -> datetime.date:
    """
    Calculate the date a given number of weeks after a start date.

    :param start: the date to count from
    :param weeks: the number of weeks to add
    :precondition: start must be a datetime.date
    :precondition: weeks must be an integer
    :postcondition: build a new date, leaving start unmodified
    :return: the date that many weeks later

    >>> add_weeks(datetime.date(2026, 9, 8), 1)
    datetime.date(2026, 9, 15)
    >>> add_weeks(datetime.date(2026, 9, 8), 0)
    datetime.date(2026, 9, 8)
    >>> add_weeks(datetime.date(2026, 12, 29), 1)
    datetime.date(2027, 1, 5)
    """
    return start + datetime.timedelta(weeks=weeks)


def describe_date(day: datetime.date) -> str:
    """
    Format a date as a readable sentence.

    strftime turns a date into a string using format codes. %A is the weekday
    name, %B the month name, %d the day, and %Y the four digit year. The full
    list is in the datetime documentation, and nobody memorises it.

    :param day: the date to describe
    :precondition: day must be a datetime.date
    :postcondition: build the description without modifying any argument
    :return: the formatted date as a string

    >>> describe_date(datetime.date(2026, 9, 8))
    'Tuesday, September 08, 2026'
    >>> describe_date(datetime.date(2026, 12, 11))
    'Friday, December 11, 2026'
    """
    return day.strftime("%A, %B %d, %Y")


def parse_date(text: str) -> datetime.date:
    """
    Convert a date written as YYYY-MM-DD into a real date structure.

    strptime is strftime run backwards: it reads a string using the same
    format codes. It raises ValueError when the text does not match, which is
    a feature. A wrong date should fail loudly and immediately, not quietly
    become nonsense three functions later.

    :param text: a date written in YYYY-MM-DD form
    :precondition: text must be a string in YYYY-MM-DD form naming a real date
    :postcondition: build a date without modifying any argument
    :return: the date as a datetime.date
    :raises ValueError: if text is not a real date in YYYY-MM-DD form

    >>> parse_date("2026-11-09")
    datetime.date(2026, 11, 9)
    >>> parse_date("2026-02-29")
    Traceback (most recent call last):
    ValueError: day 29 must be in range 1..28 for month 2 in year 2026
    """
    return datetime.datetime.strptime(text, "%Y-%m-%d").date()


def main():
    """
    Drive the program. Demonstrate dates, durations, and formatting.
    """
    # datetime.date.today() and datetime.datetime.now() read the system clock,
    # so they give a different answer every day. That is exactly why neither
    # one appears in a doctest above.
    today = datetime.date.today()
    print(f"Today is {describe_date(today)}")

    print(f"The term began on {describe_date(TERM_START)}")

    # Week 1 is the term's first week, so week 14 is thirteen weeks after it,
    # not fourteen. Off-by-one errors do not stop at list indices.
    final_week = add_weeks(TERM_START, TERM_WEEKS - 1)
    print(f"Week {TERM_WEEKS} begins on {describe_date(final_week)}")
    print(f"That is {days_between(TERM_START, final_week)} days of COMP 1510")

    elapsed = days_between(TERM_START, today)
    if elapsed < 0:
        print(f"The term starts in {-elapsed} days")
    else:
        print(f"The term started {elapsed} days ago")

    # Comparison works the way you would hope, because these are real values.
    print(f"Has the term started? {today >= TERM_START}")

    parsed = parse_date("2026-11-09")
    print(f"Parsed '2026-11-09' into {parsed}, a {type(parsed).__name__}")


if __name__ == "__main__":
    main()
