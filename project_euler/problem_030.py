"""
Project Euler - Problem 30
Copyright (c) Matthew Kracht. All rights reserved.

Surprisingly there are only three numbers that can be written as the sum of fourth powers of
their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

FIFTH_POWERS = {i: i ** 5 for i in range(10)}


def sum_of_digit_fifth_powers(number):
    """Compute the sum of the fifth powers of all digits in the provided number."""
    return sum(
        FIFTH_POWERS[int(char)]
        for char in str(number)
    )


def brute_force_solution():
    """
    Compute sum of a fith powers for every number from 1 to N.

    In order to brute force this solution an upper bound for numbers must be determined.

    For the value 9 the sum of its fifth powers is 9^5 = 59049, as you add a 9 digit you multiply
    the value by ~10 but only double the sum of the fifth powers:

    99 = 2 * (9^5) = 118,098
    999 = 177,147
    9,999 = 236,196
    99,999 = 295,245
    999,999 = 345,294
    0,999,999 = 345,295
    1,999,999 = 345,295
    etc.

    From this it can be seen that any number >999,999 has no chance of being a sum of its powers
    since any digit added will at least double the value but will not add more than 59049 to the
    sum.

    If you replace the MSD 9 with 0, 1, or 2 in order to make the value less than the 999,999
    sum you get:

    099,999 = 295,245 + 1 = 295,246
    199,999 = 295,245 + 1 = 295,246
    299,999 = 295,245 + 4 = 295,249

    Since there can exist six digit numbers whose sum is less than the number we assume there could
    exist a six digit number whose sum is equal the number.
    """
    return sum([
        i
        for i in range(2, 1000000)
        if sum_of_digit_fifth_powers(i) == i
    ])


SOLUTIONS = [
    brute_force_solution,
]
