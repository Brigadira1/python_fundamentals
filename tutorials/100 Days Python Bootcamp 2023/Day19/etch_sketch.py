from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()


def go_forwards():
    tim.forward(10)


def go_backwards():
    tim.back(10)


def angle_left():
    tim.left(5)


def angle_right():
    tim.right(5)


screen.onkey(key="Left", fun=go_backwards)
screen.onkey(key="Right", fun=go_forwards)
screen.onkey(key="Up", fun=angle_left)
screen.onkey(key="Down", fun=angle_right)
screen.exitonclick()
