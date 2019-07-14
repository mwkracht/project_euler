"""
Project Euler - Problem 31
Copyright (c) Matthew Kracht. All rights reserved.

In England the currency is made up of pound, £, and pence, p, and there are eight coins in
general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
import functools

TOTAL = 200  # pence
COINS = (1, 2, 5, 10, 20, 50, 100, 200)  # pence


@functools.lru_cache(maxsize=None)
def coin_search(total, coins):
    """
    Recursively build list of coin combinations which sum to provided total.

    By memoizing function (lru_cache) overlapping subproblems of coin search are only computed
    once.
    """
    combinations = []

    for coin in coins:
        if coin == total:
            combinations.append([coin])
        elif coin < total:
            sub_total = total - coin

            # remove any coins which are smaller than the current coin to avoid getting
            # permutations of coins instead of combinations - for example if total is 10
            # and coin is 1 then the only combination should be 10 1s. The combination of one 5
            # and five 1s will be returned when coin is 5 (along with two 5s)
            sub_coins = tuple(sub_coin for sub_coin in coins if sub_coin <= coin)

            combinations.extend([
                [coin] + sub_combinations
                for sub_combinations in coin_search(sub_total, sub_coins)
            ])

    return combinations


def brute_force_search_solution():
    """Recrusively search for all COIN combinations which sum to TOTAL."""
    return len(coin_search(TOTAL, COINS))


def dynamic_programming_solution():
    """
    Use traditional dynamic programming algorithm to compute solution.

    As an example, here is computing a total of 10p using 1p, 2, and 5p coins:

    Total   -   1p  2p  5p
    0p      0   0   0   0
    1p      0   1   1   1
    2p      0   1   2   2
    3p      0   1   2   2
    4p      0   1   3   3
    5p      0   1   3   4
    6p      0   1   4   5
    7p      0   1   4   6
    8p      0   1   5   7
    9p      0   1   5   8
    10p     0   1   6   10

    You add the number of combinations possible for the given total without the given coin to
    the amount of combinations possible if you remove the given coin from the total to get the
    combinations possible for a total with a subset of coins.

    The code will condense the 2D structure above into a single array of length TOTAL + 1 and
    compute current iteration state using state in the array from previous iterations.
    """
    num_combos = [1] * (TOTAL + 1)

    # ignore 1p coin since we are initializing num_combos with that value
    for coin in COINS[1:]:
        for total in range(TOTAL + 1):
            # if coin value is greater than total then num_combos cannot change
            if coin <= total:  
                num_combos[total] += num_combos[total - coin]

    return num_combos[TOTAL]


SOLUTIONS = [
    brute_force_search_solution,
    dynamic_programming_solution,
]
