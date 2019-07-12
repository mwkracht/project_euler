"""
Project Euler - Problem 28
Copyright (c) Matthew Kracht. All rights reserved.

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5
spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

"""
3 x 3:
7  8  9
6  1  2
5  4  3
sum: 25

5 x 5:
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
sum: 25 + (13 + 17 + 21 + 25) = 25 + (9+4 + 9+8 + 9+12 + 9+16) = 101

7 x 7:
43 44 45 46 47 48 49
42 21 22 23 24 25 26
41 20  7  8  9 10 27
40 19  6  1  2 11 28
39 18  5  4  3 12 29
38 17 16 15 14 13 30
37 36 35 34 33 32 31
sum: 101 + (31 + 37 + 43 + 49) = 101 + (25+6 + 25+12 + 25+18 + 25+24) = 261

As the spiral is expanded the sum(n), where n is the number of rows/colums in the spiral, is
equal to sum(n-2) + 4 * (n-2)^2 + 10(n - 1)
"""
SIZE = 1001


def spiral_sum(n):
    """Return the spiral sum of a spiral with nxn dimensions."""
    return spiral_sum(n-2) + 4 * ((n-2)**2) + 10 * (n - 1)


def fast_compute():
    """
    Use above formula to compute spiral sums iteratively.

    Not computing spiral sum recursively to avoid max recursion depth in python.
    """
    spiral_sum = 1

    for n in range(3, SIZE + 1, 2):
        spiral_sum += 4 * ((n - 2) * (n - 2)) + 10 * (n - 1)

    return spiral_sum


def closed_form_solution():
    """Use stolen closed form solution to compute in O(1)."""
    return int(((4 * (SIZE ** 3)) + (3 * (SIZE ** 2)) + 8 * SIZE - 9) / 6)


SOLUTIONS = [
    fast_compute,
    closed_form_solution
]

