from turtle import Turtle, xcor

UP = 90
MOVE_DISTANCE = 20


class Paddle():
    def __init__(self, x_cor, y_cor=0):
        self.paddles = []
        self.create_paddles(x_cor, y_cor)

    def create_paddles(self, x_cor, y_cor):
        for n in range(5):
            paddle = Turtle('square')
            paddle.color('white')
            paddle.penup()
            paddle.goto(x=x_cor, y=y_cor)
            y_cor += 20
            paddle.setheading(UP)
            self.paddles.append(paddle)

    def move_up(self):
        for paddle in self.paddles:
            paddle.forward(MOVE_DISTANCE)

    def move_down(self):
        for paddle in self.paddles:
            paddle.backward(MOVE_DISTANCE)
