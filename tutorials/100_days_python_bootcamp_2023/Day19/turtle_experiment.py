from turtle import Turtle, Screen

snake = []
t = Turtle("square")
t.color("white")
t.penup()

t1 = Turtle("square")
t1.color("white")
t1.penup()
t1.goto(-20, 0)

t2 = Turtle("square")
t2.color("white")
t2.penup()
t2.goto(-40, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=1000)

screen.exitonclick()