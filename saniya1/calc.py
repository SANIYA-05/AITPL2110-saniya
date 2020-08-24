from tkinter import *
cal = Tk()
cal.geometry("354x460")
cal.title("Calculator")
#label = Label(text="CALCULATOR", bg='dark gray')
#label.grid(side=TOP)
cal.config(background='Dark gray')
txt = StringVar()
operator = "" #this is global


def clickbut(numb):
    global operator
    operator = operator + str(numb)
    txt.set(operator)


def equalbut():
    global operator
    add = str(eval(operator))
    txt.set(add)
    operator = ''


def equalbut():
    global operator
    sub = str(eval(operator))
    txt.set(sub)
    operator = ''


def equalbut():
    global operator
    mul = str(eval(operator))
    txt.set(mul)
    operator = ''


def equalbut():
    global operator
    div = str(eval(operator))
    txt.set(div)
    operator = ''


def clrbut():
    txt.set('')


caltxt = Entry(textvar=txt, width=25,bd=5)
caltxt.grid(columnspan=20, ipadx=70)
but1 = Button(padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(1), text="1",
              font=( 16))
but1.grid(row=2,column=0)

but2 = Button(padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(2), text="2",
              font=( 16))
but2.grid(row=2,column=1)

but3 = Button(padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(3), text="3",
              font=( 16))
but3.grid(row=2,column=2)

but4 = Button(padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(4), text="4",
              font=(16))
but4.grid(row=3,column=0)

but5 = Button(padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(5), text="5",
              font=( 16))

but5.grid(row=3,column=1)
but6 = Button(padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(6), text="6",
              font=(16))

but6.grid(row=3,column=2)
but7 = Button(padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(7), text="7",
              font=(16))

but7.grid(row=4,column=0)
but8 = Button(padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(8), text="8",
              font=( 16))
but8.grid(row=4,column=1)

but9 = Button(padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(9), text="9",
              font=(16))
but9.grid(row=4,column=2)

but0 = Button(padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(0), text="0",
              font=( 16))
but0.grid(row=5,column=0)
butplus = Button(padx=14, pady=14, bd=4, bg='white', text="+", command=lambda: clickbut("+"),
               font=(16))
butplus.grid(row=2,column=3)

butsub = Button(padx=14, pady=14, bd=4, bg='white', text="-", command=lambda: clickbut("-"),
                font=( 16))
butsub.grid(row=4,column=3)

butmul = Button(padx=14, pady=14, bd=4, bg='white', text="*", command=lambda: clickbut("*"),
               font=( 16))
butmul.grid(row=5,column=3)

butdiv = Button(padx=14, pady=14, bd=4, bg='white', text="/", command=lambda: clickbut("/"),
                font=(16))

butdiv.grid(row=5,column=2)
butclear = Button(padx=14, pady=119, bd=4, bg='white', text="CE", command=clrbut, font=(16))

butclear.grid(row=5,column=1)
butequal = Button(padx=151, pady=14, bd=4, bg='white', command=equalbut, text="=", font=(16))
butequal.grid(row=5,column=0)
cal.mainloop()