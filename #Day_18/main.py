### This code will not work in repl.it as there is no access to the colorgram package here.###
## We talk about this in the video tutorials##
import colorgram  # It's used to extract color from images
import turtle as t
from random import choice

# Our Turtle
tim = t.Turtle()
screen = t.Screen()
t.colormode(255)

x_length = 10
y_length = 10
space = 50
dot_size = 20

rgb_colors = []
# extracting 30 colors from image
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

# Set the initial position of the turtle
tim.penup()
tim.goto(-250, -250)  # Start from the left side of the screen
tim.pendown()
tim.speed("fast")

for y in range(y_length):
    tim.penup()
    tim.setpos(-250, -250 + y*space)
    for x in range(x_length):
        tim.pendown()
        tim.dot(dot_size, choice(rgb_colors))
        tim.penup()
        tim.forward(50)

tim.hideturtle()
# Turtle on screen
screen.exitonclick()
