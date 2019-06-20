"""
Project Euler - Problem 7
Copyright (c) Matthew Kracht. All rights reserved.

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""
import math

from project_euler import utils


NTH_PRIME_NUMBER = 10001


def brute_force_solution():
    """Test sequential natural numbers for primeness until Nth prime is found."""
    i, total_primes = 2, 0

    while total_primes < NTH_PRIME_NUMBER:
        if utils.smallest_prime_factor(i) == i:
            total_primes += 1

        i += 1

    return i - 1


def sieve_of_eratosthenes(limit):
    """Compute set of all prime numbers up to limit using sieve of eratosthenes."""
    primes = set(range(2, limit))

    for i in range(2, math.floor(math.sqrt(limit))):
        if i in primes:
            primes -= set(range(i * 2, limit, i))

    return primes


def untuned_sieve_solution():
    """Guessing large sieve limit in hopes that it contains the NTH_PRIME_NUMBER."""
    return sorted(list(sieve_of_eratosthenes(1000000)))[NTH_PRIME_NUMBER - 1]


def tuned_sieve_solution():
    """Using a priori knowledge of the solution to set sieve limit for highest performance."""
    return sorted(list(sieve_of_eratosthenes(104744)))[NTH_PRIME_NUMBER - 1]


solutions = [
    brute_force_solution,
    untuned_sieve_solution,  # ~ equivalent speed but calculates ~78k total primes
    tuned_sieve_solution # ~12x faster than brute_force_solution
]
solution = solutions[-1]
