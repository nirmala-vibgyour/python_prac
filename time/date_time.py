import datetime
import time

dt = datetime.datetime.now()
print(dt)
print(f"Year: {dt.year}, Month: {dt.month}, Day: {dt.day}")
print(f"Hour: {dt.hour}, Minute: {dt.minute}, Second: {dt.second}")

# prints argument in datetime like format
new_dt = datetime.datetime(2015, 10, 31, 0, 0, 0)
print(new_dt)

# datetime.datetime.fromtimestamp(current_time) converts the seconds into a datetime object
current_time = time.time()
dt_now = datetime.datetime.fromtimestamp(current_time)
print(current_time)
print(dt_now)

#  timedelta data type
# keyword arguments: weeks, days, hours, minutes, seconds, milliseconds, microseconds

first_date = datetime.datetime(year=2024, month=1, day=1)
second_date = datetime.datetime(year=2024, month=5, day=27)
interval0 = second_date - first_date
print(interval0)

# timedelta gives the interval like the above
interval1 = datetime.timedelta(days=10, seconds=3600)
print(interval1)

# use of timedelta: adding intervals to intervals.
print(f"Added 10 days and 1 hour: {interval0 + interval1}.")

# 'days', 'max', 'microseconds', 'min', 'resolution', 'seconds', 'total_seconds()'
# above things can be given out by timedelta
interval = datetime.timedelta(
    weeks=1,
    hours=10,
    minutes=22,
    milliseconds=1042,
)

print(f"{interval}")
print(f"{interval.days}")
print(f"{interval.seconds}")
print(f"{interval.microseconds}")
print(f"{interval.total_seconds()}")
print(f"{interval.resolution}")

# Even though the call to timedelta() includes arguments for weeks, hours, minutes, and milliseconds,
# the constructor converts these units to days, seconds, and microseconds. 
# The print() calls include f-strings with an equals sign = to display the variable name and its value.(used above)

# timedelta objects can be added or subtracted with datetime objects or
# other timedelta objects using the + and - operators. A timedelta object can be
# multiplied or divided by integer or float values with the * and / operators.

# actual use of timedelta
oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
time_before = oct21st - (2*aboutThirtyYears)

print(f"60 years ago, from {oct21st}: {time_before}")

# Pausing Until a Specific Date
# halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)
# while datetime.datetime.now() < halloween2016:
#     time.sleep(1)

# Use the strftime() method to display a datetime object as a string
oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
print(oct21st.strftime('%I:%M %p'))
print(oct21st.strftime("%B of '%y"))

# strptime(): takes a custom format string using the same directives as strftime() must be passed so that strptime() knows
# how to parse and understand the string. (The p in the name of the strptime() function stands for parse.)
# here, we can make datetime object of various formats.
dt2 = datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
print(dt2, type(dt2))

dt3 = datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
print(dt3, type(dt3))

dt4 = datetime.datetime.strptime("October of '15", "%B of '%y")
print(dt4, type(dt4))

dt5 = datetime.datetime.strptime("November of '63", "%B of '%y")
print(dt5, type(dt5))