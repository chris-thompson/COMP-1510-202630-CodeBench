"""
An if-elif-else example.

The pH scale measures how acidic or basic a solution is. A value below
7.0 is acidic, exactly 7.0 is neutral, and above 7.0 is basic (alkaline).

Notice that the branches are mutually exclusive: exactly one of them
runs. We test for the neutral case last, after we have ruled out acidic
and basic.

The program works like this:
    Enter the pH level (include the decimal): 6.4
    6.4 is acidic.
"""

ph = float(input('Enter the pH level (include the decimal): '))

if ph < 7.0:
    print(ph, "is acidic.")
elif ph > 7.0:
    print(ph, "is basic.")
else:
    print(ph, "is neutral.")
