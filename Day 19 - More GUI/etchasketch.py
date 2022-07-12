from turtle import Turtle, Screen

t = Turtle()
s = Screen()


def moveForward():
    t.forward(10)


def moveBackward():
    t.backward(10)


def rotateLeft():
    t.left(15)


def rotateRight():
    t.right(15)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


s.listen()
s.onkey(moveForward, "w")
s.onkey(moveBackward, "s")
s.onkey(rotateLeft, "a")
s.onkey(rotateRight, "d")
s.onkey(clear, "c")

s.exitonclick()