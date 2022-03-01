from turtle import Turtle, Screen

etch = Turtle()
screen = Screen()
screen.listen()


def move_forwards():
    etch.forward(10)


def move_backwards():
    etch.backward(10)


def turn_left():
    etch.left(10)


def turn_right():
    etch.right(10)


def reset():
    etch.reset()


screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)

screen.onkey(key="c", fun=reset)

screen.exitonclick()