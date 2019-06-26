"""
Project Euler - Problem 20
Copyright (c) Matthew Kracht. All rights reserved.

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
import math


N = 100


def brute_force():
    """Let python do the work for us..."""
    return sum(map(int, str(math.factorial(N))))


SOLUTIONS = [
    brute_force,
]
