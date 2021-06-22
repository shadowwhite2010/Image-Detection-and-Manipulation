from PIL import Image 
import numpy as np
from cryptography.fernet import Fernet
# key = Fernet.generate_key()
key=b'tiVLAX1-pZuEJe6HhgX-I-GQouJvyYMfV93czogiCPU='
f = Fernet(key)
token = f.encrypt(b'''https://ai.googleblog.com/2019/05/efficientnet-improving-accuracy-and.html
http://www.ijltet.org/wp-content/uploads/2015/02/60.pdf

in t9.py method to use scrolbar, 
use that method to create function for deepfake result showing 
deepfake result would be shown in image showing canvas

use opt_can showing the options of deepfake detection

#####
24.04.21
del_crface and show_res to complete

show_res for showing df result
del_crface for to delete cr_face dir images


#####
24.04.21 6.59
in t1 traying to demo progressvar
read from tkinter book for progressbar
using progressbar for plting the prediction percentege
in main file still workinng on deepfake

####
25.04.21
on line 10 in testt.py

####
26.04.21 1.47 am
solve window blue screen problem

####
password for new mail = Veda@spit

####
lot of work
currently improving the stego code
then move the stego options in main script to somewhere else so that we can place treeview at that place
then edit options: search, create , add as much as you can 

####
26.04.21
working on encd and dode placement in tkinter''')

# token = f.encrypt(b'''atharva''')

pasw = b'aaaa'

# def encode(*args):
#     return

# def decode(*args):
#     return 

try :
    img = Image.open('D:/books\google_hash/temp\gen_face.png')
except:
    print("no image")

px=img.load()

lenth=img.size[0]
wid=img.size[1]
pasw_tr=0
x=0
y=0

def bina(t):
    s=bin(t)
    s=s[2:]
    if(len(s)<9):
        s=(9-len(s))*'0' + s
    
    return s

def next_zero(rec, i):
    flag = i
    for t in range(i+1, len(rec), 1):
        if rec[t]==0:
            flag = t
            print("1: ", flag)
            break
    if (flag==i):
        for t in range(1, i, 1):
            if rec[t]==0:
                flag = t
                print("2: ", flag)
                break
    print("flag : ", flag)
    return flag


# r_end = 0
rec = np.zeros(wid, dtype = int)
pass_pos = np.zeros(len(pasw), dtype = int)

def compa(st, gt):
    print("msg len:", len(st), "   token len: ", len(gt))
    if len(st)==len(gt):
        for i in range (len(st)):
            if st[i]!=gt[i]:
                print("we got at: ", st[i], gt[i], i)

for i in token:
    crypt=bina(i)
    if (pass_pos[pasw_tr]==0):
        y = next_zero( rec, int(pasw[pasw_tr]-30))
        pass_pos[pasw_tr] = y
    else :
        # print("type of y", type(y))
        y = int(pass_pos[pasw_tr])
        # print(type(y))

    # print(type(y))
    if (rec[y]+2<lenth):
        x = int(rec[y])
    else :
        temp = next_zero(rec, y)
        if (temp!=y):
            print("y change: from", y, temp, "cause rec[y]: ", rec[y])
            y = int(temp)
            pass_pos[pasw_tr] = y
            x = int(rec[y])
    rec[y] = rec[y] + 3
    # if x>=lenth :
    #     y=y+1
    #     x=x%lenth
    for j in range(3):
        lis=list(px[x, y])
        for k in range(3):
            if (lis[k]%2)and(crypt[(j*3)+k]=='0'):
                lis[k]=lis[k]-1
            elif (lis[k]%2==0)and(crypt[(j*3)+k]=='1'):
                lis[k]=lis[k]+1

        px[x, y]=(lis[0], lis[1], lis[2])

        # px[x, y]=(lis[0]+int(crypt[(j*3)+0]), lis[1]+int(crypt[(j*3)+1]), lis[2]+int(crypt[(j*3)+2]))
        x=x+1
        if x==lenth:
            y=y+1
            x=0
    # px[x, y]
    # pass[k]
    pasw_tr=pasw_tr+1
    if pasw_tr==len(pasw):
        pasw_tr=0    



