"""
Experiment with comprehensions. Use the debugger to see what is happening!
"""


def main():
    """
    Drive the program.
    """
    # The loop way: map each uppercase letter to a starting count of zero.
    # chr converts a code point to its character: chr(65) is 'A'.
    tally = {}
    for code in range(65, 91):
        tally[chr(code)] = 0
    print(tally)

    # The comprehension way: one line that builds the same dictionary.
    tally_2 = {chr(code): 0 for code in range(65, 91)}
    print(tally_2)

    # Is this efficient? How many times does the expression run? Step
    # through it with the debugger and count.
    letters = [chr(code) for code in range(65, 91)]
    counts = [0] * 26
    tally_3 = {letter: count for letter in letters for count in counts}
    print(tally_3)

    # A set comprehension uses curly braces with no colon, and a set
    # keeps only one copy of each value.
    vowels_seen = {letter for letter in "encyclopedia" if letter in "aeiou"}
    print(vowels_seen)


if __name__ == "__main__":
    main()
