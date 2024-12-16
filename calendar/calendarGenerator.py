#!/usr/bin/env python3

"""A simple python script to display calendar of any year.

"""

from calendar import *

year = int(input("Enter any year: "))
print(calendar(year))
