"""
Project Euler - Problem 6
Copyright (c) Matthew Kracht. All rights reserved.

he sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the
square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and
the square of the sum.
"""

MAX_N = 100


def brute_force_solution():
    """Solve difference by calcluating sums directly."""
    square_of_sums = (((1 + MAX_N) / 2) * MAX_N) ** 2

    sum_of_squares = sum(
        i ** 2
        for i in range(MAX_N + 1)
    )

    return square_of_sums - sum_of_squares


solutions = [
    brute_force_solution,
]
solution = solutions[-1]
