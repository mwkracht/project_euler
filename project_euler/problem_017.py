"""
Project Euler - Problem 17
Copyright (c) Matthew Kracht. All rights reserved.

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains
23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing
out numbers is in compliance with British usage.
"""
LIMIT = 1001

# Adding [10, 20) to this list as well since it does not follow the same pattern of speech for
# ints [20, 100)
ONES_TO_ENGLISH = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
    'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
]

TENS_TO_ENGLISH = [
    '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
]


def int_to_english(n):
    """
    Convert integer N to English.

    Ignores spaces and hyphens for English text.
    """
    if n < len(ONES_TO_ENGLISH):
        return ONES_TO_ENGLISH[n]
    elif n < 100 and n % 10:
        return '{0}{1}'.format(TENS_TO_ENGLISH[n // 10], ONES_TO_ENGLISH[n % 10])
    elif n < 100 and not n % 10:
        return TENS_TO_ENGLISH[n // 10]
    elif n < 1000 and n % 100:
        return '{0}hundredand{1}'.format(ONES_TO_ENGLISH[n // 100], int_to_english(n % 100))
    elif n < 1000 and not n % 100:
        return '{0}hundred'.format(ONES_TO_ENGLISH[n // 100])
    elif n < 1e6 and n % 1000:
        return '{0}thousand{1}'.format(int_to_english(n // 1000), int_to_english(n % 1000))
    elif n < 1e6 and not n % 1000:
        return '{0}thousand'.format(int_to_english(n // 1000))

    raise ValueError('Integer {0} out of range'.format(n))


def brute_force_solution():
    """Calculate english text for all ints and sum length."""
    return sum(
        len(int_to_english(i))
        for i in range(1, LIMIT)
    )


SOLUTIONS = [
    brute_force_solution,
]
