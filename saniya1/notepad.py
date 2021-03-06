from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename ## to open a file and to save
import os
def cut():
    TextArea.event_generate(("<<Cut>>")) ##tkinter automatically cuts the char
def copy():
    TextArea.event_generate(("<<Copy>>")) #automatically copies
def paste():
    TextArea.event_generate(("<<Paste>>")) #automatically pastes
def about():
    showinfo("Notepad","Notepad created by saniya")
def quitapp():
    a.destroy()
def newfile():
    global file
    a.title("untitled-Notepad") #new file before saving automatically generates title like this
    file=None
    TextArea.delete(1.0,END)#firstline 0th char to last char it erases and new file creates

a=Tk()
a.title("Untitled-Notepad")
a.geometry("500x500+100+100")
a.wm_iconbitmap("n.ico")
#to add text
TextArea=Text(a,font="20")
TextArea.pack()
file=None #this points to the file which is being opened in notepad
m1=Menu()
#fileMenu
l1=Menu()
l1.add_command(label="New",command=newfile)
l1.add_command(label="NewWindow")
l1.add_command(label="Open")
l1.add_command(label="Save")
l1.add_command(label="Save As")
l1.add_separator()
l1.add_command(label="PageSetup")
l1.add_command(label="Print")
l1.add_command(label="Exit",command=quitapp)
#eDIT menu
l2=Menu()
l2.add_command(label="Undo")
l2.add_command(label="Cut",command=cut)
l2.add_command(label="Copy",command=copy)
l2.add_command(label="Delete")
l2.add_separator()
l2.add_command(label="Paste",command=paste)
l2.add_command(label="Search with Bing")
l2.add_command(label="Paste")
l2.add_command(label="Find")
l2.add_command(label="Find Next")
l2.add_command(label="Find Previous")
l2.add_command(label="Replace")
l2.add_command(label="goto")
l2.add_separator()
l2.add_command(label="Select All")
l2.add_command(label="Time/Date")
#format menu
l3=Menu()
l3.add_command(label="Wordwrap")
l3.add_command(label="Font")
#zoom
l6=Menu()
l6.add_command(label="ZoomIn")
l6.add_command(labe="ZoomOut")
l6.add_command(label="Restore Default Zoom")
#View menu
l4=Menu()
#l4.add_command(label="Zoom")
l4.add_cascade(label="Zoom",menu=l6)
l4.add_command(label="Status Bar")
#help menu
l5=Menu()
l5.add_command(label="View Help")
l5.add_command(label="Send Feedback")
l5.add_separator()
l5.add_command(label="About Notepad",command=about)
#cascading all menus
m1.add_cascade(label="File",menu=l1)
m1.add_cascade(label="Edit",menu=l2)
m1.add_cascade(label="Format",menu=l3)
m1.add_cascade(label="View",menu=l4)
m1.add_cascade(label="Help",menu=l5)

a.config(menu=m1)
a.mainloop()