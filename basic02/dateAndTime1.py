from datetime import datetime, date, time, timedelta, timezone

# Get the current date and time
current_datetime = datetime.now()
print("Current Date & Time:", current_datetime)

#  Get the current date
current_date = date.today()
print("Current Date:", current_date)

#  Create a specific date object
custom_date = date(2024, 12, 25)
print("Custom Date (Christmas):", custom_date)

#  Create a specific time object
custom_time = time(14, 30, 0)  # 2:30 PM
print("Custom Time:", custom_time)

#  Combine date and time to create a datetime object
combined_datetime = datetime(2024, 12, 25, 14, 30)
print("Combined DateTime:", combined_datetime)

#  Format datetime into a string
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Current DateTime:", formatted_datetime)

# 7️⃣ Parse string into datetime object
parsed_datetime = datetime.strptime("2025-01-01 10:00:00", "%Y-%m-%d %H:%M:%S")
print("Parsed DateTime from String:", parsed_datetime)

# 8️⃣ Add 7 days using timedelta
future_date = current_date + timedelta(days=7)
print("Date After 7 Days:", future_date)

# 9️⃣ Subtract 3 days using timedelta
past_date = current_date - timedelta(days=3)
print("Date Before 3 Days:", past_date)

# 🔟 Convert timestamp to datetime
timestamp = 1715581230  # Sample UNIX timestamp
date_from_timestamp = datetime.fromtimestamp(timestamp)
print("Date from Timestamp:", date_from_timestamp)

#  Create a timezone-aware datetime (UTC+5:30 for India)
india_timezone = timezone(timedelta(hours=5, minutes=30))
datetime_with_timezone = datetime.now(india_timezone)
print("Datetime with Indian Timezone (UTC+5:30):", datetime_with_timezone)
