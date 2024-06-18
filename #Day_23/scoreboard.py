from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(x=-200, y=250)
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def update_score(self):
        self.level += 1
        self.clear()
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over.", align="center", font=FONT)


