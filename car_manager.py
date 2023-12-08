from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars=[]
        self.create()
        self.speed_increase=MOVE_INCREMENT
        self.move_dist=STARTING_MOVE_DISTANCE


    def create(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(1, 2)
        car.color(random.choice(COLORS))
        car.penup()
        car.goto(y=random.randint(-250, 250), x=300)
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(self.move_dist)

    def level_up(self):
        self.move_dist += self.speed_increase











