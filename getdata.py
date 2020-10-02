from tkinter import *
root=Tk()
def go():
    print(e.get())

a=Label(root,text="Enter name")
a.pack()
e=Entry(root)
e.pack()
b=Button(root,text="Submit",command=go)
b.pack()
