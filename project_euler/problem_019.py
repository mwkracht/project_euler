"""
Project Euler - Problem 19
Copyright (c) Matthew Kracht. All rights reserved.

You are given the following information, but you may prefer to do some research for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is
  divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""
import datetime


NUM_DAYS_IN_WEEK = 7
DAYS_IN_MONTH = [
    31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
]


def days_in_month(month, year):
    """Return number of days in month where month is zero indexed."""
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    if month == 1 and is_leap_year(year):
        return DAYS_IN_MONTH[month] + 1

    return DAYS_IN_MONTH[month]


def brute_force():
    """Iterate through every first of the month to determine if it falls on a Monday."""
    day_of_week = 0  # monday is the 0th day of the week
    first_sundays = 0

    # progress date from Monday 1 Jan 1900 to 1 Jan 1901 which is the date to begin the count
    for year in range(1900, 1901):
        for month in range(len(DAYS_IN_MONTH)):
            day_of_week = (day_of_week + days_in_month(month, year)) % NUM_DAYS_IN_WEEK

    for year in range(1901, 2001):
        for month in range(len(DAYS_IN_MONTH)):
            if day_of_week == 6:
                first_sundays += 1

            day_of_week = (day_of_week + days_in_month(month, year)) % NUM_DAYS_IN_WEEK

    return first_sundays


def cleaner_brute_force():
    """Use python datetime module (even though its a bit slower) to compute day of the week."""
    return sum([
        datetime.datetime(year, month, 1).weekday() == 6
        for year in range(1901, 2001)
        for month in range(1, 13)
    ])


SOLUTIONS = [
    brute_force,
    cleaner_brute_force,
]
