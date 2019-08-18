"""
Project Euler - Problem 40
Copyright (c) Matthew Kracht. All rights reserved.

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
import itertools


def compute_champernowne_constant(limit):
    """
    Calculate Champernowne constant up to limit digits a single int at a time.

    Iterating and appending is faster than doing a ''.join() on iterable which has full set of
    ints [1, limit].
    """
    constant = ''
    i = 1

    while len(constant) <= limit:
        constant += str(i)
        i += 1

    return constant


def brute_force_solution():
    """Solution using slower cmapernowne_constant computation."""
    champernowne_constant = compute_champernowne_constant(1000000)

    return (
        int(champernowne_constant[0])
        * int(champernowne_constant[9])
        * int(champernowne_constant[99])
        * int(champernowne_constant[999])
        * int(champernowne_constant[9999])
        * int(champernowne_constant[99999])
        * int(champernowne_constant[999999])
    )


def champernowne_constant_index(index):
    """Return the ith character of Champernowne's constant without computing full constant."""
    for p in itertools.count(1):
        # p=1 -> 9 digits [1,9] -> 9 champernowne constant indexes (digits 1 char wide)
        # p=2 -> 90 digits [10,99] -> 180 champernowne constant indexes (digits 2 char wide)
        # p=3 -> 900 digits [100, 999] -> 2,700 champernowne constant indexes (digits 3 char wide)
        # etc.
        champ_indexes_per_p = 9 * (10 ** (p - 1)) * p

        if index < champ_indexes_per_p:
            base = 10 ** (p - 1)
            champ_i = base + index // p
            return str(champ_i)[index % p]
        else:
            index -= champ_indexes_per_p

    return -1


def direct_compute_solution():
    """Directly compute translations between Champernowne constant index and value."""
    return (
        int(champernowne_constant_index(0))
        * int(champernowne_constant_index(9))
        * int(champernowne_constant_index(99))
        * int(champernowne_constant_index(999))
        * int(champernowne_constant_index(9999))
        * int(champernowne_constant_index(99999))
        * int(champernowne_constant_index(999999))
    )


SOLUTIONS = [
    brute_force_solution,
    direct_compute_solution,
]
