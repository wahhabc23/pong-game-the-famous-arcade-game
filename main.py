from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
scoreborad = Scoreboard()
screen.bgcolor('black')
screen.setup(height=600, width=800)
screen.listen()
screen.tracer(0)
screen.title("Ping-Pong")
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
game_on = True
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")
screen.update()
timespeed = 0.1
while game_on:
    time.sleep(timespeed)
    screen.update()
    ball.move()
    if ball.xcor() > 380:
        ball.reset_position()
        scoreborad.l_score += 1
        scoreborad.update()
        timespeed = 0.1
    if ball.xcor() < -380:
        ball.reset_position()
        scoreborad.r_score += 1
        scoreborad.update()
        timespeed = 0.1
    elif ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_top_bottom()
    for paddle in r_paddle.paddles:
        if paddle.distance(ball) < 30:
            ball.bounce_left_right()
            timespeed -= 0.005
            break
    for paddle in l_paddle.paddles:
        if paddle.distance(ball) < 30:
            ball.bounce_left_right()
            timespeed -= 0.005
            break
screen.exitonclick()
