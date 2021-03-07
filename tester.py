import strings as s
from random import randint, choice, seed
from string import ascii_letters

string_methods = (s.num_chars_same, s.stretch, s.length_of_matching_suffix)

def main():
    test_methods = (compare_mike, random_test, select_test)

    user_input = -1
    while user_input == -1:
        user_input = get_input()
    test_methods[user_input]()

    done_user_input = input("\nTests done. Enter y to do more tests: ").lower()
    return done_user_input == "y"


def get_input():
    user_input = -1
    choices = ("m", "r", "s")
    choice = input("Enter one of the following\n    - m to Mike's same example\n" +
                "    - r to run random tests\n" +
                "    - s to select a certain method\n\n" +
                "Your choice: ")

    if len(choice) > 0:
        try:
            user_input = choices.index(choice[0])
        except:
            print("User choice not found. Please try again!\n\n")
    else:
        print("Empty input. Please try again!\n\n")

    return user_input


def compare_mike():
    mike_examples = ((2, "catch", "cots", "catch", "cat chaser", "dog",
                        3, "dog", 1, "cat", "doggo", "dog", "doggo"),
                    (1, "catch", "batches", "dog", 0, "cats", "dogs"),
                    (3, "dog", "cats", " ", "cats", "Hamilton", "ham stands!", "Dogs!", 4, "1234",
                        2, "!!!", 1, "cats", " ", "cats", "maniacs", "dog", "cat and dog",
                        "Last words are the same", "Words are the same"))
    example_num = -1
    while example_num == -1:
        try:
            example_num = eval(input("Enter the example number (1, 2, or 3): "))
            if example_num < 1 or example_num > 3:
                print("Value not in range. Try again please!")
                example_num = -1
        except:
            print("Not a valid number. Try again please!")
    input_strings = mike_examples[example_num - 1]
    calls_per_func = input_strings[0]
    index = 1
    print(f"----- EXAMPLE {example_num} -----")
    for func in string_methods:
        for i in range(calls_per_func):
            s1 = input_strings[index]
            s2 = input_strings[index + 1]
            print_outcome(s1, s2, func)
            index += 2


def random_test():
    num = -1
    seed_val = -1
    while num == -1:
        try:
            num = eval(input("Enter the number of random tests: "))
        except:
            print("Not a valid number. Try again please!")
    seed_val = (input("Enter a # for the seed for the test: "))
    seed(seed_val)

    for i in range(num):
        func_num = randint(0, 2)
        func = string_methods[func_num]
        s1 = "".join(choice(ascii_letters) for j in range(randint(0, 15)))
        if func_num == 0:
            s2 = ""
            for char in s1:
                s2 += char if randint(0, 100) < 35 else choice(ascii_letters)
        elif func_num == 1:
            s2 = randint(0, 5)
        else:
            if randint(0, 100) < 8:
                s2 = s1
            else:
                first_s2 = "".join(choice(ascii_letters) for j in range(randint(0, 50)))
                s2 = first_s2 + s1[randint(0, len(s1) + 1):]
        print_outcome(s1, s2, func)


def select_test():
    string_methods = (s.num_chars_same, s.stretch, s.length_of_matching_suffix)
    num = -1
    while num == -1:
        try:
            num = eval(input("Enter the number of select tests: "))
        except:
            print("Not a valid number. Try again please!")
    for i in range(num):
        func_choice = -1
        while func_choice == -1:
            try:
                print("\nEnter a function choice number:\n"
                    + "     - 0 for num_chars_same")
                print("     - 1 for stretch")
                print("     - 2 for length_of_matching_suffix")
                func_choice = eval(input("Enter your function number choice: "))
                if func_choice < 0 or func_choice > 2:
                    print("Number is not in range. Try again please!")
                    func_choice = -1
            except:
                print("Not a valid number. Try again please!")
        func = string_methods[func_choice]
        print("--------------------\nTrial #:", i + 1)
        print("Function name:", func.__name__)
        s1 = input("First parameter: ")
        s2 = input("Second parameter: ")
        if func_choice == 1:
            s2 = eval(s2)
        print("Return value:", func(s1, s2))
        print("--------------------")


def print_outcome(s1, s2, func):
    print("--------------------\nFunction name:", func.__name__)
    print("Parameter 1:", s1)
    print("Parameter 2:", s2)
    print("Return value:", func(s1, s2))
    print("--------------------")


keep_running = True
while keep_running:
    keep_running = main()
