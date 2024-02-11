#!/usr/bin/env python
# python recreation of https://twitter.com/year_progress?lang=en
from datetime import date
import datetime

#https://www.geeksforgeeks.org/python-program-to-find-number-of-days-between-two-given-dates/
def numOfDays(date1, date2):
    if date2 > date1:
        return (date2 - date1).days
    else:
        return (date1 - date2).days

def main():
    today = datetime.date.today()

    year = int(today.strftime("%Y"))

    currentYear = date(year, 1, 1)
    nextYear = date(year+1, 1, 1)
    days = numOfDays(currentYear, nextYear)
    daysLeft = numOfDays(today, nextYear)
    daysPassed = days - daysLeft
    percent = daysPassed/days
    roundedPercent = int(round(percent * 100, 0))

    bars = 15
    filled = int(round(percent * bars, 0))
    fill = "▓"
    unfill = "░"
    count = 0
    print(f"{currentYear.year} is {roundedPercent}% complete.")
    while True:
        count = count + 1
        if count <= filled:
            print(fill, end="")
        elif count <= bars:
            print(unfill, end="")
        else:
            break

if __name__ == "__main__":
    main()
