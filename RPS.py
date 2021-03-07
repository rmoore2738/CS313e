# File: RPS.py
# Description: Simulates the game rock, paper, scissors.
# Assignment number: 7
#
# Name: Rebecca Moore
# EID: rrm2738
# Email: rebeccamoore32@utexas.edu
# Grader: Skyler
#
# On my honor, Rebecca Moore, this programming assignment is my own work
# and I have not provided this code to any other students.


import random


# Takes the user inputs for name, rounds and seed.
def inputs(prompt):
    print("***** INITIAL INPUT *****")
    user_input = input(prompt)
    print("Thank you!")
    print()
    return user_input


# This function gets the users move.
def moves(name, num_rounds):
    # This counts the rounds and how many the user wins
    user_wins = 0
    for round in range(num_rounds):
        print("**** Round " + str(round + 1) + " ****")
        print(name + ", enter your choice for this round.")
        user_move = input("R for Rock, P for Paper, S for Scissors: ")
        computer_move = random.randint(1, 3)
        print("I pick " + (convert_int_to_word(computer_move)))
        user_wins += comparison(convert_move_to_int(user_move),\
        computer_move, user_wins)
        print()
    return user_wins


# This converts the players move to an integer.
def convert_move_to_int(move):
    if move == "R":
        return 1
    elif move == "P":
        return 2
    else:
        return 3


# This converts the integer to the coresponding word.
def convert_int_to_word(int):
    if int == 1:
        return "Rock."
    elif int == 2:
        return "Paper."
    else:
        return "Scissors."


# This compares the user and computer to see who wins.
def comparison(user_guess, computer_guess, user_wins):
    if user_guess == computer_guess:
        print("We picked the same thing. Round is a draw.")
    elif user_guess == 1 and computer_guess == 2:
        print("Paper covers Rock. I win.")
    elif user_guess == 1 and computer_guess == 3:
        print("Rock breaks Scissors. You win.")
        user_wins += 1
    elif user_guess == 2 and computer_guess == 1:
        print("Paper covers Rock. You win.")
        user_wins += 1
    elif user_guess == 2 and computer_guess == 3:
        print("Scissors cut paper. I win.")
    elif user_guess == 3 and computer_guess == 1:
        print("Rock breaks Scissors. I win.")
    elif user_guess == 3 and computer_guess == 2:
        print("Scissors cut paper. You win.")
        user_wins += 1
    return user_wins


# This plays rock, paper, scissors with the computer.
def main():
    print("Welcome to ROCK PAPER SCISSORS. " +
    "I, Computer, will be your opponent.")

    # this takes the inputs.
    name = inputs("Please enter your name: ")
    num_rounds = int(inputs("Please enter the number of rounds to play: "))
    answer = inputs("Please enter y if you want to set the seed: ")
    if answer == 'y':
        random.seed(int(inputs('Please enter an integer for the seed: ')))

    # Plays number of rounds of RPS
    user_wins = moves(name, num_rounds)

    # These print the final stats.
    print("We played " + str(num_rounds) + (" round" if num_rounds == 1\
        else " rounds") + " of ROCK PAPER SCISSORS.")
    print(name + " won " + str(user_wins) + (" round." if user_wins == 1\
        else " rounds."))
    print("Well played.")


main()
