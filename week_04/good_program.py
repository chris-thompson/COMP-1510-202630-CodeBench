"""
When a function is done, we want it to return.

There is a sloppy way and a tidy way to move between functions.

The sloppy way: instead of returning, a function calls another function to
"continue" the work. Nothing ever returns, so every call is added to the
call stack and none is ever removed. The stack fills up sooner than we
think. Written that way, menu() calls do_something(), which calls
do_something_else(), which calls menu() again -- a loop of calls that keeps
growing the stack until, given enough time, it overflows.

The tidy way (this file): when a function finishes its work, it returns and
lets the calling function decide what to do next. menu() drives the program
with a while loop; do_something() and do_something_else() each return instead
of calling onward. The stack never grows past a couple of frames.

Profile your code to see the difference. From the main menu, choose:

    Run > Run good_program.py > Profile 'good_program.py'

This program, when profiled, reveals no loops of calls -- we are not stacking
function calls on the call stack.

What is the largest number of function calls that will ever be on the
function call stack when we execute this code?
"""


def menu():
    while True:
        # does stuff
        do_something()


def do_something():
    user_input = True  # Or calculate some value that can vary
    if user_input:  # Or if the value meets some test
        do_something_else()
    else:
        return None


def do_something_else():
    user_input = False
    if user_input:
        return
    else:
        # do whatever has to be done
        return


def main():
    menu()


if __name__ == "__main__":
    main()

# Call stack

# do_something()
# menu
# main
