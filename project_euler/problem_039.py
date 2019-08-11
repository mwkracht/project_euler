"""
Project Euler - Problem 39
Copyright (c) Matthew Kracht. All rights reserved.

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are
exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
import collections
import math
import operator


LIMIT = 1001


def total_right_triangle_solutions(perimeter):
    """Return count of unique right triangle solutions with the given perimeter."""
    return len([
        (a, b, perimeter - a - b)
        for a in range(1, perimeter // 2 + 1)  # must be less than half perimeter to be side
        for b in range(1, min([a + 1, (perimeter - a) // 2 + 1]))  # force b to be shorter side
        if a**2 + b**2 == (perimeter - a - b)**2
    ])


def brute_force_solution():
    """
    Compute number of solutions for every p <= 1000 and return the max number of solutions.

    Using the equation a^2 + b^2 = c^2 we can find that it is not possible for the perimeter to
    be odd for a right triangle:

    a     | b    | c    | perimeter
    odd     odd    even   even
    odd     even   odd    even
    even    odd    odd    even
    even    even   even   even
    """
    return max(range(4, LIMIT, 2), key=total_right_triangle_solutions)


def total_right_triangle_solutions_faster(perimeter):
    """Return count of unique right triangle solutions with the given perimeter."""
    def calc_b(a, perimeter):
        """See problem 009."""
        return ((perimeter**2/2) - (perimeter * a)) / (perimeter - a)

    solutions = []

    for a in range(1, perimeter // 2 + 1):  # must be less than half perimeter to be side
        b = calc_b(a, perimeter)
        if b.is_integer():
            solutions.append((a, int(b), perimeter - a - int(b)))

    return len(solutions)


def faster_brute_force_solution():
    """
    Use closed form solution from problem 009 for computing b in pythagorean triple given a
    and sum of a, b, and c. This removes the inner loop that searched values for b.
    """
    return max(range(4, LIMIT, 2), key=total_right_triangle_solutions_faster)


def precompute_pythagorean_triples_solution():
    """
    Instead of iterating through every perimeter p, iterate through every possible side values
    for a and b and compute whether or not they can form a pythagorean triple. 
    """
    pythagorean_triples = collections.defaultdict(int)

    for a in range(1, LIMIT // 2 + 1):
        # (a + 1) won't allow b to exceed a which prevents calculating duplicate triples
        # (e.x. 3,4,5 and 4,3,5). The other term in the min forces b to not exceed the possible
        # length of the hypotenuse (c) value given the perimeter LIMIT
        for b in range(1, min([a + 1, (LIMIT - a) // 2 + 1])):
            c = math.sqrt(a**2 + b**2)
            if c.is_integer():
                pythagorean_triples[int(a + b + c)] += 1

    return max(pythagorean_triples.items(), key=operator.itemgetter(1))[0]


SOLUTIONS = [
    # brute_force_solution,  # ignoring in order to keep tests fast
    faster_brute_force_solution,
    precompute_pythagorean_triples_solution,
]