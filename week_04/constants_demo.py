"""
Two ways to work with values that must never change: constants.

Python has no 'const' keyword, so a constant is a promise we make to
ourselves and other developers. Two conventions help us keep that promise.
"""

# Convention 1: module-level constants, written in ALL_CAPS and defined at the
# top of the module (after the imports, before the functions). The capital
# letters tell every reader "do not reassign me."
CM_PER_INCH = 2.54
INCHES_PER_FOOT = 12


def avogadro_constant():
    """
    Return Avogadro's constant (particles per mole).

    Wrapping a fixed value in a function is a small hack for a constant we
    truly never want reassigned: there is no variable to overwrite, only a
    function to call.

    :postcondition: return Avogadro's constant as a float
    :return: Avogadro's constant, 6.02e23, as a float

    >>> avogadro_constant()
    6.02e+23
    """
    return 6.02e23


def main():
    """
    Drive the program.
    """
    height_in_inches = 5 * INCHES_PER_FOOT + 9
    print("5 feet 9 inches is", height_in_inches * CM_PER_INCH, "cm")

    moles = 2
    print(moles, "moles is", moles * avogadro_constant(), "particles")


if __name__ == "__main__":
    main()
