def triangle(n):
    for i in range(0,n):
        num = '0 1'
        for j in range(0,i+1):
            print(num,end=' ')
        print('\n')
n=int(input())
triangle(n)