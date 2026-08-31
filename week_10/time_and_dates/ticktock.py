"""
Hickory dickory dock, the mouse ran up the clock.

The other timing files in this folder ask how long something took.
This one does the opposite: time.sleep(seconds) pauses the program on purpose.

Sleeping is how a program waits without burning the processor doing nothing.
We will want it whenever we are polling something, animating something, or
being polite to a web server we are asking for data repeatedly.

This program takes six seconds to run, and it is meant to. Watch the clock.
"""

import time

TICKS = 3
SECONDS_BETWEEN = 1


def main():
    """
    Drive the program. Demonstrate pausing execution with time.sleep.
    """
    for _ in range(TICKS):
        print("Tick")
        time.sleep(SECONDS_BETWEEN)
        print("Tock")
        time.sleep(SECONDS_BETWEEN)


if __name__ == "__main__":
    main()
