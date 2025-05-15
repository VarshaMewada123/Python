# Importing necessary classes from datetime module
from datetime import datetime, date, time, timedelta

# 1. Getting the current date and time
# 'datetime.now()' returns the current date and time
current_datetime = datetime.now()
print("Current date and time:", current_datetime)  # Output example: 2025-05-12 13:47:58.123456

# 2. Getting only the current date
# 'date.today()' returns the current date (without time part)
current_date = date.today()
print("Current date:", current_date)  # Output example: 2025-05-12

# 3. Creating a custom date
# You can create a date manually by providing year, month, and day
custom_date = date(2022, 12, 25)
print("Custom date:", custom_date)  # Output: 2022-12-25

# 4. Creating a custom time
# You can create a time manually by providing hour, minute, and second
custom_time = time(14, 30, 45)
print("Custom time:", custom_time)  # Output: 14:30:45

# 5. Formatting a datetime object
# 'strftime()' allows you to format a datetime object into a string in a specific format
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_datetime)  # Output example: 2025-05-12 13:47:58

# 6. Parsing a string into a datetime object
# 'strptime()' allows you to convert a string into a datetime object
date_string = "2025-07-19 10:15:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed date and time:", parsed_date)  # Output: 2025-07-19 10:15:00

# 7. Adding and subtracting time using timedelta
# 'timedelta' allows you to perform arithmetic on dates and times
# Adding 5 days to the current date
new_date = current_date + timedelta(days=5)
print("New date after 5 days:", new_date)  # Output example: 2025-05-17

# Subtracting 3 hours from the current datetime
new_time = current_datetime - timedelta(hours=3)
print("New time after subtracting 3 hours:", new_time)  # Output example: 2025-05-12 10:47:58.123456

# 8. Calculating difference between two dates
# You can subtract two dates to find the difference between them
date1 = date(2023, 5, 10)
date2 = date(2023, 6, 15)
date_diff = date2 - date1
print("Difference between dates:", date_diff)  # Output: 36 days, 0:00:00

# 9. Working with time zone (using timezone object)
# You can also work with time zone information using the 'timezone' class
from datetime import timezone
current_datetime_with_timezone = datetime.now(timezone.utc)
print("Current date and time with timezone:", current_datetime_with_timezone)
# Output example: 2025-05-12 13:47:58.123456+00:00
