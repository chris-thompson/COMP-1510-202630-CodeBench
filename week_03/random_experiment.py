"""
Play with the random module: random integers, single choices, and sampling.

random.choices(population, k=n) returns n items chosen *with* replacement, so
repeats are allowed. We must name the k parameter (I'll show you why in a few
weeks -- trust me for now). random.sample chooses *without* replacement, so we
can never ask for more items than the population contains.
"""
import random


def main():
    """
    Drive the program. Let's play with random!
    """
    my_random = random.randint(0, 10)
    print(my_random)

    population = "1234567890"

    one_digit = random.choice(population)
    print(one_digit)

    chosen_digits = random.choices(population, k=6)  # k must be named
    print(chosen_digits)

    pin = "".join(chosen_digits)
    print(pin)

    unique_digits = random.sample(population, 6)  # no repeats
    print(unique_digits)


if __name__ == "__main__":
    main()
