"""
Problem 4 from Project Euler

    Find the largest palindrome made from the product of two 3-digit numbers.

Carlos Cuevas
11-04-19
"""
from math import ceil

# functions

def divide_in_digits(number):
    """Returns a list with every digit from the input number"""
    digits = []

    # fill the list with digits
    while number != 0:
        digits.insert(0, number % 10)
        number = number // 10

    return digits

def compare_lists(first, second):
    """Compares two lists object by object"""
    for i in range(0, len(first)):
        if first[i] != second[i]:
            return False
    else: return True


# main program

# test every three digit number
for i in range(100, 1000):
    for j in range(100, 1000):
        digits = divide_in_digits(i * j)
        # reverse list
        digits_inv = digits[::-1]
        if compare_lists(digits, digits_inv) is True:
            answer = [i, j, i * j]

print(answer)