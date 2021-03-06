"""
Problem 2 from Project Euler

    By considering the terms in the Fibonacci sequence whose values do not exceed four million,
    find the sum of the even-valued terms.

Carlos Cuevas
09-04-19
"""

value_1 = 1
value_2 = 2
sum = 0
target = 4000000

while True:
    new_value = value_1 + value_2
    if new_value > target:
        break
    if not (new_value % 2):
        sum += new_value
    value_1 = value_2
    value_2 = new_value
sum += 2

print('The sum is : ' + str(sum))

