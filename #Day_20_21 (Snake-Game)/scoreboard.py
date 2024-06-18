from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.write(f"score: {self.score}", align="center", font=('Arial', 20, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"score: {self.score}", align="center", font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game Over.", align="center", font=('Arial', 24, 'normal'))