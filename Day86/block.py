from turtle import Turtle

class Block(Turtle):
	def __init__(self,position):
		super().__init__()
		self.color("white")
		self.pu()
		self.create_block()
		self.goto(position)

	def create_block(self):
		self.shape("square")
		self.shapesize(stretch_wid=1,stretch_len=4)

