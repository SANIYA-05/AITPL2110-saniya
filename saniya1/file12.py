from tkinter import *
a=Tk()
a.title("my first window")
a.geometry("500x500+100+100")
l=Label(text='label1',fg='red',bg='yellow',font=20)
l1=Label(text='label2',fg='blue',bg='green',font=20)
l.pack()
l1.pack()
a.mainloop()