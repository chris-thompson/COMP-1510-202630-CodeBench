"""
Some fun looping exercises for you. Implement the code!
"""


def get_user_input():
    """
    Get user input using a sentinel while loop, and return a list of
    string when QUIT is typed.
    """
    pass


def print_using_for(any_old_list):
    """
    Iterate over the list, and print it out one item per line, using a
    for item in loop.
    """
    pass


def print_using_range(any_old_list):
    """
    Iterate over the list, and print it out one item per line, using a
    loop with a range.
    """
    pass


def print_using_while(word_list):
    """
    Iterate over the list, and print it out one item per line, using a
    while loop and a list index.
    """
    pass


def print_in_reverse(word_list):
    """
    Iterate over the list, and print it out one item per line in reverse
    order, using a while loop and a list index.
    """
    pass


def long_word(word_list):
    """
    Iterate over the list, return the length of the longest word in the
    list, using a for item in loop
    """
    pass


def short_word(word_list):
    """
    Iterate over the list, return the minimum word length in the list,
    using a while loop and a list index
    """
    return 0


def avg_word_length(word_list):
    """
    Iterate over the list, return the average word length,
    using a for loop with a range.
    """
    return 0


def unique_words(word_list):
    """
    Iterate over the list, create and return a new list that only contains
    the unique words from the original list
    """
    return []


def tests():
    a_list = get_user_input()
    print("Test 1: a_list=", a_list)

    print("\nTest 2: print_using_for...")
    print_using_for(a_list)

    print("\nTest 3: print_using_range...")
    print_using_range(a_list)

    print("\nTest 4: print_using_while...")
    print_using_while(a_list)

    print("\nTest 5: print_in_reverse...")
    print_in_reverse(a_list)

    lng = long_word(a_list)
    print(f"\nTest 6: longest word has {lng} chars")

    sht = short_word(a_list)
    print(f"\nTest 7: shortest word has {sht} chars")

    avg = avg_word_length(a_list)
    print(f"\nTest 8: avg word length is {avg:.1f}")

    ul = unique_words(a_list)
    print("\nTest 9: unique_list =", ul)


def main():
    """
    Drive the tests.
    """
    tests()


if __name__ == "__main__":
    main()
