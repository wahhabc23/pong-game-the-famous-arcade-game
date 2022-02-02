from turtle import Turtle
from random import randint
MOVE_DISTANCE = 20


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_top_bottom(self):
        self.y_move *= -1

    def bounce_left_right(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_left_right()
