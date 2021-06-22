import cv2
import tkinter as tk
from tkinter import Tk, mainloop, LEFT, TOP
from tkinter.ttk import *
from tkinter import ttk
from PIL import ImageTk, Image
from PIL import  Image
from PIL import Image , ImageDraw, ImageFont
import math
from tkinter import filedialog, colorchooser
from tkinter.messagebox import showinfo
import numpy
import numpy as np
# import functions
import tkinter as tk
window = tk.Tk() 



# window.geometry('700x700+300+150')
window.title("hallo")
window.state('zoomed')
window.iconbitmap("C:\c program codes\c program 2021\opencv\images/vi1.jpg")
window.resizable(width = True, height = True)

lenth=910
wid=610

global img
img_list = []

panel=tk.LabelFrame(window, padx=10, pady=10, height=wid, width=lenth)
panel.grid(row=1, column=1, padx=10, pady=50)

panel1=tk.LabelFrame(window, padx=10, pady=10, height=wid, width=lenth/4)
panel1.grid(row=1, column=2, padx=10, pady=10)

show_canv = tk.Canvas(panel, bg='#4f5154', height=wid, width=lenth)
opt_canv=tk.Canvas(panel1, bg='#35363b', height=wid, width = lenth/4)

pane = tk.Label(panel, bg='#4f5154') 
# pane.pack()

def show_error():
    tk.messagebox.showerror(title="shadow", message="open image")
    return

def openfilename(): 
    filename = filedialog.askopenfilename(title ='pen') 
    return filename

def show_img(img, panel):
    global lenth, wid,pane
    l=int(img.size[0])
    w=int(img.size[1]) 
    if(l>w)and(lenth<l):
        print("1\n", lenth, " l: ", l)
        w=int(((lenth-10)/l)*w)
        l=lenth-10
        
        print(w, " ")
    elif(l<w)and(w>wid):
        print("2\n", wid)
        l=int(((wid-10)/w)*l)
        w=wid-10
    

    img = img.resize((l, w), Image.ANTIALIAS) 
  
    # PhotoImage class is used to add image to widgets, icons etc 
    img = ImageTk.PhotoImage(img) 
    pane.config(image='')
    pane = tk.Label(panel, image = img) 
      
    # set the image as img  
    pane.image = img 
    # pane.pack()
    show_canv.create_window(lenth/2, wid/2, window=pane)

def open_img(): 
    # Select the Imagename  from a folder  
    global panel, lenth, wid,  show_canv
    global pane
    global img_list
    x = openfilename() 
  
    # opens the image 
    img=cv2.imread(x)
    
    

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_list.append(img)
    imgr=Image.fromarray(img_list[0]) 

    show_img(imgr, panel)

def edit_img1():
    global img, img_list
    flag=False
    try:
        print(type(img))
        flag=True
    except:
        show_error()
    if (flag):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imggray=Image.fromarray(img)
        show_img(imggray, panel)
