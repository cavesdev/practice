"""
Helper file to p3_euler.py
"""


class Node():
    """Class used to create binary tree nodes"""

    factors = []

    # initialization
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def get_data(self):
        """Return data from tree node"""
        return self.data

    def find_factors(self):
        """Function used to find two factors for a given number. Left is always a prime factor"""
        max_factor = int(self.data // 2)
        if max_factor < 2:
            return

        # find factor and create child nodes
        for i in range(2, max_factor):
            if not (self.data % i):
                self.left = Node(i)
                self.right = Node(int(self.data / i))
                Node.factors.append(int(self.data / i))
                self.right.find_factors()
                break
        return
