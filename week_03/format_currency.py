"""
We can use an f-string to display a floating point number as a currency.

The format specifier ,.2f adds a comma as the thousands separator and shows
2 digits after the decimal point.
"""

monthly_pay = 5000.0  # Is that enough to pay a mortgage in Vancouver?
annual_pay = monthly_pay * 12
print(f'Your annual pay is ${annual_pay}')
print(f'Your annual pay is ${annual_pay:,.2f}')
