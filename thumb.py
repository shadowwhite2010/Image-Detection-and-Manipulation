import cv2
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image 
from tkinter import filedialog, colorchooser
from tkinter.messagebox import showinfo
import numpy
# import functions
import tkinter as tk
window = tk.Tk() 


# window.geometry('700x700+300+150')
window.title("hallo")
window.iconbitmap("atha.ico")
window.resizable(width = True, height = True)

lenth=910
wid=610

panel=tk.LabelFrame(window, padx=10, pady=10, height=wid, width=lenth)
panel.grid(row=1, column=1, padx=50, pady=50)

C = tk.Canvas(panel, bg='white', height=wid, width=lenth)
C.pack()

pane = tk.Label(panel) 
# pane.pack()

def openfilename(): 
  
    # open file dialog box to select image 
    # The dialogue box has a title "Open" 
    filename = filedialog.askopenfilename(title ='pen') 
    return filename

def open_img(): 
    # Select the Imagename  from a folder  
    global panel, lenth, wid,  C
    global pane 
    x = openfilename() 
  
    # opens the image 
    img=cv2.imread(x)
    
    

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img=Image.fromarray(img) 
    print(type(img.size[1]))
    l=int(img.size[0])
    w=int(img.size[1]) 
    # resize the image and apply a high-quality down sampling filter 
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
    # C = tk.Canvas(panel, bg='blue', height=wid, width=lenth)
    # create a label
    # panel.delete() 
    # panel=tk.LabelFrame(window, padx=10, pady=10, height=wid, width=lenth)
    # panel.grid(row=1, column=1, padx=50, pady=50)
    
    # C.create_image(0, 0, image=img, tags='currentimg')
    # C.itemconfigure('currentimg')
    # C.config()
    
    # panel.grid_remove()

    # pane.pack_forget()
    pane.config(image='')
    pane = tk.Label(panel, image = img) 
      
    # set the image as img  
    pane.image = img 
    # pane.pack()
    C.create_window(lenth/2, wid/2, window=pane)
    # pane.config()
    return img

menubar = tk.Menu(window)



file= tk.Menu(menubar, tearoff=0)
file.add_command(label="Open", command=lambda:open_img())  
file.add_separator()
file.add_command(label="Quit!", command=window.quit)  

menubar.add_cascade(label="File", menu=file)

# try:
#     print(img.size)
# except:
#     print("no image right now")

window.config(menu=menubar)  


# C.pack()
# b_file_open=tk.Button(window, text="open_image", padx=10, pady=5, command=open_img, cursor="plus")
# b_file_open.grid(row=0, column=0, sticky=tk.NW)


# tk.colorchooser.askcolor(color=None)



window.mainloop()
