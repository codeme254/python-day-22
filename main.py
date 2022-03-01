from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong game by Dennis Otwoma")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

game_is_on = True
while game_is_on:
    time.sleep(0.0586)
    screen.update()
    ball.move()
    
    # detecting collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detecting collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() <- 320:
        ball.paddle_bounce()
    
    # detect when either paddle misses the ball
    if ball.xcor() > 380 :
        ball.reset_ball()
        scoreboard.l_point()
    
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()
    
screen.exitonclick()