from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, x_pos, player):
        super().__init__()
        self.score = 0
        self.x_pos = x_pos
        self.player = player
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=self.x_pos, y=250)
        self.write(f"{self.player} : {self.score}", align="center", font=('Arial', 30, 'normal'))

    def update_score(self, player):
        self.score += 1
        self.clear()
        self.write(f"{player} : {self.score}", align="center", font=('Arial', 30, 'normal'))

