import turtle

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]



def h_tree(order, center, size):
    draw_turtle(center, size)

    if order >= 0:
        end_point1, end_point2, end_point3, end_point4 = get_endpoints(center, size)

        h_tree(order - 1, (end_point1, end_point2), size / 2)
        h_tree(order - 1, (end_point1, end_point4), size / 2)
        h_tree(order - 1, (end_point3, end_point2), size / 2)
        h_tree(order - 1, (end_point3, end_point4), size / 2)

def draw_turtle(center, size):
    turtle.penup()
    turtle.goto(center)
    turtle.pendown()
    #This makes the right side of the H
    turtle.forward(size / 2)
    turtle.left(90)
    turtle.forward(size / 2)
    turtle.right(180)
    turtle.forward(size)

    turtle.penup()
    turtle.goto(center)
    turtle.pendown()
    # This makes the left side of the H
    turtle.right(90)
    turtle.forward(size / 2)
    turtle.right(90)
    turtle.forward(size / 2)
    turtle.right(180)
    turtle.forward(size)
    # Puts turtle back to start
    turtle.right(90)

def get_endpoints(center, size):
    end_point1 = center[0] + size / 2
    end_point2 = center[1] + size / 2
    end_point3 = center[0] - size / 2
    end_point4 = center[1] - size / 2

    return end_point1, end_point2, end_point3, end_point4

def draw_star(points, size, color, start):
    turtle.clear()
    angle = 360 / (points - 2)
    turtle.setheading(start)
    for i in range(points):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)
    turtle.update()
    return

def rotator(points, size, color, start):
    turtle.goto(0,0)
    draw_star(points, size, color, start)
    turtle.tracer(0)
    return rotator(points, size, color, start + 1)

def animate(x, y):
    rotator(5, 50, "black", 0)
    return

def main():

    # Q1 - call the recursive reverse_string() function
    print(reverse_string("desserts"))
    print(reverse_string("flow"))
    print(reverse_string("abcdefg"))

    # Q2 - call the recursive H-Tree fractal function
    turtle.speed(0)
    turtle.hideturtle()
    h_tree(2, [0, 0], 300)

    # Q3 - when the mouse is clicked in the turtle window,
    # call the animate() function to display a spinning star
    turtle.onscreenclick(animate)

    turtle.done()

if __name__ == '__main__':
    main()
