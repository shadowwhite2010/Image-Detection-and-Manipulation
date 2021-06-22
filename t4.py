import tkinter as tk
from tkinter import ttk
# from tkinter.constants import ANCHOR
from PIL import ImageTk, Image, ImageEnhance, ImageOps, ImageFilter 
import cv2
import numpy as np
img = Image.open("temp\gen_face.png")
img = img.convert("RGB")
img  = img.convert("L")
imgc = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
# cv2.imshow("hello", imgc)

# cv2.waitKey(0)
print(type(imgc))
print(imgc[250, 300], imgc.shape)

b, g, r = cv2.split(imgc)

print(r.dtype)
# tt = np.ones(r.shape, dtype=r.dtype)*50
# tt = np.true_divide(r, r[r>0], dtype = r.dtype)*50
_, tt = cv2.threshold(r, 0, 110, cv2.THRESH_BINARY)
# tt = tt*50
print(tt.dtype)
print(r)

r = cv2.add(r, tt)
print(r.shape)
print(g.shape)
print(b.shape )
print(tt[225:275, 300:310])
# cv2.imshow("hello", r)
# cv2.waitKey(0)
imgc = cv2.merge((b, g, r))

# e1 = cv2.getTickCount()
# test = imgc%2
# e2 = cv2.getTickCount()

# print(e2-e1)
# # test = test[ : , :, 1] * 255
# test = test[ : , :] * 255
# print(test[250, 300])
# # e1 = cv2.getTickCount()

# # test1 = cv2.bitwise_and(imgc, test, mask = None)
# # e2 = cv2.getTickCount()
# imgc[:, :, 0] = 200


# print(e2-e1)
cv2.imshow("hello", imgc)

cv2.waitKey(0)