"""
Project Euler - Problem 15
Copyright (c) Matthew Kracht. All rights reserved.

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
import math

GRID_SIZE = 20


def compute_solution():
    """
    Compute solution using closed form expression.

    The grid traversal can be translated into determining the unique permutations of a set
    where the set contains N number of both 'down' and 'right' items. For instance a 2x2 grid:

    {r r d d} -> 24 permutations -> 6 unique permutations

    To calculate unique permutations of a set S containing duplicates:

        (all elements in S)! / (num a elements in S)! * (num b elements S)! ....
    """
    return int(math.factorial(GRID_SIZE * 2) / (math.factorial(GRID_SIZE) ** 2))


SOLUTIONS = [
    compute_solution,
]
