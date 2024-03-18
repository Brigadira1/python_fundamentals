import random
from turtle import Turtle, Screen


def prepare_turtels(turtles, rainbow_colors):
    for turtle_index in range(len(rainbow_colors)):
        current_turtle = Turtle(shape="turtle")
        current_turtle.color(rainbow_colors[turtle_index])
        current_turtle.penup()
        current_turtle.goto(-240, -100 + turtle_index * 40)
        turtles[rainbow_colors[turtle_index]] = current_turtle


def compete(turtles, user_bet):
    current_pos = -240
    while current_pos < 230:
        for color, turtle in turtles.items():
            rand = random.randint(1, 10)
            turtle.forward(rand)
            current_pos, _ = turtle.pos()
            if current_pos >= 230:
                break

    if color == user_bet:
        print(f"The winner is {color}. You win!!!")
    else:
        print(f"The winner is {color}. You lose - more luck next time.")


def main():
    rainbow_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtles = {}
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

    prepare_turtels(turtles, rainbow_colors)
    compete(turtles, user_bet)
    screen.exitonclick()


if __name__ == "__main__":
    main()
