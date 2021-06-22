from tkinter import Tk, Button
root = Tk()
def click():
    print(root.winfo_x(), root.winfo_y())
Button(text="Get position", command=click).grid()
root.mainloop()