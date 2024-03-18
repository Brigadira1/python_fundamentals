from turtle import Turtle, Screen
import time


class Snake:
    SNAKE_COORDINATES: list[tuple: float] = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]
    MOVEMENT_FACTOR = 20
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0

    def __init__(self):
        self.snake: list[Turtle] = []
        self.create_snake()
        self.head: Turtle = self.snake[0]

    def create_snake(self) -> None:
        for coordinates in range(len(Snake.SNAKE_COORDINATES)):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(Snake.SNAKE_COORDINATES[coordinates])
            self.snake.append(segment)

    def move_snake(self) -> None:
        for seg in range(len(self.snake) - 1, 0, -1):
            x_coord = self.snake[seg - 1].xcor()
            y_coord = self.snake[seg - 1].ycor()
            self.snake[seg].goto(x_coord, y_coord)
        self.head.forward(Snake.MOVEMENT_FACTOR)

    def up(self):
        if self.head.heading() != Snake.DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != Snake.UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != Snake.RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != Snake.LEFT:
            self.head.setheading(0)
