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
    """
    Use dynamic programming solution to avoid overlapping sub-problems.

    For instance every number 1101, 2101, 3101, 4101, 5101, 6101, 7101, 8101, 9101, will need
    to also compute the sum of digit factorials for 101. Using memoization, this method will only
    compute the sum of 101 once.
    """
    if num < 10:
        return math.factorial(num)

    return dp_sum_of_digit_factorials(num // 10) + dp_sum_of_digit_factorials(num % 10)


def brute_force_solution():
    """
    Check all numbers from 3 to sum upper bound to see if they are "curious" numbers.

    The upper bound for the check can be determined by finding at what number of 9 digits pass
    the linear increase in 9!. For instance:

        9! * 5          = 1,814,400 >    99,999
        9! * 6          = 2,177,280 >   999,999
        9! * 7          = 2,540,160 < 9,999,999

    Since 9! is the greatest possible value for a single digit, and 9,999,999 is greater than the
    sum of the factorial of all digits then no number with 8 or more digits can possibly equal the
    sum of the factorial of each digit.
    """
    return sum(
        i
        for i in range(3, 10000000)
        if sum_of_digit_factorials(i) == i
    )


def dynamic_programming_solution():
    """
    Use recurse + memoization approach to avoid repetive computation of slices of larger numbers.

    We can also reduce the run time by creating a more accurate upper bound for the possible
    solutions. The upper bound can be found by finding the intersection of two equations which
    represent the max sum of factorials for a number and the number itself:

        y = x
        y = 9! * log(x)

    These two lines intersection just before 2309171.
    """
    return sum(
        i
        for i in range(3, 2309172)
        if dp_sum_of_digit_factorials(i) == i
    )


SOLUTIONS = [
    # brute_force_solution,  # disabling to prevent slowing down automated tests
    dynamic_programming_solution,
]
