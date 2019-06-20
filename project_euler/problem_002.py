"""
Project Euler - Problem 2
Copyright (c) Matthew Kracht. All rights reserved.

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""

MAX_TERM = 4000000


def is_even(term):
    """Returns whether given integer is even or not."""
    return term % 2 == 0


def fibonacci(max_term):
    """Generator expression that returns terms of Fibonacci sequence up to max_term."""
    curr_term, next_term = 0, 1

    while curr_term < max_term:
        yield curr_term
        curr_term, next_term = next_term, curr_term + next_term


def only_even_fibonacci(max_term):
    """
    Generator expression that returns only even terms of Fibonacci sequence up to max_term.

    After 2, every third term in the Fibonacci sequence is even since the sum of only two odd or
    two even numbers can produce an even number.
    """
    curr_term, next_term = 2, 3

    while curr_term < max_term:
        yield curr_term

        # Skip two terms for both current and next variables
        curr_term, next_term = curr_term + (next_term * 2), curr_term * 2 + next_term * 3


def first_solution():
    return sum(
        x
        for x in fibonacci(MAX_TERM)
        if is_even(x)
    )


def second_solution():
    return sum(only_even_fibonacci(MAX_TERM))


SOLUTIONS = [
    first_solution,
    second_solution
]
