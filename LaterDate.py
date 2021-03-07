# File: LaterDate.py
# Description: calculate the days after a specific date given inputs
# Assignment number: 4
#
# Name: Rebecca Moore
# EID: rrm2738
# Email: rebeccamoore32@utexas.edu
# Grader: Skyler
# Slip days used this assignment: 0
#
# On my honor, Rebecca Moore, this programming assignment is my own work
# and I have not provided this code to any other students.


# This function calculates the days to skip.
def main():
    # These print a description of the program for the user.
    print("This program asks for a date and days to skip.")
    print("It then displays the date that many days after the given date.")
    print()

    # These take the input for the month, day, year and days to skip.
    month = input(str("Enter the month: "))
    day = int(input("Enter the day of the month: "))
    year = int(input("Enter the year: "))
    print()
    skip_days = int(input("Enter the number of days to skip: "))
    print()

    # This initializes the varibles used below.
    new_month, new_day, new_year = None, None, year
    # This defines the length of the months.
    over_28, over_29, over_30, over_31 = (day + skip_days) > 28, (day + skip_days) > 29, (day + skip_days) > 30, (day + skip_days) > 31

    # These are the conditionals for each month.
    if month == "January":
        new_month = "February" if over_31 else "January"
        new_day = (day + skip_days) - 31 if over_31 else (day + skip_days)
    elif month == "February":
        # This checks if the year is a leap year.
        if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 ==     0)):
            new_month = "March" if over_29 else "February"
            new_day = (day + skip_days) - 29 if over_29 else (day + skip_days)
        else:
            new_month = "March" if over_28 else "February"
            new_day = (day + skip_days) - 28 if over_28 else (day + skip_days)
    if month == "March":
        new_month = "April" if over_31 else "March"
        new_day = (day + skip_days) - 31 if over_31 else (day + skip_days)
    if month == "April":
        new_month = "May" if over_30 else "April"
        new_day = (day + skip_days) - 30 if over_30 else (day + skip_days)
    if month == "May":
        new_month = "June" if over_31 else "May"
        new_day = (day + skip_days) - 31 if over_31 else (day + skip_days)
    if month == "June":
        new_month = "July" if over_30 else "June"
        new_day = (day + skip_days) - 30 if over_30 else (day + skip)
    if month == "July":
        new_month = "August" if over_31 else "July"
        new_day = (day + skip_days) - 31 if over_31 else (day + skip_days)
    if month == "August":
        new_month = "September" if over_31 else "August"
        new_day = (day + skip_days) - 31 if over_31 else (day + skip_days)
    if month == "September":
        new_month = "October" if over_30 else "September"
        new_day = (day + skip_days) - 30 if over_30 else (day + skip_days)
    if month == "October":
        new_month = "November" if over_31 else "October"
        new_day = (day + skip_days) - 31 if over_31 else (day + skip_days)
    if month == "November":
        new_month = "December" if over_30 else "November"
        new_day = (day + skip_days) - 30 if over_30 else (day + skip_days)
    if month == "December":
        new_month = "January" if over_31 else "December"
        new_day = (day + skip_days) - 31 if over_31 else (day + skip_days)
        new_year = year + 1 if over_31 else year

    # This prints the output.
    days_after = " day after " if skip_days == 1 else " days after "
    print(str(skip_days) +  days_after + month + " " + str(day) + ", " + str(year) + " is " + new_month + " " + str(new_day) + ", " + str(new_year) + ".")
    print()


main()
