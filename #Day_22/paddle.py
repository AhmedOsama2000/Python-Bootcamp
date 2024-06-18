from turtle import Turtle
MAX_Y_POS = 200
MIN_Y_POS = -200


class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_pos = x_pos
        self.goto(x=self.x_pos, y=0)
        self.shapesize(stretch_len= 1, stretch_wid= 5.0)

    def move_up(self):
        if self.ycor() < MAX_Y_POS:
            self.goto(x=self.x_pos, y=self.ycor() + 45)

    def move_down(self):
        if self.ycor() > MIN_Y_POS:
            self.goto(x=self.x_pos, y=self.ycor() - 45)