def edit_img(number):
    global img_list,panel
    list_size=len(img_list)
    if number == 1 :
        img = cv2.cvtColor(img_list[list_size-1], cv2.COLOR_BGR2GRAY)
        img_list.append(img)
        imggray=Image.fromarray(img_list[list_size])
        show_img(imggray,  panel)
    if number == 2:
        img = cv2.GaussianBlur(img_list[list_size-1],(7,7),cv2.BORDER_DEFAULT)
        img_list.append(img)
        imgblur=Image.fromarray(img_list[list_size])
        show_img(imgblur, panel)
    if number == 3: # Edge Cascade
        img = cv2.Canny(img_list[list_size-1], 125, 175)
        img_list.append(img)
        imgcanny=Image.fromarray(img_list[list_size])
        show_img(imgcanny,  panel)
    if number == 4: # Dilating the image
        img = cv2.dilate(img_list[list_size-1], (7,7), iterations=3)
        img_list.append(img)
        imgdilate=Image.fromarray(img_list[list_size])
        show_img(imgdilate,  panel)
    if number == 5: # Eroding
        img = cv2.erode(img_list[list_size-1], (7,7), iterations=3)
        img_list.append(img)
        imgerode=Image.fromarray(img_list[list_size])
        show_img(imgerode,  panel)
    if number == 7: #croping
        w,h=img_list[list_size-1].shape[1],img_list[list_size-1].shape[0]
        print(w)
        print(h)
        #crop_width = dim[0] if dim[0]<img_list[list_size-1].shape[1] else img_list[list_size-1].shape[1]
	    
        crop_width = int(w)
        
        crop_height=int(h-0)
        #crop_height = dim[1] if dim[1]<img_list[list_size-1].shape[0] else img_list[list_size-1].shape[0]
        
        mid_x =int(w/8)
        mid_y = int(h/100)
	    
        cw2 = int(crop_width-mid_x)
        print(cw2)

        ch2 = int(crop_height-0)
        print(ch2)
	    
        crop_img =img_list[list_size-1][mid_y-ch2:mid_y+ch2, 0:mid_x+cw2]
        #crop_img =img_list[list_size-1][w:0,0:-10]
        #img=  img_list[list_size-1][0:w-10, 0:h-10]
        img_list.append(crop_img)
        imgcrop=Image.fromarray(img_list[list_size])
        show_img(imgcrop, panel)
    if number == 9: #apply sepia
        kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
        img=cv2.filter2D(img_list[list_size-1], -1, kernel)
        img_list.append(img)
        imgsep=Image.fromarray(img_list[list_size])
        show_img(imgsep,  panel)

    if number==11: #invert image
        img=cv2.bitwise_not(img_list[list_size-1])
        img_list.append(img)
        imginvert=Image.fromarray(img_list[list_size])
        show_img(imginvert,  panel)
    if number==12: #dnoise 
        img = cv2.fastNlMeansDenoisingColored(img_list[list_size-1],None,10,10,7,21)
        img_list.append(img)
        imgx=Image.fromarray(img_list[list_size])
        show_img(imgx,  panel)
    if number==13: #image sharp
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        img=cv2.filter2D(img_list[list_size-1], -1, kernel)
        img_list.append(img)
        imgsharp=Image.fromarray(img_list[list_size])
        show_img(imgsharp,  panel)
    if number==14: #image 
        kernel = np.array([[0,-1,-1],
                            [1,0,-1],
                            [1,1,0]])
        img=cv2.filter2D(img_list[list_size-1], -1, kernel)
        img_list.append(img)
        imgvi=Image.fromarray(img_list[list_size])
        show_img(imgvi,  panel)
    if number==15: # adjust as 
        img = cv2.resize(img_list[list_size-1], (0, 0), fx = 0.4, fy = 0.4) 
        img_list.append(img)     
        imgvi3=Image.fromarray(img_list[list_size])
        show_img(imgvi3,  panel)
    if number == 16:#thick image
        img = cv2.resize(img_list[list_size-1], (0, 0), fx = 3, fy = 3)  
        img_list.append(img)    
        imgvi1=Image.fromarray(img_list[list_size])
        show_img(imgvi1,  panel)
    if number == 17: #widen the image
        img =  cv2.resize(img_list[list_size-1], (780, 540),
               interpolation = cv2.INTER_NEAREST)  
        img_list.append(img)  
        imgvi2=Image.fromarray(img_list[list_size])
        show_img(imgvi2, panel)
    if number==18:
        w,h=img_list[list_size-1].shape[1],img_list[list_size-1].shape[0]
        print(w)
        print(h)
        #crop_width = dim[0] if dim[0]<img_list[list_size-1].shape[1] else img_list[list_size-1].shape[1]
	    
        crop_width = int(w)
        
        crop_height=int(h-0)
        #crop_height = dim[1] if dim[1]<img_list[list_size-1].shape[0] else img_list[list_size-1].shape[0]
        
        mid_x =int(w/100)
        mid_y = int(h/2)
	    
        cw2 = int(crop_width-0)
        print(cw2)

        ch2 = int(crop_height-mid_y)
        print(ch2)
	    
        crop_img =img_list[list_size-1][0:mid_y+ch2, mid_x-cw2:mid_x+cw2]
        #img =  img_list[list_size-1][0:500, 50:500]
        img_list.append(crop_img)
        imgcrop1=Image.fromarray(img_list[list_size])
        show_img(imgcrop1, panel)


    if number==19:
        w,h=img_list[list_size-1].shape[1],img_list[list_size-1].shape[0]
        print(w)
        print(h)
        #crop_width = dim[0] if dim[0]<img_list[list_size-1].shape[1] else img_list[list_size-1].shape[1]
	    
        crop_width = int(h)
        
        crop_height=int(w-0)
        #crop_height = dim[1] if dim[1]<img_list[list_size-1].shape[0] else img_list[list_size-1].shape[0]
        
        mid_x =int(h/20)
        mid_y = int(w/100)
	    
        cw2 = int(crop_width-0)
        print(cw2)

        ch2 = int(crop_height-mid_y)
        print(ch2)
	    
        #crop_img =img_list[list_size-1][0:mid_x+cw2, mid_y-ch2:mid_y+ch2]
        crop_img1 =img_list[list_size-1][mid_y-ch2:mid_y+ch2, 0:mid_x+cw2]
        print('hello')
        #img =  img_list[list_size-1][0:500, 50:500]
        img_list.append(crop_img1)
        imgcrop2=Image.fromarray(img_list[list_size])
        show_img(imgcrop2, panel)
    

    if number==20:
        w,h=img_list[list_size-1].shape[1],img_list[list_size-1].shape[0]
        print(w)
        print(h)
        #crop_width = dim[0] if dim[0]<img_list[list_size-1].shape[1] else img_list[list_size-1].shape[1]
	    
        crop_width = int(h-0)
        
        crop_height=int(w-0)
        #crop_height = dim[1] if dim[1]<img_list[list_size-1].shape[0] else img_list[list_size-1].shape[0]
        
        mid_x =int(h/100)
        mid_y = int(w/100)
	    
        cw2 = int(crop_width-0)
        print(cw2)

        ch2 = int(crop_height-mid_y)
        print(ch2)
	    
        crop_img =img_list[list_size-1][mid_x-ch2:mid_x+ch2,0:mid_y+cw2]
        #img =  img_list[list_size-1][0:500, 50:500]
        img_list.append(crop_img)
        imgcrop1=Image.fromarray(img_list[list_size])
        show_img(imgcrop1, panel)
    
    if number==21:
        w,h=img_list[list_size-1].shape[1],img_list[list_size-1].shape[0]
        print(w)
        print(h)
        #crop_width = dim[0] if dim[0]<img_list[list_size-1].shape[1] else img_list[list_size-1].shape[1]
	    
        #crop_width = int(w)
        
        #crop_height=int(h-0)
        #crop_height = dim[1] if dim[1]<img_list[list_size-1].shape[0] else img_list[list_size-1].shape[0]
        
        
        right=0
        left =0
        top = int(h)
        bottom=int(w)

	    
        #cw2 = int(crop_width-0)
        #print(cw2)

        #ch2 = int(crop_height-mid_x)
        #print(ch2)
	    
        crop_img =img_list[list_size-1][left:top,right:bottom]
        #img =  img_list[list_size-1][0:500, 50:500]
        img_list.append(crop_img)
        imgcrop1=Image.fromarray(img_list[list_size])
        show_img(imgcrop1, panel)


    if number==22: #rotate 90 clockwise
        img = cv2.rotate(img_list[list_size-1], cv2.ROTATE_90_CLOCKWISE)  
        img_list.append(img)    
        img_90c=Image.fromarray(img_list[list_size])
        show_img(img_90c,  panel)

    if number==23: #rotate counter clockwise
        img = cv2.rotate(img_list[list_size-1], cv2.ROTATE_90_COUNTERCLOCKWISE)  
        img_list.append(img)    
        img_90co=Image.fromarray(img_list[list_size])
        show_img(img_90co,  panel)

    if number==24: #rotae 180
        img = cv2.rotate(img_list[list_size-1], cv2.ROTATE_180)  
        img_list.append(img)    
        img_180=Image.fromarray(img_list[list_size])
        show_img(img_180,  panel)
    





    


    
        

    

        



    
