from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_pos = 0
        self.y_pos = 0
        self.x_move = 2
        self.y_move = 2
        self.move_speed = 0.01


    def move(self):
        self.x_pos = self.xcor() + self.x_move
        self.y_pos = self.ycor() + self.y_move
        self.goto(self.x_pos, self.y_pos)


    def bounce_y(self):
        self.y_move *= -1 


    def bounce_x(self):
        self.x_move *= -1
        if self.move_speed > 0.003:
            self.move_speed *= 0.9
        

    def reset(self):
        self.goto(0,0)
        self.move_speed = 0.01
        self.bounce_x()



        