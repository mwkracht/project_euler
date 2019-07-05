"""
Project Euler - Problem 21
Copyright (c) Matthew Kracht. All rights reserved.

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly
into n). If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of
a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from project_euler import utils

LIMIT = 10000


def brute_force_solution():
    """Compute factors for all integers up to LIMIT and then compare sums of those factors."""
    divisor_sums = [
        sum(utils.get_factors(i)[:-1])  # ignore final factor which is the number itself and not a divisor
        for i in range(LIMIT + 1)
    ]

    amicable_numbers = []
    for i in range(1, len(divisor_sums)):
        j = divisor_sums[i]
        if i != j and j < len(divisor_sums) and i == divisor_sums[j]:
            amicable_numbers.append(i)

    return sum(amicable_numbers)


def brute_force_factor_table_solution():
    """Compute factor table which should yield a faster list of divisor sums."""
    divisor_sums = [
        sum(row[:-1])  # ignore final factor which is the number itself and not a divisor
        for row in utils.factor_table(LIMIT)
    ]

    amicable_numbers = []
    for i in range(1, len(divisor_sums)):
        j = divisor_sums[i]
        if i != j and j < len(divisor_sums) and i == divisor_sums[j]:
            amicable_numbers.append(i)

    return sum(amicable_numbers)


SOLUTIONS = [
    brute_force_solution,
    brute_force_factor_table_solution,
]
