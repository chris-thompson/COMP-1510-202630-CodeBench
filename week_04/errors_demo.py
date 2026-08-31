"""
Three kinds of error, in one place.

A Python program can go wrong in three different ways. This file gathers all
three so we can tell them apart.

1. SYNTAX ERROR: the code breaks the rules of the language, so the interpreter
   refuses to run ANY of it. We cannot show a live syntax error in a file that
   still runs, because the whole file would refuse to start. Here is what one
   looks like (leave it commented -- uncomment it and nothing in this file
   runs):

       print"Hello world"      # missing parentheses -> SyntaxError

2. RUNTIME ERROR (an "exception") -- the code is valid, so the program starts,
   but something impossible happens while it runs and the program crashes. The
   classic example is dividing by zero. See the commented line in main().

3. LOGIC ERROR (a "semantic" error) -- the code is valid AND it runs to the end
   without crashing, but the answer is simply wrong. These are the hardest to
   find, because Python gives us no warning at all. The divide() function below
   has one: it was supposed to divide, but it adds.
"""


def divide(quotient, divisor):
    # LOGIC ERROR: this should return quotient / divisor, but it adds instead.
    return quotient + divisor


def main():
    # The program runs happily and prints an answer -- but the answer is wrong.
    # We asked for 6 / 2 (which is 3.0) and got 8. Nothing crashed, nothing was
    # underlined in red. That is what makes a logic error dangerous.
    print("6 divided by 2 should be 3.0, but divide() returns:", divide(6, 2))

    # RUNTIME ERROR: uncomment the next line to watch the program crash with a
    # ZeroDivisionError. Notice the crash happens WHILE the program runs, not
    # before it starts.
    # print(10 / 0)


if __name__ == "__main__":
    main()
