#  File: Radix.py

#  Description: Assignment 17

#  Student Name: Rebecca Moore

#  Student UT EID: rrm2738

#  Partner Name: Jacob Baack

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 50485

#  Date Created: 11/01/2020

#  Date Last Modified:

import sys

class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    # check if the queue if empty
    def is_empty(self):
        return len(self.queue) == 0

    # return the size of the queue
    def size(self):
        return len(self.queue)

    def max_length(a):
        # find the longest word
        max_len = 0
        for i in a:
            if len(i) > max_len:
                max_len = len(i)
        return max_len

    # add 0 to make them all the same length
    def padded_list(a, max_len):
        padded_list = []
        for i in a:
            new_list = ['0' * (max_len - len(i))]
            padded_list.append(i + ''.join(new_list))
        return padded_list

    # Input: a is a list of strings that have either lower case
    #        letters or digits
    # Output: returns a sorted list of strings
    def radix_sort(a, index):
    dict = {}
    dict['0'] = 0
    dict['1'] = 1
    dict['2'] = 2
    dict['3'] = 3
    dict['4'] = 4
    dict['5'] = 5
    dict['6'] = 6
    dict['7'] = 7
    dict['8'] = 8


def main():
    # read the number of words in file
    line = sys.stdin.readline()
    line = line.strip()
    num_words = int (line)

    # create a word list
    word_list = []
    for i in range (num_words):
        line = sys.stdin.readline()
        word = line.strip()
        word_list.append (word)

    print(word_list)
    # use radix sort to sort the word_list
    sorted_list = Queue.radix_sort(word_list, 0)

    index = 0
    for word in sorted_list:
        sorted_list[index]= re.sub('[0]', '', word)
        index += 1



    # print the sorted_list
    print(sorted_list)

if __name__ == "__main__":
  main()
