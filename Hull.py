
#  File: Hull.py

#  Description: Assignment 6

#  Student Name: Rebecca Moore

#  Student UT EID: rrm2738

#  Partner Name: Jacob Baack

#  Partner UT EID: jb72873

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 10/29/20

#  Date Last Modified: 10/30/20

import sys

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
    det = (q.x * r.y) + (p.x * q.y) + (p.y * r.x) - (p.y * q.x) - (q.y *   r.x) - (p.x * r.y)
    return det

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
    upper_hull = []
    lower_hull = []
    sorted_points.sort(key = lambda point: (point.x, point.y))

    for i in range(2):
        upper_hull.append(sorted_points[i])
    end = len(sorted_points)
    for j in range(2, end):
        upper_hull.append(sorted_points[j])
        while len(upper_hull)>= 3 and det(upper_hull[-3], upper_hull[-2], upper_hull[-1]) >= 0:
            upper_hull.remove(upper_hull[-2])

    lower_hull = [sorted_points[-1],sorted_points[-2]]
    for j in range(end-3, -1,-1):
        lower_hull.append(sorted_points[j])
        while len(lower_hull)>= 3 and det(lower_hull[-3], lower_hull[-2], lower_hull[-1]) >= 0:
            #print(lower_hull[-2])
            lower_hull.remove(lower_hull[-2])
    lower_hull.remove(sorted_points[0])
    lower_hull.remove(sorted_points[-1])


    return upper_hull + lower_hull

# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
    num = 0.0
    positives = 0
    negatives = 0
    for i in range(0, (len(convex_poly) - 1)):
        positives += convex_poly[i].x * convex_poly[i + 1].y
        negatives -= convex_poly[i].y * convex_poly[i + 1].x
    area = abs(positives + negatives) * 0.5
    return area

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases

  return "all test cases passed"


def main():
  # create an empty list of Point objects
  points_list = []

  # read number of points
  line = sys.stdin.readline()
  line = line.strip()
  num_points = int (line)

  # read data from standard input
  for i in range (num_points):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    x = int (line[0])
    y = int (line[1])
    points_list.append (Point (x, y))

  # sort the list according to x-coordinates
  sorted_points = sorted(points_list)

  # print the sorted list of Point objects
  #for p in sorted_points:
    #print (str(p))


  # get the convex hull
  hull = convex_hull(sorted_points)
  # run your test cases

  # print your results to standard output
  print("Convex Hull")
  for i in hull:
    print(str(i))

  # get the area of the convex hull
  convex_poly = convex_hull(sorted_points)
  convex_poly.append(sorted_points[0])
  area = area_poly(convex_poly)
  # print the area of the convex hull
  print("Area of Convex Hull = ", area)

if __name__ == "__main__":
  main()
