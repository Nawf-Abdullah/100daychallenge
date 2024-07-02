from turtle import Turtle,Screen

tim = Turtle()

for i in range(3,11):
	for j in range(i):
		tim.forward(100)
		tim.right(360/i)



screen = Screen()
screen.endonclick()