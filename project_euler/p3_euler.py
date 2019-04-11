"""
Problem 3 from Project Euler

    What is the largest prime factor of the number 600851475143 ?

Carlos Cuevas
10-04-19
"""
from includes.p3_tree import Node


target = 600851475143

root = Node(target)
root.find_factors()

print('The largest prime factor is : ' + str(min(root.factors)))


# testing
def print_tree(root2):
    if root2 is None: return
    print(root2.get_data())
    print_tree(root2.left)
    print_tree(root2.right)

# print_tree(root)
