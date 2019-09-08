"""
Project Euler - Problem 46
Copyright (c) Matthew Kracht. All rights reserved.

It was proposed by Christian Goldbach that every odd composite number can be written as the sum
of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
import itertools

from project_euler import sequences, utils


def odd_composite_numbers():
    """Generator expression which returns sequence of odd composite numbers."""
    for i in itertools.count(9, step=2):
        if not utils.is_prime(i):
            yield i


def prime_numbers():
    """Generator expression which returns sequence of prime numbers."""
    yield 2

    for i in itertools.count(3, step=2):
        if utils.is_prime(i):
            yield i


def is_sum_of_prime_and_twice_square(value):
    """Return True if value can be written as sum of prime and twice a square."""
    for prime in prime_numbers():
        if prime > value:
            break

        if sequences.SquareNumbers.has_term((value - prime) / 2):
            return True

    return False


def brute_force_solution():
    """
    Iterate over all odd composite numbers and verify if any prime can be subtracted to to create
    a number that is twice a square.
    """
    return next(
        number
        for number in odd_composite_numbers()
        if not is_sum_of_prime_and_twice_square(number) 
    )


SOLUTIONS = [
    brute_force_solution,
]
