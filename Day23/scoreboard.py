from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.pu()
		self.goto(-100,260)
		self.cur_score = 1
		self.write(arg=f"Level:{self.cur_score}",move=False ,font=FONT,align="right")

	def update(self):
		self.cur_score+=1
		self.clear()
		self.write(arg=f"Level:{self.cur_score}",move=False ,font=FONT,align="right")

	def game_over(self):
		self.home()
		self.write(arg="Game Over",move=False,font=FONT,align="center")