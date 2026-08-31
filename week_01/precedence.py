"""
When an expression contains more than one operator, Python evaluates the
operators in a fixed order called operator precedence (you may remember PEDMAS
from high school math).

Parentheses are evaluated first, then ** (exponent), then * / // %, and finally
+ and -. We can always add parentheses to change the order, or just to make our
intention obvious to the next human who reads the code.
"""

# Multiplication happens before addition, so this is 2 + (3 * 4) = 14.
print('2 + 3 * 4 is', 2 + 3 * 4)

# Parentheses force the addition to happen first: (2 + 3) * 4 = 20.
print('(2 + 3) * 4 is', (2 + 3) * 4)

# Exponent happens before multiplication, so this is 3 * (2 ** 2) = 12.
print('3 * 2 ** 2 is', 3 * 2 ** 2)

# We can use str() to convert a number into a string before printing it.
# This is the third conversion function, alongside int() and float().
answer = 2 + 3 * 4
answer_as_text = str(answer)
print('The answer as a string is ' + answer_as_text)
print('The type is', type(answer_as_text))
