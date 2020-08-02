def sort(n):
    n = input().split('')
    n.sort()
    for i in n:
        print(str(i),end=' ')
        print(type(i))
sort()