"""
Project Euler - Problem 26
Copyright (c) Matthew Kracht. All rights reserved.

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions
with denominators 2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10    =   0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has
a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal
fraction part.
"""

LIMIT = 1000


def decimal_fraction(numerator, denominator):
    """
    Return tuple of decimal fraction as prefix and repeating fraction.

    Note: index 0 of the prefix will be the ones digit

    As division takes place, a record of the index in prefix that each numerator was seen is kept
    track of. If a numerator is seen twice then the prefix from the first index that numerator was
    seen to the second is the repeating portion.
    """
    numerator_idxs = {}
    decimal_digits = []

    while numerator:
        if numerator in numerator_idxs:
            break

        numerator_idxs[numerator] = len(decimal_digits)
        decimal_digits.append(numerator // denominator)

        numerator = (numerator % denominator) * 10

    start_of_repeat = numerator_idxs.get(numerator, len(decimal_digits))
    return decimal_digits[:start_of_repeat], decimal_digits[start_of_repeat:]


def brute_force_solution():
    """Compute decimal fraction for each number up to LIMIT to find longest repeating fraction."""
    max_repeating_fraction = []
    max_repeating_fraction_i = None

    for i in range(3, LIMIT):
        prefix, repeating = decimal_fraction(1, i)
        if len(repeating) > len(max_repeating_fraction):
            max_repeating_fraction = repeating
            max_repeating_fraction_i = i

    return max_repeating_fraction_i


SOLUTIONS = [
    brute_force_solution,
]