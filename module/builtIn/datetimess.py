# Importing the datetime module
import datetime

# 1. datetime.datetime.now(): Returns the current local date and time
current_datetime = datetime.datetime.now()
print(f"Current Date and Time: {current_datetime}")

# 2. datetime.date.today(): Returns the current local date
current_date = datetime.date.today()
print(f"Today's Date: {current_date}")

# 3. datetime.timedelta(days=1): Represents a duration of one day
one_day = datetime.timedelta(days=1)
yesterday = current_date - one_day
tomorrow = current_date + one_day

print(f"Yesterday's Date: {yesterday}")
print(f"Tomorrow's Date: {tomorrow}")
