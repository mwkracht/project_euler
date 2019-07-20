"""
Project Euler - Problem 34
Copyright (c) Matthew Kracht. All rights reserved.

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
import math
import functools


FACTORIAL_TABLE = {
    i: math.factorial(i)
    for i in range(0, 10)
}


def sum_of_digit_factorials(num):
    """Return the sum of the factorials of each digit in provided number."""
    return sum(
        FACTORIAL_TABLE[int(char)]
        for char in str(num)
    )


@functools.lru_cache(maxsize=None)
def dp_sum_of_digit_factorials(num):
    """Use dynamic programming solution to avoid overlapping sub-problems."""
    if num < 10:
        return math.factorial(num)

    return dp_sum_of_digit_factorials(num // 10) + dp_sum_of_digit_factorials(num % 10)


def brute_force_solution():
    """
    Check all numbers from 3 to sum upper bound to see if they are "curious" numbers.

    The upper bound for the check can be determined by finding at what number of 9 digits pass
    the linear increase in 9!. For instance:

        9! * 5 = 1,814,400 >    99,999
        9! * 6 = 2,177,280 >   999,999
        9! * 7 = 2,540,160 < 9,999,999

    Since 9! is the greatest possible value for a single digit, and 9,999,999 is greater than the
    sum of the factorial of all digits then no number with 7 or more digits can possibly equal the
    sum of the factorial of each digit.
    """
    return sum(
        i
        for i in range(3, 1000000)
        if sum_of_digit_factorials(i) == i
    )


def dynamic_programming_solution():
    """
    Use recurse + memoization approach to avoid repetive computation of slices of larger numbers.

    Reduces compute time by roughly 10x.
    """
    return sum(
        i
        for i in range(3, 1000000)
        if dp_sum_of_digit_factorials(i) == i
    )


SOLUTIONS = [
    brute_force_solution,
    #dynamic_programming_solution,
]
