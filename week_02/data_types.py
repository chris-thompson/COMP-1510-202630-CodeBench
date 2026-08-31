"""
Every datum has a type.

The type of a value decides what we are allowed to do with it. We can
add and subtract integers, but it makes no sense to find the square root
of a word. Python tracks the type of every value for us, and the built-in
type() function lets us ask what that type is.

These are the basic types we use in COMP 1510:

    int      whole numbers, such as -4, 17, or 2022
    float    numbers with a decimal point, such as 3.14 or -19.73
    bool     the truth values True and False
    str      strings of characters in quotes, such as "blue"
    NoneType the special value None, meaning "no data"

The program works like this:
    The type of 17 is: <class 'int'>
"""

# Ask Python for the type of one value of each basic kind.
print("The type of 17 is:", type(17))
print("The type of 3.14 is:", type(3.14))
print("The type of True is:", type(True))
print("The type of 'blue' is:", type('blue'))
print("The type of None is:", type(None))

# The type also follows the value a variable refers to.
colour_of_eyes = "blue"
print("colour_of_eyes holds a", type(colour_of_eyes))

# A value's type decides what operations make sense.
# We can add two integers...
print("17 + 4 is", 17 + 4)
# ...but adding an integer to a word is not allowed, so we do not try it.
