from turtle import *

STARTING_POSTION = [(0,0),(-20,0),(-40,0)]
class Snake:

	def __init__(self):
		self.segments = []
		self.creake_snake()
		


	def creake_snake(self):
		for position in STARTING_POSTION:
			self.add_segment(position)

	def add_segment(self,position):
		new_segment = Turtle()
		new_segment.pu()
		new_segment.shape("square")
		new_segment.goto(position)
		new_segment.color('white')
		self.segments.append(new_segment)

	def extend(self):
		self.add_segment(self.segments[-1].position())
		


	def move(self):

		for seg_num in range(len(self.segments)-1,0,-1):
			new_x = self.segments[seg_num-1].xcor()
			new_y = self.segments[seg_num-1].ycor()
			self.segments[seg_num].goto(new_x,new_y)

		self.segments[0].forward(20)

	def up(self):
		if self.segments[0].heading() == 270:
			pass
		else:
			self.segments[0].setheading(90)

	def down(self):
		if self.segments[0].heading() == 90:
			pass
		else:
			self.segments[0].setheading(270)

	def left(self):
		if self.segments[0].heading() == 0:
			pass
		else:
			self.segments[0].setheading(180)

	def right(self):
		if self.segments[0].heading() == 180:
			pass
		else:
			self.segments[0].setheading(0)


