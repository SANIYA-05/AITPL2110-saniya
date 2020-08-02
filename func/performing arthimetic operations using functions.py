def addition(x,y):
    print(x+y)
def subtraction(x,y):       ##getting output partially # while loop not exiting
    print(x-y)
def multiplication(x,y):
    print(x*y)
def division(x,y):
    print(x/y)
def modiv(x,y):
    print(x%y)
def fdiv(x,y):
    print(x//y)
a = input("enter your choice y/n")
while a=='y' or 'Y':
    i = int(input("enter your number"))
    x = int(input("x value"))
    y = int(input('y value'))
    if i == 1:
        w = addition(x,y)
    elif i == 2:
        x = subtraction(x,y)
    elif i == 3:
        y = multiplication(x,y)
    elif i == 4:
        z = division(x,y)
    elif i == 5:
        p = modiv(x,y)
    elif i == 6:
        q = fdiv(x,y)
    elif i>=7:
        print("invalid choice")
    print("do you want to continue")
    a = input("enter your choice y/n")