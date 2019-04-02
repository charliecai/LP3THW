# Exercise 13. Parameters, Unpacking, Variables

from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("This script is called: ", script)
print("Your first variable is: ", first)
print(f"Your second variable is: {second}")
print("Your third variable is: ", third)