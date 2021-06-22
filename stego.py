from PIL import Image 
import numpy as np
from cryptography.fernet import Fernet
# key = Fernet.generate_key()
key=b'tiVLAX1-pZuEJe6HhgX-I-GQouJvyYMfV93czogiCPU='
f = Fernet(key)
token = f.encrypt(b"my deep dark secret")


pasw = b'hello'

def encode(*args):
    return

def decode(*args):
    return 

try :
    img = Image.open('D:/blender artwork/test1.png')
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

# r_end = 0
# rec = np.zeros(wid)
for i in token:
    crypt=bina(i)

    x=x+pasw[pasw_tr]-31
    if x>=lenth :
        y=y+1
        x=x%lenth
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
if(len(s)<27):
    crypt = (27-len(crypt))*'0' + crypt

x=lenth-1
y=wid-1
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
y=wid-1

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
for i in range(no_of_char):
    x=x+pasw[pasw_tr]-31
    crypt=""
    if(x>=lenth):
        y=y+1
        x=x%lenth
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
    pasw_tr=pasw_tr+1
    if pasw_tr==len(pasw):
        pasw_tr=0    

msg=bytes(msg, 'utf-8')

print('\n', msg)


print(f.decrypt(msg))
# img.show()
img.save("D:/books/google_hash/atha1.png")