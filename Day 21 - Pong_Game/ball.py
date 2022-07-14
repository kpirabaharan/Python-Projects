from turtle import Turtle

BALL_SPEED = 2
INIT_HEADING = 70


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.shapesize(1.2, 1.2)
        self.setheading(INIT_HEADING)

    def move(self):
        self.forward(BALL_SPEED)

    def bounce_wall(self):
        self.setheading(self.heading()*-1)

    def bounce_paddle(self):
        self.setheading((self.heading() + 90))

    def missed_paddle(self):
        pass
