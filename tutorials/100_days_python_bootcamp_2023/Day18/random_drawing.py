import random
from turtle import Turtle, Screen

timi = Turtle()
timi.pensize(15)
screen = Screen()
screen.colormode(255)

random_movements = [timi.forward, timi.right, timi.left]

for _ in range(200):
    timi.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    random.choice(random_movements)(random.randint(50, 80))

screen.exitonclick()
