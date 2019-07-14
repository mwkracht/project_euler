"""
Project Euler - Problem 32
Copyright (c) Matthew Kracht. All rights reserved.

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly
once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier,
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a
1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in
your sum.
"""
import math


def is_pandigital(a, b, c, width=9):
    """Return True if a, b, and c are pandigital with the given width."""
    digits = str(a) + str(b) + str(c)
    if len(digits) != width:
        return False

    return set(str(i) for i in range(1, width + 1)) == set(digits)


def brute_force_solution():
    """
    Iterate through every possible a and b combination to determine set of pandigit products
    then return sum.

    A one digit number mulitplied by a 4 digit number can product a 4 digit number while a two
        digit number multipleid by a 4 digit number cannot.
    A two digit number multiplied by a 3 digit number can product a 4 digit number while a three
        digit number multiplied by a 3 digit number cannot.

    Based on these two statements and since multiplication is commutative, a can be up to a 2 digit
    number and b can be up to a four digit number.
    """
    pandigital_products = set(
        a * b
        for a in range(1, 100)
        for b in range(1 ,10000)
        if is_pandigital(a, b, a * b)
    )

    return sum(pandigital_products)


def reverse_brute_force_solution():
    """
    Iterate through the possible products and search factors to find pandigital pairs.

    10,000 can be used a max product for the search because it is a 5 digit number and the max
    2 digit time 2 digit number is 99 * 99 = 9801 which is less than 10000 and the max one digit
    number times 3 digit number is 9 * 999 = 8991 which is also less than 10000.

    Overall this should be faster than other brute force solution. Both solutions have to iterate
    1 to 9999 in one loop but in this solution the second loop on average iterates up to 67 while
    the other always iterates up to 100.
    """
    pandigital_products = set(
        product
        for product in range(1, 10000)
        for multiplier in range(1, math.floor(math.sqrt(product)) + 1)
        if product % multiplier == 0 and is_pandigital(int(product / multiplier), multiplier, product)
    )

    return sum(pandigital_products)


SOLUTIONS = [
    brute_force_solution,
    reverse_brute_force_solution,
]
