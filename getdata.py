from tkinter import *
root=Tk()
def go():
    print(e.get())

a=Label(root,text="Enter name")
e=Entry(root)
b=Button(root,text="Submit",command=go)
