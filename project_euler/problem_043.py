"""
Project Euler - Problem 43
Copyright (c) Matthew Kracht. All rights reserved.

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the
digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""
import itertools


def passes_divisibility_tests(number):
    """Return True if number passes all divisibility tests defined in problem statement."""
    divisibilty_tests = [(1, 2), (2, 3), (3, 5), (4, 7), (5, 11), (6, 13), (7, 17)]
    number_str = str(number)

    # Return False on first failed divisibility test
    return next((
        False
        for starting_index, divisor in divisibilty_tests
        if int(number_str[starting_index:starting_index + 3]) % divisor != 0
    ), True)


def pandigital_numbers():
    """Generator expression which iterates through all pandigital numbers."""
    for pandigital_digits in itertools.permutations(list(range(10))):
        yield int(''.join(map(str, pandigital_digits)))


def brute_force_solution():
    """Test every possible pandigital number to determine if it has specified properties."""
    partial_numbers = [
        pandigital_number
        for pandigital_number in pandigital_numbers()
        if passes_divisibility_tests(pandigital_number)
    ]

    return sum(partial_numbers)


def pandigital_partials(n, suffix='', limit=1000):
    """
    Return list of pandigital partial strings where the str[0:3] is a multiple of n, str[2:] is
    equal to suffix, and str contains no duplicate digits.
    """
    def has_duplicate_digits(n):
        return len(str(n)) != len(set(str(n)))

    multiples = []
    count = n

    while count < limit:
        count_str = '0' * (3 - len(str(count))) + str(count)

        if suffix and suffix[:2] == count_str[-2:]:
            count_str = count_str[:-2] + suffix
            if not has_duplicate_digits(count_str):
                multiples.append(count_str)

        elif not suffix and not has_duplicate_digits(count_str):
            multiples.append(count_str)

        count += n

    return multiples


def prefix_pandigital_number(number):
    """Prefix number with last digit required to make it pandigital."""
    remaining_digits = set(''.join(map(str, range(10)))) - set(number)
    if len(remaining_digits) != 1:
        raise ValueError('{0} requires more than one digit to be pandigital'.format(number))

    return remaining_digits.pop() + number


def reverse_search():
    """
    Find 3 digit sequences which are divisible by specified numbers and merge these 
    together to find final set of pandigital numbers.
    """
    partial_numbers = pandigital_partials(17)

    for i in [13, 11, 7, 5, 3, 2]:
        partial_numbers = [
            prefix[0] + partial_number
            for partial_number in partial_numbers
            for prefix in pandigital_partials(i, suffix=partial_number)
        ]

    # first digit has not been solved more yet so complete pandigital 0-9 number
    pandigital_numbers = [
        prefix_pandigital_number(partial_number)
        for partial_number in partial_numbers
    ]

    return sum(map(int, pandigital_numbers))


SOLUTIONS = [
    brute_force_solution,
    reverse_search,
]
