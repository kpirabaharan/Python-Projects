from turtle import Turtle, Screen
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake_list = []
x_pos = 0
for sk in range(3):
    new_cell = Turtle("square")
    new_cell.color("white")
    new_cell.penup()
    new_cell.goto(x=x_pos, y=0)
    x_pos -= 20
    snake_list.append(new_cell)

screen.update()

game_on = True
while game_on:
    screen.update()
    sleep(0.1)
    for sk in snake_list:
        sk.forward(20)










screen.exitonclick()
