"""
Project Euler - Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import functools


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


solutions = [
    functools.partial(largest_prime_factor, TEST_NUMBER, get_factors),
    functools.partial(largest_prime_factor, TEST_NUMBER, get_factors_faster)
]
solution = solutions[-1]
