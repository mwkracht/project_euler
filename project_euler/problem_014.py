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

MAX_STARTING_VALUE = 1000000


def collatz_sequence(number):
    """Generator for collatz sequence where number is first item returned."""
    def next_number(i):
        return (3 * i) + 1 if i % 2 else number / 2

    while number != 1:
        yield number
        number = next_number(number)

    yield number


def brute_force_solution():
    """Iterate through every possible integer and compute sequence length."""
    max_sequence_len = 0
    max_sequence_n = 0

    for i in range(1, MAX_STARTING_VALUE + 1):
        sequence = list(collatz_sequence(i))
        if len(sequence) > max_sequence_len:
            max_sequence_len = len(sequence)
            max_sequence_n = i

    return max_sequence_n


def brute_force_subset_solution():
    """
    Brute force iteration but ignore numbers which have already been traversed.

    If an integer N has already been traversed as part of another integer M's collatz sequence then
    N cannot have a collatz sequence longer than M and can be ignored.
    """
    traversed = set()
    max_sequence_len = 0
    max_sequence_n = 0
    not_computed = 0

    # iterate in descending order to attempt to maximize the amount of sequences which can be
    # ignored under the assumption that the larger the starting number the more likely it is to
    # have a larger sequence length.
    for i in range(MAX_STARTING_VALUE, 0, -1):
        if i in traversed:
            not_computed += 1
            continue

        sequence = set(collatz_sequence(i))
        traversed |= sequence

        if len(sequence) > max_sequence_len:
            max_sequence_len = len(sequence)
            max_sequence_n = i

    print(not_computed)
    return max_sequence_n


SOLUTIONS = [
    brute_force_solution,
    brute_force_subset_solution
]
