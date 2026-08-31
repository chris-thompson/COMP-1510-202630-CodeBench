"""
Waiting until a particular moment, with datetime and time.

A program that runs while we watch it is one thing. A program that runs at
three in the morning without us is another, and it is how a great deal of
real software works: backups, reports, tidying up yesterday's files.

The crude way to arrange it is the loop below. Work out the moment we are
waiting for, then sleep in short naps until the clock passes it. Sleeping is
how a program waits without burning the processor doing nothing.

time and datetime were introduced in Week 10, in week_10/time_and_dates/.
The new idea here is only what we are using them for.

This is the crude way on purpose, because it fits in ten lines and shows the
shape of the problem. A real scheduled job is handed to the operating system
instead, with cron on macOS and Linux or Task Scheduler on Windows, so that
it runs even when no Python program is sitting there waiting.

This file waits a few seconds, not until three in the morning.
"""

import datetime
import time

SECONDS_TO_WAIT = 5
NAP_SECONDS = 1


def moment_after(start: datetime.datetime,
                 seconds: int) -> datetime.datetime:
    """
    Work out the moment a number of seconds after a starting moment.

    :param start: a datetime
    :param seconds: an integer of 0 or greater
    :precondition: start must be a datetime
    :precondition: seconds must be an integer of 0 or greater
    :postcondition: start is unchanged
    :return: a datetime the given number of seconds after start

    >>> midnight = datetime.datetime(2026, 11, 23, 0, 0, 0)
    >>> moment_after(midnight, 90)
    datetime.datetime(2026, 11, 23, 0, 1, 30)
    >>> moment_after(midnight, 0)
    datetime.datetime(2026, 11, 23, 0, 0)
    """
    return start + datetime.timedelta(seconds=seconds)


def seconds_remaining(now: datetime.datetime,
                      deadline: datetime.datetime) -> float:
    """
    Work out how many seconds are left before a deadline.

    :param now: a datetime
    :param deadline: a datetime
    :precondition: now must be a datetime
    :precondition: deadline must be a datetime
    :postcondition: now is unchanged
    :postcondition: deadline is unchanged
    :return: the seconds from now until deadline, negative once the
             deadline has passed

    >>> start = datetime.datetime(2026, 11, 23, 0, 0, 0)
    >>> seconds_remaining(start, moment_after(start, 30))
    30.0
    >>> seconds_remaining(moment_after(start, 30), start)
    -30.0
    """
    return (deadline - now).total_seconds()


def main():
    """
    Drive the program.
    """
    deadline = moment_after(datetime.datetime.now(), SECONDS_TO_WAIT)
    print(f"It is now  {datetime.datetime.now():%H:%M:%S}")
    print(f"Waiting for {deadline:%H:%M:%S}\n")

    while datetime.datetime.now() < deadline:
        left = seconds_remaining(datetime.datetime.now(), deadline)
        print(f"  still waiting, {left:.1f} seconds to go", flush=True)
        time.sleep(NAP_SECONDS)

    print(f"\nIt is now  {datetime.datetime.now():%H:%M:%S}. Off we go.")


if __name__ == "__main__":
    main()
