# File: strings.py
# Description: Implements three functions that use
# and manipulate strings.
# Assignment Number: 8
#
# Name: Rebecca Moore
# EID: rrm2738
# Email: rebeccamoore32@utexas.edu
# Grader: Skyler
#
# On my honor, Rebecca Moore, this programming assignment is my own work
# and I have not provided this code to any other students.


# s1 and s2 shall be strings. This function returns the number of chars
# in s1 and s2 that match based on position.
def num_chars_same(s1, s2):
    count = 0
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            count += 1
    return count


# s1 shall be a string and num shall be an integer >= 0.
# The function returns a stretched version of s1 with each
# character repeated. The number of repitions is num times
# the position of that character if we were to use 1 based indexing.
def stretch(s1, num):
    result = ''
    for i in range(len(s1)):
        num_reps = num * (i + 1)
        for j in range(num_reps):
            result = result + s1[i]
    return result


# s1 and s2 shall be strings.
# The method returns the number of characters at the end of
# s1 and s2 that match. Stops at the first mistmatched character.
def length_of_matching_suffix(s1, s2):
    count = 0
    index = -1
    while abs(index) <= min(len(s1), len(s2)) and s1[index] == s2[index]:
        count += 1
        index -= 1
    return count


# Run tests on the functions. Ask the user for input.
def main():
    num_tests = eval(input('Enter the number of tests per method: '))
    print('Testing num chars same function.')
    test_functions_with_two_string_parameters(num_tests, num_chars_same)
    print('Testing stretch function.')
    stretch_tests(num_tests)
    print('Testing length of matching suffix function.')
    test_functions_with_two_string_parameters(num_tests,
                                              length_of_matching_suffix)


# Test the functions that take 2 String parameters.
def test_functions_with_two_string_parameters(num_tests, function_to_test):
    for i in range(0, num_tests):
        s1 = input('Enter first string: ')
        s2 = input('Enter second string: ')
        print(function_to_test(s1, s2))
    print()


# Test the stretch function.
def stretch_tests(num_tests):
    for i in range(0, num_tests):
        s1 = input('Enter the string: ')
        num = eval(input('Enter number of times to repeat: '))
        print(stretch(s1, num))
    print()


main()
