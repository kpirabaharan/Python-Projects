from turtle import Turtle

FONT_SCORE = ("Arial", 20, "normal")
FONT_GAMEOVER = ("TIMES NEW ROMAN", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write(arg=f"Score: {self.score}", align="center", font=FONT_SCORE)

    def increment(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=FONT_SCORE)

    def game_over(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.write(arg=f"GAME OVER", align="center", font=FONT_GAMEOVER)
