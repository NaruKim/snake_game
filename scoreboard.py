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
        file = open('data.txt', mode='r')
        self.high_score = int(file.read())
        file.close()
        self.update()


    def update(self):
        self.clear()
        self.write(f"Score = {self.score}   High Score = {self.high_score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open('data.txt', mode='w')
            file.write(f"{self.high_score}")
            file.close()
        self.score = 0
        self.update()
