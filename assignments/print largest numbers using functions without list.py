def large(a,b,c):
    if(a>b & a>c):
        print("a is largest")
    elif(b>c):
        print("b is largest")
    else:
        print("cis largest")
a=int(input())
b=int(input())
c=int(input())
n=large(a,b,c)