"""
Project Euler - Problem 27
Copyright (c) Matthew Kracht. All rights reserved.

Euler discovered the remarkable quadratic formula:
n^2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 ≤ n ≤ 39.
However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is
clearly divisible by 41.

The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive
values 0 ≤ n ≤ 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4

Find the product of the coefficients, a and b, for the quadratic expression that produces
the maximum number of primes for consecutive values of n, starting with n=0.
"""
import itertools

from project_euler import utils


def refined_brute_force_solution():
    """
    Iterate throughe very combination of a/b and compute the number of consecutive primes.

    Use some basic math to reduce the search space for both a and b.
    """
    most_consecutive_primes = 0
    most_consectuive_primes_product = 0

    # given the quadratic formula, b must be prime otherwise the condition where n=0 will not
    # produce a prime
    b_ints = [i for i in range(1001) if utils.is_prime(i)]

    # since we are only considering b values which are primes, the condition where n=1 produces
    # 1 + a - b. In order for this to be prime, a must be an odd number otherwise the resulting
    # value will be even and not prime for n=1
    for a in range(-999, 1000, 2):
        for b in b_ints:
            # starting at n=0 the number of consecutive primes is equal to the index of the first
            # non-prime
            consecutive_primes = next(
                n
                for n in itertools.count()
                if not utils.is_prime(n ** 2 + (a * n) + b)
            )

            if consecutive_primes > most_consecutive_primes:
                most_consecutive_primes = consecutive_primes
                most_consectuive_primes_product = a * b

    return most_consectuive_primes_product


SOLUTIONS = [
    refined_brute_force_solution,
]