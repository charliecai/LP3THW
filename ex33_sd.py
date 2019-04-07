# Exercise 33. While Loops
from sys import argv

def print_num(x, y):
    i = 0
    j = 0
    numbers = []
    while i < x:
        print(f"At the top j is {j}")
        numbers.append(j)

        i += 1
        j += y
        print("Numbers now: ", numbers)
        print(f"At the bottom j is {j}")

    print("The numbers: ")

    for num in numbers:
        print(num)

def print_num_for(x, y):
    j = 0
    numbers = []
    for i in range(0, x):
        print(f"At the top i is {j}")
        numbers.append(j)

        j += y
        print("Numbers now: ", numbers)
        print(f"At the bottom j is {j}")

    print("The numbers: ")

    for num in numbers:
        print(num)

print_num(3,2)

print_num_for(3, 3)