import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed(0)
for i in range(int(360 / 5)):
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    tim.color(r, g, b)
    tim.left(5)
    tim.circle(200)

screen.exitonclick()
