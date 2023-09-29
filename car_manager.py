from turtle import Turtle
from random import randrange, choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.speed('fastest')
        self.color(choice(COLORS))
        start_coors = (-600, randrange(-250, 250, 10))
        self.goto(start_coors)

    def go_left(self, level):
        new_x = self.xcor() - level * MOVE_INCREMENT - STARTING_MOVE_DISTANCE
        self.goto(new_x, self.ycor())