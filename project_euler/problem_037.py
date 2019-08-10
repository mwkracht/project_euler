"""
Project Euler - Problem 37
Copyright (c) Matthew Kracht. All rights reserved.

The number 3797 has an interesting property. Being prime itself, it is possible to continuously
remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly
we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and
right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
from project_euler import utils


def brute_force_solution():
    """Search for 11 truncatable primes starting with two digit integers."""
    truncatable_primes = []
    i = 9

    while len(truncatable_primes) < 11:
        i += 2  # skip even numbers...

        i_str = str(i)
        for j in range(1, len(i_str)):
            left_2_right = int(i_str[:j])
            right_2_left = int(i_str[-j:])

            if not utils.is_prime(left_2_right) or not utils.is_prime(right_2_left):
                break
        else:
            # At this point, all subsets of i from left to right and right to left must be prime
            if utils.is_prime(i):
                truncatable_primes.append(i)

    return sum(truncatable_primes)


SOLUTIONS = [
    brute_force_solution,
]
