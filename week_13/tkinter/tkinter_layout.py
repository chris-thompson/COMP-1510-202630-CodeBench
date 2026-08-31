"""
Three ways tkinter arranges widgets in a window: pack, grid, and place.
Pick ONE geometry manager per container -- mixing pack and grid in the
same parent raises an error.
"""

import tkinter as tk


def build_with_pack() -> tk.Tk:
    """
    Stack three labels with pack, which places widgets in order.

    :postcondition: a Tk root window is created with three labels stacked
                     top to bottom by pack
    :return: the Tk root window
    """
    root = tk.Tk()
    root.title('pack')
    tk.Label(root, text='Top').pack()
    tk.Label(root, text='Middle').pack()
    tk.Label(root, text='Bottom').pack()
    return root


def build_with_grid() -> tk.Tk:
    """
    Lay out a small form with grid, which places widgets in rows and columns.

    :postcondition: a Tk root window is created with two labelled entry
                     fields arranged by grid in two rows and two columns
    :return: the Tk root window
    """
    root = tk.Tk()
    root.title('grid')
    tk.Label(root, text='Name:').grid(row=0, column=0)
    tk.Entry(root).grid(row=0, column=1)
    tk.Label(root, text='Score:').grid(row=1, column=0)
    tk.Entry(root).grid(row=1, column=1)
    return root


def build_with_place() -> tk.Tk:
    """
    Pin a label at an exact pixel position with place.

    :postcondition: a Tk root window is created with one label positioned
                     at exact x, y pixel coordinates by place
    :return: the Tk root window
    """
    root = tk.Tk()
    root.title('place')
    root.geometry('200x120')
    tk.Label(root, text='Pinned at (50, 40)').place(x=50, y=40)
    return root


def main():
    """
    Drive the program.
    """
    root = build_with_grid()
    root.mainloop()


if __name__ == '__main__':
    main()
