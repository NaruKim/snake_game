from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def add_segment(self, position):
        t = Turtle('square')
        t.color('white')
        t.penup()
        t.hideturtle()
        t.goto(position)
        t.showturtle()
        self.segments.append(t)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x, y)
        self.segments[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].seth(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].seth(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].seth(RIGHT)