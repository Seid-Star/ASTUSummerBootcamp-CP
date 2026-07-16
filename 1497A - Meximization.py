a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    brr=[]
    crr=[]
    for i in arr:
        if i in brr:
            crr.append(i)
        else:
            brr.append(i)
    drr=brr+crr
    print(*drr)
