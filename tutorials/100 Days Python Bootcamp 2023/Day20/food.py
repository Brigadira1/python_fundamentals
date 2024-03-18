import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        self.x_axis = random.randint(-480, 480)
        self.y_axis = random.randint(-380, 380)
        self.goto(self.x_axis, self.y_axis)
