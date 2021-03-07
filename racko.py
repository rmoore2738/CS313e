# File: racko.py
# Description: A program that simulates the card and number game
# Rack-O. Players use the keyboard and take turns.
# Assignment Number: 10
#
# Name: Rebecca Moore
# EID:  rrm2738
# Email: rebeccamoore32@utexas.edu
# Grader:  Skyler
#
# On my honor, Rebecca Moore, this programming assignment is my own work
# and I have not provided this code to any other student.

import random


# Play one game of Rack-O.
def main():
    # Get the rack size, create the deck, and deal the initial racks.
    rack_size = prep_game()
    deck = list(range(1, 61))
    random.shuffle(deck)
    player = 1
    player_1_rack = get_rack(deck, rack_size)
    player_2_rack = get_rack(deck, rack_size)
    discard = [deck.pop(0)]

    while not is_sorted(player_1_rack) and not is_sorted(player_2_rack):
        print("Player " + str(player) + "'s turn.")
        take_turn(deck, discard,
                    player_1_rack if player == 1 else player_2_rack)
        player = 1 if player == 2 else 2

        # checks if deck is empty and if it is, shuffles discard pile and
        # makes it the new draw deck
        if len(deck) == 0:
            print("Deck is empty, shuffling discard pile.")
            random.shuffle(discard)
            deck = discard
            discard = [deck.pop(0)]

    print("Player " + str(1 if player == 2 else 2) + " wins!")


# Get ready to play 1 game.
# Show the instructions if the user wants to see them.
# Set the seed for the random number generator.
# Return the size of the rack to use.
def prep_game():
    print('----- Welcome to Rack - O! -----')
    if input('Enter y to display instructions: ') == 'y':
        instructions()
    print()
    random.seed(eval(input('Enter number for initial seed: ')))
    rack_size = eval(input('Enter the size of the rack to use. '
                            + 'Must be between 5 and 10: '))
    while not 5 <= rack_size <= 10:
        print(rack_size, 'is not a valid rack size.')
        rack_size = eval(input('Enter the size of the rack to use. '
                            + 'Must be between 5 and 10: '))
    print()
    return rack_size


# Print the instructions of the game.
def instructions():
    print()
    print('The goal of the game is to get the cards in your rack of cards')
    print('into ascending order. Your rack has ten slots numbered 1 to 10.')
    print('During your turn you can draw the top card of the deck or take')
    print('the top card of the discard pile.')
    print('If you draw the top card of the deck, you can use that card to')
    print('replace a card in one slot of your rack. The replaced card goes to')
    print('the discard pile.')
    print('Alternatively you can simply choose to discard the drawn card.')
    print('If you take the top card of the discard pile you must use it to')
    print('replace a card in one slot of your rack. The replaced card goes')
    print('to the top of the discard pile.')


# Take the player's turn. Give them the choice of drawing or taking
# the top card of the discard pile. If they draw they can replace
# a card or discard the draw. If they take the top card of the discard
# pile they must replace a card in their rack.
def take_turn(deck, discard, player_rack):
    # shows the player their rack and the top of the discard pile
    print("Your current rack  " + str(player_rack))
    print("Top of discard pile  " + str(discard[0]))

    # ask player if they want to draw a card from deck or top of discard
    turn_type = str(input("Enter d to draw anything else to take " +\
        "top of discard pile: "))
    print()

    if turn_type == "d":
        # player wants to draw from Deck
        drawn_card = deck.pop(0)
        print("drew the " + str(drawn_card))

        # asks to keep the card or discard it
        should_discard = str(input("Enter p to place card, " +\
                "anything else to discard it: "))

        if should_discard == "p":
            place_card(player_rack, drawn_card, discard)
        else:
            discard.insert(0, drawn_card)
    else:
        # player takes card from top of discard
        place_card(player_rack, discard.pop(0), discard)

    # print the final rack of the turn
    print("The rack after the turn  " + str(player_rack))
    print()


# Ask the player which card to replace in their rack.
# Replace it with the given new card. Place the card removed
# from the player's rack at the top of the discard pile.
# Error checks until player enters a card that is currently
# in their rack.
def place_card(player_rack, new_card, discard):
    # ask the player which card in their deck to replace
    replace = int(input("Enter the card number to replace with the "\
        + str(new_card) + ": "))

    # check the card is in the deck
    while replace not in player_rack:
        print(str(replace) + " is not in your rack.")
        replace = int(input("Enter the card number to replace with the "\
            + str(new_card) + ": "))

    # replace old card with new and move old to discard pile
    discard.insert(0, replace)
    player_rack[player_rack.index(replace)] = new_card


# Return True if this rack is sorted in ascending order, False otherwise.
# Do not create any new lists in this function.
def is_sorted(rack):
    return sorted(rack) == rack


# Deal the top 10 cards of the deck into a new rack. The first
# card goes in the first slot, the second card goes in the second
# slot, and so forth. We assume len(deck) >= rack_size. Return the
# list of ints representing the rack.
def get_rack(deck, rack_size):
    rack = []
    for i in range(rack_size):
        rack.append(deck.pop(0))
    return rack


main()
