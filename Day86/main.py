from turtle import  *
from paddle import Paddle
from ball import Ball
from time import sleep
from block import Block
from scoreboard import ScoreBoard

screen = Screen()
screen.title("Break Out")
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)

ball = Ball()

paddle = Paddle((0,-250))

score = ScoreBoard(300)
def check_the_blast():
	for i in bricks:
		if ball.distance(i)<60:
			i.hideturtle()
			bricks.remove(i)
			ball.bounce_y()
			score.point()


screen.update()
screen.listen()

life = 3
bricks = []
rows = [-300,-200,-100,0,100,200,300]
columns = [250,200,150,100,50]
colors = ['red','blue','green','purple','yellow','orange','red']
for n,i in enumerate(rows):
	print(n)
	colored = colors[n]
	for j in columns:
		block = Block((i,j))
		block.color(colored)
		bricks.append(block)
	

screen.onkey(key="Right",fun=paddle.right)
screen.onkey(key="Left",fun=paddle.left)
game_is_on = True
sleep_time = 0.1
while game_is_on:
	screen.update()
	sleep(0.1)
	ball.move()
	if ball.ycor()>280:
		ball.bounce_y()
	if ball.distance(paddle)<50 and ball.ycor()<-240:
		sleep_time *= 0.9
		ball.bounce_y()
	if ball.xcor()>320 or ball.xcor()<-320:
		ball.bounce_x()
	if ball.ycor()<-280:
		ball.home()
		life-=1
		print(life)
		if life == 0:
			print("Game Over")
			game_is_on = False
	check_the_blast()


screen.exitonclick()