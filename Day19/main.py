import turtle as t

tim = t.Turtle()
screen = t.Screen()

def move_forward():
	tim.forward(10)

def move_backward():
	tim.backward(10)
def turn_left():
	tim.left(10)

def turn_right():
	tim.right(10)

def clear():
	tim.clear()
	tim.pu()
	tim.home()
	tim.pd()


screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")

screen.onkey(clear,"c")
screen.exitonclick()