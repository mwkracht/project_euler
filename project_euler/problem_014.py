"""
Project Euler - Problem 14
Copyright (c) Matthew Kracht. All rights reserved.

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although
it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""
import functools
import sys


sys.setrecursionlimit(4000)


MAX_STARTING_VALUE = 1000000


@functools.lru_cache(maxsize=None)
def collatz_sequence_length(number):
    """Return collatz sequence length."""
    def next_number(i):
        return (3 * i) + 1 if i % 2 else number / 2

    if number == 1:
        return 1

    return 1 + collatz_sequence_length(next_number(number))


def brute_force_solution():
    """Iterate through every possible integer and compute sequence length."""
    max_sequence_len = 0
    max_sequence_n = 0

    for i in range(1, MAX_STARTING_VALUE + 1):
        sequence_length = collatz_sequence_length(i)
        if sequence_length > max_sequence_len:
            max_sequence_len = sequence_length
            max_sequence_n = i

    return max_sequence_n


SOLUTIONS = [
    brute_force_solution,
]
