from tkinter import *
import tkinter.messagebox
a=Tk()
a.title("my first window")
a.geometry("1080x768+0+0")

b=tkinter.messagebox
b.showinfo('this is the msg box')
ch=b.askquestion('are you a intern')
if ch=='yes':
    print('hello welcome')
a.mainloop()
# create a basic calculator with +,-,*,/
# create a window like notepad
# create a username password text boxes,create login button,default username=admin,password=adminadmin,show sucess or failure msg box
