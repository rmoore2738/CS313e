# File: EasterDate.py
# Description: calculate the month and day of easter for any year
# Assignment number: 2
#
# Name: Rebecca Moore
# EID: rrm2738
# Email: rebeccamoore32@utexas.edu
# Grader: Skyler
# Slip days used this assignment: 0
#
# On my honor, Rebecca Moore, this programming assignment is my own work
# and I have not provided this code to any other students.

# this function will calculate the day and month of easter for any year.


def main():


    year = int(input("Enter year: "))

    lunar_year_cycle_position = year % 19
    weekday_slide_part_1 = year % 4
    weekday_slide_part_2 = year % 7
    leap_year_100 = year // 100
    leap_year_400 = leap_year_100 // 4
    lunar_orbit_correction = (13 + 8 * leap_year_100) // 25
    century_start = (15 - lunar_orbit_correction + leap_year_100 -
                     leap_year_400) % 30
    sunday_offset = (4 + leap_year_100 - leap_year_400) % 7
    days_added = (19 * lunar_year_cycle_position + century_start) % 30
    day_of_week_offset = (2 * weekday_slide_part_1 + 4 * weekday_slide_part_2
                          + 6 * days_added + sunday_offset) % 7
    total_days_added = (22 + days_added + day_of_week_offset)
    day_of_easter = total_days_added % 31
    month_of_easter = (3 + (total_days_added // 31))

    print("In", year, "Easter Sunday is on month", month_of_easter, "and day",
          day_of_easter)


main()
