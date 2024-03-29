"""
Project Euler - Problem 12
Copyright (c) Matthew Kracht. All rights reserved.

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle
number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""
import functools
import itertools
import operator

from project_euler import utils


NUM_FACTORS = 500


def product(*items):
    return functools.reduce(operator.mul, items)


def brute_force_solution():
    """Calculate factors for each number in the triangular number series until NUM_FACTORS found."""
    series_number = 1
    i = 2

    while len(utils.get_factors(series_number)) <= NUM_FACTORS:
        series_number += i
        i += 1

    return series_number


def refined_brute_force_solution():
    """Use faster prime factorization to help reduce series numbers which must be factored."""
    series_number = 0

    for i in itertools.count(1):
        # The total number of factors of a number must be less than or equal to the total
        # combinations of all of prime factors of that number. The number of combinations of a set
        # is equal to 2^N where N is the size of the set so we can quickly compute whether that
        # number is at least NUM_FACTORS
        prime_factors = utils.get_prime_factorization(series_number)
        if 2 ** len(prime_factors) > NUM_FACTORS:
            if len(utils.get_factors(series_number)) > NUM_FACTORS:
                break

        series_number += i

    return series_number


SOLUTIONS = [
    brute_force_solution,
    refined_brute_force_solution
]