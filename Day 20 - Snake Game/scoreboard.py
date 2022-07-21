from turtle import Turtle

FONT_SCORE = ("Arial", 20, "normal")
FONT_GAMEOVER = ("TIMES NEW ROMAN", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as hsfile:
            self.highscore = int(hsfile.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", align="center", font=FONT_SCORE)

    def increment(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as hsfile:
                hsfile.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()