# crypt=bin(len(token))
# crypt=crypt[2:]
#no of charactres containing secrete message kipping in last pixels of image
#########original
# crypt=bina(len(token))

# x=lenth-4
# y=wid-1
# for j in range(3):
#     lis=list(px[x, y])
#     for k in range(3):
#         if (lis[k]%2)and(crypt[(j*3)+k]=='0'):
#             lis[k]=lis[k]-1
#         elif (lis[k]%2==0)and(crypt[(j*3)+k]=='1'):
#             lis[k]=lis[k]+1

#     px[x, y]=(lis[0], lis[1], lis[2])
#     x=x+1


###########
# crypt=bina(len(token))
crypt = bin(len(token))
crypt = crypt[2:]
if(len(crypt)<27):
    crypt = (27-len(crypt))*'0' + crypt

x=lenth-1
y=0
for j in range(9):
    lis=list(px[x, y])
    for k in range(2, -1, -1):
        if (lis[k]%2)and(crypt[(j*3)+2-k]=='0'):
            lis[k]=lis[k]-1
        elif (lis[k]%2==0)and(crypt[(j*3)+2-k]=='1'):
            lis[k]=lis[k]+1

    px[x, y]=(lis[0], lis[1], lis[2])
    x = x-1


#decryption XXXXXXXXXXXXXXXXXXXXXXXXX
# x=lenth-4
# y=wid-1

# crypt=""
# for j in range(3):
#     lis=list(px[x, y])
#     for k in range(3):
#         if (lis[k]%2) :
#             crypt=crypt+'1'
#         else:
#             crypt=crypt+'0'
#     x=x+1

# no_of_char=int(crypt, 2)
# print(no_of_char, len(token))

#####################
x=lenth-1
y=0

crypt=""
for j in range(9):
    lis=list(px[x, y])
    for k in range(2, -1, -1):
        if (lis[k]%2) :
            crypt=crypt+'1'
        else:
            crypt=crypt+'0'
    x=x-1

no_of_char=int(crypt, 2)
print(no_of_char, len(token))

##########
x=0
y=0
pasw_tr=0
msg=""

rec = np.zeros(wid)
pass_pos = np.zeros(len(pasw))

for i in range(no_of_char):
    # x=x+pasw[pasw_tr]-31
    crypt=""
    # if(x>=lenth):
    #     y=y+1
    #     x=x%lenth
    if (pass_pos[pasw_tr]==0):
        y = next_zero(rec, int(pasw[pasw_tr]-30))
        pass_pos[pasw_tr] = y
    else :
        y = int(pass_pos[pasw_tr])
    
    if rec[y]+2<lenth:
        x = int(rec[y])
    else :
        temp = next_zero(rec, y)
        if (temp!=y):
            y = int(temp)
            pass_pos[pasw_tr] = y
            x = int(rec[y])
        
    rec[y] = rec[y] + 3
    for j in range(3):
        lis=list(px[x, y])
        for k in range(3):
            if (lis[k]%2):
                crypt=crypt+'1'
            else:
                crypt=crypt+'0'
        x=x+1
        if x==lenth:
            y=y+1
            x=0
    val=int(crypt, 2)
    msg=msg+chr(val)
    if (val!=token[i]):
        print("shape: ", x, y)
        print("rec[y]: ", rec[y])
        print("pass_pos[pasw_tr]: ",pass_pos[pasw_tr])
        break
    
    pasw_tr=pasw_tr+1
    if pasw_tr==len(pasw):
        pasw_tr=0    

msg=bytes(msg, 'utf-8')

print('msg:\n', msg)
print("token:\n", token)
# compa(msg, token)
# print(f.decrypt(msg))
# img.show()
# img.save("D:/books/google_hash/g2.png")