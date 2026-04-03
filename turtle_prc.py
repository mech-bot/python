# import turtle
# t = turtle.Turtle()
# t.penup()

# for i in range(2):
#     t.forward(20)
#     t.pendown()
#     t.circle(50)
#     t.write(str(i))
#     t.penup()
# turtle.done()


# import turtle

# count = 0
# turtle.speed(10)

# while(count < 180):

#     turtle.forward(2)

#     turtle.right(1)

#     count = count + 1

# turtle.speed(1)

# turtle.right(45)

# turtle.forward(300)

# turtle.left(90)

# turtle.back(150)

# turtle.right(45)

# turtle.back(250)

# turtle.done()


# # for angle in range(0, 360, 20):

# #     setheading(angle)

# #     forward(100)

# #     write(str(angle) + '*')

# #     backward(100)
import turtle
t1 = turtle.Turtle()
t2 = turtle.Turtle()
for i in range(360):
    t1.speed(10)
    t2.speed(10)
    t1.color("red")
    t2.color("blue")
    t1.forward(1)
    t1.left(1)
    t2.forward(2)
    t2.left(1)
# t1.color("red")
# t2.color("blue")
# t1.circle(50)
# t2.circle(100)
turtle.done()