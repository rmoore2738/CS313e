# File: movies_2.py
# Description: A program uses dictionaries to find what words
# appear in reviews with good and bad ratings,
# as well as the length of good and bad reviews.
# Based on the Nifty Assignment:
# http://nifty.stanford.edu/2016/manley-urness-movie-review-sentiment/
# Assignment Number: 13
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
    print('Welcome to the movie sentiment program - Version 2.')
    file_name = input('Enter file name with reviews: ')
    get_dictionaries(file_name)
    words_dictionary, num_words_dictionary = get_dictionaries(file_name)
    choice = get_choice()
    while '1' <= choice <= '3':
        # Get the index of the function to call.
        if choice == '1':
            show_individual_stats(words_dictionary, 'a word')
        elif choice == '2':
            cutoff_stats(words_dictionary)
        else:
            show_individual_stats(num_words_dictionary, 'the number of words')
        choice = get_choice()


# Display the menu and get the users choice.
# Returns the user's choice as a String.
def get_choice():
    print()
    print('OPTIONS:')
    print('1. See statistics for a given word.')
    print('2. See all words that meet given cut-offs.')
    print('3. See statistics for reviews with a given number of words.')
    print('4. Or anything else to quit.')
    result = input('Please enter your choice: ')
    print()
    return result


# Given the file name, create and return two dictionaries.
# All strings in reviews are shifted to lower case.
#
# The first dictionary has keys that are words (any and all
# strings in the reviews) with the value a list of length 2.
# Both elements of the list are integers.
# The first element in the list is the number of reviews that
# contain the word (key) and the second is the sum of all the
# review scores that contain the word (key).
#
# The second dictionary has keys that are also strings representing
# the number of words (any and all strings) in a review.
# So for example '12' if the review has 12 words. The value
# for each key is also a list of length 2.Just like the first
# dictionary the first element in the list is the number of reviews
# that contain the word (key) and the second is the sum of all the
# review scores that contain the word (key).
def get_dictionaries(file_name):
    words = {}
    num_words = {}
    num_reviews = 0
    sum = 0
    count = 0
    file = open(file_name)
    infile = file.readlines()
    for line in infile:
        line = line.lower()
        split = line.split()
        for word in split:
            if len(word) > 0:
                count += len(line[1:])
            if len(word) > 0:
                if word in line:
                    num_reviews += 1
                    sum += int(line[0])
                else:
                    num_reviews = 1

        words[word] = [num_reviews, sum]
        num_words[word] = [num_reviews, sum]
    return words, num_words


# Ask the user for a key and show the statistics for that
# key if present in the given dictionary.
# The key entered by the user is converted to lower case.
def show_individual_stats(dictionary, prompt):
    word = input("Enter a word: ")
    lowercase_word = word.lower()
    num_reviews = get_dictionaries(words)
    average = get_dictionaries(words)
    if lowercase_word in words:
        print("Number of reviews = " + num_reviews)
        print("Average review score = " + average)
    else:
        print(input + " is not present in the dictionary.")


# Ask the user if they want words above or below a given cutoff.
# Get the cutoff for average review score and the minimum number
# of reviews the word must appear in.
# Display the results.
def cutoff_stats(words_dictionary):
    print("Enter the letter a to show scores above a given cutoff")
    cutoff =input("anything else to show scores below a given cutoff:")
    score = input("Enter the score cutoff between 0 and 4: ")
    min_reviews = input("Enter the minimum number of reviews required: ")


main()
