# import tkinter as tk
# from tkinter import ttk
# from PIL import ImageTk, Image
import json
import os
a_dictionary = {
    "atha": "fdsasf"
    }

# with open("key_store.json", "r+") as file:
#     data = json.load(file)
#     print(data)
#     data.update(a_dictionary)
#     file.seek(0)
#     json.dump(data, file)

with open("key_store.json", "r") as file:
    data = json.load(file)

# for d in data:
#     print()

# with open("key_store.json", "w") as file:
    
#     print(data)
#     try:
#         del data["atha"]
#     except:
#         pass
#     data.update(a_dictionary)
#     # file.seek(0)
#     json.dump(data, file)




# root = tk.Tk()
# # root.title('Codemy.com - Set Image as Background')
# # root.iconbitmap('c:/gui/codemy.ico')
# root.geometry("800x600")
# test_can = tk.Canvas(root, bg = "#898F8C")
# test_can.pack(fill = tk.BOTH, expand = 1)

# lab = tk.Frame(test_can, height = 200, width = 200, bg = "black", relief = tk.SUNKEN)
# test_can.create_window((0, 0), anchor = tk.NW, window = lab)

# img = Image.open("D:/books\google_hash/temp\gen_face.png")

# # img = img.transpose(Image.ROTATE_180)
# img = img.crop((150, 150, 210, 210))
# img = img.resize((600, 600), Image.ANTIALIAS)
# print(img.size[0], img.size[1])
# img = ImageTk.PhotoImage(img)
# lab = tk.Label(lab, image = img, font = ('calibre',25,'bold'))
# lab.pack()
# root.mainloop()