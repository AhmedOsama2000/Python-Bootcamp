"""
    Snake Game using Python
    Author: Ahmed Osama
"""
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

# TODO 1. set up the game screen
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)  # close the tracer until snake is created

# TODO 2. Create snake body
food = Food()
scoreboard = Scoreboard()
snake = Snake()
screen.update()

# TODO 3. Move the snake
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

game_is_on = True
while game_is_on:
    x_dist = snake.head.xcor()
    y_dist = snake.head.ycor()
    screen.update()
    time.sleep(0.05)
    snake.move()

    # TODO 4. Detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_body()
        scoreboard.update_score()

    # TODO 5. Detect collistion with the wall
    if x_dist > 265 or x_dist < -265 or y_dist > 265 or y_dist < -265:
        game_is_on = False
        scoreboard.game_over()

    # TODO 6. Detect collision with tail
    for seg in snake.snake[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
