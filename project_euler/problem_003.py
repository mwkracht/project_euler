"""
Project Euler - Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import functools
import math


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


def get_prime_factorization(number):
    """
    Return list of prime integer factorization of provided number.

    This is a more optimal approach that is borrowed from other solutions. The fundamental theory
    of arithmetic establishes the basis for describing any integer with a unique set of prime
    factors. This method computes those prime factors.

    The decomposition works by finding the least prime factor in the given number and then
    finding the least prime factor of the number divided by the previously found factor and so on.
    """
    def smallest_prime_factor(n):
        return next((i for i in range(2, math.floor(math.sqrt(n))) if n % i == 0), n)

    primes = []

    while True:
        primes.append(smallest_prime_factor(number))
        if primes[-1] < number:
            number = number // primes[-1]
        else:
            break

    return primes


def largest_prime_factor_fast():
    return get_prime_factorization(TEST_NUMBER)[-1]


solutions = [
    functools.partial(largest_prime_factor, TEST_NUMBER, get_factors),
    functools.partial(largest_prime_factor, TEST_NUMBER, get_factors_faster),
    largest_prime_factor_fast
]
solution = solutions[-1]
