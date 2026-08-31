"""
The Canvas widget is tkinter's drawable area for shapes, text, and custom
graphics. Here we bind a mouse click so each click draws a circle where the
pointer is -- the start of a simple paint tool.
"""

import tkinter as tk


def build_canvas_window() -> tk.Tk:
    """
    Build a window with a Canvas that draws a circle wherever it is clicked.

    :postcondition: a Tk root window is created containing a white Canvas
                     whose left-mouse-click is bound to a handler that draws
                     a blue circle centred on the click position
    :return: the Tk root window
    """
    root = tk.Tk()
    root.title('Canvas Demo')
    canvas = tk.Canvas(root, width=400, height=300, bg='white')
    canvas.pack()

    def draw_circle(event: tk.Event) -> None:
        """
        Draw a blue circle centred on the position that was clicked.
        """
        radius = 20
        canvas.create_oval(
            event.x - radius, event.y - radius,
            event.x + radius, event.y + radius,
            fill='blue')

    # '<Button-1>' is the left mouse button; the handler receives an event
    # object carrying the click coordinates as event.x and event.y.
    canvas.bind('<Button-1>', draw_circle)
    return root


def main():
    """
    Drive the program.
    """
    root = build_canvas_window()
    root.mainloop()


if __name__ == '__main__':
    main()
