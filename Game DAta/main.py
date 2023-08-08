import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


colors = ["white", "black", "tan", "bisque", "darkkhaki"]
bg = random.choice(colors)
screen = Screen()
screen.bgcolor(bg)
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_profile = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


def change_bg():
    another_color = random.choice(colors)
    if screen.bgcolor() == another_color:
        screen.bgcolor(random.choice(colors))
    else:
        screen.bgcolor(another_color)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_profile.create_cars()
    car_profile.move_em()

    # Detects collision
    for car in car_profile.cars:
        if car.distance(player) < 19:
            game_is_on = False
            score.game_over()

# Checking if player reaches finish line
    if player.ycor() > 275:
        change_bg()
        score.score_user()
        player.checkout()
        car_profile.increase_speed()

screen.exitonclick()
