import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


# TODO 1.Create classes
player = Player()
car = CarManager()
scoreboard = Scoreboard()

# TODO 2. Move the turtle
screen.listen()
screen.onkeypress(key="Up", fun=player.move_turtle)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_car()

    # Detect collistion with the car
    for a_car in car.cars_list:
        if player.distance(a_car) < 30:
            game_is_on = False
            scoreboard.game_over()

    # Detect when the turtle reaches the other side
    if player.ycor() > 280:
        scoreboard.update_score()
        car.increase_speed()
        player.reset_player()


screen.exitonclick()