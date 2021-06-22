import tkinter as tk
# Lots of tutorials have from tkinter import *, but that is pretty much always a bad idea
from tkinter import ttk
from tkinter.constants import ANCHOR
from PIL import ImageTk, Image, ImageEnhance, ImageOps, ImageFilter 
root = tk.Tk()
bit_var = tk.StringVar()
opt_var = tk.StringVar()
root.geometry("1010x700")
root.title("Labaoratory")
img_can = tk.Canvas(root, relief = tk.RAISED, bd = 4)

img = Image.open("temp\gen_face.png")
img = img.convert("RGB")
# img = ImageOps.posterize(img, 2)



# labr = tk.Label(img_can)
# labg = tk.Label(img_can)
# labb = tk.Label(img_can)

def show_lab(e):
    global img
    # labr.config(image = "")
    # labg.config(image = "")
    # labb.config(image = "")
    imgc = ImageOps.posterize(img, int(e))
    imgr, imgg, imgb = imgc.split()
    imgr = ImageTk.PhotoImage(imgr) 
    imgg = ImageTk.PhotoImage(imgg) 
    imgb = ImageTk.PhotoImage(imgb) 
    img_can.delete("all")
    labr = tk.Label(img_can, image = imgr) 
    labr.image = imgr
    labg = tk.Label(img_can, image = imgg) 
    labg.image = imgg 
    labb = tk.Label(img_can, image = imgb) 
    labb.image = imgb

    img_can.create_window(
        (0, 0), anchor=tk.NW,
        width=  img_can.winfo_width()/2,
        window = labr
        )
    img_can.create_window(
        (505, 0), anchor=tk.NW,
        width=  img_can.winfo_width()/2,
        window = labb
        )
    img_can.create_window(
        (250, 330), anchor=tk.NW,
        width=  img_can.winfo_width()/2,
        window = labg
        )
# show_lab(8)

def test_opt_fun(val):
    img_can.delete("all")
    if (val=="effect_noise"):
        imgc = Image.effect_noise((img.size[0], img.size[1]), 4)
    elif(val == "effect_spread"):
        imgc = img.effect_spread(test_scal_opt.get())
    elif(val == "linear_gradient"):
        imgc = Image.linear_gradient('L')
    elif(val == "radial_gradient"):
        imgc = Image.radial_gradient('L')
    elif(val == "MedianFilter"):
        imgc = img.filter(ImageFilter.MedianFilter(test_scal_opt.get()))
    elif(val == "MinFilter"):
        imgc = img.filter(ImageFilter.MinFilter(test_scal_opt.get()))
    imgc = ImageTk.PhotoImage(imgc)
    labr = tk.Label(img_can, image = imgc) 
    labr.image = imgc
    img_can.create_window(
        (0, 0), anchor=tk.NW,
        width=  img_can.winfo_width()/2,
        window = labr
        )
    

opt_menu = [
    "nothing", "effect_noise", "effect_spread", 
    "linear_gradient", "radial_gradient", "MedianFilter",
    "MinFilter"]

opt_test = tk.OptionMenu(
    root, opt_var,
    *opt_menu,
    command= test_opt_fun
)

bit_var.set(8)
effect_opt = tk.Scale(
    root,
    from_ = 1,
    to = 8,
    variable = bit_var,
    orient=tk.HORIZONTAL,
    command = show_lab)
test_scal_opt = tk.Scale(
    root,
    from_ = 0,
    to = 8,
    orient=tk.HORIZONTAL)
effect_opt.pack(anchor=tk.NE)
opt_test.pack(anchor = tk.NW)
test_scal_opt.pack(anchor = tk.N, side = tk.TOP)
img_can.pack(fill = tk.BOTH, expand = 1, anchor=tk.N)
# lab.pack(fill = tk.BOTH, expand = 1)
root.mainloop()