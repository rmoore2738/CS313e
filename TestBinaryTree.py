#  File: TestBinaryTree.py

#  Description: assignment 22

#  Student Name: Rebecca Moore

#  Student UT EID: rrm2738

#  Partner Name: Jacob Baack

#  Partner UT EID: jb72873

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 11/18/2020

#  Date Last Modified: 11/20/2020

import sys


class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            while current != None:
                parent = current
                if data < current.data:
                    current = current.lchild
                else:
                    current = current.rchild
            if data < parent.data:
                parent.lchild = new_node
            else:
                parent.rchild = new_node

    def in_order(self, aNode):
        if aNode != None:
            self.in_order(aNode.lchild)
            print(aNode.data)
            self.in_order(aNode.rchild)

    # Returns true if two binary trees are similar
    def is_similar(self, pNode):
        if self.root == None and pNode == None:
            return True
        elif pNode != None and self.root != None:
            tree1 = Tree()
            tree2 = Tree()
            tree1.root = self.root.lchild
            tree2.root = self.root.rchild
            return self.root.data == pNode.data and tree1.is_similar(pNode.lchild) and tree2.is_similar(pNode.rchild)
        return False

    # Prints out all nodes at the given level
    def print_level(self, level):
        if self.root == None:
            return None
        if level == 1 and self.root != None:
            print(self.root.data, end=' ')
        if self.root != None:
            level1 = Tree()
            level2 = Tree()
            level1.root = self.root.lchild
            level2.root = self.root.rchild
            level1.print_level(level - 1)
            level2.print_level(level - 1)

    # Returns the height of the tree
    def get_height(self):
        if self.root == None:
            return 0
        if self.root != None and self.root.lchild == None and self.root.rchild == None:
            return 0
        elif self.root != None:
            height_l = Tree()
            height_r = Tree()
            height_l.root = self.root.lchild
            height_r.root = self.root.rchild
            lheight = height_l.get_height()
            rheight = height_r.get_height()
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes(self):
        num_of_nodes = 1
        if self.root == None:
            return 0
        if self.root != None and self.root.lchild == None and self.root.rchild == None:
            return 1
        elif self.root != None:
            left = Tree()
            right = Tree()
            left.root = self.root.lchild
            right.root = self.root.rchild
            num_of_nodes += left.num_nodes() + right.num_nodes()
            return num_of_nodes

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list (map (int, line)) 	# converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list (map (int, line)) 	# converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list (map (int, line)) 	# converts elements into ints

    tree1 = Tree()
    for i in tree1_input:
        tree1.insert(i)

    tree2 = Tree()
    for i in tree2_input:
        tree2.insert(i)

    tree3 = Tree()
    for i in tree3_input:
        tree3.insert(i)

    #Test is_similar for every combination of trees
    print(tree1.is_similar(tree2.root))
    print(tree1.is_similar(tree3.root))

    print(tree2.is_similar(tree1.root))
    print(tree2.is_similar(tree3.root))

    print(tree3.is_similar(tree1.root))
    print(tree3.is_similar(tree2.root))

    #Lets assume that tree1 and tree2 are different
    #print different levels
    tree1.print_level(2) #assumed to print out on one line
    tree2.print_level(2) #assumed to print out on one line

    tree1.print_level(5) #assumed to print out on one line
    tree2.print_level(5) #assumed to print out on one line

    #print heights
    print(tree1.get_height())
    print(tree2.get_height())

    #print num_nodes of each tree
    print(tree1.num_nodes())
    print(tree2.num_nodes())
    print(tree3.num_nodes())

if __name__ == "__main__":
  main()
