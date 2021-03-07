import csv
array = []
with open("office.txt") as file:
reader = csv.reader(file, delimiter=' ')
for row in reader:
array.append(row)


i = 0
n = len(array)

def room_details(size, no_of_employee, employee_data):
   w = size[0]
   h = size[1]
   # creating building matrix where all square places are initialised with 0 which means they are empty
   building = [[0 for i in range(h)] for j in range(w)]

   # each employee's room size is initially zero
   employee_room_size = [0 for i in range(no_of_employee)]

   for index in range(no_of_employee):
       name = employee_data[index][0]
       x1 = employee_data[index][1]
       y1 = employee_data[index][2]
       x2 = employee_data[index][3]
       y2 = employee_data[index][4]

       for x in range(x1, x2):
           for y in range(y1, y2):
               building[x][y] += 1

   Total = w*h
   Unallocated = 0
   Contested = 0

   for x in range(w):
       for y in range(h):
           if building[x][y] == 0:
               Unallocated += 1
           elif building[x][y] > 1:
               Contested += 1
           else:
               # search if the given square area is allocated to which employee
               for employee in range(no_of_employee):
                   x1 = employee_data[employee][1]
                   y1 = employee_data[employee][2]
                   x2 = employee_data[employee][3]
                   y2 = employee_data[employee][4]
                   if x1 <= x and x < x2 and y1 <= y and y < y2 :        #if in the range of the employee there is a place which is is occupied by only one employee then it belongs to the employee
                       employee_room_size[employee] += 1

   print("Total", Total)
   print("Unallocated", Unallocated)
   print("Contested", Contested)
   for index in range(no_of_employee):
       print(employee_data[index][0], employee_room_size[index])
   print()

while i < n:
   building_size = [int(array[i][0]), int(array[i][1])]
   i += 1
   no_of_employee = int(array[i][0])
   i += 1

   employee_data = []
   for x in range(no_of_employee):
       employee_data.append([array[i][0], int(array[i][1]), int(array[i][2]), int(array[i][3]), int(array[i][4])])
       i += 1

   room_details(building_size, no_of_employee, employee_data)
