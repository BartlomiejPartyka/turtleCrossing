from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.speed('fastest')
        self.goto(STARTING_POSITION)
        self.seth(90)
        self.current_level = 0

    def go_up(self):
        self.fd(MOVE_DISTANCE)

    def finished(self):
        """Returns true if player crossed the finish line, otherwise returns false"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def reset(self):
        self.goto(STARTING_POSITION)
        self.current_level += 1
