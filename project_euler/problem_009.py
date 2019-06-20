"""
Project Euler - Problem 9
Copyright (c) Matthew Kracht. All rights reserved.

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

TRIPLET_SUM = 1000


def brute_force_solution():
    """Iterate through all possible combinations of a, b, c and determine triplet eq. is sat."""
    def is_pythagorean_triplet(a, b, c):
        return c**2 == a**2 + b**2

    return next(
        a * b * (TRIPLET_SUM - a - b)
        for a in range(1, TRIPLET_SUM)
        for b in range(a + 1, TRIPLET_SUM - a)
        if is_pythagorean_triplet(a, b, TRIPLET_SUM - a - b)
    )


def faster_brute_force_solution():
    """
    Return product of pythagorean triplet whose sum is TRIPLET_SUM.

    Using equation a^2 + b^2 = c^2:
        c = sqrt(a^2 + b^2)

    The value of c can be substitued into the sum equation:
        SUM - a - b = sqrt(a^2 + b^2)
        (SUM - a - b)(SUM - a - b) = a^2 + b^2
        SUM^2 - 2SUMa - 2SUMb + 2ab + a^2 + b^2 = a^2 + b^2
        (SUM^2)/2 - SUMa - SUMb + ab = 0
        (SUM^2)/2 - SUMa = b(SUM - a)
        b = ((SUM^2)/2 - SUMa) / (SUM - a)

    Since a, b, and c must be positive only integers [1, sum] must be tested for a to see if 
    the equation for b returns an integer. This removes the inner loop which tested for b within
    the original brute_force_equation.
    """
    def calc_b(a, sum):
        return ((sum**2/2) - (sum * a)) / (sum - a)

    a, b = next(
        (a, calc_b(a, TRIPLET_SUM))
        for a in range(1, TRIPLET_SUM)
        if calc_b(a, TRIPLET_SUM).is_integer()
    )

    return a * b * (TRIPLET_SUM - a - b)


solutions = [
    brute_force_solution,
    faster_brute_force_solution,
]
solution = solutions[-1]
