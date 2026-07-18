a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    brr=sorted(arr)
    c=brr[-1]
    d=brr[-2]
    for i in range(len(arr)):
        if arr[i]!=c:
            arr[i]=arr[i]-c
        else:
            arr[i]=c-d
    print(*arr)