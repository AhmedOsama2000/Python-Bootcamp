from turtle import Turtle
from random import choice
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.current_speed = STARTING_MOVE_DISTANCE
        self.cars_list = []

    def create_cars(self):
        random_chance = random.randint(1, 6)
        # decrease the frequency the cars have been created
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_len= 2.0,stretch_wid = 1.0)
            new_car.penup()
            new_car.goto(x=300, y= random.randint(-280, 280))
            self.cars_list.append(new_car)


    def move_car(self):
        for _ in self.cars_list:
            new_x = _.xcor() - self.current_speed
            _.goto(x=new_x, y=_.ycor()) 

    def increase_speed(self):
        self.current_speed += MOVE_INCREMENT
