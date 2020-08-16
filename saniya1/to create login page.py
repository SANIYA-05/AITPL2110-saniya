from tkinter import *
import tkinter.messagebox
a=Tk()
b=tkinter.messagebox
a.title("Login Page")
a.geometry("600x600")
def result():
    username=txt1.get()
    password=txt2.get()
    if(username=='admin' and password=='adminadmin'):
        print(username,password)
        print("success")
        b.showinfo("submitted sucessfully")
        #a.destroy()
    elif(username=='' or password==''):
        print("invalid")
        b.showinfo("enter username and password")
    else:
        print("invalid")
        b.showinfo("invalid username or password")
        #a.destroy()


l1=Label(text="username",fg="red",font=20)
l1.grid(row=0,column=0,padx=2,pady=2)
txt1=Entry(fg='grey',font=16)
txt1.grid(row=0,column=1)
l2=Label(text="password",fg="red",font=20)
l2.grid(row=1,column=0,padx=2,pady=2)
txt2=Entry(fg='grey',font=16)
txt2.grid(row=1,column=1)
button=Button(text="SUMBIT",fg="red",font=20,command=result)
button.grid(row=2,column=1)
a.mainloop()