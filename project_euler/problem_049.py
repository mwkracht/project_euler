"""
Project Euler - Problem 49
Copyright (c) Matthew Kracht. All rights reserved.

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit
numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this
property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""
import itertools

from project_euler import utils


FOUR_DIGIT_PRIMES = [
    prime
    for prime in utils.sieve_of_eratosthenes(10000)
    if prime > 999
]


def prime_permutations(value):
    """Return all permutations of digits in value which are prime."""
    return list(set([
        int(''.join(perm))
        for perm in itertools.permutations(str(value))
        if int(''.join(perm)) in FOUR_DIGIT_PRIMES
    ]))


def linearly_increasing(values):
    """Return True if values are linearly increasing."""
    return all(
        values[i] - values[i - 1] == values[1] - values[0]
        for i in range(2, len(values))
    )


def brute_force_solution():
    """Iterate through all 4 digit primes until conditions are met."""
    special_sequences = []
    # exclude 1487 permutations so we don't have to later filter out the known sequence
    searched_primes = set(prime_permutations(1487))

    for prime in FOUR_DIGIT_PRIMES:
        if prime in searched_primes:
            continue

        prime_perms = sorted(prime_permutations(prime))
        searched_primes.update(prime_perms)

        # prime_perms is sorted so combinations will return sorted combinations - if prime_perms
        # is less than 3 then no groups are returned
        special_sequences.extend([
            group
            for group in itertools.combinations(prime_perms, 3)
            if linearly_increasing(group)
        ])

    return int(''.join(map(str, special_sequences[0])))


SOLUTIONS = [
    brute_force_solution,
]