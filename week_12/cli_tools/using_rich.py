"""
rich dresses up plain terminal output: colour, styled text, and tables.

Everything we have printed so far has been undifferentiated grey text. That
is fine while a program is small, but a report of thirty rows is much easier
to read when the headings stand out and the numbers line up in columns.

rich gives us a Console with a print() of its own. It takes the same kinds
of arguments the built-in print() takes, and it understands square-bracket
markup for style, which works rather like HTML tags.

rich is not part of the standard library. Install it first:

    pip3 install rich
"""

from rich.console import Console
from rich.table import Table

console = Console()

GRADES = [("Amy", 91), ("Bo", 78), ("Genevieve", 85), ("Hiro", 64)]


def build_grades_table(grades: list) -> Table:
    """
    Build a rich Table of student names and grades.

    Building the table and printing it are two different jobs, so they are
    two different functions. This one can be tested without anything
    reaching the screen at all.

    :param grades: a list of (name, grade) tuples
    :precondition: grades must be a list of (string, integer) tuples
    :postcondition: grades is unchanged
    :return: a rich.table.Table with one row for each tuple in grades

    >>> build_grades_table([("Amy", 91)]).row_count
    1
    >>> build_grades_table([("Amy", 91), ("Bo", 78)]).row_count
    2
    >>> build_grades_table([]).row_count
    0
    """
    table = Table(title="Grades")
    table.add_column("Name")
    table.add_column("Grade", justify="right")
    for name, grade in grades:
        table.add_row(name, str(grade))
    return table


def describe_grade(grade: int) -> str:
    """
    Describe a grade as rich markup, coloured by how good it is.

    The square brackets are rich's markup. Each opening tag names a style
    and each closing tag begins with a slash, exactly as in HTML. rich
    strips the tags out and colours the text between them.

    :param grade: an integer between 0 and 100 inclusive
    :precondition: grade must be an integer between 0 and 100 inclusive
    :return: the grade as rich markup, green at 80 and above, yellow from
             50 to 79, and red below 50

    >>> describe_grade(91)
    '[green]91[/green]'
    >>> describe_grade(79)
    '[yellow]79[/yellow]'
    >>> describe_grade(49)
    '[red]49[/red]'
    """
    if grade >= 80:
        return f"[green]{grade}[/green]"
    if grade >= 50:
        return f"[yellow]{grade}[/yellow]"
    return f"[red]{grade}[/red]"


def main():
    """
    Drive the program.
    """
    console.print("Plain text.")
    console.print("Bold, and in colour.", style="bold magenta")
    console.print("[bold red]Errors[/bold red] and [green]successes[/green] "
                  "can be marked up inline, rather like HTML.")

    console.print(build_grades_table(GRADES))

    console.print("\nThe same grades, coloured by how good they are:")
    for name, grade in GRADES:
        console.print(f"  {name}: {describe_grade(grade)}")


if __name__ == "__main__":
    main()
