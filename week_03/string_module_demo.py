"""
The string module gives us handy ready-made collections of characters.

These constants are just plain strings, so everything we know about strings
works on them: len(), indexing with [], looping, and so on. Lab 03 will put
them to use.
"""
import random
import string


def main():
    """
    Drive the program.
    """
    print('Lowercase letters:', string.ascii_lowercase)
    print('Uppercase letters:', string.ascii_uppercase)
    print('Digits:', string.digits)
    print('Punctuation:', string.punctuation)

    print('There are', len(string.ascii_lowercase), 'lowercase letters')
    print('The first lowercase letter is', string.ascii_lowercase[0])

    # Combine string and random: pick one random lowercase letter
    random_letter = random.choice(string.ascii_lowercase)
    print('A random letter:', random_letter)


if __name__ == '__main__':
    main()
