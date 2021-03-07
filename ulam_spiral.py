# File: ulam_spiral.py
# Description: A program that makes an ulam spiral of a specific integer
# Assignment Number: 11
#
# Name: Rebecca Moore
# EID:  rrm2738
# Email: rebeccamoore32@utexas.edu
# Grader:  Skyler
#
# On my honor, Rebecca Moore, this programming assignment is my own work
# and I have not provided this code to any other student.


# Takes the user input and loops until it is acceptable.
def user_input():
    num = int(input("Enter an odd integer greater than or equal to 1: "))
    while num < 1 or num % 2 == 0:
        print(str(num) + " is not an odd integer >= 1.")
        num = int(input("Enter an odd integer greater than"\
                + " or equal to 1: "))
    return num
    #returns the input once it is acceptable


# Makes the integer spiral
def integer_spiral(size):
    num = size * size
    spiral = [[1 for c in range(size)] for r in range(size)]
    for i in range(0, size - 1):
        # to move left
        col = size - i - 1
        row = size - i - 1
        while col >= i:
            spiral[row][col] = num
            num -= 1
            col -= 1
        # to move up
        col = i
        row = size - i - 2
        while row >= i:
            spiral[row][col] = num
            num -= 1
            row -= 1
        # to move right
        col = i + 1
        row = i
        while col <= size - i - 1:
            spiral[row][col] = num
            num -= 1
            col += 1
        # to move down
        col = size - i - 1
        row = i + 1
        while row < size - i - 1:
            spiral[row][col] = num
            num -= 1
            row += 1
    return spiral


# prints the integer spiral.
def print_integer_spiral(spiral):
    print("----- The Integer Spiral Size " + str(len(spiral)) + " -----")
    for row in range(len(spiral)):
        for column in range(len(spiral) - 1):
            print(str(spiral[row][column]), end = "")
            print(" ", end = "")
        print(spiral[row][len(spiral) - 1], end = "\n")
    print()


# prints the spiral replacing every prime with a *
def ulam_spiral(spiral):
    print("----- The Ulam Spiral Size " + str(len(spiral)) + " -----")
    for row in range(len(spiral)):
        for column in range(len(spiral)):
            if is_prime(spiral[row][column]) and not \
                    spiral[row][column] == 1:
                print("*", end = "")
            else:
                print(" ", end = "")
        print()


# determines if a number is prime.
def is_prime(num):
    divisor = 2
    while divisor <= num / 2:
        if num % divisor == 0:
            return False
        divisor += 1
    return True


# calls the above functions and prints opening statement.
def main():
    print("This program displays an Ulam Spiral of the specified size.")
    print()
    size = user_input()
    spiral = integer_spiral(size)
    print_integer_spiral(spiral)
    ulam_spiral(spiral)


main()
