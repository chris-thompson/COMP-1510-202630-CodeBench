"""
Two ways to put quote characters inside a string.

1. Surround the string with the *other* kind of quote.
2. Escape the quote with a backslash.
"""

# Surround with double quotes, so the apostrophe (a single quote) needs
# no escaping
print("Don't fear!")
print("I'm here!")

# Surround with single quotes, so the double quotes need no escaping...
print('Your assignment is to read "Hamlet" by tomorrow.')

# ...or keep the double quotes and escape them with a backslash
print("Your assignment is to read \"Hamlet\" by tomorrow.")
