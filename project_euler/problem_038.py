"""
Project Euler - Problem 38
Copyright (c) Matthew Kracht. All rights reserved.

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576
the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the
pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated
product of an integer with (1,2, ... , n) where n > 1?
"""
from project_euler import utils


def concatenated_products(base):
    concatenated_product = ''
    n = 1

    while len(concatenated_product) < 10:
        concatenated_product += str(n * base)
        n += 1
        yield int(concatenated_product)


def brute_force_solution():
    """
    Compute the concatenated product for every number up to some limit and find the large product
    which is also pandigital.

    Because n > 1 and the max 1 to 9 pandigital number can only be 9 digits, the upper limit on
    the search must be a 4 digit number. A five digit number concatenated with the product of
    itself and 2 cannot produce a result that is only 9 digits.
    """
    return max(
        product
        for i in range(1, 10000)
        for product in concatenated_products(i)
        if utils.is_pandigital(product)
    )


SOLUTIONS = [
    brute_force_solution,
]