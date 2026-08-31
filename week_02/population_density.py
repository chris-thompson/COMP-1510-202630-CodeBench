"""
A worked solution to an in-lecture self-check.

Suppose population is a whole number of people and land_area_km is a
floating point number of square kilometres. The population density is the
number of people per square kilometre. Print "Densely populated" when the
density is greater than 60.0 people per square kilometre, and
"Sparsely populated" in all other cases.

The program works like this:
    Enter the population: 500000
    Enter the land area in square km: 1200
    Densely populated
"""

population = int(input("Enter the population: "))
land_area_km = float(input("Enter the land area in square km: "))

density = population / land_area_km

if density > 60.0:
    print("Densely populated")
else:
    print("Sparsely populated")
