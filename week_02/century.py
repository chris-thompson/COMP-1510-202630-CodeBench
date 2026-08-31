"""
A worked solution to an in-lecture self-check.

Read a whole-number year and describe when it falls using a multi-branch
if-elif-else statement:

    2101 or later   -> "In the distant future"
    2001 to 2100    -> "In the 21st century"
    1901 to 2000    -> "In the 20th century"
    1900 or earlier -> "Long, long ago..."

The branches are tested from the largest year downward. Because each elif
is only reached when every test above it was False, we do not need to
write the upper bound of each range.

The program works like this:
    Enter a year: 1969
    In the 20th century
"""

year = int(input("Enter a year: "))

if year >= 2101:
    print("In the distant future")
elif year >= 2001:
    print("In the 21st century")
elif year >= 1901:
    print("In the 20th century")
else:
    print("Long, long ago...")
