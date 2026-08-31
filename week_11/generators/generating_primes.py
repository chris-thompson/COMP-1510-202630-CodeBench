"""
A practical use for a generator: a sequence we do not want to build first.

There are infinitely many prime numbers, so no list can hold them all. A
generator does not need to hold them all. It computes the next one only when
something asks for it, which means an endless sequence costs us nothing but
the place we stopped.
"""

from typing import Iterator


def is_prime(candidate: int) -> bool:
    """
    Determine whether a whole number is prime.

    A prime number is a whole number greater than one whose only divisors
    are one and itself.

    :param candidate: an integer greater than or equal to zero
    :precondition: candidate must be an integer greater than or equal to zero
    :return: True if candidate is prime, otherwise False

    >>> is_prime(7)
    True
    >>> is_prime(9)
    False
    >>> is_prime(2)
    True
    >>> is_prime(1)
    False
    """
    if candidate < 2:
        return False
    for potential_divisor in range(2, candidate):
        if candidate % potential_divisor == 0:
            return False
    return True


def prime_numbers_up_to(bound: int) -> Iterator[int]:
    """
    Generate every prime number from two up to the bound inclusive.

    :param bound: an integer greater than or equal to zero
    :precondition: bound must be an integer greater than or equal to zero
    :postcondition: create a generator that yields the primes in order
    :return: a generator of the prime numbers from 2 to bound inclusive

    >>> list(prime_numbers_up_to(10))
    [2, 3, 5, 7]
    >>> list(prime_numbers_up_to(7))
    [2, 3, 5, 7]
    >>> list(prime_numbers_up_to(1))
    []
    """
    for candidate in range(2, bound + 1):
        if is_prime(candidate):
            yield candidate  # What in the great Pythonic jungle is this?


def endless_prime_numbers() -> Iterator[int]:
    """
    Generate prime numbers forever, starting at two.

    Never pass this generator to list(). A list would have to hold every
    value, and there is no last value to stop at. Take a fixed number of
    values with next() instead, or break out of the for-loop yourself.

    :postcondition: create a generator that yields prime numbers endlessly
    :return: a generator of the prime numbers in ascending order

    >>> primes = endless_prime_numbers()
    >>> [next(primes), next(primes), next(primes)]
    [2, 3, 5]
    """
    candidate = 2
    while True:
        if is_prime(candidate):
            yield candidate
        candidate += 1


def main():
    """
    Drive the program.
    """
    number = input("Find every prime up to which number? ")

    if not number.isnumeric():
        print("That is not a positive integer.")
    else:
        bound = int(number)
        primes = list(prime_numbers_up_to(bound))
        if primes:
            print(f"The primes up to {bound} are: {primes}")
        else:
            print(f"There are no primes up to {bound}.")

    print("-" * 25)

    # The endless generator. We take five values and then simply walk away;
    # the generator is left paused, forever, having computed nothing more.
    print("The first five primes, taken one at a time from an endless"
          " generator:")
    endless = endless_prime_numbers()
    for _ in range(5):
        print(" ", next(endless))


if __name__ == "__main__":
    main()
