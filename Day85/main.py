from tkinter import *
from tkinter import messagebox
import random
 
window = Tk() 
window.title("Speed typing test")
seconds = 0
FONT_NAME = "Courier"



def start():
	word.delete(0,'end')
	sentences = ['Bismillah Hirahman Niraheem','I love to code','I love python','I am not a Robot','I am Happy']
	sentence = random.choice(sentences)
	sample.config(text=sentence)
	testing(sentence)


def testing(sentence):
	global seconds,timer
	seconds += 1
	time_label.config(text=f"Time:{seconds}")
	if word.get()!=sentence:
		timer = window.after(1000,testing,sentence)
	else:
		window.after_cancel(timer)
		messagebox.showinfo(title="You've done Awesome",message=f"""Time taken to Type {len(sentence.split(' '))}
		 words is {seconds} seconds""")
		start_btn.config(text="Next")
		seconds = 0


time_label = Label(text= f"Time:{seconds}",font=(FONT_NAME,50))
time_label.grid(column=0,row=0)

sample = Label(text="",font=('Helvatica',40,'bold'))
sample.grid(column=1,row=0)

word = Entry(width=40,font=('Helvatica',30,'bold'))
word.grid(row=1,column=0,columnspan=2,padx=20,pady=20)


start_btn = Button(text='Start',font=("Helvatica",20),command=start)	
start_btn.grid(column=0,row=2)

window.mainloop()