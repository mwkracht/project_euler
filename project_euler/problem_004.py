"""
Project Euler - Problem 4
Copyright (c) Matthew Kracht. All rights reserved.

A palindromic number reads the same both ways. The largest palindrome made from the product of two
2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(number):
    """Return true if integer is palindrome."""
    num_str = str(number)
    return num_str == num_str[::-1]


def first_solution():
    """
    Simple solution which calculates all multiples of two 3-digit numbers.

    No need to iterate over 3-digit numbers greater than i in for loop because of commutative
    property of multiplication (i.e. 999 * 998 = 998 * 999)
    """
    return max(
        i * j
        for i in range(999, 99, -1)
        for j in range(i + 1, 99, -1)
        if is_palindrome(i * j)
    )


solutions = [
    first_solution
]
solution = solutions[-1]
