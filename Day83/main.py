from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("TIc Tac Toe")
press= 1

def changer(n):
	global press
	if press%2==0:
		n['text']="X"
		is_winner()
		n['state']='disabled'
	else:
		n['text']="O"
		is_winner()
		n['state']='disabled'
	press+=1
	
	

def is_winner():
	global button11,button12,button13,button21,button22,button23,button31,button32,button33
	print("running")
	if button11['text'] == "O" and button12['text'] == "O" and button13['text'] == "O":
		messagebox.showinfo(title="Winner",message='O is the Winner!')
		reset()

	elif button21['text'] == "O" and button22['text'] == "O" and button23['text'] == "O":
		messagebox.showinfo(title="Winner",message='O is the Winner!')
		reset()

	elif button31['text'] == "O" and button32['text'] == "O" and button33['text'] == "O":
		messagebox.showinfo(title="Winner",message='O is the Winner!')
		reset()

	elif button11['text'] == "O" and button22['text'] == "O" and button33['text'] == "O":
		messagebox.showinfo(title="Winner",message='O is the Winner!')
		reset()

	elif button13['text'] == "O" and button22['text'] == "O" and button31['text'] == "O":
		messagebox.showinfo(title="Winner",message='O is the Winner!')
		reset()

	elif button11['text'] == "O" and button21['text'] == "O" and button31['text'] == "O":
		messagebox.showinfo(title="Winner",message='O is the Winner!')
		reset()

	elif button12['text'] == "O" and button22['text'] == "O" and button32['text'] == "O":
		messagebox.showinfo(title="Winner",message='O is the Winner!')
		reset()

	elif button13['text'] == "O" and button23['text'] == "O" and button33['text'] == "O":
		messagebox.showinfo(title="Winner",message='O is the Winner!')
		reset()

	elif button11['text'] == "X" and button12['text'] == "X" and button13['text'] == "X":
		messagebox.showinfo(title="Winner",message='X is the Winner!')
		reset()

	elif button21['text'] == "X" and button22['text'] == "X" and button23['text'] == "X":
		messagebox.showinfo(title="Winner",message='X is the Winner!')
		reset()

	elif button31['text'] == "X" and button32['text'] == "X" and button33['text'] == "X":
		messagebox.showinfo(title="Winner",message='X is the Winner!')
		reset()

	elif button11['text'] == "X" and button22['text'] == "X" and button33['text'] == "X":
		messagebox.showinfo(title="Winner",message='X is the Winner!')
		reset()

	elif button13['text'] == "X" and button22['text'] == "X" and button31['text'] == "X":
		messagebox.showinfo(title="Winner",message='X is the Winner!')
		reset()

	elif button11['text'] == "X" and button21['text'] == "X" and button31['text'] == "X":
		messagebox.showinfo(title="Winner",message='X is the Winner!')
		reset()

	elif button12['text'] == "X" and button22['text'] == "X" and button32['text'] == "X":
		messagebox.showinfo(title="Winner",message='X is the Winner!')
		reset()

	elif button13['text'] == "X" and button23['text'] == "X" and button33['text'] == "X":
		messagebox.showinfo(title="Winner",message='X is the Winner!')
		reset()

	else:
		print("Nope")



def reset():
	global button11,button12,button13,button21,button22,button23,button31,button32,button33
	buts = [button11,button12,button13,button21,button22,button23,button31,button32,button33]
	print("reset runing")
	for i in buts:
		print('yep')
		i['text']=' '
		i['state']='active'
	


button11 = Button(text=' ',font=("Helvatica",30),command=lambda: changer(button11))
button12 = Button(text=' ',font=("Helvatica",30),command=lambda: changer(button12))
button13 = Button(text=' ',font=("Helvatica",30),command=lambda: changer(button13))

button21 = Button(text=' ',font=("Helvatica",30),command=lambda: changer(button21))
button22 = Button(text=' ',font=("Helvatica",30),command=lambda: changer(button22))
button23 = Button(text=' ',font=("Helvatica",30),command=lambda: changer(button23))

button31 = Button(text=' ',font=("Helvatica",30),command=lambda: changer(button31))
button32 = Button(text=' ',font=("Helvatica",30),command=lambda: changer(button32))
button33 = Button(text=' ',font=("Helvatica",30),command=lambda: changer(button33))

button11.grid(row=0,column=0,ipadx=30,ipady=20)
button12.grid(row=0,column=1,ipadx=30,ipady=20)
button13.grid(row=0,column=2,ipadx=30,ipady=20)

button21.grid(row=1,column=0,ipadx=30,ipady=20)
button22.grid(row=1,column=1,ipadx=30,ipady=20)
button23.grid(row=1,column=2,ipadx=30,ipady=20)

button31.grid(row=2,column=0,ipadx=30,ipady=20)
button32.grid(row=2,column=1,ipadx=30,ipady=20)
button33.grid(row=2,column=2,ipadx=30,ipady=20)



root.mainloop()