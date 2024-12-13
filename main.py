from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.colormode(255)
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')

left_paddle = Paddle('left')
right_paddle = Paddle('right')
ball = Ball()

screen.listen()
screen.onkey(key='Up', fun=right_paddle.go_up)
screen.onkey(key='Down', fun=right_paddle.go_down)

screen.onkey(key='w', fun=left_paddle.go_up)
screen.onkey(key='s', fun=left_paddle.go_down)

score_board = ScoreBoard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with a paddle
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50 or ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.bounce_x()

    # Detect right paddle miss
    if ball.xcor() > 380:
        score_board.l_point()
        ball.reset_position()

    # Detect lefi side paddle miss
    if ball.xcor() < -380:
        score_board.r_point()
        ball.reset_position()


screen.exitonclick()
