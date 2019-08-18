"""
Project Euler - Problem 41
Copyright (c) Matthew Kracht. All rights reserved.

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly
once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
import itertools

from project_euler import utils


def reverse_pandigital_iter(max_width):
    """
    Return all permutations of pandigital numbers.

    Method starts with largest max width number (e.x. 987654321 for max_width=9) and ends always
    ends with 1.
    """
    for curr_width in range(max_width, 0, -1):
        pandigital_digits = ''.join(map(str, range(curr_width, 0, -1)))

        # permutations will emit results in lexicographic sort order - since the pandigital
        # digits input is in reverse order then permutations will emit permutations in decreasing
        # value
        for pandigital_permutation in itertools.permutations(pandigital_digits):
            yield int(''.join(pandigital_permutation))


def reverse_search_solution():
    """
    Search list of pandigital numbers, starting with 9 digit numbers, for the first prime.

    Using a sieve to compute primes up to 9 digits is much more expensive than iterating over
    pandigital number set.

    Iterating from 987654321 to 1 by decrementing is also much more expensive than computing
    permutations of pandigital set since most numbers will not be pandigital.
    """
    return next(
        pandigital_number
        for pandigital_number in reverse_pandigital_iter(max_width=9)
        if utils.is_prime(pandigital_number)
    )


def sieve_solution():
    """
    Use Sieve of Eratosthenes to compute primes up to 7 digits and then test for pandigital.

    The 3 divisibility rule states that an number whose digits sum to a number that is divisible
    by 3 then the whole number is divisible by 3. These reduces the search space to a max of 7
    digit numbers:

        1+2+3+4+5+6+7+8+9=45 -> All 9 digit pandigital numbers are divisible by 3
        1+2+3+4+5+6+7+8=36 -> All 8 digit pandigital numberes are divisible by 3

    """
    primes = utils.sieve_of_eratosthenes(10000000)

    return next(
        prime
        for prime in sorted(utils.sieve_of_eratosthenes(10000000) , reverse=True)
        if utils.is_pandigital(prime)
    )


def reverse_search_solution_max_seven_digits():
    """
    Use the 3 divisiblity rule to reduce search space for reverse search solution.

    Both reverse search solutions are still much faster than precomputing all primes up to 7
    digits using sieve approach. Rough performance outline:

        reverse_search_solution_max_seven_digits: 1x (~300usec)
        reverse_search_solution: 3,500x
        sieve_solution: 30,000x

    """
    return next(
        pandigital_number
        for pandigital_number in reverse_pandigital_iter(max_width=7)
        if utils.is_prime(pandigital_number)
    )


SOLUTIONS = [
    reverse_search_solution,
    sieve_solution,
    reverse_search_solution_max_seven_digits,
]
