from tkinter import *
from PIL import Image, ImageTk, ImageDraw 
from tkinter.filedialog import askopenfilename
 
SOURCE_DIRECTORY = "F:/"
TARGET_DIRECTORY = "/Watermarked Photos"

root = Tk()
root.title("GUI Water Marker")

def open_file():
	file = askopenfilename(initialdir=SOURCE_DIRECTORY, title="Select A File", filetype=(("jpeg files", "*.jpg"), ("all files", "*.*"),('PNG',"*.png")))
	if file:
		with Image.open(file).convert("RGBA") as base:

		    # make a blank image for the text, initialized to transparent text color
		    txt = Image.new("RGBA", base.size, (255,255,255,0))

		    # get a font
		    # get a drawing context
		    d = ImageDraw.Draw(txt)

		    # draw text, half opacity
		    d.text((50,50), water.get(), fill=(255,255,255,128))
		    # draw text, full opacity

		    out = Image.alpha_composite(base, txt)

		    out.show()
		    out = out.convert("RGB")
		    out.save(f"watermarked/{file.split('/')[-1]}")
		    my_image = ImageTk.PhotoImage(out)
		    canvas.itemconfig(image_el,image=my_image)


image_canvas = Canvas(width=200,height=224,highlightthickness=0)
image_canvas.grid(row=0,column=0)
image_el = image_canvas.create_image(10,10,image=ImageTk.PhotoImage(file='watermarked/apolo.jpg'))

water = Entry(width=30)
water.grid(row=2,column=0)

open_btn = Button(text="Open File",command =open_file)
open_btn.grid(row=2,column=1)

root.mainloop()