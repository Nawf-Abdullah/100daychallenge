from turtle import *

class Score(Turtle):

	def __init__(self):
		super().__init__()
		self.curr_score = 0
		self.hideturtle()
		self.color("white")
		self.pu()
		self.goto(0,260)
		self.write(arg = f"Score: {self.curr_score}",move=False,align = "center",font = ("Arial",24,"normal"))
		self.goto(0,260)

	def game_over(self):
		self.home()
		self.write(arg = "Game Over",move=False,align = "center",font = ("Arial",24,"normal"))


	def point(self):
		self.clear()
		self.curr_score += 1
		self.write(arg = f"Score: {self.curr_score}",move=False,align = "center",font = ("Arial",24,"normal"))