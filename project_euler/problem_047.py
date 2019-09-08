"""
Project Euler - Problem 47
Copyright (c) Matthew Kracht. All rights reserved.

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the
first of these numbers?
"""
import itertools

from project_euler import utils


DISTINCT_PRIMES = 4
CONSECUTIVE_NUMBERS = 4


def has_distinct_prime_factors(value, num_prime_factors):
    """Return True if value has distinct num_prime_factors."""
    return len(set(utils.get_prime_factorization(value))) == num_prime_factors


def brute_force_solution():
    """Search all integers until 3 consecutive integers are found w/ 4 distinct prime factors."""
    consecutive_found = 0

    for i in itertools.count():
        if has_distinct_prime_factors(i, DISTINCT_PRIMES):
            consecutive_found += 1
        else:
            consecutive_found = 0

        if consecutive_found == CONSECUTIVE_NUMBERS:
            return i - CONSECUTIVE_NUMBERS + 1


SOLUTIONS = [
    brute_force_solution,
]
