"""
Project Euler - Problem 24
Copyright (c) Matthew Kracht. All rights reserved.

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation
of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import itertools
import math


def brute_force_solution():
    """Let python do the heavy lifting.

    permutation method returns permutations in lexicographic order as long as input is sorted.
    """
    perm = next(itertools.islice(itertools.permutations(range(10)), int(1e6) - 1, None))
    return int(''.join(map(str, perm)))


def recursive_compute_solution():
    """
    The Nth item in the lexigraphic order can be found recursively starting with the MSDigit.

    0 (123456789) -> the first 9! [1, 362880] start with 0,
    1 (023456789) -> the second 9! [362881, 725760] start with 1,
    2 (013456789) -> the third 9! [725761, 1088640] start with 2 so the 1,000,000th starts with 2

    Then start on the second digit with a set of 9 numbers etc.
    """
    def lexicographic_permutation(nums, idx):
        """Return list of digits which represent idx-th lexicgraphic permutation of ORDERED nums."""
        if idx == 0:
            return nums

        # determine the amount of permutations which can be traversed with the current digit
        perm_per_digit = math.factorial(len(nums) - 1)
        digit_idx = int(idx // perm_per_digit)

        # select the current digit and then lexicographically sort the remaining digits
        return [nums[digit_idx]] + lexicographic_permutation(
            nums[:digit_idx] + nums[digit_idx + 1:],
            idx - (perm_per_digit * digit_idx)
        )

    perm = lexicographic_permutation(list(range(10)), 999999)
    return int(''.join(map(str, perm)))


SOLUTIONS = [
    brute_force_solution,
    recursive_compute_solution,
]
