from turtle import Turtle

UP = 90
DOWN = 270
PACE = 15


class Paddle(Turtle):

    def __init__(self, xpos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(UP)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.goto(xpos, 0)

    def move_up(self):
        self.setheading(UP)
        self.forward(PACE)

    def move_down(self):
        self.setheading(DOWN)
        self.forward(PACE)
