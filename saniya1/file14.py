from tkinter import *
a=Tk()
a.title("my first window")
a.geometry("500x500+100+100")
m1=Menu()
m1.add_cascade(label="File")
m1.add_cascade(label="Edit")
m1.add_cascade(label="Format")
m1.add_cascade(label="View")
m1.add_cascade(label="Help")
a.config(menu=m1)

a.mainloop()
