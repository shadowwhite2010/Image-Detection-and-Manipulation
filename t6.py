import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image 
import numpy as np
import os

window = tk.Tk()
# window.geometry('500x500')

def resz_img(imgt, x, y):
    l=int(imgt.size[0])
    w=int(imgt.size[1])
    if(l>w)and(x<l):
        # print("1\n", x, " l: ", l)
        w=int(((x-10)/l)*w)
        l= x-20
        
        # print(w, " ")
    elif(l<=w)and(w>y):
        # print("2\n", y)
        l=int(((y-10)/w)*l)
        w=y-20
    print(l, w)
    return imgt.resize((l, w), Image.ANTIALIAS)

i = 0
path = "D:/books\google_hash/temp"
h = 500
w = 500
# with Image.open("D:/books\google_hash/temp\stego8.png") as img:
#     img = resz_img(img, 150, 150)
#     img = ImageTk.PhotoImage(img)



# tk.Label(window, image = img, relief = tk.RIDGE,  bd = 10).grid(row = 0, column = 0)
lis = np.empty((len(os.listdir(path)), 2), dtype=object)
dfres_can = tk.Canvas(window, height = 600, width = 500)
dfres_fr = tk.Frame(dfres_can)
my_scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL)
my_scrollbar.config(command =dfres_can.yview)
my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
dfres_can.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
dfres_can.create_window((0,0), window=dfres_fr, anchor="nw")
dfres_fr.bind('<Configure>', lambda e: dfres_can.configure(scrollregion = dfres_can.bbox("all")))

for tr in os.listdir(path):
    with Image.open(os.path.join(path, tr)) as img:
    # img = Image.open(os.path.join(path, tr))
        x = 150
        y = 150
        l=int(img.size[0])
        w=int(img.size[1])
        if(l>w)and(x<l):
            # print("1\n", x, " l: ", l)
            w=int(((x-10)/l)*w)
            l= x-20
            
            # print(w, " ")
        elif(l<=w)and(w>y):
            # print("2\n", y)
            l=int(((y-10)/w)*l)
            w=y-20
        # img = resz_img(img, 150, 150)
        img = img.resize((l, w), Image.ANTIALIAS)
        print(img.size)
        img = ImageTk.PhotoImage(img)
        
    lis[i, 0] = tk.Label(dfres_fr, image = img, relief = tk.RIDGE,  bd = 5, height = 150, width = 150)
    lis[i, 0].image = img
    # lis1 = tk.Label(window, image = img, relief = tk.RIDGE,  bd = 5, height = 150, width = 150)
    # lis1.image = img
    # entry.config(highlightbackground = "red", highlightcolor= "red")
    lis[i, 0].grid(row = i+1, column = 0, pady = 5)
    lis[i, 1] = tk.Canvas(dfres_fr, relief = tk.RIDGE,  bd = 5, height = 150, width = 400, bg = "white")
    lis[i, 1].create_rectangle(18, 18, 400-4, 150-4 , width = 5, outline = "red")
    pb = ttk.Progressbar(
        dfres_fr,
        orient='horizontal',
        mode='determinate',
        style = 'Horizontal.TProgressbar',
        length=300
    )
    pb['value'] = 10.5
    lis[i, 1].create_window(185, 50, window = pb)
    lis[i, 1].grid(row = i+1, column = 1, pady = 5)
    # lis1.grid(row = i+1, column = 0, pady = 5)
    # # lis2 = tk.Label(window, relief = tk.RIDGE, text = "hallo", bd = 5, height = 10)
    # lis2 = tk.Canvas(window, relief = tk.RIDGE,  bd = 5, height = 150, width = 200, bg = "white")
    # lis2.create_rectangle(4, 4, 150-4, 200-4, width = 5, outline = "red")
    # lis2.grid(row = i+1, column = 1, pady = 5)
    # lab2 = tk.Label(window, relief = tk.RIDGE, text = "hallo",  height = 155, width = w-175, bd = 10)

    # lab1
    # lab2.
    i = i + 1
    if (i==4):
        break



window.mainloop()
