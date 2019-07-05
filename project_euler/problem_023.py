"""
Project Euler - Problem 23
Copyright (c) Matthew Kracht. All rights reserved.

A perfect number is a number for which the sum of its proper divisors is exactly equal to the
number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called
abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be
written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that
all integers greater than 28123 can be written as the sum of two abundant numbers. However, this
upper limit cannot be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant
numbers.
"""
import functools
import itertools
import operator

from project_euler import utils


LIMIT = 28123


def sum_of_divisors(number):
    """
    Return the sum of divisors for the provided number.

    To find the sum of divisors S(num), first find the prime factorization of the number:
    S(num) = S(a^m * b^n ...) where a^m * b^n ... is the prime factorization

    S(a^m * b^n ...) can then be written as S(a^m) * S(b^n) * ...

    To find the sum of divisors for a number which can be described as p^k:
    S(p^k) = (p^(k+1) - 1) / (p-1)
    """
    prime_factorization = utils.get_prime_factorization(number)

    def divisor_sum_of_prime(prime, count):
        return ((prime ** (count + 1)) - 1) / (prime - 1)

    return int(functools.reduce(operator.mul, [
        divisor_sum_of_prime(prime, prime_factorization.count(prime))
        for prime in set(prime_factorization)
    ]))


def abundant_numbers(limit):
    """Return list of abundant numbers up to limit."""
    return [
        i
        for i in range(12, limit)
        if sum_of_divisors(i) > (i * 2)  # i is included in divisor sum
    ]


def brute_force_solution():
    """
    Find all abundant numbers under LIMIT, sum all combinations of 2 and then compute numbers not
    in that set of combinations.
    """
    abundants = abundant_numbers(LIMIT)
    sums_of_2_abundants = set(map(sum, itertools.product(abundants, repeat=2)))

    return sum(
        i
        for i in range(LIMIT)
        if i not in sums_of_2_abundants
    )


SOLUTIONS = [
    brute_force_solution,
]
