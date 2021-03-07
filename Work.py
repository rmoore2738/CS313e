
#  File: Work.py

#  Description: assignment 7

#  Student Name: Rebecca Moore

#  Student UT EID: rrm2738

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 10/29/20

#  Date Last Modified: 10/30/20

import sys

import time

# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
    sum = v
    power = 1
    while (v//k**power) >0:
        r = (v//k**power)
        sum = sum + r
        power = power + 1
    return sum


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
    for v in range(n, n + 1):
        if sum_series(v, k) >= n:
            return v
    return 0


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
    counter = n
    min = 0
    while min <= n and counter >= 1:
        counter = counter / 2
        lines = sum_series(min,k)
        if lines == n:
            return round(min)
        if lines < n:
            min += counter
        else:
            min -= counter


    return round((min))


def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()
