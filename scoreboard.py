from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.score(0)

    def score(self, score):
        self.clear()
        self.write(f"Score: {score}", False, align="center", font=("Arial", 25, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 25, "normal"))
