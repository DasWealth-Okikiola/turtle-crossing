from turtle import Turtle
FONT = ("Courier", 24, "normal")
Alignment = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("green")
        self.penup()
        self.hideturtle()
        self.goto(x=-280, y=250)
        self.prin()

    def prin(self):
        self.write(f"Level:{self.score}", align=Alignment, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(x=0, y=260)
        self.write(f"Game Over", align="center", font=FONT)
        self.goto(x=-280, y=-250)
        self.write(f"Score is:{self.score}", align="left", font=FONT)

    def score_user(self):
        self.score += 1
        self.clear()
        self.prin()
