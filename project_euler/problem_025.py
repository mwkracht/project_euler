"""
Project Euler - Problem 25
Copyright (c) Matthew Kracht. All rights reserved.

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

def fibonacci():
    """Generator for fibonacci sequeuence."""
    f_curr = 1
    f_prev = 0

    while True:
        yield f_curr
        f_prev, f_curr = f_curr, f_curr + f_prev


def brute_force_solution():
    """Let python arbitrarily long integers do the heavy lifting."""
    return next(
        i + 1
        for i, f_i in enumerate(fibonacci())
        if f_i >= (10 ** 999)
    )


SOLUTIONS = [
    brute_force_solution,
]
