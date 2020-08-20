from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

a=Tk()
p=PhotoImage(file="test.jpg")
l=Label(a,image=p).pack()
a.mainloop()

