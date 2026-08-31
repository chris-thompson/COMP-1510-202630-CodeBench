"""
tkinter widgets (including the root window) can listen for keyboard events.
Here every key press is reported by name, the foundation for games,
navigation, and shortcuts.
"""

import tkinter as tk


def describe_key(keysym: str) -> str:
    """
    Build the message shown when a key with the given keysym is pressed.

    :param keysym: the symbolic name tkinter gives a key, e.g. 'a', 'Return'
    :precondition: keysym is a non-empty string
    :postcondition: keysym is unchanged
    :return: a human-readable description of the key press

    >>> describe_key('a')
    'Key pressed: a'
    >>> describe_key('Return')
    'Key pressed: Return'
    """
    return f'Key pressed: {keysym}'


def build_keyboard_window() -> tk.Tk:
    """
    Build a window that prints a description of every key the user presses.

    :postcondition: a Tk root window is created whose key-press event is
                     bound to a handler that prints describe_key(...) for
                     each press
    :return: the Tk root window
    """
    root = tk.Tk()
    root.title('Keyboard Demo')
    root.geometry('300x200')

    def on_key(event: tk.Event) -> None:
        """
        Report the name of the key that was pressed.
        """
        # event.keysym names the key: 'a', 'space', 'Return', 'Left', ...
        print(describe_key(event.keysym))

    # '<KeyPress>' fires for any key; bind to the root so focus is the window.
    root.bind('<KeyPress>', on_key)
    return root


def main():
    """
    Drive the program.
    """
    root = build_keyboard_window()
    root.mainloop()


if __name__ == '__main__':
    main()
