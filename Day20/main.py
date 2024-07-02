from turtle import *
from snake import Snake
from time import sleep
from food import Food
from scoreboard import Score 

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snake = Snake()
food = Food()
game_is_on = True 
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


while game_is_on:
	screen.update()
	sleep(0.1)
	snake.move()
	if snake.segments[0].distance(food)<15:
		food.refresh()
		score.point()
		snake.extend()

	if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
		game_is_on = False
		print("Game Over")
		score.game_over()

	for segment in snake.segments[1:]:
		if snake.segments[0].distance(segment)<10:
			game_is_on = False
			score.game_over()


screen.exitonclick()