"""
Project Euler - Problem 50
Copyright (c) Matthew Kracht. All rights reserved.

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms,
and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
from project_euler import utils


LIMIT = 1000000
PRIME_SET = utils.sieve_of_eratosthenes(LIMIT)  # fast membership tests
PRIME_LIST = list(PRIME_SET)


def max_prime_sequence(start):
    """Return consecutive prime sequence which sums to a prime number."""
    sequence = []
    seq_len, seq_sum = 1, PRIME_LIST[start]

    for i in range(start + 1, len(PRIME_LIST)):
        seq_sum += PRIME_LIST[i]
        seq_len += 1

        if seq_sum > LIMIT:
            break
        if seq_sum in PRIME_SET:
            sequence = PRIME_LIST[start:start + seq_len]

    return sequence


def brute_force_solution():
    """Compute sum of every possible consecutive sum of prime numbers below 1M."""
    prime_sequence = []

    for i, _ in enumerate(PRIME_LIST):
        sequence = max_prime_sequence(i)

        if len(sequence) > len(prime_sequence):
            prime_sequence = sequence

    return sum(prime_sequence)


SOLUTIONS = [
    brute_force_solution,
]
