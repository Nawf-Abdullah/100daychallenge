import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()
carr = CarManager()

screen.listen()
screen.onkey(key="Up",fun=turtle.up)

cars = []

game_is_on = True
while game_is_on:
	time.sleep(0.1)
	carr.create_cars()
	carr.move()
	screen.update()
	for car in carr.all_cars:
		if turtle.distance(car)<20:
			game_is_on = False
			scoreboard.game_over()

	if turtle.ycor()>=280:
		scoreboard.update()
		turtle.goto((0, -280))


screen.exitonclick()