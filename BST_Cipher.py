#  File: BST_Cipher.py

#  Description: assignment 21

#  Student Name: Rebecca Moore

#  Student UT EID: rrm2738

#  Partner Name: Jacob Baack

#  Partner UT EID: jb72873

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 11/15/2020

#  Date Last Modified: 11/16/2020
import sys


class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree(object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
    def __init__(self, encrypt_str):
        self.root = Node(encrypt_str[0])
        for i in range(1, len(encrypt_str)):
            if (97 <= ord(encrypt_str[i]) <= 122) or ord(encrypt_str[i]) == 32:
                self.insert(encrypt_str[i])

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
    def insert(self, ch):
        new_node = Node(ch)
        if self.search(ch) == '':
            parent = self.root
            current = self.root
            while current != None:
                parent = current
                if ord(ch) < ord(current.data):
                    current = current.lchild
                else:
                    current = current.rchild
            if ord(ch) < ord(parent.data):
                parent.lchild = new_node
            else:
                parent.rchild = new_node

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
    def search(self, ch):
        arrows = []
        current = self.root
        if ch == current.data:
            # root of tree
            return '*'
        while current != None:
            if ord(ch) == ord(current.data):
                # string with series of < and >
                return arrows
            elif ord(ch) < ord(current.data):
                arrows.append('<')
                current = current.lchild
            else:
                arrows.append('>')
                current = current.rchild
        # doesn't exist so return blank string
        return ''

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
    def traverse(self, st):
        current = self.root
        for char in st:
            if char == '*':
                current = self.root
            elif char == '>':
                current = current.rchild
            elif char == '<':
                current = current.lchild
        if current.data == None:
            return ''
        else:
            return current.data

  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
    def encrypt(self, st):
        st = st.lower()
        encrypted = ''
        for char in st[:-1]:
            string = ''
            encrypted = encrypted + string.join(self.search(char))
            if string.join(self.search(char)) != '':
                encrypted = encrypted + '!'
        string = ''
        encrypted = encrypted + string.join(self.search(st[-1]))

        return encrypted

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
    def decrypt(self, st):
        st = st.split('!')
        decrypted = ''
        for item in st:
            decrypted = decrypted + self.traverse(item)
        return decrypted

def main():
  # read encrypt string
    line = sys.stdin.readline()
    encrypt_str = line.strip()

  # create a Tree object
    the_tree = Tree (encrypt_str)

  # read string to be encrypted
    line = sys.stdin.readline()
    str_to_encode = line.strip()

  # print the encryption
    print(the_tree.encrypt(str_to_encode))

  # read the string to be decrypted
    line = sys.stdin.readline()
    str_to_decode = line.strip()

  # print the decryption
    print(the_tree.decrypt(str_to_decode))

if __name__ == "__main__":
    main()
