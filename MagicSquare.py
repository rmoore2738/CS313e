#  File: MagicSquare.py

#  Description:Assignment 13

#  Student Name:Jacob Baack

#  Student UT EID:Jb72873

#  Partner Name:Rebecca Moore

#  Partner UT EID:rrm2738

#  Course Name: CS 313E

#  Unique Number:50845

#  Date Created:10/17/20

#  Date Last Modified:10/19/20
import math


# checks if a 1-D list if converted to a 2-D list is magic
# a is 1-D list of integers
# returns True if a is magic and False otherwise
def is_magic(a):
    magic_square = one_dim_to_two_dim(a)

    n = len(magic_square)
    magic_constant = n *(n*n + 1) / 2


    # checks rows
    for row in magic_square:
        if magic_constant - sum(row[:-1]) != row[-1]:
            return False

    # checks columns
    for col in zip(*magic_square):
        if magic_constant - sum(col[:-1]) != col[-1]:
            return False

    # checks diagonal
    diagonal = []
    diagonal2 = []

    for i in range(len(magic_square)):
        diagonal.append(magic_square[i][i])
    for i in range(len(magic_square)):
        diagonal2.append(magic_square[i][n - 1 - i])

    if magic_constant - sum(diagonal[:-1]) != diagonal[-1] or magic_constant - sum(diagonal2[:-1]) != diagonal2[-1]:
        return False

    return True


# this function recursively permutes all magic squares
# a is 1-D list of integers and idx is an index in a
# it stores all 1-D lists that are magic in the list all_magic
def permute(a, idx, all_magic):
    hi = len(a)
    if idx == hi and is_magic(a):
        # print all magic squares
        print(a)
    else:
        for i in range(idx, hi):
            a[idx], a[i] = a[i], a[idx]
            permute(a, idx + 1, all_magic)
            a[i], a[idx] = a[idx], a[i]


def one_dim_to_two_dim(the_list):
    k = int(math.sqrt(len(the_list)))
    grid = [[the_list[i + j] for j in range(k)] for i in range(0, k ** 2, k)]
    return grid


def main():
    # read the dimension of the magic square
    in_file = open('magic.in', 'r')
    line = in_file.readline()
    line = line.strip()
    n = int(line)
    in_file.close()

    # create an empty list for all magic squares
    all_magic = []
    # create the 1-D list that has the numbers 1 through n^2
    the_list = [i + 1 for i in range(n ** 2)]
    # generate all magic squares using permutation
    permute(the_list, 0, all_magic)


if __name__ == "__main__":
    main()
