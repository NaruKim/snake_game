import turtle
from snake import Snake
import time

screen=turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Naru's snake game")
screen.tracer(0)

snake=Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while True:
    screen.update()
    time.sleep(0.05)

    snake.move()

screen.exitonclick()