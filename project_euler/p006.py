"""
Problem 7 from Project Euler

    Find the difference between the sum of the squares of the first one hundred natural numbers
    and the square of the sum

Carlos Cuevas
11-04-19
"""
n = 100

# sum of the squares:
# formula: (n(n+1)(2n+1)) / 6

sum_squares = (n * (n + 1) * ((2 * n) + 1)) / 6

# square of the sum:
# formula: (n(n+1)) / 2

square_sum = (n * (n + 1)) / 2
square_sum = square_sum * square_sum

answer = - 1 * int(sum_squares - square_sum)

print("The difference is : " + str(answer))