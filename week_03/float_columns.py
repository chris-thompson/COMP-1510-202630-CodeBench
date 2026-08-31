"""
We can use an f-string to display a floating point number in a field of
7 spaces with 2 decimal places.

The part after the colon, 7.2f, is a format specifier: a field 7 characters
wide, showing 2 digits after the decimal point, for a float (f).
"""

num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999

print(f'{num1:7.2f}')
print(f'{num2:7.2f}')
print(f'{num3:7.2f}')
print(f'{num4:7.2f}')
print(f'{num5:7.2f}')
print(f'{num6:7.2f}')
