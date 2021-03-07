# File: Bowling.py
# Description: calculate bowling average and handicap
# Assignment number: 3
#
# Name: Rebecca Moore
# EID: rrm2738
# Email: rebeccamoore32@utexas.edu
# Grader: Skyler
# Slip days used this assignment: 0
#
# On my honor, Rebecca Moore, this programming assignment is my own work
# and I have not provided this code to any other students.


from math import floor


# this function calculates the bowlers average and handicap.
def main():
    # Name takes input of a name from the user.
    name = input("Enter your name: ")
    print()

    # Each one takes an input of a game score.
    game_one = int(input("Enter Game 1: "))
    game_two = int(input("Enter Game 2: "))
    game_three = int(input("Enter Game 3: "))
    print()

    # Average calculates the average of the three inputs.
    average = (game_one + game_two + game_three) // 3
    print(name + "\'s average is: " + str(average))

    # Handicap calculates the handicap using the inputs and average.
    handicap = floor((200 - average) * .8)
    print(name + "\'s handicap is: " + str(handicap))
    print()


main()
