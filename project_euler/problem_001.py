"""
Project Euler - Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import math


def sum_multiples(base, limit):
    """
    Return the sum of all multiples of base from 0 up to limit.

    Alternate slower list comprehension sum:
        sum([x for x in range(0, base, limit)])
    """
    num_multiples = int(math.floor(float(limit) / base))
    max_multiple = num_multiples * base
    return int(((max_multiple + base) / 2.0) * num_multiples)


def solution():
    return sum_multiples(3, 1000) + sum_multiples(5, 1000) - sum_multiples(15, 1000)
