from turtle import Turtle, Screen
from random import randint

colors = ["green", "red", "purple", "orange", "yellow", "blue"]


# create turtles
red_tim = Turtle(shape="turtle")
green_tim = Turtle(shape="turtle")
yellow_tim = Turtle(shape="turtle")
blue_tim = Turtle(shape="turtle")
purple_tim = Turtle(shape="turtle")
orange_tim = Turtle(shape="turtle")

turtels_list = [red_tim, green_tim, yellow_tim, blue_tim, purple_tim, orange_tim]

screen = Screen()
screen.setup(width=500, height=400)  # determine the resolution of the screen
user_turtle = screen.textinput(title="Choose your pet", prompt="Which one will win the race, pick a color: ")

index = 0

for turtle in turtels_list:
    turtle.color(colors[index])
    turtle.penup()
    index += 1

is_race_on = False
if user_turtle:
    is_race_on = True

red_tim.goto(-230, -100)
orange_tim.goto(-230, -50)
purple_tim.goto(-230, 0)
blue_tim.goto(-230, 50)
yellow_tim.goto(-230, 100)
green_tim.goto(-230, 150)

while is_race_on:
    for turtle in turtels_list:

        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_turtle:
                print(f"You've won, the {winning_turtle} is the winner!")
            else:
                print(f"You've lost, the {winning_turtle} is the winner!")

            is_race_on = False

        else:
            turtle.forward(randint(1,10))

screen.exitonclick()