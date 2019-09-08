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


def reduce_fraction(numerator, denominator):
    """Return the reduced fraction given by the numerator and denominator."""
    _gcd = gcd(numerator, denominator)
    return int(numerator / _gcd), int(denominator / _gcd)


def is_pandigital(number):
    """Return True only if number is 1 to N pandigital."""
    width = len(str(number))
    if width > 9:
        return False

    return set(str(number)) == set(map(str, range(1, width + 1)))


class FigurativeNumberSequence(object):

    # Cache calculated terms of the sequence - use set of O(1) membership lookupts
    SEQUENCE = [1]
    NUMBERS = {1}

    @classmethod
    def term(cls, n):
        """Return the value of the Nth term of the sequence."""
        raise NotImplementedError('Method must be implemented by child class')

    @classmethod
    def has_term(cls, value):
        """Return True if provided value is member of sequence."""
        while value > cls.SEQUENCE[-1]:
            next_term = cls.term(len(cls.SEQUENCE) + 1)
            cls.SEQUENCE.append(next_term)
            cls.NUMBERS.add(next_term)

        return value in cls.NUMBERS  # use set to test membership for constant time complexity


class TriangularNumbers(FigurativeNumberSequence):

    @classmethod
    def term(cls, n):
        """Return the value of the Nth term of the sequence."""
        return int((n * (n + 1)) / 2)


class PentagonalNumbers(FigurativeNumberSequence):

    @classmethod
    def term(cls, n):
        """Return the value of the Nth term of the sequence."""
        return int(n * ((3 * n) - 1) / 2)


class HexagonalNumbers(FigurativeNumberSequence):

    @classmethod
    def term(cls, n):
        """Return the value of the Nth term of the sequence."""
        return int(n * ((2 * n) - 1))
