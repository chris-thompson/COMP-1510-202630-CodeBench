"""
f-strings are the modern, readable way to build strings in Python.

An f-string is a string literal prefixed with f or F. Any expression inside
curly braces is evaluated, and its value is inserted into the string.
"""


def main():
    """
    Drive the program.
    """
    name = 'Phoebe'
    age = 59
    print(f'Hello {name}!')
    print(f'{name} is {age} years old')

    # Any expression works inside the braces, not just a plain variable
    print(f'Next year {name} will be {age + 1}')

    # We can even call a method inside the braces
    course = 'oop 2 with python'
    print(f'My favourite course (so far) is {course.title()}!')

    # A format specifier goes after a colon: comma separator, 2 decimals
    price = 1234567.5
    print(f'The total is ${price:,.2f}')


if __name__ == '__main__':
    main()
