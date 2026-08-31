"""
We often want to update a variable using its own current value.

For example, we might want to add 1 to a variable, or subtract 50 from it.
We can always write this out the long way:

    age_years = age_years + 1

The variable appears on both sides of the equal sign. The expression on the
right is evaluated first, and then the result is assigned back to the variable
on the left. The original value is replaced.

Because we do this so often, Python gives us a typing shortcut called a
compound (or augmented) assignment operator. Each one combines an arithmetic
operator with the equal sign.
"""

# Start with some values.
age_years = 20
account_balance = 100.00
number_of_calls = 4
remainder = 9
offset = 17
base = 5

# Add 1 to age_years (age_years += 1 means age_years = age_years + 1).
age_years += 1
print('age_years:', age_years)

# Subtract 50.00 from account_balance.
account_balance -= 50.00
print('account_balance:', account_balance)

# Multiply number_of_calls by 2.
number_of_calls *= 2
print('number_of_calls:', number_of_calls)

# Divide remainder by 2 (this always produces a float).
remainder /= 2
print('remainder:', remainder)

# Replace offset with the remainder of offset divided by base.
offset %= base
print('offset:', offset)
