from turtle import Turtle
file_name = "data.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        with open(file_name) as score_file:
            self.highest_score = int(score_file.read())
        self.write(f"score: {self.score} Highest Score: {self.highest_score}", align="center", font=('Arial', 20, 'normal'))

    def update_score(self):
        self.clear()
        self.write(f"score: {self.score} Highest Score: {self.highest_score}", align="center", font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open(file_name, "w") as score_file:
                score_file.write(str(self.highest_score))
        self.score = 0
        self.update_score()