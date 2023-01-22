import datetime

# Date
DAYS = [str(i) for i in range(1 , 32)]
WEEKDAYS = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September","October", "November", "December"]
YEARS = [str(i) for i in range(datetime.datetime.now().year-5, datetime.datetime.now().year+10)]

# CSV 
FIELD_NAMES = ["Amount", "Day", "Month", "Year", "Description"]

# Passive income
ROUTINES = ["daily", "monthly", "yearly"]

# Basic ops
TYPES_OF_FLOWS = ["Expense", "Income"]

# Logs 
LOG_FILE = "/.data/logs.log"

# Settings std
CURRENCYS = ["USD/$", "Euro/€", "Yen/\u00A5", "Pound/\u00A3"]
