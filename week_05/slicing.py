"""
Slicing sequences.

Indexing with one integer gives us a single element. Slicing with a
colon gives us a new sequence built from a range of elements. Slicing
works on any sequence type: strings, lists, tuples, and ranges.
"""


def main():
    """
    Drive the program.
    """
    greeting = 'hello world'
    print(greeting[4])  # indexing: a single element
    print(greeting[1:5])  # from index 1 up to, but not including, 5
    print(greeting[:5])  # omitting the first index starts at the front
    print(greeting[6:])  # omitting the second index runs to the end

    letters = list('Hello world')
    print(letters)
    print(letters[0:5])
    print(letters[6:])

    # Negative indices count backwards from the end
    print(letters[-1])
    print(letters[-5:])

    # A slice is a new sequence; the original is untouched
    first_five = letters[:5]
    first_five[0] = 'J'
    print(first_five)
    print(letters)

    # Slicing a tuple makes a new tuple
    measurements = (1, 2, 3, 4, 5)
    print(measurements[1:4])


if __name__ == '__main__':
    main()
