from tkinter import *
a=Tk()
def hello():
    c=Label(text='you have pressed enter',fg='black',bg='yellow',font=20).pack()
def delete():
    d=Label(text='you have pressed delete',fg='black',bg='yellow',font=20).pack()
a.title("my first window")
a.geometry("500x500+100+100")
l=Label(text='label1',fg='red',bg='yellow',font=20).pack()
#l1=Label(text='label2',fg='blue',bg='green',font=20).pack()
button1=Button(text='enter',fg='red',bg='yellow',command=hello,font=20).pack()
button2=Button(text='delete',fg='red',bg='yellow',command=delete,font=20).pack()

a.mainloop()