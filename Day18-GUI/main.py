from turtle import Turtle, Screen

colorlist = ['red', 'blue', 'green', 'orange', 'purple', 'pink', 'brown', 'cyan']


def square(frank: Turtle):
    for i in range(4):
        frank.forward(100)
        frank.right(90)


def dashed(frank: Turtle):
    for _ in range(20):
        frank.forward(10)
        frank.penup()
        frank.forward(10)
        frank.pendown()


def shapes(frank: Turtle):
    for i in range(3, 11):
        for j in range(i):
            frank.color(colorlist[i-3])
            frank.forward(100)
            frank.right(360/i)


franklin = Turtle()
franklin.shape("turtle")
franklin.color("DodgerBlue")

shapes(franklin)
















screen = Screen()
screen.exitonclick()