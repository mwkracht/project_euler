"""
Project Euler - Problem 5
Copyright (c) Matthew Kracht. All rights reserved.

2520 is the smallest number that can be divided by each of the numbers from 1 to 10
without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import collections
import math

from project_euler import utils


def counter_product(counter):
    product = 1

    for key in counter:
        product *= (key ** counter[key])

    return product


def lcm(numbers):
    """
    Compute the least common multiple (LCM) of the provided list of numbers.

    If the prime factorization of one number is contained within the set of all prime factors
    then that number is already a multiple of the number that is multiple of all prime factors.
    """
    lcm_prime_factors = {}

    for i in numbers:
        i_prime_factors = collections.Counter(utils.get_prime_factorization(i))

        for key in i_prime_factors:
            if i_prime_factors[key] > lcm_prime_factors.get(key, 0):
                lcm_prime_factors[key] = i_prime_factors[key]

    return counter_product(lcm_prime_factors)


def simple_solution():
    """Smallest number that is evenly divisible by any set of numbers is the LCM."""
    return lcm(list(range(1, 21)))


SOLUTIONS = [
    simple_solution
]
