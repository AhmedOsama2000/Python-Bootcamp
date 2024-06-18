"""
    PING PONG Game using Python
    Author: Ahmed Osama
"""
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time
# from scoreboard import Scoreboard

screen = Screen()

# TODO 1. set up the game screen
screen.title("Ping Pong")
screen.setup(width=800, height=600)  # Set the width and height of the screen
screen.bgcolor("black")
screen.tracer(0)  # close the tracer until snake is created

# TODO 2. create the paddle / score / ball
ball = Ball()
r_paddle = Paddle(x_pos=350)
l_paddle = Paddle(x_pos=-350)
r_score = Scoreboard(x_pos=70, player="R")
l_score = Scoreboard(x_pos=-70, player="L")
screen.update()


# TODO 3. Move/Control the paddle
screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.move_up)
screen.onkeypress(key="Down", fun=r_paddle.move_down)
screen.onkeypress(key="w", fun=l_paddle.move_up)
screen.onkeypress(key="s", fun=l_paddle.move_down)


game_is_on = True


# TODO Game On!
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collistion with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collistion with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
    
    # Detect when ball misses with r_paddle
    if ball.xcor() > 390:
        ball.reset()
        l_score.update_score("L")
        time.sleep(0.3)

    if ball.xcor() < -390:
        ball.reset()
        r_score.update_score("R")
        time.sleep(0.3)

screen.exitonclick()