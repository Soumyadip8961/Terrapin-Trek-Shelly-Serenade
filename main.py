import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
STARTING_POSITION = (0, -280)

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")



game_is_on = True
count=0
while game_is_on:
    num=random.randint(1,6)
    if num == 1:
        car_manager.create()

    time.sleep(0.1)
    car_manager.move()
    screen.update()

    ### Detecting collison with Buses
    for car in car_manager.cars:
        if player.distance(car) < 25:
            game_is_on=False
            scoreboard.game_over()

    ### Updating Level
    if player.ycor() >= 280:
        player.goto(STARTING_POSITION)
        car_manager.level_up()
        scoreboard.keep_score()



screen.exitonclick()
