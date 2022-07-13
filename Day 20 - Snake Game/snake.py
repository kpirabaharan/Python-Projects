from turtle import Turtle, Screen

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        print("Snake Created")
        self.len = 3
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_cell(position)

    def right(self):
        if self.head.heading() != LEFT:
            self.snake_list[0].setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.snake_list[0].setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.snake_list[0].setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.snake_list[0].setheading(DOWN)

    def move(self):
        for sk in range(len(self.snake_list) - 1, 0, -1):
            x_cord = self.snake_list[sk - 1].xcor()
            y_cord = self.snake_list[sk - 1].ycor()
            self.snake_list[sk].goto(x_cord, y_cord)
        self.snake_list[0].forward(MOVE_DISTANCE)

    def increase_size(self):
        self.add_cell(self.snake_list[-1].position())

    def add_cell(self, position):
        new_cell = Turtle("square")
        new_cell.color("white")
        new_cell.penup()
        new_cell.goto(position)
        self.snake_list.append(new_cell)

