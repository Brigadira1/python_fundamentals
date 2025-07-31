from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.pensize(4)

for i in range(8):
    tim.home()
    tim.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    for j in range(i+3):
        tim.forward(100)
        tim.right(360/(i + 3))

screen.exitonclick()