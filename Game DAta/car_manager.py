from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "dodgerblue", "purple", "magenta", "grey"]
MOVE_INCREMENT = 1.5


class CarManager:

    def __init__(self):
        self.cars = []
        self.Move_distance = 5

    def create_cars(self):
        unit = random.randint(1, 6)
        if unit == 1:
            car = Turtle("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            x = 300
            y = random.randint(-250, 260)
            car.penup()
            car.goto(x=x, y=y)
            self.cars.append(car)

    def move_em(self):
        for car in self.cars:
            car.backward(self.Move_distance)

    def increase_speed(self):
        self.Move_distance *= MOVE_INCREMENT
        self.move_em()
