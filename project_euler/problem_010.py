"""
Project Euler - Problem 10
Copyright (c) Matthew Kracht. All rights reserved.

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from project_euler import utils

LIMIT = 2000000


def sieve_solution():
    """Use sieve of eratosthenes to get sum of all primes below LIMIT."""
    return sum(utils.sieve_of_eratosthenes(LIMIT))


solutions = [
    sieve_solution,
]
solution = solutions[-1]
