from turtle import Turtle, Screen
from scoreboard import Scoreboard
from food import Food
from snake import Snake
import time

screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

sn = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(sn.up, "Up")
screen.onkey(sn.down, "Down")
screen.onkey(sn.left, "Left")
screen.onkey(sn.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    sn.move_snake()
    if sn.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh_food()

screen.exitonclick()
