"""
Project Euler - Problem 36
Copyright (c) Matthew Kracht. All rights reserved.

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""


def is_palindrome(num, base_str='d'):
    """
    Return True if provided number is a palindrome when converted to string with given base.

    base_str argument should follow format specification.
    """
    num_str = ('{0:' + base_str + '}').format(num)

    # In genearl the [::-1] notation for reversing a string is faster in python than iteratively
    # checking each index or using built in methods to reverse ordering
    return num_str == num_str[::-1]


def brute_force():
    """
    Search every number less than one million and test if it is decimal and binary palindrome.

    Even numbers can be excluded from search since they will always have 0 in least significant
    digit of binary represenation and we are not including leading 0s in palindrome calculation.

    Check whether number is a decimal palindrome first because the string representation will be
    both shorter and the probability of getting a match at every digit is smaller (1/10 for
    decimal but 1/2 for binary) which should also reduce number of digits to check.
    """
    return sum(
        i
        for i in range(1, 1000000, 2)
        if is_palindrome(i, base_str='d') and is_palindrome(i, base_str='b')
    )


SOLUTIONS = [
    brute_force,
]
