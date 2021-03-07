#  File: Reducible.py

#  Description:Assignment 16

#  Student Name: Rebecca Moore

#  Student UT EID: rrm2738

#  Partner Name: jacob Baack

#  Partner UT EID: jb72873

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 10/28/30

#  Date Last Modified: 10/30/20
# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime(n):
    if (n == 1):
        return False
    limit = int(n ** 0.5) + 1
    div = 2
    while (div < limit):
        if (n % div == 0):
            return False
        div += 1
    return True


# Input: takes as input a string in lower case and the size
#        of the hash table
# Output: returns the index the string will hash into
def hash_word(s, size):
    hash_idx = 0
    for j in range(len(s)):
        letter = ord(s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx


# Input: takes as input a string in lower case and the constant
#        for double hashing
# Output: returns the step size for that string
def step_size(s, const):
    key = 0
    for j in range(len(s) -1, -1, -1):
        letter = ord(s[j]) - 96
        key += letter * (26 ** j)
    return const - (key % const)


# Input: takes as input a string and a hash table
# Output: no output; the function enters the string in the hash table,
#         it resolves collisions by double hashing
def insert_word(s, hash_table):
    size = len(hash_table)
    idx = hash_word(s, size)
    step = step_size(s, 13)
    while hash_table[idx] != '':
        idx = (idx + step) % size
    hash_table[idx] = s


# Input: takes as input a string and a hash table
# Output: returns True if the string is in the hash table
#         and False otherwise
def find_word(s, hash_table):
    size = len(hash_table)
    idx = hash_word(s, size)
    step = step_size(s, 13)
    while hash_table[idx] != '':
        if hash_table[idx] == s:
            return True
        else:
            idx = (idx + step) % size
    return False


# Input: string s, a hash table, and a hash_memo
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo
#         and returns True and False otherwise
def is_reducible(s, hash_table, hash_memo):
    if len(s) == 1 and s in ['a', 'i', 'o']:
        return True
    elif len(s) == 1:
        return False

    if find_word(s, hash_memo):
        return True
    elif not find_word(s, hash_table):
        return False

    for i in range (len(s)):
        new_s = s[:i] + s[i + 1:]
        if is_reducible(new_s, hash_table, hash_memo):
            insert_word (new_s, hash_memo)
            return True
    return False


def main():
    # create an empty word_list
    word_list = []
    # open the file words.txt
    file = open("words.txt", "r")
    # read words from words.txt and append to word_list
    for word in file:
        word = word.strip('\n')
        word_list.append(word)
    # close file words.txt
    file.close()
    # find length of word_list
    length_list = len(word_list)
    # determine prime number N that is greater than twice
    # the length of the word_list
    prime_number = length_list * 2
    while not is_prime(prime_number):
        prime_number += 1
    # create an empty hash_list
    hash_list = []
    # populate the hash_list with N blank strings
    for i in range(0,prime_number):
        hash_list.append("")
    # hash each word in word_list into hash_list
    # for collisions use double hashing
    for word in word_list:
        insert_word(word, hash_list)
    # create an empty hash_memo of size M
    # we do not know a priori how many words will be reducible
    # let us assume it is 10 percent (fairly safe) of the words
    # then M is a prime number that is slightly greater than
    # 0.2 * size of word_list
    hash_memo = []
    m = int(0.2 * len(word_list))
    while not is_prime(m):
        m += 1
    # populate the hash_memo with M blank strings
    for i in range(m):
        hash_memo.append('')
    # create an empty list reducible_words
    reducible_words = []
    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    for word in word_list:
        if len(word) == 10:
            reducible_word = is_reducible(word, hash_list, hash_memo)
            if reducible_word:
                reducible_words.append(word)
    # find words of length 10 in reducible_words
    # print the words of length 10 in alphabetical order
    # one word per line
    for i in reducible_words:
        print(i)


if __name__ == "__main__":
    main()
