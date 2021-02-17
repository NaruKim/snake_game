from turtle import Turtle
ALIGNMENT='center'
FONT=('courier', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.color('white')

        self.score=0
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.clear()
        self.write("Game Over", align=ALIGNMENT, font=FONT)


    # def score(self):
    #     self.penup()
    #     self.hideturtle()
    #     self.goto(0, 265)
    #     self.color('white')
    #     self.write(f"Score = {eat}", False, align="center", font=('Arial', 20, 'normal'))