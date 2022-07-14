from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_right = Paddle(350)
paddle_left = Paddle(-350)
ball = Ball()
screen.update()

game_on = True

while game_on:

    screen.listen()
    screen.onkeypress(paddle_left.move_up, "w")
    screen.onkey(paddle_left.move_down, "s")
    screen.onkey(paddle_right.move_up, "Up")
    screen.onkey(paddle_right.move_down, "Down")

    ball.move()

    # Detect Collision with wall
    if abs(ball.ycor()) > 285:
        ball.bounce_wall()

    # Detect Collision with paddles
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or\
            ball.distance(paddle_left) < 50 and ball.xcor() < - 320:
        ball.bounce_paddle()
    elif ball.distance(paddle_right) > 50 and ball.xcor() > 320 or\
            ball.distance(paddle_left) > 50 and ball.xcor() < - 320:
        ball.missed_paddle()

    print(f"Right: {ball.distance(paddle_right)}")
    print(f"Left: {ball.distance(paddle_left)}")

    sleep(0.01)
    screen.update()




screen.exitonclick()
