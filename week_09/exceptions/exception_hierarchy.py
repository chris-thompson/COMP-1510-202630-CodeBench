"""
Every exception type in Python has a parent, and catching a parent catches
every one of its children.

The family tree begins at BaseException. Almost everything a program should
handle sits underneath Exception:

    BaseException
     +-- KeyboardInterrupt         the user pressed Ctrl-C
     +-- SystemExit                the program asked to stop
     +-- Exception
          +-- ArithmeticError
          |    +-- ZeroDivisionError
          +-- LookupError
          |    +-- IndexError
          |    +-- KeyError
          +-- OSError
          |    +-- FileNotFoundError
          |    +-- PermissionError
          +-- TypeError
          +-- ValueError

Two consequences follow, and this module demonstrates both:

1. A parent handler catches its children. One 'except LookupError' handles
   both IndexError and KeyError.
2. Order matters. Python tries each except block from top to bottom and
   uses the first one that matches, so a broad handler placed above a
   narrow one makes the narrow one unreachable. This is a debugging
   nightmare. Trust me. I've done it. Don't do it.
"""


def divide(numerator: int, denominator: int) -> str:
    """
    Divide two integers and report the result, catching arithmetic failures.

    ZeroDivisionError is a child of ArithmeticError, so the parent handler
    below catches it. We use type(error).__name__ here to prove which child
    actually arrived.

    :param numerator: an int to divide (dividend)
    :param denominator: an int to divide by (divisor)
    :precondition: numerator is an int
    :precondition: denominator is an int
    :return: a str holding either the quotient or the name of the exception

    >>> divide(10, 2)
    '5.0'
    >>> divide(1, 0)
    'ArithmeticError handled ZeroDivisionError'
    >>> divide(0, 5)
    '0.0'
    """
    try:
        quotient = numerator / denominator
    except ArithmeticError as error:
        return f'ArithmeticError handled {type(error).__name__}'
    else:
        return str(quotient)


def look_up(container, key) -> str:
    """
    Look up a key in a container and report the result.

    A list raises IndexError and a dictionary raises KeyError, but both are
    children of LookupError, so a single handler covers both containers.

    :param container: a list or a dict
    :param key: an int index if container is a list, otherwise a dict key
    :precondition: container is a list or a dict
    :precondition: key is an int if container is a list
    :return: a str holding either the value found or the name of the exception

    >>> look_up({'ada': 1815}, 'ada')
    '1815'
    >>> look_up({'ada': 1815}, 'grace')
    'LookupError handled KeyError'
    >>> look_up([10, 20], 5)
    'LookupError handled IndexError'
    """
    try:
        value = container[key]
    except LookupError as error:
        return f'LookupError handled {type(error).__name__}'
    else:
        return str(value)


def convert_specific_first(text: str) -> str:
    """
    Convert a str to an int, trying the narrow handler before the broad one.

    This is the correct order: ValueError is a child of Exception, so it must
    be listed first or it will never be reached.

    :param text: a str to convert
    :precondition: text is a str
    :return: a str holding either the converted number or a diagnosis

    >>> convert_specific_first('42')
    '42'
    >>> convert_specific_first('forty-two')
    'that is not a number'
    >>> convert_specific_first('')
    'that is not a number'
    """
    try:
        number = int(text)
    except ValueError:
        return 'that is not a number'
    except Exception:
        return 'something else went wrong'
    else:
        return str(number)


def convert_general_first(text: str) -> str:
    """
    Convert a str to an int, wrongly trying the broad handler first.

    Python never reaches the ValueError block below: Exception is its parent,
    so the first handler matches every time and the specific message is dead
    code. Compare the output with convert_specific_first.

    :param text: a str to convert
    :precondition: text is a str
    :return: a str holding either the converted number or a diagnosis

    >>> convert_general_first('42')
    '42'
    >>> convert_general_first('forty-two')
    'something else went wrong'
    >>> convert_general_first('')
    'something else went wrong'
    """
    try:
        number = int(text)
    except Exception:
        return 'something else went wrong'
    except ValueError:
        return 'that is not a number'
    else:
        return str(number)


def main():
    """
    Drive the program.
    """
    print('A parent handler catches its children:')
    print(' ', divide(10, 2))
    print(' ', divide(1, 0))
    print(' ', look_up({'ada': 1815}, 'grace'))
    print(' ', look_up([10, 20], 5))

    print('\nOrder matters. Same input, two different answers:')
    print('  specific first:', convert_specific_first('forty-two'))
    print('  general first: ', convert_general_first('forty-two'))
    print('\nThe second function loses the useful message. Never handle')
    print('Exception before the specific errors you actually expect.')


if __name__ == '__main__':
    main()
