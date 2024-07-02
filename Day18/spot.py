from colorgram import *
import turtle as t
import random 

tim = t.Turtle()

screen = t.Screen()
screen.colormode(255)

'''
rgb_colors = []
img = "images/spot.jpg"
colors = extract(img,10)
print(colors)
for color in colors:
	r = color.rgb.r
	g = color.rgb.g
	b = color.rgb.b
	new_color = (r,g,b)
	rgb_colors.append(new_color)

print(rgb_colors)
'''
color_list = [ (237, 224, 80), (205, 4, 73), (236, 50, 130), (198, 164, 8), (111, 179, 218), (204, 75, 12)]
tim.pu()
tim.hideturtle()
tim.setheading(210)
tim.forward(300)
tim.setheading(0)

for i in range(10):
	for j in range(10):
		tim.dot(20,random.choice(color_list))
		tim.forward(50)
	tim.setheading(90)
	tim.forward(50)
	tim.setheading(180)
	tim.forward(500)
	tim.setheading(0)

screen.exitonclick()