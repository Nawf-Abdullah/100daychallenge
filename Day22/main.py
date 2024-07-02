from turtle import  *
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import ScoreBoard

screen = Screen()
screen.title("Ping Pong")
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)

ball = Ball()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.update()
screen.listen()

screen.onkey(key="Up",fun=r_paddle.up)
screen.onkey(key="Down",fun=r_paddle.down)
r_score = ScoreBoard(deg=100)


screen.onkey(key='w',fun=l_paddle.up)
screen.onkey(key="s",fun=l_paddle.down)
l_score = ScoreBoard(deg=-100)
sleep_time = 0.1
game_is_on = True

while game_is_on:
	screen.update()
	sleep(sleep_time)
	ball.move()

	if ball.ycor()>280 or ball.ycor()<-280:
		ball.bounce_y()

	if ball.distance(r_paddle)<50 and ball.xcor()>330 or ball.distance(l_paddle)<50 and ball.xcor()<-330:
		sleep_time *= 0.9
		ball.bounce_x()

	if ball.xcor()>400:
		l_score.point()
		sleep(1)
		ball.home()
		ball.bounce_x()
		

	if ball.xcor()<-400:
		r_score.point()
		sleep(1)
		ball.home()
		ball.bounce_x()
		



screen.exitonclick()