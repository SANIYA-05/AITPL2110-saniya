def palindrom(n):
    p=n[::-1]
    if(n==p):
        print(n+" is palindrom")
    else:
        print(n+" not a palindrom")
n=input()
palindrom(n)