def asscii_art():
    global img_list,panel
    list_size=len(img_list)
    chars="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
    chars="#Wo- "[::-1]
    charArray =list(chars)
    charLength=len(charArray)
    interval = charLength/256

    scaleFactor =0.1

    oneCharWidth=8
    oneCharHeight=18


    def getchar(inputInt):
        return charArray[math.floor(inputInt*interval)]

    text_file=open("Output.txt","w")
    img = cv2.cvtColor(img_list[list_size-1], cv2.COLOR_BGR2RGB)
    im=Image.fromarray(img)
    img_list.append(im)
    fnt=ImageFont.truetype('C:\Windows\Fonts\lucon.ttf',15)
    width,height=im.size
    print(width,height,height/width)
    im=im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))),Image.NEAREST)
    width,height=im.size
    pix=im.load()
    outputImage=Image.new('RGB',(oneCharWidth*width,oneCharHeight*height),color=(0,0,0))
    d=ImageDraw.Draw(outputImage)


    for i in range (height):
        for j in range(width):
            r ,g , b =pix[j,i]
            h=int(r/3 + g/3 + b/3)
            pix[j,i]=(h,h,h)
            text_file.write(getchar(h))
            d.text((j*oneCharWidth,i*oneCharHeight),getchar(h),font=fnt,fill=(r,g,b))

        text_file.write('\n')

    opencvImage = cv2.cvtColor(np.array(outputImage), cv2.COLOR_RGB2BGR)
    img_list.append(opencvImage)
    img_18=Image.fromarray(opencvImage)
    show_img(img_18,  panel)


