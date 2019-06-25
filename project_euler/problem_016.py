"""
Project Euler - Problem 16
Copyright (c) Matthew Kracht. All rights reserved.

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

def compute_solution():
    """Let python do all of the heavy lifting..."""
    return sum(
        int(c)
        for c in str(2 ** 1000)
    )


SOLUTIONS = [
    compute_solution
]
