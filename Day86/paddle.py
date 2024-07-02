from turtle import Turtle 

class Paddle(Turtle):
	def __init__(self,position):
		super().__init__()
		self.color("white")
		self.pu()
		self.create_paddle()
		self.goto(position)

	def create_paddle(self):
		self.shape("square")
		self.shapesize(stretch_wid=1,stretch_len=5)

	def right(self):
		self.forward(20)

	def left(self):
		self.backward(20)