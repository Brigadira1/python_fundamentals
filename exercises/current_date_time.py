import time
import datetime

current_date = time.ctime()

print("Current date/time is: " + current_date)

current_date = datetime.datetime.now()

print(f"Second way of showing the current date/time: {current_date}")
print(f"Year: {current_date.year}")
print(f"Day: {current_date.day}")
print(f"Hour: {current_date.hour}")
