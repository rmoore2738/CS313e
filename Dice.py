# File: Dice.py
# Description: Simulates the game craps.
# Assignment number: 6
#
# Name: Rebecca Moore
# EID: rrm2738
# Email: rebeccamoore32@utexas.edu
# Grader: Skyler
#
# On my honor, Rebecca Moore, this programming assignment is my own work
# and I have not provided this code to any other students.


import random


def main():
    # This describes the program to the user.
    print("This program simulates the dice game of craps.")

    # Asks the user if they want to set a seed.
    answer = input("Do you want to set the seed? Enter y for yes, " +\
    "anything else for no: ")
    if answer == "y":
        seed = int(input("Enter an int for the initial seed: "))
        random.seed(seed)

    # This gets the number of rounds to play.
    number_of_rounds = max(0, \
    int(input("Enter the number of rounds to run: ")))

    # This simulates craps for the number of times entered.
    number_of_wins = 0
    max_rolls = 0
    for round in range(number_of_rounds):
        number_of_rolls = 1
        point = random.randint(1,6) + random.randint(1,6)

        # if this is the initial roll, the player wins.
        if point == 7 or point == 11:
            number_of_wins += 1
        # If the player rolls 2, 3, or 12, they lose.
        elif not (point == 2 or point == 3 or point == 12):
            roll = random.randint(1,6) + random.randint(1,6)
            number_of_rolls += 1
            # player did not lose second roll, continue until rolls
            # 7 or point.
            while roll != 7 and roll != point:
                roll = random.randint(1,6) + random.randint(1,6)
                number_of_rolls += 1
            # player rolled point and won.
            if roll == point:
                number_of_wins += 1
        # checks if this round went longer than previous once.
        if number_of_rolls > max_rolls:
            max_rolls = number_of_rolls

    # This prints the results.
    print("Player won " + str(number_of_wins) + " times in " +
        str(number_of_rounds) + " rounds.")
    print("Maximum number of rolls in a round = " + str(max_rolls))


main()


# Analysis:
# 1. yes the simulation supports that in the long run casinos come out
# the winner. When i ran a simulation of 1,000,000 games, there was only
# about a 50% chance i would win. this was the printed outcome:
# Do you want to set the seed? Enter y for yes, anything else for no: n
# Enter the number of rounds to run: 1000000
# Player won 493731 times in 1000000 rounds.
# Maximum number of rolls in a round = 43
# 0.493731 (this is the percent of wins)

# 2. I would chose to keep the money. Based on question 1, the casino
# comes out the winner a litte more than 50% of the time and thats a risk
# i am not willing to take with my money. The only way i would play is if
# the amount i could win was 2 times greater than my bet or more. If This
# was the case, i would be about 2 times more likely to win money rather
# than lose all my money.
