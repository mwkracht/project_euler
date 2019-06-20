"""
Module contains utility methods used to solve Project Euler problems.
Copyright (c) Matthew Kracht. All rights reserved.
"""
import math


def smallest_prime_factor(n):
    return next((
        i
        for i in range(2, math.floor(math.sqrt(n)) + 1)
        if n % i == 0
    ), n)


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
