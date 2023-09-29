import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randrange

player = Player()
scoreboard = Scoreboard()

cars = []
for c in range(randrange(1, 10)):
    cars.append(CarManager())
    cars[c].goto(randrange(-300, 300, 10), cars[c].ycor())

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkeypress(player.go_up, 'Up')
iteration = 0

game_is_on = True
while game_is_on:
    iteration += 1
    time.sleep(0.1)
    screen.update()
    num_of_cars = len(cars)

    scoreboard.update_score()

    if iteration % 4 == 0:
        cars.append(CarManager())
        cars[-1].goto(340, randrange(-250, 250, 20))

    for c in range(len(cars)):
        cars[c].go_left(player.current_level)

    if player.finished():
        player.reset()
        scoreboard.add_score()

    for c in range(len(cars)):
        if player.distance(cars[c].xcor(), cars[c].ycor()) < 30:
            game_is_on = False
            scoreboard.game_over()
            screen.update()

screen.exitonclick()