def cartoon_w():
    global img_list,panel
    list_size=len(img_list)
    gray = cv2.cvtColor(img_list[list_size-1], cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # 2) Color
    color = cv2.bilateralFilter(img_list[list_size-1], 9, 300, 300)

    # 3) Cartoon
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    img_list.append(cartoon)
    img_cartoon=Image.fromarray(cartoon)
    show_img(img_cartoon,  panel)





    
    
def edit_w1():
    global panel1
    panel2=tk.LabelFrame(panel1, padx=10, pady=10, height=wid, width=lenth/4)
    #panel2.pack()
    try:
        opt_canv.delete('all')
    except:
        pass
    opt_canv.create_window(115, 305, window=panel2)
    panel2.config(bg='#35363b')
    
    #=tk.Canvas(panel1, bg='#131414', height=wid, width = lenth/4)
    
    b1=tk.Button(panel2,padx=20,pady=8, borderwidth=4,  text="color gray", command=lambda :edit_img(1))
    b1.pack()
    b2=tk.Button(panel2,padx=40,pady=8,borderwidth=4,  text="blur", command=lambda :edit_img(2))
    b2.pack()
    b3=tk.Button(panel2,padx=12,pady=8,borderwidth=4,  text="Edge Cascade", command=lambda :edit_img(3))
    b3.pack()
    b4=tk.Button(panel2,padx=16,pady=8,borderwidth=4,  text="Dilate image", command=lambda :edit_img(4))
    b4.pack()
    b5=tk.Button(panel2,padx=38,pady=8,borderwidth=4,  text="Erode", command=lambda :edit_img(5))
    b5.pack()
    b9=tk.Button(panel2,padx=41,pady=8,borderwidth=4,  text="Sepia", command=lambda :edit_img(9))
    b9.pack()
    b11=tk.Button(panel2,padx=40,pady=8,borderwidth=4,  text="Invert", command=lambda :edit_img(11))
    b11.pack()
    b12=tk.Button(panel2,padx=36,pady=8,borderwidth=4,  text="denoise", command=lambda :edit_img(12))
    b12.pack()
    b13=tk.Button(panel2,padx=41,pady=8,borderwidth=4,  text="Sharp", command=lambda :edit_img(13))
    b13.pack()
    b14=tk.Button(panel2,padx=37,pady=8,borderwidth=4,  text="Special", command=lambda :edit_img(14))
    b14.pack()
    b = Button(panel2, text="close",command= lambda:panel2.destroy())
    b.pack()
    


    


def resize_w():
    panel3=tk.LabelFrame(panel1, padx=10, pady=10, height=wid, width=lenth/4)
    try:
        opt_canv.delete('all')
    except:
        pass
    opt_canv.create_window(115, 220, window=panel3)
    panel3.config(bg='#35363b')
    b15=tk.Button(panel3,padx=41,pady=10,borderwidth=4,  text="set1", command=lambda :edit_img(15))
    b15.pack()
    b16=tk.Button(panel3,padx=41,pady=10,borderwidth=4,  text="Set2", command=lambda :edit_img(16))
    b16.pack()
    b17=tk.Button(panel3,padx=41,pady=10,borderwidth=4,  text="Set3", command=lambda :edit_img(17))
    b17.pack()
    b = Button(panel3, text="close",  command= lambda:panel3.destroy())
    b.pack()


def crop_w():
    panel4=tk.LabelFrame(panel1, padx=10, pady=10, height=wid, width=lenth/4)
    try:
        opt_canv.delete('all')
    except:
        pass
    opt_canv.create_window(115, 220, window=panel4)
    panel4.config(bg='#35363b')
    b7=tk.Button(panel4,padx=41,pady=10,borderwidth=4,  text="top", command=lambda :edit_img(7))
    b7.pack()
    b18=tk.Button(panel4,padx=41,pady=8,borderwidth=4,  text="left", command=lambda :edit_img(18))
    b18.pack()
    b19=tk.Button(panel4,padx=41,pady=8,borderwidth=4,  text="Right", command=lambda :edit_img(19))
    b19.pack()
    b20=tk.Button(panel4,padx=41,pady=8,borderwidth=4,  text="Bottom", command=lambda :edit_img(20))
    b20.pack() 
    b = Button(panel4, text="close",  command= lambda:panel4.destroy())
    b.pack()


def rotate_w():
    panel5=tk.LabelFrame(panel1, padx=10, pady=10, height=wid, width=lenth/4)
    try:
        opt_canv.delete('all')
    except:
        pass
    opt_canv.create_window(115, 220, window=panel5)
    panel5.config(bg='#35363b')
    b22=tk.Button(panel5,padx=16,pady=8,borderwidth=4,  text="90 clockwise", command=lambda :edit_img(22))
    b22.pack() 
    b23=tk.Button(panel5,padx=30,pady=8,borderwidth=4,  text="90 anti", command=lambda :edit_img(23))
    b23.pack() 
    b24=tk.Button(panel5,padx=40,pady=8,borderwidth=4,  text="180", command=lambda :edit_img(24))
    b24.pack() 
    b = Button(panel5, text="close",  command= lambda:panel5.destroy())
    b.pack()




def edit_undo():
    global panel
    global img_list
    list_len=len(img_list)
    img_list.pop()
    img1=Image.fromarray(img_list[list_len-2])
    show_img(img1, panel)

#menubar start/*
menubar = tk.Menu(window)

file= tk.Menu(menubar, tearoff=0)
file.add_command(label="Open", command=open_img)  
file.add_separator()
file.add_command(label="Quit!", command=window.quit) 
menubar.add_cascade(label="File", menu=file)

editmenu= tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Open", command=edit_w1)  
editmenu.add_separator()
editmenu.add_command(label="Undo", command=edit_undo)
#editmenu.add_command(label="Redo", command=edit_w1().edit_undo)  
#editmenu.add_command(label="Quit!", command=panel1.quit)
menubar.add_cascade(label="edit", menu=editmenu)

Resizemenu= tk.Menu(menubar, tearoff=0)
Resizemenu.add_command(label="Open", command=resize_w)  
Resizemenu.add_separator()
Resizemenu.add_command(label="Quit!", command=panel1.quit)
menubar.add_cascade(label="Resize", menu=Resizemenu)

cropmenu= tk.Menu(menubar, tearoff=0)
cropmenu.add_command(label="Open", command=crop_w)  
menubar.add_cascade(label="Crop", menu=cropmenu)
rotatemenu= tk.Menu(menubar, tearoff=0)
rotatemenu.add_command(label="Open", command=rotate_w)  
menubar.add_cascade(label="Rotate", menu=rotatemenu)
specialmenu= tk.Menu(menubar, tearoff=0)
specialmenu.add_command(label="Ascii_art", command=asscii_art)
specialmenu.add_separator()
specialmenu.add_command(label="Cartoon", command=cartoon_w) 

menubar.add_cascade(label="Special", menu=specialmenu)



window.config(menu=menubar)  
#*/menubar end/*


show_canv.pack()
opt_canv.pack()




window.mainloop()