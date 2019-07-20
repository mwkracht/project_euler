"""
Project Euler - Problem 35
Copyright (c) Matthew Kracht. All rights reserved.

The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
from project_euler import utils


def rotations(num):
    """Generator expression that produces all rotations of the provided number."""
    digits = str(num)

    for _ in range(len(digits)):
        yield int(digits)
        digits = digits[1:] + digits[0]


def brute_force_solution():
    """Iterate through every number and test if it and it's rotations are prime."""
    circular_primes = [
        i
        for i in range(2, 1000000)
        if all(utils.is_prime(rotation) for rotation in rotations(i))
    ]

    return len(circular_primes)


def circular_prime_search_space(start, limit):
    """Generator expression that filters out numbers which we know cannot be circular primes."""
    invalid_digits = {'0', '2', '4', '5', '6', '8'}
    start = start if start % 2 else start - 1  # make sure start is odd so range below skips evens

    for i in range(start, limit, 2):  # skip all even numbers
        if not set(str(i)) & invalid_digits:
            yield i


def brute_force_reduce_search_solution():
    """
    Similar approach to original method but reduce the search space.

    We can reduce the set of numbers we need to calculate because we know that any number
    that contains an even digit (0, 2, 4, 6, 8) or a 5 cannot have all rotations be prime
    since one rotation will have (0, 2, 4, 6, 8, 5) in the ones digit and that number is
    always divisible.

    This reduces compute time by roughly 5x.
    """
    circular_primes_over_100 = [
        i
        for i in circular_prime_search_space(101, 1000000)
        if all(utils.is_prime(rotation) for rotation in rotations(i))
    ]

    return len(circular_primes_over_100) + 13  # 13 circular primes below 100


SOLUTIONS = [
    brute_force_solution,
    brute_force_reduce_search_solution
]