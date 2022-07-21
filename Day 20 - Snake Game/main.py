from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from time import sleep
import math

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

score = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "Down")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "Left")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "Right")
screen.onkey(snake.right, "d")

game_on = True
while game_on:
    snake.move()

    # Detect Collision with Food
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.increase_size()
        score.increment()

    # Detect Collision with Wall
    if abs(snake.head.xcor()) >= 300 or abs(snake.head.ycor()) >= 300:
        snake.reset()
        score.reset()

    # Detect Collision with Tails
    for sk in snake.snake_list[1:]:
        if snake.head.distance(sk) < 10:
            snake.reset()
            score.reset()

    screen.update()
    sleep(0.1)

screen.exitonclick()
