"""
Project Euler - Problem 48
Copyright (c) Matthew Kracht. All rights reserved.

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

def brute_force_solution():
    """Let python do the heavy lifting..."""
    answer = sum((i ** i) for i in range(1, 1001)) % (10 ** 10)
    return '0' * (10 - len(str(answer))) + str(answer)  # zero pad answer


SOLUTIONS = [
    brute_force_solution,
]
