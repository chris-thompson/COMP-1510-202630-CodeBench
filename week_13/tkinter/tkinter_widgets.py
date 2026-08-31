"""
Three of the most common tkinter widgets: Label (shows text), Entry (a
one-line text box), and Button (runs a function when clicked).
"""

import tkinter as tk


def build_window() -> tk.Tk:
    """
    Build a window with an Entry, a Button, and a Label that the
    button updates.

    :postcondition: a Tk root window is created with an entry, a
                     button, and a label, wired together so clicking
                     the button copies the entry's text into the label
    :return: the Tk root window
    """
    root = tk.Tk()
    root.title('Widgets Demo')

    name_entry = tk.Entry(root)
    name_entry.pack(padx=20, pady=(20, 5))

    greeting_label = tk.Label(root, text='Type a name and press the button.')
    greeting_label.pack(padx=20, pady=5)

    def on_button_click() -> None:
        """
        Update the greeting label with the text from the entry.
        """
        name = name_entry.get() or 'World'
        greeting_label.config(text=f'Hello, {name}!')

    greet_button = tk.Button(root, text='Greet', command=on_button_click)
    greet_button.pack(padx=20, pady=(5, 20))

    return root


def main():
    """
    Drive the program.
    """
    root = build_window()
    root.mainloop()


if __name__ == '__main__':
    main()
