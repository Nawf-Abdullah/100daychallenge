import turtle as t
import random

screen = t.Screen()
screen.setup(width=500,height=400)
user_guess= screen.textinput(title = "Guess",prompt="which one will win?")
colors = ['red','orange','yellow','green','blue','violet']
objects = [] 
x_ = -100
for i in colors:
	objects.append(t.Turtle(shape='turtle'))

#print(objects)
for i in objects:
	i.penup()
	i.color(colors[objects.index(i)])
	i.goto(x=-230,y=x_)
	x_+=30
is_on = True

while is_on:
	random.choice(objects).forward(random.randint(1,10))
	for turtle in objects:
		if turtle.xcor()>230:
			is_on = False
			wining_color = turtle.pencolor()
			if wining_color.lower() == user_guess.lower():
				print(f"You won the race!The {wining_color} is the winner")

			else:
				print(f"You lost the race!The {wining_color} is the winner")

screen.exitonclick()