""""
Helps work with dates and times in real-world applications like scheduling or logging.
Allows easy calculation of differences between two dates or times.
Supports formatting and parsing of date/time strings for user-friendly outputs.
Useful for time-stamping events, files or data entries.
Essential for handling time zones, durations and calendar-based operations.
Class                 Description

date             Represents a date (year, month, day) in the Gregorian calendar

time             Represents a time independent of any date (hour, minute, second, microsecond, tzinfo)

datetime         Combines date and time (year, month, day, hour, minute, second, microsecond, tzinfo)

timedelta        Represents difference between two dates or times

tzinfo           Abstract base class for timezone information

timezone         Fixed offset timezone class (subclass of tzinfo) introduced in Python 3.2

Date class
The date class provided by datetime module, is used to create and manipulate date objects. When an instance of this class is created, it represents a specific calendar date in ISO 8601 format: YYYY-MM-DD.

Syntax
class datetime.date(year, month, day)

Parameters:

year: An integer between MINYEAR (usually 1) and MAXYEAR (usually 9999).
month: An integer from 1 (January) to 12 (December).
day: An integer valid for the specified month and year (e.g., 28 or 29 for February, depending on leap year).
Example 1: Creating a Date Object


from datetime import date
d = date(1996, 12, 11)
print(d)

Output
1996-12-11
Example 2: Get Current Date


from datetime import date
t = date.today()
print(t)

Output
2025-07-26
Example 3: Accessing Year, Month and Day Attributes


from datetime import date
t = date.today()
print(t.year)
print(t.month)
print(t.day)

Output
2025
7
26
Example 4: Create Date from Timestamp


from datetime import datetime
date_time = datetime.fromtimestamp(1887639468)
print(date_time)
print(date_time.date())

Output
2029-10-25 16:17:48
2029-10-25
Example 5: Convert Date to String


from datetime import date
t = date.today()
date_str = t.isoformat()
print(date_str)
print(type(date_str))

Output
2025-07-26
<class 'str'>

strftime()	Returns a string representation of the date with the given format
today()	Returns the current local date
weekday()	Returns the day of the week as integer where Monday is 0 and Sunday is 6

Datetime class
The datetime class represents both date and time components in a single object.

Timedelta Class
Python timedelta class is used for calculating differences in dates and also can be used for date manipulations in Python.
# Get the current date and time
now = datetime.now()
print("Current Date & Time:", now)
​
# Add 2 years (approx. 730 days)
after_2_years = now + timedelta(days=730)
print("After 2 Years:", after_2_years)
​
# Add 2 days
after_2_days = now + timedelta(days=2)
print("After 2 Days:", after_2_days)

Output
Current Date & Time: 2025-07-26 05:38:58.395824
After 2 Years: 2027-07-26 05:38:58.395824
After 2 Days: 2025-07-28 05:38:58.395824

Difference between two date and times
# Current date and time
now = datetime.now()
print("Current Time:", now)
​
# New time after 2 days
new_time = now + timedelta(days=2)
print("New Time (+2 days):", new_time)
​
# Time difference
print("Time Difference:", new_time - now)

Output
Current Time: 2025-07-26 05:40:17.572931
New Time (+2 days): 2025-07-28 05:40:17.572931
Time Difference: 2 days, 0:00:00
"""