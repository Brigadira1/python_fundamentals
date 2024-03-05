def is_leap_year(year: int) -> bool:
    is_leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_leap = True
            else:
                is_leap = False
        else:
            is_leap = True
    else:
        is_leap = False

    return is_leap

days_in_month = {"january":31, "february": 28, "march": 31, "april": 30, "may": 31, "june": 30, "july": 31, "august": 31,"september": 30,"october": 31, "november": 30, "december": 31}

year = int(input("Enter the year: "))
if is_leap_year(year):
    days_in_month["february"] = 29
month = input("Enter month to check how many days it has: ").lower()
if not days_in_month.get(month):
    print("Invalid month name....Exiting....")
    exit(1)
else:
    print(f"The month of {month} has {days_in_month[month]} days")




