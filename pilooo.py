from PIL import ImageTk, Image 
import os
import tkinter as tk


window=tk.Tk()
window.title("hallo")
window.iconbitmap("icons/atha.ico")
num=0

path=os.getcwd() + "/temp"
imdir=os.listdir(path)
imls = []

lenth  = 800
wid = 800

# def show_img(imgt, panel):
#     # global lenth, wid, pane 
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
#     pane = tk.Label(panel, image = imgt) 
      
#     # set the image as img  
#     pane.image = imgt 
#     # pane.pack()
#     # show_canv.create_image(lenth/2, wid/2, image = imgt)
#     show_canv.create_window(lenth/2, wid/2,  window=pane)


def img_stt_chk(num):
    if num == len(imdir)-1:
        b_for['state']=tk.DISABLED
        b_back['state']=tk.NORMAL

    if num == 0:
        b_for['state']=tk.NORMAL
        b_back['state']=tk.DISABLED

    if 0<num<len(imdir)-1:
        b_for['state']=tk.NORMAL
        b_back['state']=tk.NORMAL

for i in imdir:
    img = Image.open(path + "/" + i) 
    img = img.resize((int(img.size[0]/2), int(img.size[1]/2)), Image.ANTIALIAS) 
    img = ImageTk.PhotoImage(img) 
    imls.append(img)


img = Image.open(path + "/" + imdir[num]) 
img = img.resize((int(img.size[0]/2), int(img.size[1]/2)), Image.ANTIALIAS) 
img = ImageTk.PhotoImage(img) 
label=tk.Label(window, image= img)
label.grid(row=0, column=0, columnspan=3)

def image_decl(num):
    global label
    label.grid_forget()
    label=tk.Label(window)
    show_img(imls[num], label)
    label.grid(row=0, column=0, columnspan=3)

def forward():
    global num
    print("forward ")
    num=num+1
    image_decl(num)
    img_stt_chk(num)
    ll=tk.Label(window, text=path + "/" + imdir[num])
    lll=tk.Label(window, text="num: " + str(num))
    ll.grid(row=1, column=1)
    lll.grid(row=2, column=1, sticky=tk.S)

# def show_img(imgt, panel):
#     global lenth, wid, pane 
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
#     pane = tk.Label(panel, image = imgt) 
      
#     # set the image as img  
#     pane.image = imgt 
#     # pane.pack()
#     # show_canv.create_image(lenth/2, wid/2, image = imgt)
#     show_canv.create_window(lenth/2, wid/2,  window=pane)

def back():
    global num
    global lll, ll
    
    print("back ")
    num=num-1
    image_decl(num)
    img_stt_chk(num)
    ll=tk.Label(window, text=path + "/" + imdir[num])
    lll=tk.Label(window, text="num: " + str(num))
    ll.grid(row=1, column=1)
    lll.grid(row=2, column=1, sticky=tk.S)



b_for = tk.Button(window, text=">>", padx=10, pady=5, command=forward)
b_back = tk.Button(window, text="<<", padx=10, pady=5, command=back)
ll=tk.Label(window, text=path + "/" + imdir[num])

lll=tk.Label(window, text="num: " + str(num))
# b_cropx = tk.Button(window, text = "x+", command = )


ll.grid(row=1, column=1)
b_back.grid(row=1, column=0, sticky=tk.W)
b_for.grid(row=1, column=2, sticky=tk.E)
lll.grid(row=2, column=1, sticky=tk.S)
# print(imdir)



window.mainloop()