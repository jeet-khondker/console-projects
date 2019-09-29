# Flag Of Bangladesh

# Importing Turtle Module
import turtle

# Setting Up The Length, Height & The Angle
length = 200
angle = 90
height = 100

# Creating A Flag Object
flag = turtle.Turtle()

# Making A Border Color Of Black And A Background Color Of Green
border_color = "#000"
background_color = "green"
flag.color(border_color, background_color)

# Filling Up The Flag
flag.begin_fill()

# Creating Sides
for sides in range(2):
    flag.forward(length)
    flag.right(angle)
    flag.forward(height)
    flag.right(angle)

# Finishing The Flag
flag.end_fill()

# Taking Out The Pen From The Canvas
flag.penup()

# Fixing The Position For The Middle Circle
flag.forward(100)
flag.right(90)
flag.forward(50)

# Putting The Pen Down In The Canvas
flag.pendown()

# Creating The Circle
circle_radius = 40
circle_background_color = "red"
flag.dot(circle_radius, circle_background_color)

# Wrapping It Up
turtle.done()








