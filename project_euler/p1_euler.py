"""
Problem 1 from Project Euler

    Find the sum of all the multiples of 3 or 5 below 1000.

Carlos Cuevas
09-04-19
"""

multiples_3 = 0
multiples_5 = 0

for i in range(3, 1000):
    if not i % 3:
        multiples_3 += i
    elif not i % 5:
        multiples_5 += i

total = multiples_3 + multiples_5

print('The sum is : ' + str(total))
