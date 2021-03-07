inputs = 3.0000, 12.0000
area = inputs[0]
materials = inputs[1]

sides = materials / 4

if sides >= area:
    print("Diablo is happy!")
else:
    print("Need more material")




    import math
#
# Complete the 'is_rectangle' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts ARRAY of INTEGER TUPLES points as parameter.
#

def is_rectangle(points):
    dist_1 = abs((math.sqrt(points[1][0] - points[0][0])**2) + ((math.sqrt(points[1][1])- points[0][1])**2))
    dist_2 = abs((math.sqrt(points[2][0] - points[1][0])**2) + ((math.sqrt(points[2][1])- points[1][1])**2))
    dist_3 = abs((math.sqrt(points[3][0] - points[2][0])**2) + ((math.sqrt(points[3][1])- points[2][1])**2))
    dist_4 = abs((math.sqrt(points[4][0] - points[3][0])**2) + ((math.sqrt(points[4][1])- points[3][1])**2))
    print(dist_1, dist_2, dist_4)
    #if dist_1 == dist_2 + dist_3 or dist_1 == dist_3 + dist_4 or dist_1 == dist_2 + dist_4:
        #print('y')
    #if dist_2 == dist_1 + dist_3 or dist_2 == dist_1 + dist_4 or dist_2 == dist_1 + dist_4:
       # print('y')
    #if dist_3 == dist_1 + dist_2 or dist_3 == dist_1 + dist_4 or dist_3 == dist_2 + dist_4:
      #  print('y')
    #if dist_4 == dist_1 + dist_2 or dist_4 == dist_2 + dist_3 or dist_4 == dist_1 + dist_3:
      #  print('y')




      print(ids)
    for i in ids:
        print(i)
        count = ids.count(i)
        new_count = ids.count(i + 1)
        if count < new_count:
            lst.append(i)
        elif count > new_count:
            i += 1
    return lst



     for letter in letters:
        for word in words:
            for i in range(len(word)):
                if letter in word and word[i] in letters:
                    count += 1
                    break

    return count
