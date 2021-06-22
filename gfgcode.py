from tkinter import *
import PIL
from PIL import Image, ImageDraw, ImageTk


def save():
    global image_number
    filename = f'image_{image_number}.png'   # image_number increments by 1 at every save
    image1.save(filename)
    image_number += 1


def activate_paint(e):
    global lastx, lasty
    label.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y


def paint(e):
    global lastx, lasty, image1, label
    x, y = e.x, e.y
    # cv.create_line((lastx, lasty, x, y), width=1)
    #  --- PIL
    draw.line((lastx, lasty, x, y), fill='black', width=1)
    lastx, lasty = x, y
    
    photo = ImageTk.PhotoImage(image1)
    label.configure(image = photo)
    label.image = photo
    # label.pack()


root = Tk()

lastx, lasty = None, None
image_number = 0
image1 =Image.open("temp\gen_face.png")
label = Label(root)
label.bind('<1>', activate_paint)
label.pack()
# --- PIL

draw = ImageDraw.Draw(image1)

photo = ImageTk.PhotoImage(image1)
label.configure(image = photo)
label.image = photo
# cv = Canvas(root, width=640, height=480)


btn_save = Button(text="save", command=save)
btn_save.pack()

root.mainloop()