from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# NOTE about functions:
"""
    when we call a function we should use the () because it's responsible for trigger the function,
    but when we pass a function as an argument, we don't write the ()
    Higher Order Functions: a functions that take another functions as parameters
"""
def move_forward():
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()