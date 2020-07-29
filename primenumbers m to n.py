n = int(input())
m = int(input())
while n <= m:
    count = 0
    i=1
    while i <= n:
        if n % i == 0:
            count += 1
        i=i+1
    if count==2:
        print(n)
    n+=1



