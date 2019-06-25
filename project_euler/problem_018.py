"""
Project Euler - Problem 18
Copyright (c) Matthew Kracht. All rights reserved.

By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the TRIANGLE below:
"""
import functools


TRIANGLE = (
    (75,),
    (95, 64),
    (17, 47, 82),
    (18, 35, 87, 10),
    (20, 4, 82, 47, 65),
    (19, 1, 23, 75, 3, 34),
    (88, 2, 77, 73, 7, 63, 67),
    (99, 65, 4, 28, 6, 16, 70, 92),
    (41, 41, 26, 56, 83, 40, 80, 70, 33),
    (41, 48, 72, 33, 47, 32, 37, 16, 94, 29),
    (53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14),
    (70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57),
    (91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48),
    (63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31),
    (4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23),
)


def triangle_sum_compute(triangle):
    """
    Traverse triangle by computing a frontier of sums for each row.

    Not all routes need to be traversed or computed. At any given row and any given index only
    one maximum sum can exist and that what needs to be kept track of. As the method traverses
    the rows it will keep the current max sum at each index in that row which will then be used
    to compute the max sum for the next row.
    """
    def largest_sum(frontier, index, value):
        """Compute largest sum possible at index given frontier sums and value at index."""
        if index == 0:
            return frontier[index] + value
        if index == len(frontier):
            return frontier[index - 1] + value
        return max([frontier[index - 1] + value, frontier[index] + value])

    sum_frontier = triangle[0]

    for i in range(1, len(triangle)):
        sum_frontier = [
            largest_sum(sum_frontier, j, triangle[i][j])
            for j in range(len(triangle[i]))
        ]

    return max(sum_frontier)


SOLUTIONS = [
    functools.partial(triangle_sum_compute, TRIANGLE),
]
