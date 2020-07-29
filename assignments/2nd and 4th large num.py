a,b,c,d,e=int(input()),int(input()),int(input()),int(input()),int(input())
if((a<c and a>c and a>d and a> e) or (a<b and a>c and a>d and a>e) or (a<d and a>c and a>b and a>e) or (a<e and a>b and a>c and a>d)):
    print("a is second largest")
    if(b<a and b<c and b<d and b>e) or (b<d and b<e and b<a and b>c) or (b<e and b<a and b<c and b>d)or(b<c and b<d and b<e and b>a)or(b<a and b<e and b<a and b>c)or(b<e and b<a and b<c and b<d):
        print(" bis 4th largest")
    elif (c<a and c<b and c<d and c>e) or (c<d and c<e and c<a and c>b) or (c<e and c<a and c<b and c>d)or(c<b and c<d and c<e and c>a)or(c<a and c<e and c<a and c>b)or(c<e and c<a and c<b and c<d):
        print(" c is 4th largest")
    elif(d<a and d<b and d<c and d>e) or (d<c and d<e and d<a and d>b) or (d<e and d<a and d<b and d>c)or(d<b and d<c and d<e and d>a)or(d<a and d<e and d<a and d>b)or(d<e and d<a and d<b and d<c):
        print(" d is 4th largest")
    else:
        print(" e is fourth largest")

elif((b<c and b>a and b>d and b>e) or (b<c and b>a and b>d and b>e) or (b<d and b>c and b>a and b>e) or (b<e and b>a and b>c and b>d)):
    print(" a is second largest")
    if(a<b and a<c and a<d and a>e) or (a<d and a<e and a<b and a>c) or (a<e and a<b and a<c and a>d)or(a<c and a<d and a<e and a>b)or(a<d and a<e and a<b and a>c)or(a<e and a<b and a<c and a>d):
        print("a is 4th largest")
    elif(c<a and c<b and c<d and c>e) or (c<d and c<e and c<a and c>b) or (c<e and c<a and c<b and c>d)or(c<b and c<d and c<e and c>a)or(c<a and c<e and c<a and c>b)or(c<e and c<a and c<b and c<d):
        print(" c is 4th largest")
    elif(d<a and d<b and d<c and d>e) or (d<c and d<e and d<a and d>b) or (d<e and d<a and d<b and d>c)or(d<b and d<c and d<e and d>a)or(d<a and d<e and d<a and d>b)or(d<e and d<a and d<b and d<c):
        print(" d is 4th largest")
    else:
        print(" e is fourth largest")
elif((c<a and c>b and c>d and c>e ) or (c<b and c>a and c>d and c>e )or (c<d and c>b and c>a and c>e) or (c<e and c>a and c>b and c>d)):
    print("c is second largest")
    if(a<b and a<c and a<d and a>e) or (a<d and a<e and a<b and a>c) or (a<e and a<b and a<c and a>d)or(a<c and a<d and a<e and a>b)or(a<d and a<e and a<b and a>c)or(a<e and a<b and a<c and a>d):
        print("a is 4th largest")
    elif(b<a and b<c and b<d and b>e) or (b<d and b<e and b<a and b>c) or (b<e and b<a and b<c and b>d)or(b<c and b<d and b<e and b>a)or(b<a and b<e and b<a and b>c)or(b<e and b<a and b<c and b<d):
        print(" bis 4th largest")
    elif(d<a and d<b and d<c and d>e) or (d<c and d<e and d<a and d>b) or (d<e and d<a and d<b and d>c)or(d<b and d<c and d<e and d>a)or(d<a and d<e and d<a and d>b)or(d<e and d<a and d<b and d<c):
        print(" d is 4th largest")
    else:
        print(" e is fourth largest")
elif((d<a and d>b and d>c and d>e ) or (d<b and d>a and d>c and d>e )or (d<c and d>b and d>a and d>e) or (d<e and d>a and d>b and d>c)):
    print("d is second largest")
    if(a<b and a<c and a<d and a>e) or (a<d and a<e and a<b and a>c) or (a<e and a<b and a<c and a>d)or(a<c and a<d and a<e and a>b)or(a<d and a<e and a<b and a>c)or(a<e and a<b and a<c and a>d):
        print("a is 4th largest")
    elif(b<a and b<c and b<d and b>e) or (b<d and b<e and b<a and b>c) or (b<e and b<a and b<c and b>d)or(b<c and b<d and b<e and b>a)or(b<a and b<e and b<a and b>c)or(b<e and b<a and b<c and b<d):
        print(" bis 4th largest")
    elif(c<a and c<b and c<d and c>e) or (c<d and c<e and c<a and c>b) or (c<e and c<a and c<b and c>d)or(c<b and c<d and c<e and c>a)or(c<a and c<e and c<a and c>b)or(c<e and c<a and c<b and c<d):
        print(" c is 4th largest")
    else:
        print("e is 4th largest")
else:
    print("e is second lrgest")
    if(a<b and a<c and a<d and a>e) or (a<d and a<e and a<b and a>c) or (a<e and a<b and a<c and a>d)or(a<c and a<d and a<e and a>b)or(a<d and a<e and a<b and a>c)or(a<e and a<b and a<c and a>d):
        print("a is 4th largest")
    elif(b<a and b<c and b<d and b>e) or (b<d and b<e and b<a and b>c) or (b<e and b<a and b<c and b>d)or(b<c and b<d and b<e and b>a)or(b<a and b<e and b<a and b>c)or(b<e and b<a and b<c and b<d):
        print(" bis 4th largest")
    elif(c<a and c<b and c<d and c>e) or (c<d and c<e and c<a and c>b) or (c<e and c<a and c<b and c>d)or(c<b and c<d and c<e and c>a)or(c<a and c<e and c<a and c>b)or(c<e and c<a and c<b and c<d):
        print(" c is 4th largest")
    elif(d<a and d<b and d<c and d>e) or (d<c and d<e and d<a and d>b) or (d<e and d<a and d<b and d>c)or(d<b and d<c and d<e and d>a)or(d<a and d<e and d<a and d>b)or(d<e and d<a and d<b and d<c):
        print(" d is 4th largest")


