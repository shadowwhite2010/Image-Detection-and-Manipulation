from PIL import ImageTk, Image 
import os
from tkinter import ttk
import tkinter as tk


window = tk.Tk()

lenth  = 600
wid = 600
m_frame = tk.Frame(window, height = 800, width = 800)

m_frame.pack(fill = tk.BOTH, expand = 1)

show_canv = tk.Canvas(m_frame, height = 600, width = 600, bg = "#111111")


# pane = tk.Label(show_canv)
# show_canv.create_window(300, 300, window = pane)

s_x = None
s_y = None

def drag_handler(event):
    global s_x, s_y
    s_x = event.x
    s_y = event.y
    print(event.x, event.y)
    show_canv.bind("<B1-Motion>", draw_rect)

def draw_rect(event):
    try:
        show_canv.delete("rect")
    except:
        pass
    show_canv.create_rectangle(s_x, s_y, event.x, event.y, tags = "rect", outline='white')
        

def show_img(imgt):
    # global pane 
    l=int(imgt.size[0])
    w=int(imgt.size[1]) 
    print("shape: ", l, w)
    if(l>w)and(lenth<l):
        print("1\n", lenth, " l: ", l)
        w=int(((lenth-10)/l)*w)
        l=lenth-10
        if(w>wid):
            l = int(((wid-10)/w)*l)
            w=wid-10
        print(w, " ")
    elif(l<=w)and(w>wid):
        print("2\n", wid)
        l=int(((wid-10)/w)*l)
        w=wid-10
        if (l>lenth):
            w = int(((lenth-10)/l)*w)
            l=lenth-10
    

    imgt = imgt.resize((l, w), Image.ANTIALIAS) 
    print("shape: ", l, w)
    # PhotoImage class is used to add image to widgets, icons etc 
    imgt = ImageTk.PhotoImage(imgt) 
    # pane.config(image='')
    # pane = tk.Label(m_frame, image = imgt) 
      
    # set the image as img  
    # pane.image = imgt 
    # pane.pack()
    try:
        show_canv.delete("img")
    except:
        pass
    can_ing = show_canv.create_image(lenth/2, wid/2, image = imgt, tags = "img")
    # can_ing['image'] = imgt
    show_canv.itemconfig(can_ing,image=imgt)
    # show_canv.create_window(lenth/2, wid/2,  window=pane)


# pane.pack()
# def show_img(imgt):
#     global pane 
#     l=int(imgt.size[0])
#     w=int(imgt.size[1]) 
#     print("shape: ", l, w)
#     if(l>w)and(lenth<l):
#         print("1\n", lenth, " l: ", l)
#         w=int(((lenth-10)/l)*w)
#         l=lenth-10
#         if(w>wid):
#             l = int(((wid-10)/w)*l)
#             w=wid-10
#         print(w, " ")
#     elif(l<=w)and(w>wid):
#         print("2\n", wid)
#         l=int(((wid-10)/w)*l)
#         w=wid-10
#         if (l>lenth):
#             w = int(((lenth-10)/l)*w)
#             l=lenth-10
    

#     imgt = imgt.resize((l, w), Image.ANTIALIAS) 
#     print("shape: ", l, w)
#     # PhotoImage class is used to add image to widgets, icons etc 
#     imgt = ImageTk.PhotoImage(imgt) 
#     pane.config(image='')
#     pane = tk.Label(m_frame, image = imgt) 
      
#     # set the image as img  
#     pane.image = imgt 
#     # pane.pack()
#     # show_canv.create_image(lenth/2, wid/2, image = imgt)
#     show_canv.create_window(lenth/2, wid/2,  window=pane)

img = [Image.open("D:/books\google_hash/atha.png")]

show_img(img[0])

def l_x(img):
    img[0] = img[0].crop((10, 0, img[0].size[0], img[0].size[1]))
    show_img(img[0])
    

def r_x(img):
    img[0] = img[0].crop((0, 0, img[0].size[0]-10, img[0].size[1]))
    show_img(img[0])
    

def t_y(img):
    img[0] = img[0].crop((0, 10, img[0].size[0], img[0].size[1]))
    show_img(img[0])
    
def b_y(img):
    img[0] = img[0].crop((0, 0, img[0].size[0], img[0].size[1]-10))
    show_img(img[0])
    

but_pane = tk.Frame(window, relief = tk.RIDGE, bd = 5)

bx_l = tk.Button(but_pane, text = ">", command = lambda:l_x(img))
bx_l.grid(row = 0, column = 0, rowspan = 2, sticky = "w")

bx_r = tk.Button(but_pane, text = "<", command = lambda:r_x(img))
bx_r.grid(row = 0, column = 1, rowspan = 2,  sticky = "w")

by_t = tk.Button(but_pane, text = "T", command = lambda:t_y(img))
by_t.grid(row = 0, column = 2, sticky = "ne")

bx_b = tk.Button(but_pane, text = "B", command = lambda:b_y(img))
bx_b.grid(row = 1, column = 2, sticky = "se")
but_pane.pack(fill = tk.X, expand = 1, padx = 10, pady = 10)

# pane.bind("<B1-Motion>", drag_handler)
show_canv.bind("<1>", drag_handler)
# # Dragging
# import tkinter

# root = tkinter.Tk()
# label = tkinter.Label(root, text="HEY")
# label.pack()

# def drag_handler(event):
#     print(event.x, event.y)

# label.bind("<B1-Motion>", drag_handler)

# root.mainloop()
show_canv.pack(fill = tk.BOTH, expand = 1)

window.mainloop()