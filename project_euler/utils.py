"""
Module contains utility methods used to solve Project Euler problems.
Copyright (c) Matthew Kracht. All rights reserved.
"""
import math
import functools


@functools.lru_cache(maxsize=None)
def smallest_prime_factor(n):
    return next((
        i
        for i in range(2, math.floor(math.sqrt(n)) + 1)
        if n % i == 0
    ), n)


def is_prime(n):
    """Return whether the provided integer N is prime."""
    if n < 2: 
        return False

    return smallest_prime_factor(n) == n


def get_prime_factorization(number):
    """
    Return list of prime integer factorization of provided number.

    Originally written as part of Problem 003.
    """
    primes = []

    while True:
        primes.append(smallest_prime_factor(number))
        if primes[-1] < number:
            number = number // primes[-1]
        else:
            break

    return primes


def get_factors(number):
    """Return list of factors of the provided number in ascending order."""
    lower_factors, upper_factors = [], []

    for i in range(1, math.floor(math.sqrt(number)) + 1):
        result = number / i
        if result.is_integer():
            lower_factors.append(i)
            if result != i:
                upper_factors.append(int(result))

    return lower_factors + upper_factors[::-1]


def factor_table(limit):
    """Return list where at each index i there is a list which contains all factors of i."""
    table = [[] for _ in range(limit + 1)] # must initialize new list object for each table row

    for i in range(1, len(table) + 1):
        for j in range(i, len(table), i):
            table[j].append(i)

    return table


def sieve_of_eratosthenes(limit):
    """
    Compute set of all prime numbers up to limit using sieve of eratosthenes.

    Originally written as part of Problem 007.
    """
    primes = set(range(2, limit))

    for i in range(2, math.floor(math.sqrt(limit))):
        if i in primes:
            primes -= set(range(i * 2, limit, i))

    return primes


def gcd(a, b):
    """Compute greatest common denominator (GCD) of two numbers using Euclid's algorithm."""
    if b == 0:
        return a
    return gcd(b, a % b)
