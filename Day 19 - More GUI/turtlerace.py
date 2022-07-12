from turtle import Turtle, Screen
import random


colorList = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-75, -45, -15, 15, 45, 75]

screen = Screen()
screen.setup(width=1800, height=800)

bet = screen.textinput(title="Make your bet!", prompt="Which colored turtle will win the race?: ")
all_turtles = []

for index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colorList[index])
    new_turtle.penup()
    new_turtle.goto(x=-890, y=y_positions[index])
    all_turtles.append(new_turtle)

if bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 880:
            race_on = False
            win = turtle.pencolor()
            if win == bet:
                print("You win!")
            else:
                print("You lose :(")
        dist = random.randint(0, 10)
        turtle.forward(dist)


screen.exitonclick()
