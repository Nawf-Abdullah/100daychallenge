from turtle import Turtle

class ScoreBoard(Turtle):
	def __init__(self,deg):
		super().__init__()
		self.color("white")
		self.hideturtle()
		self.pu()
		self.goto(deg,200)
		self.cur_score = 0
		self.write(arg = self.cur_score,move= False,align="center",font = ("Arial",80,"normal"))

	def point(self):
		self.cur_score += 1
		self.clear()
		self.write(arg = self.cur_score,move= False,align="center",font = ("Arial",80,"normal"))


