"""
A simple calculator: two Entry boxes, a Label for the result, and one
Button per operation. Putting the four arithmetic operators behind
plain functions keeps the GUI code and the math separate.
"""

import tkinter as tk
from typing import Callable


def add(left: float, right: float) -> float:
    """
    Add two numbers.

    :param left: a real number
    :param right: a real number
    :precondition: left is a real number
    :precondition: right is a real number
    :postcondition: left is unchanged
    :postcondition: right is unchanged
    :return: the sum of left and right

    >>> add(2, 3)
    5
    >>> add(-2, 2)
    0
    """
    return left + right


def subtract(left: float, right: float) -> float:
    """
    Subtract right from left.

    :param left: a real number
    :param right: a real number
    :precondition: left is a real number
    :precondition: right is a real number
    :postcondition: left is unchanged
    :postcondition: right is unchanged
    :return: left minus right

    >>> subtract(5, 3)
    2
    >>> subtract(3, 5)
    -2
    """
    return left - right


def multiply(left: float, right: float) -> float:
    """
    Multiply two numbers.

    :param left: a real number
    :param right: a real number
    :precondition: left is a real number
    :precondition: right is a real number
    :postcondition: left is unchanged
    :postcondition: right is unchanged
    :return: the product of left and right

    >>> multiply(4, 3)
    12
    >>> multiply(-2, 3)
    -6
    """
    return left * right


def divide(left: float, right: float) -> float:
    """
    Divide left by right.

    Raises ZeroDivisionError if right is 0.

    :param left: a real number
    :param right: a real number
    :precondition: left is a real number
    :precondition: right is a real number
    :postcondition: left is unchanged
    :postcondition: right is unchanged
    :return: left divided by right

    >>> divide(6, 3)
    2.0
    >>> divide(7, 2)
    3.5
    >>> divide(1, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    """
    return left / right


def build_window() -> tk.Tk:
    """
    Build the calculator window.

    :postcondition: a Tk root window is created with two entries, a
                     result label, and one button per operation, wired
                     to add/subtract/multiply/divide
    :return: the Tk root window
    """
    root = tk.Tk()
    root.title('Simple Calculator')

    left_entry = tk.Entry(root)
    left_entry.grid(row=0, column=0, padx=5, pady=5)

    right_entry = tk.Entry(root)
    right_entry.grid(row=0, column=1, padx=5, pady=5)

    result_label = tk.Label(root, text='Result: ')
    result_label.grid(row=2, column=0, columnspan=4, pady=10)

    def on_operation(task: Callable) -> None:
        """
        Perform the specified operation on the values in the entry fields.
        """
        try:
            left = float(left_entry.get())
            right = float(right_entry.get())
            result_label.config(text=f'Result: {task(left, right)}')
        except (ValueError, ZeroDivisionError) as error:
            result_label.config(text=f'Result: error ({error})')

    operations = [('+', add), ('-', subtract), ('*', multiply), ('/', divide)]
    for column, (symbol, operation) in enumerate(operations):
        button = tk.Button(root, text=symbol,
                           command=lambda op=operation: on_operation(op))
        button.grid(row=1, column=column, padx=5, pady=5)

    return root


def main():
    """
    Drive the program.
    """
    root = build_window()
    root.mainloop()


if __name__ == '__main__':
    main()
