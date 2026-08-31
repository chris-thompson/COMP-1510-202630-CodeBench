"""
Generating cryptographically secure random values with the secrets module.

The random module is fine for games and simulations, but its numbers are
predictable: an attacker who sees enough of them can guess the rest. When a
random value protects something - a password, a session token, a one-time
code - reach for the secrets module instead. It draws from the operating
system's cryptographically secure source of randomness.
"""

import secrets
import string


def secure_choice(sequence):
    """
    Return one element chosen from sequence using a secure random source.

    :param sequence: a non-empty sequence (list, tuple, or string)
    :precondition: sequence contains at least one element
    :postcondition: sequence is unchanged
    :return: one element of sequence

    >>> options = ['rock', 'paper', 'scissors']
    >>> secure_choice(options) in options
    True
    >>> secure_choice('abc') in 'abc'
    True
    >>> secure_choice((7,)) == 7
    True
    """
    return secrets.choice(sequence)


def roll_die():
    """
    Return a secure random integer from 1 to 6 inclusive.

    :postcondition: a fair, unpredictable value between 1 and 6 is produced
    :return: an integer in the range 1 to 6

    >>> 1 <= roll_die() <= 6
    True
    >>> roll_die() in {1, 2, 3, 4, 5, 6}
    True
    """
    return secrets.randbelow(6) + 1


def make_token(number_of_bytes):
    """
    Return a secure random token as a hexadecimal string.

    Each byte becomes two hexadecimal characters, so the returned string is
    twice as long as number_of_bytes.

    :param number_of_bytes: the number of random bytes to generate
    :precondition: number_of_bytes is a positive integer
    :postcondition: a fresh, unpredictable token is produced
    :return: a hexadecimal string of length 2 * number_of_bytes

    >>> len(make_token(4))
    8
    >>> len(make_token(16))
    32
    >>> set(make_token(8)) <= set(string.hexdigits)
    True
    """
    return secrets.token_hex(number_of_bytes)


def make_password(length):
    """
    Return a secure random password built from letters and digits.

    :param length: the number of characters in the password
    :precondition: length is a positive integer
    :postcondition: a fresh, unpredictable password is produced
    :return: a string of the requested length

    >>> len(make_password(12))
    12
    >>> set(make_password(20)) <= set(string.ascii_letters + string.digits)
    True
    """
    alphabet = string.ascii_letters + string.digits
    password = ''
    for _ in range(length):
        password = password + secure_choice(alphabet)
    return password


def main():
    """
    Drive the program.
    """
    print('A secure coin flip:', secure_choice(['heads', 'tails']))
    print('A secure die roll: ', roll_die())
    print('A session token:   ', make_token(16))
    print('A random password: ', make_password(12))


if __name__ == '__main__':
    main()
