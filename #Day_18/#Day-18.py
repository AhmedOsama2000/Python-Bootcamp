import turtle as t  # These are classes
from random import choice, randint

tim = t.Turtle()
colors = ["blue", "pink", "red", "peru", "orange red", "slate blue",
          "medium purple", "bisque", "dark violet"]

direction = [0, 90, 180, 270]

# Turtle shape and color
screen = t.Screen()
tim.shape("turtle")
tim.color("dark orchid")


# Turtle motion
def move_turtle(distance):
    tim.forward(distance)


# # TODO 1. Draw a square
# for _ in range(1,5):
#     move_turtle(50)
#     timmy_the_turtle.right(90)

# # TODO 2. Draw a dashed line
# tim.penup()
# tim.goto(-100, 0)
# tim.pendown()
# for _ in range(30):  # Loop to draw the dashed line; adjust range for longer or shorter lines
#     tim.forward(10)  # Draw a dash
#     tim.penup()  # Lift the pen to create a gap
#     tim.forward(10)  # Move forward without drawing
#     tim.pendown()  # Put the pen down to start the next dash

# # TODO: 3. Draw different shapes
#
# def turn_degree(n):
#     return 360 / n
#
# sides = 3
# for _ in range(7):
#     degree = turn_degree(sides)
#     tim.color(choice(colors))
#     print(degree)
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(degree)
#
#     sides += 1

# # TODO 4. Draw a different walk
# t.colormode(255)
# tim.pensize(10)
# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     return (r, g, b)
# # tim.pensize(5)
# for _ in range(100):
#     color = random_color()
#     tim.pencolor(color)
#     turn = choice(direction)
#     tim.setheading(turn)
#     tim.forward(30)


# # TODO 5. generate random RGB color
# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     return (r, g, b)

# TODO 6. Draw a spirograph
t.colormode(255)
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

# control speed
tim.speed("fastest")

for _ in range(80):
    tim.pencolor(random_color())
    tim.circle(100, 360, 100)
    tim.left(4.5)

# Turtle on screen
screen.exitonclick()
