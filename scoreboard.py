FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.score_count = 0
        self.penup()
        self.goto(x=-200, y=250)
        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.score_count}", False, align="center", font=('Courier', 24, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", False, align="center", font=('Courier', 24, 'bold'))

    def keep_score(self):
        self.clear()
        self.score_count += 1
        self.update_score()


