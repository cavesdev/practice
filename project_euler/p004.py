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

def divide_list(digits):
    """Divides a list in two sublists: one with original left half and the other one inverted"""
    left = digits[:len(digits) // 2]
    right = digits[ceil(len(digits) // 2):]
    right.reverse()

    return (left, right)

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
        # skip if length is not even
        if len(digits) % 2 != 0:
            continue
            print("not equal!")
        digits = divide_list(digits)
        #print(digits)
        if compare_lists(digits[0], digits[1]) is True:
            answer = i * j

print(answer)