def main():
    print('Welcome to the movie sentiment program - Version 2.')
    file_name = input('Enter file name with reviews: ')
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
    return words, num_words


# Ask the user for a key and show the statistics for that
# key if present in the given dictionary.
# The key entered by the user is converted to lower case.
def show_individual_stats(dictionary, prompt):
    print('Not completed') # 303e students, delete this line when you implement this function.


# Ask the user if the want words above or below a given cutoff.
# Get the cutoff for average review score and the minimum number
# of reviews the word must appear in.
# Display the results.
def cutoff_stats(words_dictionary):
        print('Not completed') # 303e students, delete this line when you implement this function.


main()
