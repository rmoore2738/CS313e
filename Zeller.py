# File: Zeller.py
# Description: Calculate the day of the week
# Assignment number: 5
#
# Name: Rebecca Moore
# EID: rrm2738
# Email: rebeccamoore32@utexas.edu
# Grader: Skyler
# Slip days used this assignment: 0
#
# On my honor, Rebecca Moore, this programming assignment is my own work
# and I have not provided this code to any other students.


# This function calculates the day of the week.
def main():
    # These take the input from the user.
    month = input(str("Enter the month (for example, January, February, etc.): "))
    day_in_month = int(input("Enter the day (an integer): "))
    year = int(input("Enter the year (an integer): "))

    # This assigns each month a number.
    if month == "January":
        month_number = 13
        year = year - 1
    elif month == "February":
        month_number = 14
        year = year - 1
    elif month == "March":
        month_number = 3
    elif month == "April":
        month_number = 4
    elif month == "May":
        month_number = 5
    elif month == "June":
        month_number = 6
    elif month == "July":
        month_number = 7
    elif month == "August":
        month_number = 8
    elif month == "September":
        month_number = 9
    elif month == "October":
        month_number = 10
    elif month == "November":
        month_number = 11
    else:
        month_number = 12

    # This calculates the days.
    variation_in_days_per_month = ( 13 * (month_number + 1)) // 5
    leap_year_days = year // 4 + year // 400
    century_days = year // 100
    total_days = day_in_month + variation_in_days_per_month + year + leap_year_days - century_days
    day_of_week = total_days % 7

    # This assigns each number a day of the week and prints it.
    if day_of_week == 0:
        day_of_week_name = "Saturday."
    elif day_of_week == 1:
        day_of_week_name = "Sunday."
    elif day_of_week == 2:
        day_of_week_name = "Monday."
    elif day_of_week == 3:
        day_of_week_name = "Tuesday."
    elif day_of_week == 4:
        day_of_week_name = "Wednesday."
    elif day_of_week == 5:
        day_of_week_name = "Thursday."
    else:
        day_of_week_name = "Friday."

    # This prints the output.
    print("The day of the week is " + day_of_week_name)


main()
