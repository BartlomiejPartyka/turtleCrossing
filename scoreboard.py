from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1

    def update_score(self):
        self.clear()
        self.goto(-100, 260)
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def add_score(self):
        self.score += 1

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT)
