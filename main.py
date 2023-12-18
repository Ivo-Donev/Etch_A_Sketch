from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
tim.pensize(6)


def change_color():
    r = random.random()
    b = random.random()
    g = random.random()
    tim.color(r, g, b)


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.forward(-10)


def rotate_left():
    tim.left(10)


def rotate_right():
    tim.left(-10)


def clear_screen():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()


def draw():
    screen.listen()
    screen.onkeypress(key="w", fun=move_forward)
    screen.onkeypress(key="s", fun=move_backwards)
    screen.onkeypress(key="a", fun=rotate_left)
    screen.onkeypress(key="d", fun=rotate_right)
    screen.onkey(key="q", fun=clear_screen)


def change_colors():
    screen.listen()
    screen.onkey(key="c", fun=change_color)


draw()
change_colors()
screen.exitonclick()
