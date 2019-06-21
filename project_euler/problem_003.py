"""
Project Euler - Problem 3
Copyright (c) Matthew Kracht. All rights reserved.

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import functools
import math

from project_euler import utils


TEST_NUMBER = 600851475143


def get_factors(number):
    """Return sorted list of factors of the provided number."""
    factors = set()
    max_remaining_factor = number
    i = 1

    while i < max_remaining_factor:
        result = number / i

        if result.is_integer():
            factors.add(i)
            factors.add(int(result))

        max_remaining_factor = result
        i += 1

    return sorted(list(factors))[::-1]


def get_factors_faster(number):
    """Return list of factors of the provided number in descending order."""
    lower_factors, upper_factors = [], []
    max_remaining_factor = number
    i = 1

    while i < max_remaining_factor:
        result = number / i

        if result.is_integer():
            lower_factors.append(i)
            if result != i:
                upper_factors.append(int(result))

        max_remaining_factor = result
        i += 1

    return upper_factors + lower_factors[::-1]


def largest_prime_factor(number, factors_method):
    factors = factors_method(number)[1:-1]  # drop 1 and itself
    if not factors:
        return number

    return next(
        factor
        for factor in factors
        if len(factors_method(factor)) == 2
    )


def largest_prime_factor_fast():
    return utils.get_prime_factorization(TEST_NUMBER)[-1]


SOLUTIONS = [
    functools.partial(largest_prime_factor, TEST_NUMBER, get_factors),
    functools.partial(largest_prime_factor, TEST_NUMBER, get_factors_faster),
    largest_prime_factor_fast
]
