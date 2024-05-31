import datetime as dt
import pytz
# Examples of the date object in datetime package

current_date = dt.date.today();
print(current_date)
print(f"Current year: {current_date.year}")
print(f"Current day: {current_date.day}")
print(f"Current month: {current_date.month}\n")

date1 = dt.date(2023, 2, 22)
print(date1)
print(str(type(date1)) + "\n")

# Examples of the datetime object in datetime package

datetime_obj = dt.datetime(2023, 2, 28, 23, 55, 34, 45675)
print(datetime_obj)
print(datetime_obj.date())
print(datetime_obj.year)
print(datetime_obj.month)
print(datetime_obj.day)
print("\n")
print(datetime_obj.time())
print("\n")

current_datetime = dt.datetime.now()
print(current_datetime)

# Examples of timedelta class of the datetime package

curr_date = dt.datetime.now()
new_year = dt.datetime(2024, 1, 1)

delta = new_year - curr_date;
print(f"Time remaining until 2024: {delta}")
print(type(delta))
print("\n")

# Handling timezones. This is very important!

local = dt.datetime.now()
print("Local: ", local.strftime("%d/%m/%Y, %H:%M:%S"))

tz_NY = pytz.timezone("America/New_York")
print(type(tz_NY))
datetime_NY = dt.datetime.now(tz_NY)
print(f"The local time in New York is: {datetime_NY}")

tz_London = pytz.timezone("Europe/London")
time_London = dt.datetime.now(tz_London)
print(f"Local time in London is: {time_London}")





