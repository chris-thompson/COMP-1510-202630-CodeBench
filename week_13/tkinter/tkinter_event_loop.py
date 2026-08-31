"""
A tkinter program looks like it "hangs" after you run it -- it hasn't
crashed. mainloop() is the event loop: it sits and waits for events
(clicks, key presses, window close) and reacts to each one as it
arrives. Closing the window is what lets main() return.
"""

import tkinter as tk


def build_window() -> tk.Tk:
    """
    Build a window containing a single label.

    :postcondition: a Tk root window is created with one child label
    :return: the Tk root window
    """
    root = tk.Tk()
    root.title('Event Loop Demo')
    label = tk.Label(root, text='Close this window to end the program.')
    label.pack(padx=20, pady=20)
    return root


def main():
    """
    Drive the program.
    """
    root = build_window()
    root.mainloop()  # blocks here until the window is closed


if __name__ == '__main__':
    main()
