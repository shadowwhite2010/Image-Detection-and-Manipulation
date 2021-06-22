import tkinter as tk
from tkinter import *
from tkinter import ttk



window = tk.Tk()
a=0
flag=0
e=tk.Entry(window, width=30, borderwidth=10)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def calci_op(ver):
    
    ver=str(e.get())+str(ver)
    e.delete(0, 'end')
    e.insert(0, ver)
    
    
def calci_add():
    global a
    if e.get()!=None:
        
        a=a+int(e.get())
        e.delete(0, 'end')
    # else:
    #     label=tk.Label(window, text="a_empty").pack()

    
def calci_clc():
    global a, flag
    e.delete(0, 'end')
    a=0
    flag=0

def calci_eql():
    global a
    if e.get()!=None:
        a=a+int(e.get())
        e.delete(0, 'end')
        e.insert(0, str(a))
    # else:
    #     label=tk.Label(window, text="error").pack()

b0=tk.Button(window, text="0", padx=40, pady=20, command=lambda:calci_op(0))
b1=tk.Button(window, text="1", padx=40, pady=20, command=lambda:calci_op(1))
b2=tk.Button(window, text="2", padx=40, pady=20, command=lambda:calci_op(2))
b3=tk.Button(window, text="3", padx=40, pady=20, command=lambda:calci_op(3))
b4=tk.Button(window, text="4", padx=40, pady=20, command=lambda:calci_op(4))
b5=tk.Button(window, text="5", padx=40, pady=20, command=lambda:calci_op(5))
b6=tk.Button(window, text="6", padx=40, pady=20, command=lambda:calci_op(6))
b7=tk.Button(window, text="7", padx=40, pady=20, command=lambda:calci_op(7))
b8=tk.Button(window, text="8", padx=40, pady=20, command=lambda:calci_op(8))
b9=tk.Button(window, text="9", padx=40, pady=20, command=lambda:calci_op(9))
b_add=tk.Button(window, text="+", padx=80, pady=20, command=calci_add)
b_clear=tk.Button(window, text="clc", padx=80, pady=20, command=calci_clc)
b_equal=tk.Button(window, text="=", padx=80, pady=20, command=calci_eql)


b0.grid(row=4, column=0)
b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=3, column=0)
b8.grid(row=3, column=1)
b9.grid(row=3, column=2)
b_add.grid(row=4, column=1, columnspan=2, sticky=tk.E)
b_clear.grid(row=5, column=1, columnspan=2, sticky=tk.E)
b_equal.grid(row=6, column=1, columnspan=2, sticky=tk.SE)
tk.mainloop()