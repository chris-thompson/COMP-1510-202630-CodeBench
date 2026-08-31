"""
I love cats. I love cat names.

There are two ways to use input(). We can print a prompt on its own line and
then call input() with no argument, or we can pass the prompt straight to
input() as an argument. Both work.
"""

# Style one: print the prompt first, then call input() with no argument.
print('Enter the name of cat 1:')
cat_name_1 = input()

# Style two: pass the prompt to input() as an argument.
cat_name_2 = input('Enter the name of cat 2: ')

cat_name_3 = input('Enter the name of cat 3: ')

# Pass the three names to print() separated by commas. print() puts a single
# space between each value for us.
print('The cat names are:')
print(cat_name_1, cat_name_2, cat_name_3)
