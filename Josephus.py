#  File: Josephus.py

#  Description:Assignment 19

#  Student Name: Rebecca Moore

#  Student UT EID: rrm2738

#  Partner Name: jacob Baack

#  Partner UT EID: jb72873

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 11/10/2020

#  Date Last Modified: 11/11/2020

import sys

class Link(object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

class CircularList(object):
    # Constructor
    def __init__ (self):
        self.first = None
        self.last = None
        self.links = 0

    # Insert an element (value) in the list
    def insert(self, data):
        new_link = Link(data)
        if self.first == None:
            self.last = new_link
        new_link.next = self.first
        self.last.next = new_link
        self.first = new_link
        self.links += 1

    # Find the link with the given data (value)
    def find(self, data):
        current = self.first
        if current == None:
            return None
        while current.data != data:
            if current.next == None:
                return None
            else:
                current = current.next
        return current

    # Delete a link with a given data (value)
    def delete(self, data):
        previous = self.first
        current = self.first
        if current == None:
            return None
        while current.data != data:
            if current.next == None:
                return None
            else:
                previous = current
                current = current.next
        if current == self.first:
            self.first = self.first.next
        else:
            previous.next = current.next
        return current

    # Delete the nth link starting from the Link start
    # Return the next link from the deleted Link
    def delete_after(self, start, n):
        previous = start
        current = start
        for i in range(n - 1):
            previous = current
            current = current.next
        if self.last == current:
            self.last = previous
        previous.next = current.next
        self.links -= 1
        print(current.data)
        return current.next

    # Return a string representation of a Circular List
    def __str__(self):
        current = self.first
        string = ''
        if current == None:
            return
        while current.next != self.first:
            string += str(current.data)
            string += '\n'
            current = current.next
        if current.next == self.first:
            string += str(current.data)
        return string 

def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int(line)

    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int(line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int(line)

    # your code
    circle = CircularList()
    for i in range(num_soldiers, 0, -1):
        circle.insert(i)
    start_count = circle.find(start_count)
    while circle.links > 0:
        start_count = circle.delete_after(start_count, elim_num)
    print(circle)

if __name__ == "__main__":
  main()
