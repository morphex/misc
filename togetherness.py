#!/usr/bin/env python3

__doc__ = """

Small utility script, to find sequential dates.  Used to find the dates every 8th
week from the start date.

"""

import datetime
import sys

WEEK_FREQUENCY = 8
START = datetime.date(2021, 1, 30)
WEEK = datetime.timedelta(days=7)

columns = []

for y in range(0, 8):
    rows = []
    start = START + (WEEK * y)
    for x in range(0, 12):
        rows.append('{:3}'.format(x+1) + ': ' + str(start + (WEEK * WEEK_FREQUENCY * x)))
    columns.append(rows)

rows = len(columns[0])
format = ""
for column in range(len(columns)):
    format += " {: >10}"
for row in range(rows):
    output_column = []
    for index in range(len(columns)):
        output_column.append(columns[index][row])
    print(format.format(*output_column))
