import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image 
from tkinter import filedialog, colorchooser

window = tk.Tk()
window.title('testing ok!!')
# window.iconbitmap('c:/gui/codemy.ico')
window.geometry("400x400")

img  = None

my_menu = tk.Menu(window)
window.config(menu=my_menu)

def openfilename(): 
    filename = filedialog.askopenfilename(title ='pen') 
    return filename

def open_img():
	global img
	x = openfilename()
	print(x, type(x))
	img = Image.open(x)

# click command
def our_command():
	my_label = tk.Label(window, text="You Clicked a Dropdown Menu!").pack()

with open("key_st.txt", "r") as key_r:
    # print(key_r.readline())
    f=key_r.readlines()
    print(len(f))

opt_lis = []

for i in range (len(f)):
	opt_lis.append(str(i))

val_str = tk.StringVar(window)

val_str.set("1")

opt_mn = tk.OptionMenu(window, val_str, *opt_lis)
opt_mn.pack()
#Create a menu item

messge = "this is atharva shitole"

# can= tk.Canvas(window, height= 100, width= 200)
pane = tk.Frame(window, bg = "#F4E7E3")
msg_label = tk.Label(pane, text = messge, font = ('calibre',10,'bold'))
msg_label.grid(row = 0, column = 0, padx = 50, pady = 10)

msg_button = tk.Button(pane, text = "X", command = pane.forget)
msg_button.grid(row = 0, column = 0,  sticky = tk.NE)

photo = tk.PhotoImage(file = "D:/books/google_hash/icons/res_load.png")
photo = photo.subsample(2, 2)
img_btn = ttk.Button(pane, image = photo, command = our_command)
img_btn.grid(row = 1, column = 0, padx = 10, pady = 10)

pane.pack()
file_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="open", command=open_img)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)





window.mainloop()