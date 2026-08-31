"""
When we request information from the user, we should specify what
kind of information we want.

Remember that the input function creates a string for us to use.

We must convert the string to the correct data type.
"""

KM_PER_MILE = 1.6
LITRES_PER_GALLON = 4.54

odometer_start = int(input('Enter starting odometer reading as an integer: '))
odometer_end = int(input('Enter ending odometer reading as an integer: '))
fuel_prompt = 'Enter liters of fuel used as a floating point number: '
litres_used = float(input(fuel_prompt))

kilometres_driven = odometer_end - odometer_start
miles_driven = kilometres_driven / KM_PER_MILE
gallons_used = litres_used / LITRES_PER_GALLON

litres_per_100km = round((100 * (litres_used / kilometres_driven)), 1)
miles_per_gallon = round(miles_driven / gallons_used, 1)

print("Your fuel efficiency is:")
print('\t', litres_per_100km, 'liters per 100 kilometers')
print('\t', miles_per_gallon, 'miles per gallon')
