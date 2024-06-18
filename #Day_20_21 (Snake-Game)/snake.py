from turtle import Turtle
MOVE_DISTANCE = 20


class Snake():
    def __init__(self):
        self.size = 3
        self.snake = []
        self.x_axis = 20
        """
            you can initialize also a function not just
            an attribute
        """
        self.create_body()
        self.head = self.snake[0]

    def create_body(self):
        for _ in range(self.size):
            tim = Turtle()
            tim.penup()
            tim.color("white")
            tim.shape("square")
            tim.goto(x=self.x_axis,y=0)
            self.snake.append(tim)
            self.x_axis -= 20

    def extend_body(self):
        tim = Turtle()
        tim.penup()
        tim.color("white")
        tim.shape("square")
        tim.goto(self.snake[-1].position())
        self.snake.append(tim)

    def move(self):
        snake_len = len(self.snake)
        for seg_num in range(snake_len-1, 0, -1):
            new_x = self.snake[seg_num-1].xcor()
            new_y = self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == 0:
            self.head.left(90)
        elif self.head.heading() == 180:
            self.head.right(90)

    def down(self):
        if self.head.heading() == 0:
            self.head.right(90)
        elif self.head.heading() == 180:
            self.head.left(90)


    def right(self):
        if self.head.heading() == 90:
            self.head.right(90)
        elif self.head.heading() == 270:
            self.head.left(90)


    def left(self):
        if self.snake[0].heading() == 90:
            self.snake[0].left(90)
        elif self.snake[0].heading() == 270:
            self.snake[0].right(90)