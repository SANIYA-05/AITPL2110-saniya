def lst():
    l=list(map(int,input().split()))
    l.sort()
    print("2nd smallest number{0} and fifth smallest number{1} ".format(l[0],l[4]))
lst()