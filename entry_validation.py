from string import ascii_uppercase, ascii_lowercase, digits
import tkinter as tk
from tkinter import  ttk

def crp_vali(inp, mn, mx):

	print(type(mn), type(mx), type(inp))
	print(mn, mx, inp)
	if ((inp.isdigit()) and (int(mn)<=int(inp)<=int(mx))) or (inp == ""):
		# print(tes.get())
		return True
	else:
		return False

# def crp_rht_vali(inp, min, max):
#     if ()
def main():
	win = tk.Tk()
	win.geometry('400x400')
	fr = tk.Frame(win)
	tes = tk.StringVar()
	tes.set('25')
	fr.pack(fill = tk.BOTH)
	# reg = fr.register(lambda input: crp_vali(input, 0, 100, tes))
	lab1 = tk.Spinbox(fr, from_ = 0, to = 100, textvariable = tes, increment = 10)
	lab1.configure(
		validate = 'key', 
		validatecommand = (fr.register(lambda input: crp_vali(input, 0, 100)), '%P'))
	lab1.pack(expand = 1, pady = 20)
	win.mainloop()
	print("in main")

if __name__ == '__main__':
	main()