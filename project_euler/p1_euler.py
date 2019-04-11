"""
Problem 1 from Project Euler

Carlos Cuevas Sosa 09-04-19
"""

multiples_3 = 0
multiples_5 = 0

for i in range(3, 1000):
    if not i % 3:
        multiples_3 += i
    elif not i % 5:
        multiples_5 += i

total = multiples_3 + multiples_5

print(total)
