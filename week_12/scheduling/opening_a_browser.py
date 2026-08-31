"""
webbrowser opens a page in whatever browser this computer prefers.

subprocess can start any program, including a browser, but we would have to
know where the browser lives and what it is called, and the answer differs
on every machine. The webbrowser module already knows.

This is a one-function module, and that is the point: some jobs that sound
hard have been done for us already. Look for the module before writing the
code.

Running this file opens a browser tab. That is not something a program
should do without warning, so it asks first.
"""

import webbrowser

BCIT_URL = "https://www.bcit.ca"
YES_ANSWERS = ("y", "yes")


def wants_to_continue(answer: str) -> bool:
    """
    Decide whether an answer typed by a user means yes.

    :param answer: a string
    :precondition: answer must be a string
    :return: True if the answer is "y" or "yes", ignoring capitals and
             surrounding spaces, otherwise False

    >>> wants_to_continue("y")
    True
    >>> wants_to_continue("  YES ")
    True
    >>> wants_to_continue("n")
    False
    """
    return answer.strip().lower() in YES_ANSWERS


def open_page(url: str) -> bool:
    """
    Open a URL in this computer's preferred browser.

    :param url: a string containing a URL
    :precondition: url must be a string containing a URL
    :postcondition: a browser is asked to open the URL
    :return: True if a browser was found and asked, otherwise False
    """
    return webbrowser.open(url)


def main():
    """
    Drive the program.
    """
    print(f"This will open {BCIT_URL} in your browser.")
    answer = input("Go ahead? (y/n) ")
    if not wants_to_continue(answer):
        print("Left alone. Nothing was opened.")
        return
    if open_page(BCIT_URL):
        print("Asked your browser to open the page.")
    else:
        print("No browser could be found on this computer.")


if __name__ == "__main__":
    main()
