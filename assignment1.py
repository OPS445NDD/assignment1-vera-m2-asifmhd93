#!/usr/bin/env python3
# Author ID: amohammad21

import sys

# check if year is a leap year
def leap_year(year):

    if year % 4 == 0:
        leap = True
    else:
        leap = False

    if year % 100 == 0:
        leap = False

    if year % 400 == 0:
        leap = True

    return leap


# get max days for a month
def mon_max(month, year):

    if leap_year(year):
        feb_max = 29
    else:
        feb_max = 28

    months = {
        1: 31,
        2: feb_max,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    return months[month]


def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    '''

    # split date into parts
    str_year, str_month, str_day = date.split('-')

    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    max_days = mon_max(month, year)

    tmp_day = day + 1  # next day

    if tmp_day > max_days:
        to_day = tmp_day % max_days
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month + 0

    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month + 0

    next_date = f"{year}-{to_month:02}-{to_day:02}"

    return next_date


if __name__ == "__main__":
    print(after('2023-01-25'))
    print(after('2016-02-28'))
    print(after('2025-12-31'))

#Milestone 2


# find day of week
def day_of_week(date):

    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])

    offset = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]

    if month < 3:
        year = year - 1

    day_num = (year + year // 4 - year // 100 + year // 400 + offset[month - 1] + day) % 7

    days = {
        0: 'Sun',
        1: 'Mon',
        2: 'Tue',
        3: 'Wed',
        4: 'Thu',
        5: 'Fri',
        6: 'Sat'
    }

    return days[day_num]


# check if date is valid
def valid_date(date):

    if len(date) != 10:
        return False

    if date[4] != '-' or date[7] != '-':
        return False

    str_year, str_month, str_day = date.split('-')

    if not str_year.isdigit():
        return False

    if not str_month.isdigit():
        return False

    if not str_day.isdigit():
        return False

    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    if month < 1 or month > 12:
        return False

    if day < 1:
        return False

    if day > mon_max(month, year):
        return False

    return True


# count Saturdays and Sundays
def day_count(start_date, end_date):

    count = 0
    current = start_date

    while True:

        day = day_of_week(current)

        if day == 'Sat' or day == 'Sun':
            count = count + 1

        if current == end_date:
            break

        current = after(current)

    return count
