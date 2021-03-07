# File: movies.py
# Description: A program works with movie ratings and reviews.
# Based on the Nifty Assignment:
# http://nifty.stanford.edu/2016/manley-urness-movie-review-sentiment/
# Assignment Number: 12
#
# Name: Rebecca Moore
# EID:  rrm2738
# Email: rebeccamoore32@utexas.edu
# Grader: Skyler
#
# On my honor, Rebecca, this programming assignment is my own work
# and I have not provided this code to any other student.


# Read the main data file and run the menu loop.
def main():
    print('Welcome to the movie sentiment program.')
    print('Enter a word to see the average rating of movies with that word.')
    file_name = input('Enter file name with reviews: ')
    reviews = get_reviews(file_name)
    choice = get_choice()
    # List of our functions. They all take a single parameter, the reviews.
    functions = [print_word_sentiment, print_sentiments_from_file,
                 print_longest_review, print_shortest_review]
    VALUE_1 = ord('1')
    while '1' <= choice <= '4':
        # Get the index of the function to call.
        index = ord(choice) - VALUE_1
        function = functions[index](reviews)
        choice = get_choice()


# Display the menu and get the users choice.
# Returns the user's choice as a String.
def get_choice():
    print()
    print('OPTIONS:')
    print('1. See average rating for a word.')
    print('2. Show average reviews for all words in a file.')
    print('3. See the longest review.')
    print('4. See the shortest review.')
    result = input('Please enter your choice: ')
    print()
    return result


# Given the file name, create a list of lists with the movie reviews.
# We expect one review per line. The first element will be an int [0, 4].
# The rest of the line shall be the review.
# All letters in the reviews are converted to lower case.
def get_reviews(file_name):
    name = open(file_name, "r")
    lines = name.readlines()
    reviews = []
    for line in lines:
        line = line.lower()
        reviews.append(line.split())
    print(reviews)


# Get a word from the user and determine the average rating of
# reviews that contain that word. reviews is a list of lists that
# contain the reviews.
# We assume the user types in a word with no spaces although the
# word can contain non letters, but no spaces.
def print_word_sentiment(reviews):
    word = input("Enter the word to search for: ")
    lowercase_word = word.lower()
    num_reviews = 0
    sum_of_reviews = 0
    for line in reviews:
        if lowercase_word in line:
            num_reviews += 1
            sum_of_reviews += int(line[0])
    if num_reviews == 0:
        print(word + " did not appear in any reviews")
    else:
        average = sum_of_reviews / num_reviews
        print(word + " appeared in " + str(num_reviews) +
        (" review." if num_reviews == 1 else " reviews.") +
            " Average review score = " + str(average))


# Ask the user for the name of a file with words and phrases.
# We assume one word per line in the file.
# For each word in the file, determine and show
# the average rating of reviews that contain the given word.
# We assume there won't be any spaces in the file.
def print_sentiments_from_file(reviews):
    file = input("Enter file name with words to check: ")
    file_open = open(file, "r")
    words = file_open.readlines()
    word_number = 0
    num_reviews = 0
    sum_of_reviews = 0
    for line in words:
        line = line.lower()
        word_number += 1
        print("Word number " + str(word_number) + " is  " + line +
         ". Results: ")
        for line in words:
            if line in reviews:
                num_reviews += 1
                sum_of_reviews += int(line[0])
        if num_reviews == 0:
            print(str(words) + " did not appear in any reviews")
        else:
            average = sum_of_reviews / num_reviews
            print(str(words)+ " appeared in " + str(num_reviews) +
                (" review." if num_reviews == 1 else " reviews.") +
                " Average review score = " + str(average))


# Print information about the longest review.
def print_longest_review(reviews):
    max_length = 0
    for line in reviews:
        if len(line) - 1 > max_length:
            max_length = len(line) - 1
    print("Longest review has " + str(max_length) + (" word."\
        if max_length == 1 else " words."))
    for line in reviews:
        if len(line) - 1 == max_length:
            print("Review as list: " + str(line[1:]))
            break


# Print information about the shortest review.
def print_shortest_review(reviews):
    min_length = len(reviews[0])
    for line in reviews:
        if len(line) - 1 < min_length:
            min_length = len(line) - 1
    print("Shortest review has " + str(min_length) + (" word."\
     if min_length == 1 else " words."))
    for line in reviews:
        if len(line) - 1 == min_length:
            print("Review as list: " + str(line[1:]))
            break


main()
