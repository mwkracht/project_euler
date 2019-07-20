"""
Project Euler - Problem 33
Copyright (c) Matthew Kracht. All rights reserved.

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to
simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling
the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value,
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""
import functools
import operator

from project_euler import utils


def is_curious_fraction(num, denom):
    """
    Return True if fraction is "curious" (what a silly name...).

    Since this problem is only concerned with two digit numbers we can ignore the case where
    the numerator and denominator have repeating digits. With two digits, a repeating number
    will mean that the number only contains that digit (e.x. 99) and removing either the first or
    second digit will not make a difference.
    """
    def remove_digit(number, digit):
        return int(str(number).replace(digit, '', 1))

    common_digits = set([char for char in str(num)]) & set([char for char in str(denom)])
    if '0' in common_digits:
        common_digits.remove('0')

    for digit in common_digits:
        try:
            if remove_digit(num, digit) / remove_digit(denom, digit) == num / denom:
                return True
        except ZeroDivisionError:
            pass

    return False


def brute_force_solution():
    """Iterate through every combination of two digit numerator/denominator to find fractions."""
    curious_fractions = [
        (numerator, denominator)
        for denominator in range(11, 100)
        for numerator in range(10, denominator)  # must never exceed denominator to ensure < 1
        if is_curious_fraction(numerator, denominator)
    ]

    numerator = functools.reduce(operator.mul, [num for num, _ in curious_fractions])
    denominator = functools.reduce(operator.mul, [denom for _, denom in curious_fractions])

    numerator, denominator = utils.reduce_fraction(numerator, denominator)

    return denominator


SOLUTIONS = [
    brute_force_solution,
]
