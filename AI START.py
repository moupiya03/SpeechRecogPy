from tkinter import *
import os

def call():
    fname="AI_project.py"
    os.system(fname)
    os.system("notepad"+fname)             #connecting with AI_project

root=Tk()
root.geometry("1200x500")
root.title("AI PROJECT")
root.configure(bg="black")

photo=PhotoImage(file="mic.png").subsample(5,5)    #adjusting size for png image

ftop=Frame(root,borderwidth=5,relief=RAISED,bg="dark cyan")
ftop.pack(side=TOP,fill="x",padx=5,pady=5)

ltop=Label(ftop,text="Hello !!! ",font="Helvetica 20 bold ",bg="dark cyan",fg="white")
ltop.pack(padx=5,pady=5)

import PIL
from PIL import Image,ImageTk

img=Image.open("pattern.jpg").resize((250,250),PIL.Image.ANTIALIAS)    #adjusting size for jpg image
pic=ImageTk.PhotoImage(img)
lpic1=Label(image=pic,bg="black")
lpic1.pack(side=LEFT)
lpic2=Label(image=pic,bg="black")
lpic2.pack(side=RIGHT)

f1=Frame(root,bg="black",relief=SUNKEN)
f1.pack(side=TOP,padx=10,pady=10,anchor="center")

l1=Label(f1,text="Click the icon below to start",font="Helvetica 16 bold ",bg="black",fg="dark cyan")
l1.pack(padx=10,pady=10,anchor="center")


fstart=Frame(root,bg="black",borderwidth=5,relief=SUNKEN)
fstart.pack(side=TOP,padx=10,pady=10,anchor="center")

bstart=Button(fstart,image=photo,font="Helvetica 16 bold",command=call)
bstart.pack(padx=10,pady=10,anchor="center")

fbottom=Frame(root,borderwidth=5,relief=GROOVE,bg="dark cyan")
fbottom.pack(side=BOTTOM,fill="x",padx=5,pady=5)

lbottom=Label(fbottom,text="Welcome To AI PROJECT !!! ",font="Helvetica 20 bold",bg="dark cyan",fg="white")
lbottom.pack(padx=5,pady=5)

f2=Frame(root,bg="black",relief=SUNKEN)
f2.pack(side=BOTTOM,padx=20,pady=20,anchor="center")

b2=Button(f2,text="QUIT",font="Helvetica 25 bold underline",bg="black",fg="red",command=root.destroy)    #to quit program
b2.pack(padx=20,pady=20,anchor="center")




root.mainloop()
