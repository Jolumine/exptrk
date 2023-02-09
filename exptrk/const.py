# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the exptrk python project,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import datetime

# Date
DAYS = [str(i) for i in range(1 , 32)]
WEEKDAYS = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September","October", "November", "December"]
YEARS = [str(i) for i in range(datetime.datetime.now().year-5, datetime.datetime.now().year+10)]

# CSV 
FIELD_NAMES = ["ID", "Amount", "Day", "Month", "Year", "Description"]

# Passive income
ROUTINES = ["daily", "monthly", "yearly"]

# Basic ops
TYPES_OF_FLOWS = ["Expense", "Income"]

# Settings std
CURRENCYS = ["USD/$", "EUR/€", "JPY/\u00A5", "GBP/\u00A3"]
