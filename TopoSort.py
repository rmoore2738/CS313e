#  File: TopoSort.py

#  Description:Assignment 24

#  Student Name:Jacob Baack

#  Student UT EID:Jb72873

#  Partner Name:Rebecca Moore

#  Partner UT EID:rrm2738

#  Course Name: CS 313E

#  Unique Number:50845

#  Date Created:11/28/2020

#  Date Last Modified:11/30/2020


class Stack (object):
    def __init__ (self):
        self.stack = []

    # add an item to the top of the stack
    def push (self, item):
        self.stack.append ( item )

    # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()

    # check what item is on top of the stack without removing it
    def peek (self):
        return self.stack[len(self.stack) - 1]

    # check if a stack is empty
    def is_empty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size (self):
        return (len(self.stack))

class Queue (object):
    def __init__ (self):
        self.queue = []

    def enqueue (self, item):
        self.queue.append (item)

    def dequeue (self):
        return (self.queue.pop(0))

    def is_empty(self):
        return (len(self.queue) == 0)
    def size (self):
        return len (self.queue)

class Vertex (object):
    def __init__ (self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.label)

class Graph(object):
    def __init__(self):
        self.vertices = []
        self.adjMat = []

    # check if a vertex is already in the graph
    def has_vertex(self, label):
        nVert = len(self.vertices)
        for i in range(nVert):
            if (label == (self.vertices[i]).get_label()):
                return True
        return False

    # given the label get the index of a vertex
    def get_index(self, label):
        nVert = len(self.vertices)
        for i in range(nVert):
            if (label == (self.vertices[i]).get_label()):
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        if (self.has_vertex(label)):
            return

        # add vertex to the list of vertices
        self.vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        nVert = len(self.vertices)
        for i in range(nVert - 1):
            (self.adjMat[i]).append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(nVert):
            new_row.append(0)
        self.adjMat.append(new_row)


    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.vertices[i]).was_visited()):
                return i
        return -1

    # do a depth first search in a graph
    def dfs(self, v):
        # create the Stack
        theStack = Stack()

        # mark the vertex v as visited and push it on the Stack
        (self.vertices[v]).visited = True
        print(self.vertices[v])
        theStack.push(v)

        # visit all the other vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.vertices[u]).visited = True
                print(self.vertices[u])
                theStack.push(u)

        # the stack is empty, let us rest the flags
        nVert = len(self.vertices)
        for i in range(nVert):
            (self.vertices[i]).visited = False

    # do the breadth first search in a graph
    def bfs(self, v):
        # create the Queue
        queue = Queue()

        # mark the vertex v as visited and push it on the Stack
        (self.vertices[v]).visited = True
        print(self.vertices[v])
        queue.enqueue(v)

        # visit all the other vertices according to depth
        while (not queue.is_empty()):
            del_vertex = queue.dequeue()
            # get an adjacent unvisited vertex
            adj = self.get_adj_unvisited_vertex(del_vertex)
            while (adj != -1):
                (self.vertices[adj]).visited = True
                print(self.vertices[adj])
                queue.enqueue(adj)
                adj = self.get_adj_unvisited_vertex(del_vertex)

        # the stack is empty, let us rest the flags
        nVert = len(self.vertices)
        for i in range(nVert):
            (self.vertices[i]).visited = False

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def get_edge_weight (self, from_vertex_label, to_vertex_label):
        weight = self.adjMat[self.get_index(from_vertex_label)][self.get_index(to_vertex_label)]
        if weight == 0:
            return -1
        return weight

    # get a list of immediate neighbors that you can go to from a vertex
    # return empty list if there are none
    def get_neighbors (self, vertex_label):
        neighbors = []
        v = self.get_index(vertex_label)
        for i in range(len(self.vertices)):
            if (self.adjMat[v][i] > 0):
                neighbors.append(self.vertices[i])
        return neighbors

    # get a copy of the list of vertices
    def get_vertices (self):
        vert_list = []
        for i in self.vertices:
            vert_list.append(i)
        return vert_list

    # delete an edge from the adjacency matrix
    def delete_edge (self, from_vertex_label, to_vertex_label):
        start = self.get_index(from_vertex_label)
        finish = self.get_index(to_vertex_label)
        #Set edge to 0 meaning no edge
        self.adjMat[start][finish] = 0

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex (self, vertex_label):
        v = self.get_index(vertex_label)
        nVert = len(self.vertices)

        # Delete column
        for i in range(nVert):
            for j in range(v, nVert - 1):
                self.adjMat[i][j] = self.adjMat[i][j + 1]
            self.adjMat[i].pop()

        # Delete row
        self.adjMat.pop(v)

        #Delete vertex
        for vertex in self.vertices:
            if vertex.label == vertex_label:
                self.vertices.remove(vertex)

    # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result
    def has_cycle (self):
        nVert = len(self.vertices)
        for i in range(nVert):
            if self.has_cycle_helper(None, self.vertices[i]):
                return True

            #reset visited flags to false
            for i in range(nVert):
                self.vertices[i].visited = False
        return False

    #Helper function that checks all neighbors for each vertex for a cycle
    def has_cycle_helper(self, previous, vertex):
        #If vertex has already been visited then cycle is complete
        if vertex.visited == True:
            return True

        vertex.visited = True
        neighbors = self.get_neighbors(vertex.label)

        #Don't travel back to vertex visited just before
        if previous in neighbors:
            neighbors.remove(previous)
        #If there are no other neighbors then there is no cycle
        if len(neighbors) == 0:
            return False

        for i in neighbors:
            return self.has_cycle_helper(vertex,i)


    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort (self):
        topo_visit = []
        dellist = []
        while len(self.vertices) != 0:
            idx = 0
            while idx < len(self.vertices):
                has_visit = False
                vertex = self.vertices[idx].label
                for i in range(len(self.vertices)):
                    if self.adjMat[i][idx] == 1:
                        has_visit = True
                        break
                if has_visit:
                    idx += 1
                else:
                    topo_visit.append(vertex)
                    dellist.append(vertex)
                    idx += 1
            while len(dellist) != 0:
                self.delete_vertex(dellist[0])
                dellist.pop(0)
        return topo_visit


def main():
  # create a Graph object
  theGraph = Graph()

  # open file for reading
  file = open("topo.txt", "r")

  # read the Vertices
  numVertices = int((file.readline()).strip())

  for i in range(numVertices):
      letter = (file.readline()).strip()
      theGraph.add_vertex(letter)

  # read the edges
  numEdges = int((file.readline()).strip())

  for i in range(numEdges):
      edge = (file.readline()).strip()
      edge = edge.split()
      start = theGraph.get_index(edge[0])
      finish = theGraph.get_index(edge[1])

      theGraph.add_directed_edge(start, finish)

  # test if a directed graph has a cycle
  if (theGraph.has_cycle()):
      print("The Graph has a cycle.")
  else:
      print("The Graph does not have a cycle.")

  # test topological sort
  if (not theGraph.has_cycle()):
      vertex_list = theGraph.toposort()
      print("\nList of vertices after toposort")
      print(vertex_list)

if __name__ == "__main__":
    main()
