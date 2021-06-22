import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
 # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk

# create root window
root = ThemedTk(theme="clearlooks")
# root = tk.Tk()
root.title('Treeview Demo - Hierarchical Data')
root.geometry('400x200')

# configure the grid layout
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


# create a treeview
tree = ttk.Treeview(root)
tree["column"] = ("Name")
tree.column("#0")
tree.column("Name", anchor=tk.W)
tree.heading('#0', text='Departments', anchor='w')
tree.heading("Name", text="Name", anchor=tk.W)


# adding data
tree.insert('', index='end', text='Administration', values=("lax"), iid=0, open=False)
tree.insert('', index='end', text='Administration', values=("lax"), iid=1, open=False)
tree.insert(1, index='end', text='Sales', iid=2,values=("athrav"), open=False)
# tree.insert('', tk.END, text='Finance', iid=3, open=False)
# tree.insert('', tk.END, text='IT', iid=4, open=False)
# tree.insert('', tk.END, iid=8, text="Label", values=("Hello", "Second Col", "Third Col"))

# # adding children of first node
# tree.insert('', tk.END, text='John Doe', iid=5, open=False)
# tree.insert('', tk.END, text='Jane Doe', iid=6, open=False)
# tree.move(2, 0, 0)
# tree.move(6, 1, 1)

# tree.insert('', tk.END, text='atharva', iid=7, open=False)
# tree.move(7, 5, 0)

# place the Treeview widget on the root window
tree.grid(row=0, column=0, sticky='nsew')

# run the app
root.mainloop()