import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def change_bg():
    if screen.bgcolor() == "black":
        screen.bgcolor("white")
    else:
        screen.bgcolor("black")


colors = ["white", "black"]
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
